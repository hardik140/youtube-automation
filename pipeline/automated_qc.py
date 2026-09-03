#!/usr/bin/env python3
"""Phase 6: automated production QC.

Checks are intentionally cheap and deterministic. Failed checks identify the smallest
asset that needs regeneration instead of forcing a full-video rerender.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


def probe(path: Path) -> dict[str, Any]:
    cmd = ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        return {"ok": False, "error": p.stderr.strip()}
    data = json.loads(p.stdout)
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio = next((s for s in streams if s.get("codec_type") == "audio"), None)
    return {
        "ok": True,
        "duration": float(data.get("format", {}).get("duration", 0) or 0),
        "width": int(video.get("width", 0)) if video else 0,
        "height": int(video.get("height", 0)) if video else 0,
        "fps": video.get("r_frame_rate") if video else None,
        "has_audio": audio is not None,
    }


def check_file(path: Path, expected_video: bool = False) -> list[str]:
    errors = []
    if not path.exists():
        return [f"MISSING: {path}"]
    if expected_video:
        info = probe(path)
        if not info.get("ok"):
            return [f"UNREADABLE_VIDEO: {path}: {info.get('error','unknown')}"]
        if info.get("width") < 1280 or info.get("height") < 720:
            errors.append(f"LOW_RESOLUTION: {path} ({info.get('width')}x{info.get('height')})")
        if info.get("duration", 0) <= 0.5:
            errors.append(f"INVALID_DURATION: {path}")
    return errors


def run_qc(manifest: dict[str, Any], project_dir: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    scenes = manifest.get("scenes", [])

    previous_end = None
    for idx, scene in enumerate(scenes, 1):
        scene_dir = project_dir / f"scenes/scene_{idx:03d}"
        start = scene.get("frame_plan", {}).get("start_frame")
        end = scene.get("frame_plan", {}).get("end_frame")
        actual = scene.get("frame_plan", {}).get("actual_last_frame")
        for label, value in (("start_frame", start), ("end_frame", end)):
            if value:
                errors += check_file(Path(value) if Path(value).is_absolute() else project_dir / value)
            elif scene.get("frame_plan", {}).get("required", True):
                errors.append(f"MISSING_{label.upper()}: scene {idx}")

        if actual:
            errors += check_file(Path(actual) if Path(actual).is_absolute() else project_dir / actual)
        if idx > 1 and not scene.get("frame_plan", {}).get("previous_last_frame"):
            errors.append(f"BROKEN_CONTINUITY_LINK: scene {idx}")

        for beat in scene.get("beats", []):
            if not beat.get("asset"):
                warnings.append(f"NO_BEAT_ASSET: scene {idx} {beat.get('beat_id')}")
        previous_end = actual or previous_end

    # Global object-count guard for Google Vids.
    video_objects = 0
    audio_objects = 0
    for scene in scenes:
        for beat in scene.get("beats", []):
            if beat.get("asset"):
                video_objects += 1
        if scene.get("audio_file"):
            audio_objects += 1
    if video_objects > 50:
        errors.append(f"GOOGLE_VIDS_VIDEO_OBJECT_LIMIT_EXCEEDED: {video_objects} > 50")
    if audio_objects > 50:
        errors.append(f"GOOGLE_VIDS_AUDIO_OBJECT_LIMIT_EXCEEDED: {audio_objects} > 50")

    result = {
        "phase": 6,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "repair_strategy": "regenerate only the failed scene/asset, then rerun QC",
        "counts": {"scenes": len(scenes), "video_objects": video_objects, "audio_objects": audio_objects},
    }
    (project_dir / "qc_report.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("project_dir", type=Path)
    args = ap.parse_args()
    result = run_qc(json.loads(args.manifest.read_text(encoding="utf-8")), args.project_dir)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
