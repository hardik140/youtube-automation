#!/usr/bin/env python3
"""Extract the actual final video frame for cross-scene continuity."""
from __future__ import annotations
import argparse
import subprocess
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("video", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "ffmpeg", "-y", "-sseof", "-0.05", "-i", str(args.video),
        "-frames:v", "1", "-q:v", "2", str(args.output)
    ], check=True)
    print(f"Extracted {args.output}")


if __name__ == "__main__":
    main()
