#!/usr/bin/env python3
"""Phase 3: expand a scene manifest into a multi-beat visual manifest.

This stage is deliberately deterministic. It does not call an AI model and therefore
should be run freely during iteration without consuming generation credits.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

VISUAL_CYCLE = ["HOST", "BROLL", "GRAPHIC", "HOST", "MEME", "BROLL"]
PUNCT = re.compile(r"(?<=[.!?।])\s+")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def split_narration(text: str) -> list[str]:
    parts = [p.strip() for p in PUNCT.split(text or "") if p.strip()]
    return parts or ([text.strip()] if text.strip() else [])


def estimate_seconds(text: str, language: str) -> float:
    # Conservative documentary pacing. Audio duration remains the final authority.
    words = len(re.findall(r"\S+", text))
    wpm = 145 if language.lower().startswith("en") else 125
    return max(1.2, words / wpm * 60)


def choose_mode(scene: dict[str, Any], beat_index: int) -> str:
    explicit = scene.get("visual_modes") or scene.get("visual_mode")
    if isinstance(explicit, list) and explicit:
        return str(explicit[beat_index % len(explicit)]).upper()
    if isinstance(explicit, str):
        return explicit.upper()
    st = str(scene.get("scene_type", "")).lower()
    if "ppt" in st or "data" in st or "graphic" in st:
        return "GRAPHIC"
    if "broll" in st:
        return "BROLL"
    if "meme" in st:
        return "MEME"
    return VISUAL_CYCLE[beat_index % len(VISUAL_CYCLE)]


def make_beats(scene: dict[str, Any], index: int, language: str) -> list[dict[str, Any]]:
    text = scene.get("narration_text", "")
    chunks = split_narration(text)
    target = float(scene.get("duration_seconds") or sum(estimate_seconds(x, language) for x in chunks))
    if not chunks:
        chunks = [""]

    # Keep beats substantial enough to read/watch, but prevent long static shots.
    max_beats = 6 if target >= 24 else 5 if target >= 15 else 4 if target >= 9 else 3
    chunks = chunks[:max_beats]
    raw = [estimate_seconds(x, language) for x in chunks]
    total = sum(raw) or 1
    scale = target / total

    beats = []
    cursor = 0.0
    for i, (chunk, duration) in enumerate(zip(chunks, raw)):
        d = round(max(1.6, duration * scale), 2)
        if i == len(chunks) - 1:
            d = round(max(1.6, target - cursor), 2)
        mode = choose_mode(scene, i)
        beats.append({
            "beat_id": f"scene_{index:02d}_beat_{i+1:02d}",
            "start_offset": round(cursor, 2),
            "duration": d,
            "narration": chunk,
            "visual_mode": mode,
            "energy": "high" if i == 0 and index <= 2 else "medium",
            "camera_motion": "micro_push_in" if mode == "HOST" else "parallax_or_pan",
            "motion_required": mode not in {"GRAPHIC"},
            "meme_allowed": mode == "MEME",
            "presentation_allowed": mode == "GRAPHIC",
            "cut_reason": "new_information_or_emotional_beat",
            "asset_status": "pending"
        })
        cursor += d
    return beats


def expand(manifest: dict[str, Any]) -> dict[str, Any]:
    language = manifest.get("project", {}).get("language", "Hindi")
    out = json.loads(json.dumps(manifest))
    scenes = out.get("scenes", [])
    previous_end = None
    for idx, scene in enumerate(scenes, 1):
        scene["beats"] = make_beats(scene, idx, language)
        scene["beat_count"] = len(scene["beats"])
        scene["continuity"] = {
            "previous_scene_end_frame": previous_end,
            "start_frame_strategy": "previous_actual_last_frame" if previous_end else "master_character_reference",
            "end_frame_strategy": "bridge_to_next_scene",
        }
        scene["frame_plan"] = {
            "required": True,
            "start_frame": scene.get("frame_plan", {}).get("start_frame", ""),
            "end_frame": scene.get("frame_plan", {}).get("end_frame", ""),
            "actual_last_frame": scene.get("frame_plan", {}).get("actual_last_frame", ""),
            "previous_last_frame": previous_end,
        }
        previous_end = f"scenes/scene_{idx:03d}/last_frame.png"
    out.setdefault("pipeline", {})["phase3"] = {
        "name": "multi_beat_manifest",
        "deterministic": True,
        "visual_rhythm": "no_long_static_shots",
        "audio_duration_authority": True,
    }
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args()
    data = expand(load(args.manifest))
    output = args.output or args.manifest.with_name(args.manifest.stem + "_multibeat.json")
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
