---
name: hardik-ai-video-factory-phase-3-6
description: Mandatory production-engine overlay for Hardik's AI YouTube factory: multi-beat timelines, dynamic rendering, Google Vids assembly and automated QC.
---

# HARDIK VIDEO FACTORY — PHASE 3–6 ENGINE

Mandatory execution overlay for `hardik-ai-video-factory/SKILL.md`.

## Target

YouTube 16:9, 1080p/4K delivery, 8–15 minutes, Hindi/Hinglish/English, Sarvam narration, photorealistic Hardik, memes + music + SFX. Output must feel like a modern Indian explainer/documentary, **not a slideshow**.

---

# PHASE 3 — MULTI-BEAT MANIFEST

A scene is a sequence of visual beats, not one visual.

**Hard rule:** never let a single still/PPT frame occupy an entire information-heavy narration scene when a dynamic treatment or cutaway is available.

Recommended beat density:
- 5–9s: 2–3 beats
- 10–18s: 3–4 beats
- 19–30s: 4–6 beats
- >30s: 5–8 beats, with a meaningful reset every ~6–9s

Sarvam WAV duration remains the final timing authority.

Beat modes:
`HOST` · `VEO` · `BROLL` · `PPT` · `GRAPHIC` · `MEME` · `SCREEN` · `QUOTE` · `MAP` · `DATA` · `CINEMATIC`

Selection rules:
- new fact → change visual
- new number → data/graphic
- new entity/location → evidence/B-roll
- emotional reaction → Hardik or meme
- punchline/irony → meme immediately after setup
- complex explanation → diagram/PPT with motion
- major reveal → return to Hardik/cinematic hero shot
- long narration → alternate modes rather than holding one frame

Beat object:
```json
{
  "beat_id":"scene_004_beat_03",
  "start_offset":7.4,
  "duration":2.8,
  "narration":"...",
  "visual_mode":"MEME",
  "asset":"memes/example.mp4",
  "camera_motion":"cutaway",
  "energy":"high",
  "cut_reason":"ironic_reaction",
  "meme_allowed":true,
  "presentation_allowed":false,
  "motion_required":true,
  "asset_status":"pending"
}
```

---

# PHASE 3.5 — FRAME-FIRST CONTINUITY

For every important VEO/HOST cinematic scene:

```text
MASTER_CHARACTER.md + minimum relevant angle refs + clothing + environment + previous actual last frame
→ START FRAME IMAGE + END FRAME IMAGE
→ QC
→ VEO
→ EXTRACT ACTUAL LAST FRAME
```

`scene_N.actual_last_frame` is the authoritative input for scene N+1. Never rebuild the whole chain because one scene fails.

Identity is immutable; clothing/environment/camera are mutable. Photorealism is mandatory: natural skin, eyes, hair, hands, fabric, shadows, perspective and lens behavior; no CGI/beauty-filter/plastic look, face warping or identity drift.

---

# PHASE 4 — DYNAMIC RENDERER

The local renderer is the credit-saving deterministic layer. It handles:
- Ken Burns / slow push-in
- lateral pan/parallax
- graphic animation
- PPT camera movement
- meme/B-roll trimming
- audio alignment
- transitions and concat
- preview/proxy generation

It must **never regenerate AI media**.

For still/PPT beats use subtle motion: push, pan, parallax, masked reveal, chart build, count-up, callout animation, crop change or split-screen. Motion supports comprehension; it should not look like a generic template.

Visual hierarchy:
1. Veo/photorealistic Hardik hero shots
2. Real/licensed B-roll and evidence
3. Purpose-built graphics/PPT
4. Memes as punctuation
5. Music/SFX as rhythm

---

# PHASE 5 — GOOGLE VIDS AUTOMATION

Google Vids is the assembly/polish layer. Feed it prepared assets, not vague instructions to recreate the entire video.

```text
MULTI-BEAT MANIFEST → PREPARED MEDIA → VIDS LANDSCAPE PROJECT → INSERT MEDIA → OBJECT TRACK TIMING → ANIMATIONS → SARVAM AUDIO → MUSIC/SFX → PREVIEW → EXPORT
```

Do not use Vids' own narration when approved Sarvam audio exists. Do not regenerate approved Veo/PPT/meme/image assets inside Vids.

Antigravity should use a persistent browser profile. Authentication may be completed manually once; credentials must never be scraped/stored or security controls bypassed. Prefer semantic/visible selectors. On selector failure: retry once, capture screenshot, log failure, stop safely.

Before building, count objects. If the beat count would exceed Vids limits, merge deterministic beats into pre-rendered clips before import.

---

# PHASE 5.5 — MEME SYSTEM

Memes are punctuation, not wallpaper. Use `MEME_INTELLIGENCE_GUIDE.md`.

Every meme needs:
- semantic trigger
- emotion
- narrative function
- insertion point
- target duration
- preceding setup
- following payoff

Preferred timing:
`SETUP → STATEMENT/REVEAL → 0–300ms breathing room → MEME → RETURN TO STORY`

Do not insert a meme merely because a file exists. Avoid repeating the same template family too frequently.

---

# PHASE 6 — AUTOMATED QC

Run QC after every meaningful generation step and before export.

### Asset
- exists and decodes
- valid duration
- expected resolution/aspect ratio
- required audio present
- no zero-byte files

### Character
- identity stable
- correct hair/facial hair/face proportions
- realistic skin/hands
- correct clothing
- no obvious CGI/beauty-filter look

### Continuity
- previous actual last frame linked to next start frame
- clothing stable inside continuous moments
- no unexplained environment/lighting jump
- physically plausible camera movement

### Timing / pacing
- beats cover narration
- no unexplained gaps
- memes do not cover important words
- no long static information hold
- no repeated visual mode >2 times without reason
- flag >9s without meaningful visual change in information-heavy sections

### Vids
- 16:9
- object counts within current limits
- Sarvam audio present
- duplicate narration absent
- scene order matches manifest
- critical beats present

### Repair principle
**Regenerate the smallest possible unit.** Bad face → frame. Bad motion → Veo scene. Bad meme → meme only. Bad timing → manifest/renderer. Broken Vids automation → adapter only.

---

# LOW-CREDIT RULE

```text
Claude/Gemini → research, reasoning, script, beat planning
Sarvam → narration
Image generation → required start/end anchors
Veo → high-value moving hero shots
PPT/graphics → deterministic/local
Memes/B-roll → existing or licensed assets
Renderer → deterministic motion
Google Vids → assembly/polish
QC → deterministic validation
```

Never spend an AI credit on work FFmpeg/Pillow/Vids can perform deterministically.

## Commands

```bash
python pipeline/phase3_multibeat_manifest.py <manifest.json> -o <multibeat.json>
python pipeline/dynamic_renderer.py <multibeat.json> <project_dir> -o <preview.mp4>
python pipeline/google_vids_automation.py <multibeat.json> <project_dir>
python pipeline/automated_qc.py <multibeat.json> <project_dir>
```
