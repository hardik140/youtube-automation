#!/usr/bin/env python3
"""Phase 6: honest automated production/editorial QC.

Technical checks are deterministic. Visual/semantic checks are NEVER fabricated:
when no actual computer-vision/LLM evidence is available they are NOT_EVALUATED.
The gate fails on missing evidence, structural violations, or known technical faults.
"""
from __future__ import annotations
import argparse, json, subprocess, re
from pathlib import Path
from typing import Any


def probe(path: Path) -> dict[str, Any]:
    p=subprocess.run(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(path)],capture_output=True,text=True)
    if p.returncode!=0:return {"ok":False,"error":p.stderr.strip()}
    d=json.loads(p.stdout); ss=d.get("streams",[]); v=next((s for s in ss if s.get("codec_type")=="video"),None); a=next((s for s in ss if s.get("codec_type")=="audio"),None)
    return {"ok":True,"duration":float(d.get("format",{}).get("duration",0) or 0),"width":int(v.get("width",0)) if v else 0,"height":int(v.get("height",0)) if v else 0,"fps":v.get("r_frame_rate") if v else None,"has_audio":a is not None}

def exists(project: Path, value: str | None) -> bool:
    if not value:return False
    p=Path(value); return (p if p.is_absolute() else project/p).exists()

def rhythm(manifest: dict[str,Any]) -> dict[str,Any]:
    beats=[b for s in manifest.get("scenes",[]) for b in s.get("beats",[])]
    types=[str(b.get("visual_type") or b.get("visual_mode") or "UNKNOWN").upper() for b in beats]
    durations=[float(b.get("duration",0) or 0) for b in beats]
    changes=sum(a!=b for a,b in zip(types,types[1:]))
    adjacent_dup=sum(a==b for a,b in zip(types,types[1:]))
    longest=max(durations or [0])
    unique=len(set(types))
    # Structural score, not a claim about aesthetic quality.
    score=100
    score-=min(35, adjacent_dup*8)
    score-=min(20, max(0, longest-5)*5)
    score+=min(10, max(0, unique-3)*2)
    return {"visual_changes":changes,"shot_count":len(beats),"unique_visual_types":unique,"adjacent_duplicates":adjacent_dup,"average_shot_seconds":round(sum(durations)/len(durations),2) if durations else 0,"longest_shot_seconds":round(longest,2),"structural_rhythm_score":max(0,round(score)),"status":"PASS" if adjacent_dup==0 and longest<=7 else "FAIL"}

def run_qc(manifest: dict[str,Any], project: Path) -> dict[str,Any]:
    errors=[]; warnings=[]; evaluated=[]
    scenes=manifest.get("scenes",[])
    if not scenes: errors.append("NO_SCENES")
    total_beats=sum(len(s.get("beats",[])) for s in scenes)
    if total_beats < 12: errors.append(f"INSUFFICIENT_SHOT_DENSITY: {total_beats} beats")
    for si,s in enumerate(scenes,1):
        beats=s.get("beats",[]); prev=None
        if len(beats)<3: errors.append(f"SCENE_{si}: fewer than 3 shots")
        for b in beats:
            bid=b.get("beat_id","unknown"); vt=str(b.get("visual_type") or b.get("visual_mode") or "UNKNOWN").upper(); d=float(b.get("duration",0) or 0)
            if vt==prev: errors.append(f"ADJACENT_DUPLICATE_VISUAL: {bid}: {vt}")
            if d>7: errors.append(f"LONG_SHOT: {bid}: {d:.2f}s")
            if d<0.8: warnings.append(f"VERY_SHORT_SHOT: {bid}: {d:.2f}s")
            if not b.get("visual_question"): errors.append(f"MISSING_VISUAL_QUESTION: {bid}")
            if not b.get("editorial_purpose"): errors.append(f"MISSING_EDITORIAL_PURPOSE: {bid}")
            prev=vt
        fp=s.get("frame_plan",{})
        if fp.get("required",True) and not fp.get("start_frame"): warnings.append(f"START_FRAME_NOT_GENERATED: scene {si}")
        if si>1 and not fp.get("previous_last_frame"): errors.append(f"BROKEN_CONTINUITY_LINK: scene {si}")
    r=rhythm(manifest); evaluated.append({"name":"structural_rhythm","result":r})
    if r["status"]=="FAIL": errors.append("EDITORIAL_RHYTHM_STRUCTURAL_FAIL")
    # Technical media checks when a rendered output is supplied.
    rendered=manifest.get("rendered_output")
    if rendered:
        p=Path(rendered); p=p if p.is_absolute() else project/p
        info=probe(p)
        if not info.get("ok"): errors.append(f"UNREADABLE_FINAL_VIDEO: {info.get('error','unknown')}")
        else:
            if info["width"]<1280 or info["height"]<720: errors.append("FINAL_VIDEO_LOW_RESOLUTION")
            if not info["has_audio"]: errors.append("FINAL_VIDEO_MISSING_AUDIO")
            evaluated.append({"name":"technical_media","result":info})
    # Never claim semantic/face/meme quality without actual analysis artifacts.
    semantic_checks={"character_identity":"NOT_EVALUATED","visual_relevance":"NOT_EVALUATED","meme_context":"NOT_EVALUATED","cinematography":"NOT_EVALUATED","caption_sync":"NOT_EVALUATED"}
    if manifest.get("visual_qc_evidence"): semantic_checks.update(manifest["visual_qc_evidence"])
    evaluated.append({"name":"semantic_visual_checks","result":semantic_checks})
    warnings.append("Semantic/identity/meme/cinematography checks require real CV or multimodal evidence; no fabricated PASS is emitted.")
    result={"phase":6,"status":"PASS" if not errors else "FAIL","errors":errors,"warnings":warnings,"evaluated":evaluated,"gate_policy":"EXPORT ONLY WHEN TECHNICAL AND STRUCTURAL CHECKS PASS; semantic checks must be PASS or explicitly reviewed","repair_strategy":"regenerate only the smallest failing asset/shot"}
    (project/"qc_report_v2.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    return result

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument("manifest",type=Path); ap.add_argument("project_dir",type=Path); a=ap.parse_args(); r=run_qc(json.loads(a.manifest.read_text(encoding="utf-8")),a.project_dir); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["status"]=="PASS" else 1)
if __name__=="__main__":main()
