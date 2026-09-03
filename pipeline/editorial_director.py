#!/usr/bin/env python3
"""Editorial Intelligence Layer.

Turns a scene/narration manifest into shot-level editorial decisions. This module is
credit-free: it does not call an image/video model. Claude/Gemini can enrich the
result later, but the deterministic layer guarantees useful defaults, timing,
asset-source priorities, and anti-slideshow constraints.
"""
from __future__ import annotations

import argparse, json, re
from pathlib import Path
from typing import Any

PUNCT = re.compile(r"(?<=[.!?।])\s+")

VISUAL_TYPES = ["HOST", "BROLL", "GRAPHIC", "EVIDENCE", "MEME", "CINEMATIC", "PHOTO", "SCREENSHOT", "MAP", "DOCUMENT", "PRESENTATION"]


def split_text(text: str) -> list[str]:
    return [x.strip() for x in PUNCT.split(text or "") if x.strip()]


def purpose(text: str) -> str:
    t = text.lower()
    if any(x in t for x in ["because", "how", "works", "process", "means", "kaise", "kyun", "system"]):
        return "explain"
    if any(x in t for x in ["₹", "%", "crore", "lakh", "million", "billion", "number", "data", "share"]):
        return "prove"
    if any(x in t for x in ["but", "however", "lekin", "problem", "danger", "risk", "scam", "freeze"]):
        return "tension"
    if any(x in t for x in ["imagine", "socho", "what if", "suppose"]):
        return "visualize"
    return "narrate"


def choose_visual(text: str, i: int, previous: str | None, scene: dict[str, Any]) -> str:
    t = text.lower()
    if any(x in t for x in ["screenshot", "website", "app", "phone", "upi", "dashboard"]):
        candidate = "SCREENSHOT"
    elif any(x in t for x in ["₹", "%", "crore", "lakh", "million", "billion", "data", "share", "cost"]):
        candidate = "GRAPHIC"
    elif any(x in t for x in ["law", "notice", "document", "rule", "section", "report"]):
        candidate = "DOCUMENT"
    elif any(x in t for x in ["map", "city", "country", "india", "state", "region"]):
        candidate = "MAP"
    elif purpose(text) == "tension":
        candidate = "CINEMATIC"
    elif i == 0 or i % 5 == 0:
        candidate = "HOST"
    else:
        candidate = "BROLL"
    # Avoid adjacent identical categories unless the source explicitly requests it.
    if candidate == previous:
        for alt in ["BROLL", "GRAPHIC", "HOST", "CINEMATIC"]:
            if alt != previous:
                candidate = alt
                break
    return candidate


def duration_for(text: str, target_total: float) -> float:
    words = max(1, len(re.findall(r"\S+", text)))
    return max(1.25, words / 135 * 60)


def build_scene(scene: dict[str, Any], idx: int) -> dict[str, Any]:
    chunks = split_text(scene.get("narration_text", "")) or [""]
    target = float(scene.get("duration_seconds") or sum(duration_for(c, 0) for c in chunks))
    # More editorial cuts than the old 4–6 beat ceiling, while keeping the pilot manageable.
    max_beats = max(5, min(10, round(target / 2.8)))
    if len(chunks) > max_beats:
        # Split long sentences into comma/connector clauses before falling back to fewer beats.
        expanded = []
        for c in chunks:
            expanded.extend([p.strip() for p in re.split(r"[,;:—–]|\s+(?:but|and|लेकिन|लेकिन फिर|because|और)\s+", c, flags=re.I) if p.strip()])
        chunks = expanded or chunks
    chunks = chunks[:max_beats]
    raw = [duration_for(c, target) for c in chunks]
    scale = target / max(sum(raw), 0.01)
    beats = []
    cursor = 0.0
    previous = None
    for i, text in enumerate(chunks, 1):
        d = max(1.15, raw[i-1] * scale)
        if i == len(chunks): d = max(1.15, target - cursor)
        visual = choose_visual(text, i - 1, previous, scene)
        p = purpose(text)
        meme = p in {"tension", "narrate"} and any(x in text.lower() for x in ["but", "lekin", "seriously", "really", "scam", "freeze", "problem", "danger", "absurd"])
        beats.append({
            "beat_id": f"S{idx:02d}_B{i:02d}",
            "start": round(cursor, 3), "end": round(cursor + d, 3), "duration": round(d, 3),
            "narration": text,
            "editorial_purpose": p,
            "visual_question": f"What should the viewer SEE while hearing: {text}",
            "visual_type": "MEME" if meme else visual,
            "asset_strategy": "EXISTING_FIRST",
            "motion": {"required": visual not in {"DOCUMENT", "GRAPHIC", "SCREENSHOT", "PHOTO"}, "type": "editorial_cut_or_camera_motion"},
            "camera": {"shot": "medium" if visual == "HOST" else "contextual", "movement": "natural_cut" if visual != "HOST" else "subtle_dolly_or_push"},
            "meme": {"allowed": True, "required": False, "reason": "emotional/comedic punctuation"} if meme else {"allowed": True, "required": False},
            "transition_in": "hard_cut" if i > 1 else "cold_open",
            "transition_out": "match_cut" if i < len(chunks) else "bridge_to_next",
            "asset": scene.get("visual_asset") if i == 1 else None,
            "generation_priority": "HIGH" if visual in {"HOST", "CINEMATIC"} else "LOW"
        })
        cursor += d; previous = visual
    return {**scene, "beats": beats, "beat_count": len(beats), "editorial_version": 2}


def build(manifest: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(manifest))
    out["scenes"] = [build_scene(s, i) for i, s in enumerate(out.get("scenes", []), 1)]
    total = sum(len(s["beats"]) for s in out["scenes"])
    out.setdefault("pipeline", {})["editorial_intelligence"] = {
        "version": "2.0",
        "unit": "shot_beat",
        "scene_is_grouping_only": True,
        "target_visual_beats": total,
        "existing_first": True,
        "veo_reserved_for_high_value_motion": True,
        "semantic_ai_review": "recommended_before_generation"
    }
    return out


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("manifest", type=Path); ap.add_argument("-o", "--output", type=Path)
    a = ap.parse_args(); out = build(json.loads(a.manifest.read_text(encoding="utf-8")))
    p = a.output or a.manifest.with_name(a.manifest.stem + "_editorial.json"); p.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"); print(p)

if __name__ == "__main__": main()
