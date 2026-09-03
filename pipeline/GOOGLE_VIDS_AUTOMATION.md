# Phase 5 — Google Vids Automation Contract

## Why this is a UI adapter

Google's current public documentation describes Vids creation/editing through the Vids web interface, including object tracks, scene timing, media insertion, animations and export. This project therefore does **not** invent a nonexistent Vids timeline API. Antigravity is the UI automation layer.

Official constraints to respect:
- Landscape is 16:9.
- Vids supports up to 50 video objects and 50 audio objects per video (limits can change).
- Vids videos are limited to 30 minutes for normal editing; longer imported media may need to be shortened first.
- Still images can be animated with photo effects.
- Each image/video/text object has its own timing track.

## Automation contract

Input:

```text
project/
├── google_vids_job.json
├── scenes/
├── audio/
├── ppt/
├── memes/
└── broll/
```

Antigravity should:

1. Open Google Vids in a persistent browser profile.
2. If Google authentication is required, stop and allow the user to authenticate once. Never scrape, store or bypass credentials.
3. Create a new **Landscape / 16:9** Vid.
4. Insert prepared assets from `google_vids_job.json` rather than asking Vids to regenerate them.
5. Build scenes in manifest order.
6. Insert the scene's Veo video as the primary moving visual.
7. Insert meme/B-roll/PPT objects only at the beat offsets specified by the manifest.
8. Use Vids object tracks to set start/end timing.
9. Apply a subtle photo effect to image-only beats so no presentation frame becomes a dead static hold.
10. Add the pre-generated Sarvam audio. Remove/disable any duplicate Vids-generated narration.
11. Add music/SFX at low volume and duck them under narration.
12. Preview the full video.
13. If preview fails a QC rule, do not export; return to the smallest failed scene/asset.
14. Export the final MP4.

## Important editing rule

Vids is the **editor**, not the creative brain for this pipeline. Claude/Gemini create the research, script, beat manifest and prompts. Frame generation creates the visual anchors. Veo creates the motion. Sarvam owns narration timing. Vids assembles and polishes.

## Antigravity implementation notes

Prefer semantic selectors and visible UI labels over CSS class names because Vids UI can change. Keep a small selector map in the automation layer and log every successful action.

Required logs:

```json
{
  "action": "insert_media",
  "scene": "scene_004",
  "beat": "beat_03",
  "asset": "...",
  "result": "success",
  "timestamp": "..."
}
```

If a selector fails:
- retry once after waiting for UI stability;
- capture a screenshot;
- record the failing action;
- stop rather than making destructive guesses.

## Credit-saving policy

Never regenerate media inside Vids if the corresponding local asset already exists. Reuse cached images, Veo clips, memes, PPT slides and Sarvam WAV files.

The only AI generation that should be repeated is the specific asset that failed QC.
