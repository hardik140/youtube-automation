# Phase 3–6 Implementation

This branch adds the production engine for the Hardik AI Video Factory.

## Pipeline

```text
RESEARCH
  ↓
SCRIPT
  ↓
SCENE BREAKDOWN
  ↓
PHASE 3: MULTI-BEAT MANIFEST
  ↓
FRAME-FIRST START/END IMAGES
  ↓
VEO SCENES + ACTUAL LAST FRAME EXTRACTION
  ↓
PHASE 4: DYNAMIC LOCAL RENDER/PREVIEW
  ↓
PHASE 5: GOOGLE VIDS UI ASSEMBLY VIA ANTIGRAVITY
  ↓
PHASE 6: AUTOMATED QC
  ↓
FINAL EXPORT
```

## Files

- `.agents/skills/hardik-ai-video-factory/PHASE_3_6_ENGINE.md` — mandatory skill overlay.
- `pipeline/phase3_multibeat_manifest.py` — converts long scenes into timed visual beats without AI calls.
- `pipeline/dynamic_renderer.py` — deterministic motion/assembly for stills and media.
- `pipeline/extract_last_frame.py` — extracts the actual final frame used as the next scene's continuity anchor.
- `pipeline/google_vids_automation.py` — builds the Vids UI automation job manifest.
- `pipeline/GOOGLE_VIDS_AUTOMATION.md` — Antigravity operating contract.
- `pipeline/automated_qc.py` — cheap deterministic QC and smallest-unit repair reporting.
- `pipeline/run_phases_3_6.py` — deterministic orchestration.

## Why the architecture changed

The previous pipeline was scene-centric. A 20-second narration could therefore become one static visual. The new pipeline is **beat-centric**: new information, emotional changes and punchlines create visual changes.

AI generation is reserved for high-value assets. PPT motion, image movement, trimming, concat, object timing and validation remain deterministic.

## Google Vids note

The current Google documentation describes Vids editing through its web UI, object tracks, animations and media insertion; this implementation therefore uses Antigravity/browser automation rather than inventing an unsupported public Vids timeline API. Vids currently documents limits of up to 50 video objects and 50 audio objects per video, and normal editing is limited to 30 minutes. These limits can change.

## Recommended production behavior

For an 8–15 minute video, do not import hundreds of tiny beats into Vids. First merge deterministic micro-beats into sensible scene-level clips when necessary. Keep the rich beat manifest as the source of truth while keeping Vids object count manageable.
