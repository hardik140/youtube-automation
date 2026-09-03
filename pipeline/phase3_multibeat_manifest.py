#!/usr/bin/env python3
"""Phase 3: shot-level multi-beat manifest.

The production unit is a SHOT/BEAT, not a long scene. This module uses the editorial
intelligence layer and adds hard anti-slideshow/redundancy constraints. It is credit-free.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from editorial_director import build as editorial_build


def validate(manifest: dict[str, Any]) -> list[str]:
    errors = []
    for si, scene in enumerate(manifest.get("scenes", []), 1):
        beats = scene.get("beats", [])
        if len(beats) < 3:
            errors.append(f"SCENE_{si}: fewer than 3 beats")
        previous = None
        for b in beats:
            vt = b.get("visual_type") or b.get("visual_mode")
            if vt == previous:
                errors.append(f"SCENE_{si}: adjacent duplicate visual type {vt}")
            previous = vt
            if float(b.get("duration", 0)) > 7:
                errors.append(f"SCENE_{si}/{b.get('beat_id')}: shot longer than 7s")
            if not b.get("visual_question"):
                errors.append(f"SCENE_{si}/{b.get('beat_id')}: missing visual question")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("manifest", type=Path); ap.add_argument("-o", "--output", type=Path)
    a = ap.parse_args()
    source = json.loads(a.manifest.read_text(encoding="utf-8"))
    out = editorial_build(source)
    out.setdefault("pipeline", {})["phase3_validation"] = validate(out)
    out["pipeline"]["phase3_status"] = "FAIL" if out["pipeline"]["phase3_validation"] else "PASS"
    p = a.output or a.manifest.with_name(a.manifest.stem + "_multibeat.json")
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(p), "status": out["pipeline"]["phase3_status"], "beats": sum(len(s.get('beats', [])) for s in out.get('scenes', [])), "errors": out['pipeline']['phase3_validation']}, indent=2))
    raise SystemExit(1 if out["pipeline"]["phase3_status"] == "FAIL" else 0)

if __name__ == "__main__": main()
