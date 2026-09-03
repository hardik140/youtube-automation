#!/usr/bin/env python3
"""Compatibility entrypoint for the Hardik video factory.

The old implementation generated large presentation cards and reused scene-level
assets. That path is intentionally retired because it produced slideshow-like video.
Use the editorial shot pipeline instead.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PIPE=ROOT/"pipeline"

def main()->None:
    ap=argparse.ArgumentParser(description="Build documentary through shot-level editorial pipeline")
    ap.add_argument("manifest",type=Path,help="source production manifest JSON")
    ap.add_argument("--project-dir",type=Path,default=None)
    ap.add_argument("-o","--output",type=Path,default=Path("pilot/final/pilot_video.mp4"))
    args=ap.parse_args(); project=args.project_dir or args.manifest.parent
    editorial=project/(args.manifest.stem+"_multibeat.json")
    subprocess.run([sys.executable,str(PIPE/"phase3_multibeat_manifest.py"),str(args.manifest),"-o",str(editorial)],check=True)
    data=json.loads(editorial.read_text(encoding="utf-8"));
    result=subprocess.run([sys.executable,str(PIPE/"dynamic_renderer.py"),str(editorial),str(project),"-o",str(args.output)],capture_output=True,text=True)
    print(result.stdout); print(result.stderr,file=sys.stderr)
    if result.returncode!=0: raise SystemExit(result.returncode)
    data["rendered_output"]=str(args.output)
    qc=project/"qc_manifest.json"; qc.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    subprocess.run([sys.executable,str(PIPE/"automated_qc.py"),str(qc),str(project)],check=True)

if __name__=="__main__": main()
