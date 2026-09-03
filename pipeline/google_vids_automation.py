#!/usr/bin/env python3
"""Phase 5: prepare a Google Vids automation job.

Google Vids currently exposes its editing workflow primarily through the web UI rather
than a documented public timeline-editing API. This module therefore creates a stable,
UI-automation-friendly job manifest for Antigravity/Playwright instead of pretending an
unsupported API exists. Authentication is intentionally left to the user's browser
profile; no credential scraping or security bypass is performed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def build_job(manifest: dict[str, Any], project_dir: Path) -> dict[str, Any]:
    scenes = manifest.get("scenes", [])
    objects = []
    for sidx, scene in enumerate(scenes, 1):
        for bidx, beat in enumerate(scene.get("beats", []), 1):
            asset = beat.get("asset") or scene.get("video_file") or scene.get("visual_asset")
            if not asset:
                continue
            path = Path(asset)
            if not path.is_absolute():
                path = project_dir / path
            objects.append({
                "scene": sidx,
                "beat": bidx,
                "type": "video" if path.suffix.lower() in {".mp4", ".mov", ".webm", ".mkv"} else "image",
                "path": str(path.resolve()),
                "start_offset": float(beat.get("start_offset", 0)),
                "duration": float(beat.get("duration", 0)),
                "animation": "photo_effect" if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"} else "none",
                "track_name": f"scene_{sidx:03d}_beat_{bidx:02d}",
            })

    return {
        "schema_version": "1.0",
        "platform": "google_vids",
        "mode": "ui_automation",
        "canvas": {"aspect_ratio": "16:9", "target_resolution": "1920x1080"},
        "objects": objects,
        "audio": [{"path": str((project_dir / s.get("audio_file")).resolve())}
                   for s in scenes if s.get("audio_file")],
        "instructions": [
            "Open a new Landscape Google Vids project.",
            "Import/insert prepared media; do not ask Vids to regenerate the visual assets.",
            "Use object tracks to apply manifest timings.",
            "Apply photo effects to still images and transitions between scenes.",
            "Keep Sarvam audio as the narration authority; disable/remove duplicate Vids voiceovers.",
            "Preview the full timeline, then export the final video.",
        ],
        "manual_login_allowed": True,
        "credential_handling": "browser_profile_only",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("project_dir", type=Path)
    ap.add_argument("-o", "--output", type=Path, default=None)
    args = ap.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    job = build_job(data, args.project_dir)
    output = args.output or args.project_dir / "google_vids_job.json"
    output.write_text(json.dumps(job, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
