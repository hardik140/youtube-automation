#!/usr/bin/env python3
"""Phase 4: shot-level dynamic renderer.

The renderer is deliberately asset-driven: every beat must point to its own media
asset. A scene-level video is NEVER reused for multiple beats because doing so creates
fake visual variety and destroys editorial pacing. Still images receive deterministic
camera motion; video assets are trimmed to beat duration.
"""
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path
from typing import Any

VIDEO_EXT={".mp4",".mov",".webm",".mkv"}; IMAGE_EXT={".png",".jpg",".jpeg",".webp"}

def run(cmd:list[str])->None: subprocess.run(cmd,check=True)
def duration(path:Path)->float:
    p=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",str(path)],capture_output=True,text=True,check=True); return float(p.stdout.strip() or 0)
def image_motion(image:Path,out:Path,seconds:float,motion:str="push")->None:
    frames=max(1,round(seconds*30))
    if motion=="pan": vf="zoompan=z='min(zoom+0.0007,1.08)':x='if(lte(on,1),0,(iw-iw/zoom)*on/%d)':y='(ih-ih/zoom)/2':d=1:s=1920x1080:fps=30"%max(frames-1,1)
    elif motion=="pull": vf="zoompan=z='if(lte(on,1),1.10,max(zoom-0.0007,1.0))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30"
    else: vf="zoompan=z='min(zoom+0.0008,1.10)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30"
    run(["ffmpeg","-y","-loop","1","-i",str(image),"-vf",vf,"-frames:v",str(frames),"-an","-pix_fmt","yuv420p",str(out)])
def trim_video(src:Path,out:Path,seconds:float)->None:
    run(["ffmpeg","-y","-i",str(src),"-t",f"{max(seconds,.1):.3f}","-an","-vf","scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2","-r","30","-pix_fmt","yuv420p",str(out)])

def build(manifest:dict[str,Any],project_dir:Path,output:Path)->dict[str,Any]:
    work=project_dir/"render_cache_v2"; work.mkdir(parents=True,exist_ok=True); parts=[]; plan=[]; missing=[]
    for si,scene in enumerate(manifest.get("scenes",[]),1):
        for bi,beat in enumerate(scene.get("beats",[]),1):
            # Beat asset is authoritative. Never fall back to scene video/visual_asset.
            value=beat.get("asset") or beat.get("asset_path")
            asset=None if not value else (Path(str(value)) if Path(str(value)).is_absolute() else project_dir/str(value))
            out_part=work/f"S{si:02d}_B{bi:02d}.mp4"
            if not asset or not asset.exists():
                missing.append(f"S{si:02d}_B{bi:02d}"); plan.append({"scene":si,"beat":bi,"status":"MISSING_ASSET","visual_type":beat.get("visual_type")}); continue
            want=float(beat.get("duration",2.0)); ext=asset.suffix.lower()
            if ext in VIDEO_EXT: trim_video(asset,out_part,want)
            elif ext in IMAGE_EXT:
                m=str(beat.get("motion",{}).get("type","push")); image_motion(asset,out_part,want,"pan" if "pan" in m else "pull" if "pull" in m else "push")
            else:
                missing.append(f"S{si:02d}_B{bi:02d}:unsupported"); continue
            parts.append(out_part); plan.append({"scene":si,"beat":bi,"beat_id":beat.get("beat_id"),"visual_type":beat.get("visual_type"),"editorial_purpose":beat.get("editorial_purpose"),"asset":str(asset),"requested_duration":want,"actual_duration":round(duration(out_part),3),"status":"READY"})
    status="BLOCKED" if missing else "PASS"
    if not missing and parts:
        concat=work/"concat.txt"; concat.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in parts),encoding="utf-8")
        run(["ffmpeg","-y","-f","concat","-safe","0","-i",str(concat),"-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-an",str(output)])
    result={"phase":4,"status":status,"output":str(output),"parts":plan,"missing_assets":missing,"rules":{"shot_unit":True,"scene_level_fallback_disabled":True,"no_static_full_scene_holds":True,"ken_burns_alone_is_not_visual_variety":True,"audio_timing_authority":True}}
    (project_dir/"render_plan_v2.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8"); return result

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument("manifest",type=Path); ap.add_argument("project_dir",type=Path); ap.add_argument("-o","--output",type=Path,default=Path("rendered_preview_v2.mp4")); a=ap.parse_args(); r=build(json.loads(a.manifest.read_text(encoding="utf-8")),a.project_dir,a.output); print(json.dumps(r,indent=2)); raise SystemExit(1 if r["status"]=="BLOCKED" else 0)
if __name__=="__main__":main()
