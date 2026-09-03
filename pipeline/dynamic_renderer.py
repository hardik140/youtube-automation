#!/usr/bin/env python3
"""Phase 4: deterministic dynamic renderer / assembler.

AI-generated Veo clips remain the hero visual. This renderer handles everything that
should NOT spend AI credits: image motion, cutaways, timing, concat, audio and simple
transitions. It emits a render plan and can assemble ready assets with FFmpeg.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ffprobe_duration(path: Path) -> float:
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
                       capture_output=True, text=True, check=True)
    return float(p.stdout.strip())


def image_motion(image: Path, out: Path, seconds: float, motion: str = "push") -> None:
    # 1920x1080 output; zoompan provides real movement from a still without an AI call.
    frames = max(1, round(seconds * 30))
    if motion == "pan":
        z = "1.08"
        x = "if(eq(on,1),0,(iw-iw/zoom)*on/\"%d\")" % max(frames - 1, 1)
        vf = f"zoompan=z={z}:x={x}:y=(ih-ih/zoom)/2:d=1:s=1920x1080:fps=30"
    else:
        vf = "zoompan=z='min(zoom+0.0008,1.10)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30"
    run(["ffmpeg", "-y", "-loop", "1", "-i", str(image), "-vf", vf,
         "-frames:v", str(frames), "-an", "-pix_fmt", "yuv420p", str(out)])


def write_concat(parts: list[Path], concat_file: Path) -> None:
    concat_file.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in parts), encoding="utf-8")


def build(manifest: dict[str, Any], project_dir: Path, output: Path) -> dict[str, Any]:
    work = project_dir / "render_cache"
    work.mkdir(parents=True, exist_ok=True)
    parts: list[Path] = []
    plan: list[dict[str, Any]] = []

    for sidx, scene in enumerate(manifest.get("scenes", []), 1):
        for bidx, beat in enumerate(scene.get("beats", []), 1):
            mode = str(beat.get("visual_mode", "HOST")).upper()
            asset = beat.get("asset") or scene.get("video_file") or scene.get("visual_asset")
            if asset:
                asset_path = Path(asset)
                if not asset_path.is_absolute():
                    asset_path = project_dir / asset_path
            else:
                asset_path = None
            out_part = work / f"scene_{sidx:03d}_beat_{bidx:02d}.mp4"

            if asset_path and asset_path.exists() and asset_path.suffix.lower() in {".mp4", ".mov", ".webm", ".mkv"}:
                # Do not re-render an existing Veo/B-roll/meme clip unless necessary.
                shutil.copy2(asset_path, out_part)
            elif asset_path and asset_path.exists() and asset_path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                image_motion(asset_path, out_part, float(beat.get("duration", 2.0)),
                             "pan" if mode in {"BROLL", "CINEMATIC"} else "push")
            else:
                plan.append({"scene": sidx, "beat": bidx, "status": "missing_asset", "asset": str(asset or "")})
                continue
            parts.append(out_part)
            plan.append({"scene": sidx, "beat": bidx, "mode": mode, "asset": str(asset_path),
                         "duration": round(ffprobe_duration(out_part), 3), "status": "ready"})

    if parts:
        concat = work / "concat.txt"
        write_concat(parts, concat)
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
             "-an", str(output)])

    result = {"phase": 4, "output": str(output), "parts": plan,
              "dynamic_rule": "every beat must have motion or a media cut; no static full-scene holds"}
    (project_dir / "render_plan.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("project_dir", type=Path)
    ap.add_argument("-o", "--output", type=Path, default=Path("rendered_preview.mp4"))
    args = ap.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = build(manifest, args.project_dir, args.output)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
