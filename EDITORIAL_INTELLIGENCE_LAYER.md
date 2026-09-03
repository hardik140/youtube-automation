# Hardik Editorial Intelligence Layer v2

## Purpose

This is the production contract for turning narration into a YouTube explainer edit. The primary unit is a **SHOT/BEAT**. A scene is only a grouping of related shots.

```text
TOPIC → RESEARCH → SCRIPT → SARVAM AUDIO → EDITORIAL DIRECTOR → SHOT MANIFEST
→ ASSET DECISION → WORD/PHRASE TIMING → FRAME/VEO → CONTINUITY → DYNAMIC RENDER
→ GOOGLE VIDS → VISUAL QC → EDITORIAL QC → EXPORT
```

## Non-negotiable editorial rules

1. Never use a long scene as one visual.
2. A Ken Burns zoom on one image does not count as meaningful visual variety.
3. Every shot must answer: **What should the viewer SEE while hearing this line?**
4. Prefer an editorially relevant existing asset before generating a new one.
5. Reserve Veo for high-value motion: hero Hardik, demonstrations, emotional reactions, cinematic transitions and reveals.
6. Programmatic graphics handle numbers, comparisons, timelines, diagrams and statistics.
7. Screenshots/documents/maps/photos/news/archive assets handle evidence and context.
8. Memes are punctuation, not filler. They must be attached to a specific narration beat.
9. Adjacent identical visual types are rejected unless an explicit editorial reason exists.
10. Semantic repetition is rejected even when the files differ (for example, the same ₹600 graphic twice).
11. Hardik identity is locked; clothing, environment, pose, camera and lighting are scene variables.
12. The actual last frame of a Veo scene is the authoritative continuity frame for the next scene.
13. No QC result may claim PASS without evidence. Unknown visual/semantic checks are `NOT_EVALUATED`.
14. Failed assets are repaired individually; do not regenerate the entire video.

## Shot manifest contract

Every beat should contain:

- `beat_id`
- `start`, `end`, `duration`
- `narration`
- `editorial_purpose`: hook, narrate, explain, prove, tension, visualize, reveal, transition, conclude
- `visual_question`
- `visual_type`
- `asset_strategy`: `EXISTING_FIRST`, `PROGRAMMATIC`, `VEO`, `MEME`
- `asset`
- `motion`
- `camera`
- `transition_in`
- `transition_out`
- `meme`
- `generation_priority`

## Visual decision matrix

| Narration need | Preferred visual | AI-credit priority |
|---|---|---:|
| Host explanation | Existing/recorded Hardik or short Veo hero | Medium/High |
| Emotional reaction | Hardik Veo | High |
| Physical demonstration | Veo | High |
| Cinematic metaphor | Veo/B-roll | Medium/High |
| Statistic | Programmatic graphic | Low |
| Comparison | Programmatic split/comparison | Low |
| Process | Diagram/animation/B-roll | Low |
| Evidence | Screenshot/document/news/photo | Low |
| Geography | Map | Low |
| Joke/reaction | Meme library | Low |
| UI explanation | Screenshot/screen recording | Low |

## Rhythm targets

Normal explanation: ~1.5–5 seconds per shot.

High-energy/punchline: ~0.8–2.5 seconds.

Deep explanation: up to ~7 seconds only when the visual itself evolves.

A 20-second scene should normally contain multiple editorial shots, not one 20-second asset.

Every ~30 seconds calculate:

- shot count
- visual changes
- unique visual types
- adjacent duplicates
- average shot length
- longest unchanged shot
- HOST/BROLL/GRAPHIC/EVIDENCE/MEME/CINEMATIC percentages
- structural rhythm score

The score is a gate, not proof of artistic quality. Human/multimodal review remains necessary for final publishability.

## Anti-slideshow gate

Reject the edit if any of these occur:

- repeated identical visual type in adjacent shots
- a still image held beyond 7 seconds without meaningful evolution
- the same semantic visual repeated immediately
- long presenter-only stretches without editorial purpose
- graphics used as decoration instead of explanation
- a meme inserted without a narration trigger
- scene-level asset reused for multiple beats

## Continuity

```text
SCENE N START
  ↓
MASTER CHARACTER + references + scene variables
  ↓
START FRAME + END FRAME
  ↓
VEO
  ↓
ACTUAL LAST FRAME
  ↓
SCENE N+1 START FRAME
```

The intended end frame is a target. The extracted final frame is the truth.

## Google Vids

Google Vids is the editing/assembly destination, not the source of editorial intelligence. Feed it a prepared timeline with tracks for main video, B-roll/visuals, memes, graphics, overlays, captions, music and SFX. If browser automation is unavailable, produce a complete Vids-ready manifest and report the remaining manual action honestly.

## QC truth policy

Technical checks can be deterministic. Identity similarity, visual relevance, meme quality, cinematography and caption semantic quality require actual evidence from CV/multimodal analysis or human review. Never manufacture a PASS value.

Allowed states:

- `PASS`
- `FAIL`
- `NOT_EVALUATED`
- `WARNING`

## Credit policy

Do all planning, manifest generation, redundancy detection, timing, graphics and asset reuse before calling an AI generation service. Generate only missing/high-value assets. Cache successful outputs. On failure regenerate the smallest asset possible.
