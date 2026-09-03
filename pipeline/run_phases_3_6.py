#!/usr/bin/env python3
"""Run the deterministic portions of Phases 3–6 in order.

AI-generation actions (frame/image/Veo/Sarvam) are intentionally not triggered here.
They are supplied as assets and then validated/assembled by the deterministic stages.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(args: list[str]) -> None:
    print("$", " ".join(args))
    subprocess.run(args, check=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("project_dir", type=Path)
    args = ap.parse_args()
    args.project_dir.mkdir(parents=True, exist_ok=True)
    multibeat = args.project_dir / "manifest_multibeat.json"

    run([sys.executable, str(ROOT / "phase3_multibeat_manifest.py"), str(args.manifest), "-o", str(multibeat)])
    run([sys.executable, str(ROOT / "google_vids_automation.py"), str(multibeat), str(args.project_dir)])
    run([sys.executable, str(ROOT / "automated_qc.py"), str(multibeat), str(args.project_dir)])
    print(json.dumps({"status": "DETERMINISTIC_PHASES_COMPLETE", "manifest": str(multibeat),
                      "next": ["generate/approve frames", "generate Veo scenes", "extract actual last frames",
                               "run Google Vids UI automation", "final QC"]}, indent=2))


if __name__ == "__main__":
    main()
