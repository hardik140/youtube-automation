# Visual Director — Mandatory Production Rule

The final output must be a **dynamic YouTube explainer/documentary**, not a static slideshow.

## Required pipeline

```text
RESEARCH
→ SCRIPT
→ SARVAM AUDIO
→ ACTUAL AUDIO TIMING
→ SCENE + VISUAL-BEAT BREAKDOWN
→ VIDEO MANIFEST
→ ASSET PLAN
→ START/END FRAME IMAGES FOR VEO SHOTS
→ VEO 3 MOTION SHOTS
→ LAST-FRAME EXTRACTION
→ CONTINUITY CHECK
→ GOOGLE VIDS EDITING
→ QC
→ EXPORT
```

## Anti-slideshow rule

Never map one paragraph or scene to one still image for its full narration duration.

Break narration into **visual beats** whenever the meaning, subject, emotion, evidence or emphasis changes.

Typical rhythm:

```text
HOST → B-ROLL → EVIDENCE → GRAPHIC → HOST REACTION → MEME → NEW VISUAL
```

This is a flexible editorial pattern, not a fixed template.

Staticity guardrails:

- >5 seconds on the same unchanged visual = REVIEW
- >8 seconds = STRONG WARNING
- >10 seconds = REPLAN unless deliberately justified
- A Ken Burns zoom on a still image does not count as meaningful visual variety when the narration has moved to a new idea.

## Narration-first timing

Sarvam audio is the timing authority. Generate/cache the voice, measure its real duration, then build visual beats against that duration.

If phrase/word timestamps are available, use them. Otherwise use semantic sentence boundaries and actual audio duration.

Preserve the existing Sarvam caching behavior so unchanged narration does not consume credits again.

## Visual source priority — lowest AI cost first

Use the cheapest credible medium:

1. Existing reusable asset
2. Existing B-roll / archival footage
3. Existing screenshot / document / photograph
4. Programmatic graphic
5. Existing meme
6. Reusable Hardik image/cutout
7. New AI image
8. Veo 3

Do not use Veo for charts, maps, simple UI, number cards, diagrams or other deterministic graphics.

## Hardik host strategy

Hardik is the recognizable narrative anchor, but he must not remain on screen for the entire video.

Use Hardik for:

- hooks
- interpretation
- emotional reactions
- direct audience communication
- demonstrations
- important transitions

Then move to B-roll, evidence, graphics, maps, documents, screenshots and memes.

The permanent character rule locks identity. Scene variables such as outfit, pose, camera, lighting and environment may change.

## Frame-first Veo rule

For every Veo shot featuring Hardik:

```text
MASTER CHARACTER
+ RELEVANT MULTI-ANGLE REFERENCES
+ SCENE OUTFIT
+ ENVIRONMENT
+ POSE
+ EXPRESSION
+ CAMERA
+ LIGHTING
→ START FRAME
→ END FRAME
→ VEO 3
→ ACTUAL LAST FRAME
```

For physical continuation:

```text
PREVIOUS ACTUAL LAST FRAME
→ NEXT START FRAME
→ VEO 3
```

Do not rewrite the entire character identity manually for every prompt. Load the canonical identity and add only scene-specific variables.

## Meme system

Use `MEME_INTELLIGENCE_GUIDE.md` as the meme decision database.

Every meme insertion must contain:

- meme/source ID
- exact source file
- narrative trigger
- emotion
- joke/function
- start time
- duration
- reason it fits

Do not insert memes simply to fill time. Prefer short reaction inserts, generally around 0.5–2.5 seconds, trimmed to the useful moment.

## Evidence-first rule

For investigative/factual claims:

```text
CLAIM
→ SOURCE / DOCUMENT / SCREENSHOT / DATA
→ HARDIK INTERPRETATION
```

Never fabricate AI-generated evidence and present it as real.

## Graphics rule

Charts, timelines, maps, diagrams, counters and comparisons should be motion-capable. Never leave a full PPT slide unchanged for an entire narration paragraph when the narration contains multiple ideas.

## Editing rule

Google Vids is the preferred editing/orchestration layer for smooth automation.

The Video Manifest remains the deterministic source of truth so the timeline can be rebuilt or rendered by FFmpeg/Remotion/Python if necessary.

The renderer must support **multiple visual beats inside one narration scene**. It must not fall back to one static frame per scene.

## Required visual-beat manifest

```json
{
  "scene_id": "scene_001",
  "audio_file": "scene_001.wav",
  "duration_seconds": 18.4,
  "visual_beats": [
    {
      "start": 0.0,
      "end": 3.2,
      "type": "HOST",
      "asset_mode": "VEO",
      "purpose": "deliver hook"
    },
    {
      "start": 3.2,
      "end": 6.0,
      "type": "EVIDENCE",
      "asset_mode": "EXISTING",
      "purpose": "show proof"
    },
    {
      "start": 6.0,
      "end": 7.7,
      "type": "MEME",
      "asset_mode": "EXISTING",
      "purpose": "reaction",
      "trigger": "exact narration phrase"
    },
    {
      "start": 7.7,
      "end": 12.5,
      "type": "GRAPHIC",
      "asset_mode": "PROGRAMMATIC",
      "purpose": "explain mechanism"
    }
  ]
}
```

## Mandatory QC

```text
[ ] narration fully covered
[ ] visual beats follow semantic changes
[ ] no unjustified static hold
[ ] host is not overused
[ ] B-roll is specific, not generic filler
[ ] evidence shown where relevant
[ ] graphics animate when useful
[ ] memes have exact triggers
[ ] Veo is used only where motion adds value
[ ] Hardik identity is consistent
[ ] continuous shots use actual previous last frame
[ ] music/SFX support the editorial rhythm
[ ] Google Vids timeline is reconstructable from manifest
```

## Failure codes

When output looks static, diagnose before regenerating:

- `S1_ONE_ASSET_TOO_LONG`
- `S2_HOST_OVERUSE`
- `S3_PPT_DOMINANCE`
- `S4_NO_BROLL`
- `S5_NO_EVIDENCE`
- `S6_STATIC_GRAPHICS`
- `S7_RANDOM_MEMES`
- `S8_NO_CAMERA_MOTION`
- `S9_VISUAL_NARRATION_MISMATCH`
- `S10_NO_EDITORIAL_RHYTHM`

Fix the smallest affected layer to conserve AI credits.
