---
name: hardik-editorial-video-factory
description: >-
  Editorial-first, shot-level AI YouTube production system for Hardik. Rebuilds the old scene/slide workflow into a real explainer-video pipeline using narration-driven editorial decisions, photorealistic Hardik, Veo frame anchors, evidence/B-roll, programmatic graphics, memes, Sarvam voice, dynamic rendering, Google Vids finishing, and evidence-based QC.
---

# HARDIK — EDITORIAL VIDEO FACTORY
## V3 Production Skill — Shot/Beat First, Editorial Intelligence First

Version: 3.0
Status: **PRIMARY VIDEO PRODUCTION SKILL**

---

# 0. MISSION

Create YouTube explainer/documentary videos that feel **professionally edited**, not like AI-generated PowerPoint presentations.

The system must produce:

- a strong narrative
- natural Hardik presence
- frequent meaningful visual change
- cinematic B-roll
- evidence and screenshots where appropriate
- programmatic graphics for data
- memes as editorial punctuation
- occasional high-value Veo shots
- controlled camera movement
- purposeful cuts
- sound design
- music that supports the story
- continuity between AI-generated shots
- clean 16:9 delivery
- low unnecessary AI-credit consumption

The target is a modern Indian YouTube explainer/documentary language: energetic, investigative, visual, conversational, evidence-led and occasionally humorous.

The supplied reference videos are **style references only**. Extract high-level editorial principles such as pacing, visual density, evidence use, host/B-roll alternation, graphic language, tension and humor. Do not reproduce any creator's exact script, wording, signature scene, thumbnail, voice, branding or proprietary identity.

Reference URLs supplied for this project:

- https://youtu.be/54oQFGJ-xAI
- https://youtu.be/MnRjwvQJa6I
- https://youtu.be/8-DRXgPbKH0

Local/reference videos and existing repository assets must be inspected when available.

---

# 1. HARD RULE: THIS IS A VIDEO EDITOR, NOT A PRESENTATION GENERATOR

The previous failure mode was:

```text
Narration
  ↓
Scene
  ↓
Slide
  ↓
Ken Burns zoom
```

This is forbidden as the default production architecture.

The new architecture is:

```text
TOPIC
  ↓
RESEARCH
  ↓
STORY / SCRIPT
  ↓
SARVAM NARRATION
  ↓
EDITORIAL DIRECTOR
  ↓
SHOT / BEAT MANIFEST
  ↓
VISUAL DECISION ENGINE
  ↓
ASSET SELECTION / GENERATION
  ↓
FRAME ANCHORS FOR VEO WHEN REQUIRED
  ↓
SHOT GENERATION
  ↓
ACTUAL LAST-FRAME EXTRACTION
  ↓
CONTINUITY
  ↓
DYNAMIC TIMELINE
  ↓
GOOGLE VIDS FINISHING
  ↓
VISUAL + EDITORIAL QC
  ↓
FINAL VIDEO
```

A **scene is only a chapter/grouping**.

The production unit is:

> **SHOT / BEAT**

Typical shot duration:

- high-energy: 0.8–2.5 sec
- normal explainer: 1.5–5 sec
- cinematic explanation: 2–7 sec
- longer than 7 sec only when the image/video itself is genuinely evolving

A 20-second scene must normally contain multiple shots.

---

# 2. TARGET CHANNEL PROFILE

Platform: YouTube

Aspect ratio: 16:9

Delivery: 1080p minimum; 4K when source assets support it

Typical duration: 8–15 minutes

Languages: Hindi / Hinglish / English

Voice: Sarvam AI

Host: Hardik

Host representation: photorealistic AI-generated Hardik

Captions: enabled when requested by project profile

Memes: enabled

Music: enabled

SFX: enabled

Primary audience expectation:

> A viewer should feel that a human creator planned, investigated, shot and edited the video, even though AI and automation perform most production work.

---

# 3. HARDIK CREATOR IDENTITY

Hardik is a young Indian builder, investigator and explainer.

He should feel:

- intelligent
- curious
- modern
- skeptical when appropriate
- conversational
- confident
- approachable
- investigative
- occasionally funny
- emotionally responsive to discoveries

Do not turn him into:

- a TV news anchor
- a generic AI presenter
- an angry commentator
- a permanently shocked influencer
- a glossy CGI avatar
- a static talking head

Hardik's expression must follow the narrative.

Examples:

```text
mystery → curiosity
bad evidence → skepticism
major reveal → controlled surprise
absurd situation → dry amusement
serious human consequence → restrained seriousness
solution → confidence / clarity
```

---

# 4. MASTER CHARACTER SYSTEM

The canonical identity files are authoritative:

```text
character/
├── MASTER_CHARACTER.md
└── references/
    ├── front.jpg
    ├── left.jpg
    ├── right.jpg
    ├── three_quarter_left.jpg
    ├── three_quarter_right.jpg
    ├── profile_left.jpg
    ├── profile_right.jpg
    ├── closeup.jpg
    └── fullbody.jpg
```

Also respect:

```text
CHARACTER_IDENTITY_LOCK.md
Master_Character_Identity_Reference.pdf
```

Identity locks:

- facial structure
- skin tone
- age appearance
- hair identity
- facial hair pattern
- body proportions
- recognizable facial landmarks

Scene variables may change:

- clothing
- environment
- pose
- camera
- lighting
- accessories
- expression

Never manually rewrite a giant character description into every prompt. Build scene prompts from the canonical identity plus only the required scene variables.

---

# 5. PHOTOREALISM IS A HARD REQUIREMENT

The character is not an avatar.

Target:

> **A photorealistic representation of the creator captured by a real camera.**

Prioritize:

- realistic skin texture
- natural facial proportions
- realistic eyes
- natural hair
- realistic hands
- realistic fabric
- physically plausible lighting
- real lens characteristics
- natural shadows
- believable depth of field
- natural body motion
- believable facial expressions
- realistic reflections
- small natural imperfections

Reject:

- plastic skin
- CGI appearance
- beauty-filter skin
- over-smoothed pores
- artificial symmetry
- warped facial features
- deformed hands
- identity drift
- excessive sharpening
- fake cinematic haze
- impossible perspective
- mannequin movement

---

# 6. EDITORIAL INTELLIGENCE LAYER

After narration is generated, the Editorial Director must ask for every narration segment:

> **What should the viewer SEE while hearing this?**

Never start by asking:

> "What slide should I show?"

The correct decision hierarchy is:

```text
1. What is being said?
2. Why is it being said here?
3. What should the viewer understand/feel?
4. What visual best communicates that?
5. Is a useful existing asset available?
6. If not, can it be generated cheaply?
7. Does it require Veo?
8. What is the shortest effective shot duration?
9. What is the best transition into the next beat?
```

Every beat must have:

```json
{
  "beat_id": "S02_B07",
  "start": 13.4,
  "end": 15.8,
  "duration": 2.4,
  "narration": "...",
  "editorial_purpose": "explain",
  "visual_question": "What should the viewer see while hearing this?",
  "visual_type": "CINEMATIC_BROLL",
  "asset_strategy": "EXISTING_FIRST",
  "asset": "",
  "motion_required": true,
  "camera": "",
  "transition_in": "hard_cut",
  "transition_out": "match_cut",
  "meme": false,
  "generation_priority": "medium"
}
```

---

# 7. VISUAL DECISION ENGINE

Use this matrix before generating anything.

| Narrative need | Preferred visual | AI priority |
|---|---|---:|
| Host makes an important argument | Hardik hero shot | High |
| Host reacts emotionally | Hardik Veo | High |
| Physical demonstration | Veo | High |
| Cinematic metaphor | Veo / real B-roll | Medium |
| Real-world evidence | screenshot / document / footage | Low |
| Person/entity mentioned | relevant photo/footage | Low |
| Place mentioned | real footage / map / photo | Low |
| Statistic | programmatic graphic | Very Low |
| Comparison | split-screen graphic | Very Low |
| Timeline | animated timeline | Very Low |
| Process | diagram / animated flow | Very Low |
| Website/app explanation | screen recording | Low |
| Emotional punctuation | meme / reaction | Very Low |
| Transition | short cinematic bridge | Medium |

Rule:

> **Do not spend Veo credits on visuals that can be communicated better with an existing asset or deterministic graphics.**

---

# 8. VISUAL DENSITY STANDARD

The video must feel alive without becoming chaotic.

Default target:

```text
0–10 sec      4–7 meaningful visual changes
10–30 sec     6–12 shots
30–60 sec     10–18 shots
```

These are targets, not mathematical laws. Editorial meaning always wins.

Never force cuts merely to hit a number.

However, reject long stretches where nothing meaningfully changes.

Hard warning:

> **A Ken Burns movement on a still image does not count as a new visual idea.**

---

# 9. VISUAL RHYTHM

Build rhythm through changes in:

- shot size
- camera angle
- subject
- motion
- location
- texture
- visual medium
- color/contrast
- evidence vs interpretation
- host vs environment
- real footage vs generated footage
- graphic vs cinematic imagery

Healthy sequence example:

```text
HARDIK MEDIUM
→ CUTAWAY B-ROLL
→ SCREENSHOT
→ GRAPHIC
→ HARDIK CLOSEUP
→ CINEMATIC B-ROLL
→ MEME
→ EVIDENCE
→ HARDIK REACTION
```

Unhealthy sequence:

```text
SLIDE
→ SLIDE
→ SLIDE
→ SLIDE
→ SLIDE
```

Also unhealthy:

```text
HARDIK
→ HARDIK
→ HARDIK
→ HARDIK
```

unless the editorial intent specifically calls for a sustained host section.

---

# 10. ANTI-SLIDESHOW SYSTEM

The system must reject:

- a still held for more than 7 sec without meaningful evolution
- multiple adjacent presentation cards
- repeated template backgrounds
- repeated identical charts
- repeated semantic visuals
- presenter-only stretches without purpose
- a full scene represented by one asset
- zoom-only motion masquerading as editing
- graphics used merely as decoration

A presentation asset may appear, but it is one visual layer among many.

Do not let the PPT become the video.

---

# 11. PPT / NOTEBOOKLM RULE

NotebookLM or other presentation-generation tools may produce explanatory assets.

They must NOT define the final edit.

Use presentation assets for:

- dense concepts
- structured comparison
- data
- diagrams
- timelines
- evidence summaries
- system architecture

Then break them into visually useful shots.

Example:

```text
Bad:
20 sec full slide

Good:
2.2 sec title/detail
1.8 sec zoom to key number
2.0 sec highlighted evidence
2.4 sec cut to real-world B-roll
1.6 sec host reaction
```

The final timeline must remain an editorial video, not a slide deck.

---

# 12. HOST USAGE

Hardik is a recurring character, not a wallpaper.

Use host shots when they add:

- personality
- explanation
- reaction
- narrative transition
- credibility
- direct address
- emotional framing

Do not generate Hardik for every beat.

Use a mix of:

- medium shot
- medium close-up
- close-up
- three-quarter angle
- profile
- walking shot
- seated shot
- environmental shot
- reaction shot
- over-the-shoulder shot

Do not repeat the same camera/framing for consecutive host shots.

---

# 13. FRAME-FIRST VEO SYSTEM

For every important Veo shot involving Hardik or continuity-sensitive cinematic footage:

```text
MASTER CHARACTER
+
MULTI-ANGLE REFERENCES
+
SCENE VARIABLES
+
START FRAME
+
END FRAME / MOTION INTENT
↓
VEO
↓
ACTUAL LAST FRAME
```

## Start frame

The start frame defines:

- identity
- camera
- framing
- pose
- expression
- clothing
- environment
- lighting
- composition

## End frame

The end frame defines:

- final position
- final expression
- final camera state
- final environment state
- final composition

It should be designed as a bridge into the next shot where continuity matters.

## Authoritative continuity rule

The generated end-frame image is only the target.

The **actual extracted last frame from the generated video is the truth**.

Therefore:

```text
VEO VIDEO
 ↓
EXTRACT ACTUAL LAST FRAME
 ↓
QC
 ↓
NEXT START FRAME
```

Never pretend that the intended end frame equals the actual final frame.

---

# 14. CONTINUITY MODES

Every AI shot declares one of:

### HARD_CONTINUITY

Next shot must visually continue the exact physical moment.

Use actual last frame as reference.

### SOFT_CONTINUITY

Same location/time/character state, but camera may change.

### EDITORIAL_CUT

No physical continuity required.

### MATCH_CUT

Next shot intentionally matches shape, movement, object or composition.

### TIME_JUMP

Continuity intentionally breaks.

This prevents the system from forcing unnatural continuity everywhere.

---

# 15. MEME INTELLIGENCE

Memes are editorial punctuation.

Never insert a meme merely because a meme exists.

Every meme requires:

- trigger narration
- emotional purpose
- semantic relevance
- appropriate intensity
- expected duration
- transition in/out

Use the repository meme intelligence guide:

```text
MEME_INTELLIGENCE_GUIDE.md
```

The meme library must be searchable by:

- emotion
- scenario
- topic
- punchline type
- irony
- frustration
- disbelief
- confusion
- success
- failure
- absurdity
- hypocrisy
- corporate greed
- shock
- awkwardness
- overconfidence
- reaction

Preferred meme duration:

```text
0.7–2.5 sec
```

Longer only when the source meme itself requires setup/payoff.

Do not stack memes repeatedly.

A meme should normally follow a narrative trigger such as:

```text
"And then the company said..."
        ↓
MEME
```

or

```text
Unexpected reveal
        ↓
HARDIK REACTION / MEME
```

---

# 16. EVIDENCE-FIRST EDITING

For investigative topics, visuals should distinguish:

- claim
- evidence
- interpretation
- uncertainty

Whenever possible, show the actual source:

- article screenshot
- document excerpt
- public filing
- chart
- official statement
- map
- photograph
- screen recording

Do not manufacture fake evidence-looking graphics.

If a visual is illustrative rather than factual, mark it internally as `ILLUSTRATIVE`.

---

# 17. PROGRAMMATIC GRAPHICS

Use deterministic rendering for:

- counters
- percentages
- timelines
- arrows
- comparisons
- formulas
- charts
- process diagrams
- maps when source data exists
- highlighted text
- UI mockups

Graphics must explain something.

Avoid generic:

```text
DARK BACKGROUND
+ BOX
+ LARGE NUMBER
+ SLIDE-IN
```

unless the design itself communicates useful hierarchy.

Graphics should visually evolve:

```text
baseline
→ change
→ highlight
→ consequence
```

not simply appear as static cards.

---

# 18. B-ROLL STRATEGY

Prefer real/relevant assets whenever possible.

B-roll should be chosen for semantic specificity.

Bad:

> generic person using laptop

Good:

> close-up of the exact app/interface/system being discussed

Bad:

> generic city footage

Good:

> recognizable location connected to the story

B-roll must have a reason to exist.

---

# 19. SARVAM AUDIO IS THE TIMING AUTHORITY

Generate narration before final visual timing.

Pipeline:

```text
SCRIPT
 ↓
SARVAM
 ↓
WAV
 ↓
MEASURE ACTUAL DURATION
 ↓
WORD / PHRASE TIMING MAP
 ↓
SHOT TIMELINE
```

Do not guess durations from character count.

Cache unchanged audio.

If the narration text has not changed, do not regenerate it.

---

# 20. WORD / PHRASE MAP

The editorial director should divide narration into meaningful units:

```json
{
  "phrase_id": "P17",
  "start": 22.41,
  "end": 24.08,
  "text": "UPI transaction cost",
  "semantic_role": "key_concept",
  "visual_need": "graphic"
}
```

Visual changes should often happen on:

- nouns
- numbers
- names
- revelations
- contrasts
- verbs indicating action
- punchlines
- questions

Do not cut mechanically on every word.

---

# 21. SHOT MANIFEST

The manifest is the source of truth.

Required project fields:

```json
{
  "project": {
    "id": "",
    "topic": "",
    "title": "",
    "language": "",
    "aspect_ratio": "16:9",
    "resolution": "1920x1080",
    "target_duration": 600
  },
  "style_profile": {
    "mode": "modern_indian_explainer",
    "energy": "dynamic",
    "humor": "strategic",
    "evidence_density": "high",
    "visual_density": "high"
  },
  "character": {
    "id": "hardik_main",
    "master_file": "character/MASTER_CHARACTER.md",
    "references": "character/references/"
  },
  "audio": {
    "provider": "sarvam",
    "voice_id": "",
    "duration": 0,
    "word_map": []
  },
  "shots": []
}
```

Shot schema:

```json
{
  "shot_id": "S02_B07",
  "scene_id": "S02",
  "start": 13.4,
  "end": 15.8,
  "duration": 2.4,
  "narration_range": {
    "start": 13.4,
    "end": 15.8,
    "text": "..."
  },
  "editorial_purpose": "explain",
  "visual_question": "What should the viewer see?",
  "visual_type": "CINEMATIC_BROLL",
  "asset_strategy": "EXISTING_FIRST",
  "asset": "",
  "motion": {
    "required": true,
    "type": "slow_dolly"
  },
  "camera": {
    "shot": "medium",
    "lens": "50mm",
    "movement": "slow_push"
  },
  "character": {
    "present": false,
    "clothing": "",
    "expression": ""
  },
  "frame_plan": {
    "required": false,
    "start_frame": "",
    "end_frame": "",
    "previous_last_frame": "",
    "continuity_mode": "EDITORIAL_CUT"
  },
  "meme": {
    "enabled": false,
    "asset": "",
    "duration": 0,
    "trigger": ""
  },
  "transition_in": "hard_cut",
  "transition_out": "hard_cut",
  "audio": {
    "music": "continue",
    "sfx": []
  },
  "qc": {
    "status": "NOT_EVALUATED"
  }
}
```

---

# 22. EDITORIAL DIRECTOR ALGORITHM

Before generating visual assets, perform this exact reasoning sequence:

### Step A — Segment narration

Split into meaningful beats, not arbitrary sentence lengths.

### Step B — Assign editorial purpose

Choose one:

```text
HOOK
QUESTION
CONTEXT
EXPLAIN
PROVE
COMPARE
ESCALATE
REVEAL
REACTION
HUMOR
TRANSITION
CONCLUDE
```

### Step C — Ask the visual question

> What does the viewer need to SEE right now?

### Step D — Choose visual type

Choose from:

```text
HOST
CINEMATIC_BROLL
REAL_BROLL
PHOTO
DOCUMENT
SCREENSHOT
SCREEN_RECORDING
MAP
PROGRAMMATIC_GRAPHIC
TIMELINE
DIAGRAM
MEME
VEO_CINEMATIC
VEO_HOST
TRANSITION
```

### Step E — Choose cheapest acceptable asset

```text
existing asset
→ deterministic graphic
→ existing host asset
→ image generation
→ Veo
```

### Step F — Set shot duration

Duration follows narration and visual complexity.

### Step G — Check adjacent shots

Reject semantic repetition.

### Step H — Check 30-second rhythm

Compute rhythm metrics.

### Step I — Only then generate assets

Planning must precede generation.

---

# 23. SEMANTIC REDUNDANCY DETECTOR

The system must detect semantic repetition, not only filenames.

Examples of rejection:

```text
₹600 graphic
→ another ₹600 graphic
```

```text
phone payment graphic
→ slightly different phone payment graphic
```

```text
Hardik medium shot
→ Hardik medium shot
```

A visual is considered meaningfully different only when at least one important dimension changes:

- information
- subject
- perspective
- action
- emotional state
- environment
- visual metaphor

---

# 24. EDITORIAL RHYTHM SCORE

Every 30 seconds calculate:

```text
shot_count
visual_change_count
unique_visual_types
adjacent_duplicate_count
semantic_duplicate_count
average_shot_length
longest_unchanged_duration
host_percentage
broll_percentage
graphic_percentage
evidence_percentage
meme_percentage
cinematic_percentage
static_hold_percentage
```

Then produce:

```json
{
  "rhythm_score": 0,
  "shot_variety": 0,
  "visual_relevance": 0,
  "host_balance": 0,
  "evidence_density": 0,
  "meme_timing": 0,
  "staticity": 0,
  "narration_sync": 0,
  "status": "NOT_EVALUATED"
}
```

A score is not proof of artistic quality.

Multimodal/human review is required for final publication.

Suggested gate:

```text
< 75  → FAIL
75–84 → WARNING / REWORK
85–91 → PASS CANDIDATE
92+   → STRONG PASS CANDIDATE
```

Never claim final publishability from a numeric score alone.

---

# 25. QC TRUTH POLICY

QC must never fabricate evidence.

Allowed states:

```text
PASS
FAIL
WARNING
NOT_EVALUATED
```

Technical checks can be deterministic:

- file exists
- duration
- resolution
- codec
- audio presence
- audio/video duration mismatch
- black frames
- missing assets
- corrupted media
- duplicate files

Visual/editorial checks require actual analysis:

- character identity
- visual relevance
- cinematography
- semantic repetition
- meme appropriateness
- pacing
- realism
- continuity
- storytelling quality

If the system did not actually inspect it:

> `NOT_EVALUATED`

Never write:

```json
{"status":"PASS"}
```

just because the render completed.

---

# 26. LOW-CREDIT GENERATION POLICY

AI generation is the expensive layer.

Do all cheap reasoning first:

```text
research
→ script
→ audio
→ phrase map
→ shot manifest
→ asset matching
→ redundancy detection
→ deterministic graphics
→ frame planning
→ generation
```

Never generate:

- decorative B-roll without a purpose
- Hardik for every beat
- multiple versions before QC
- Veo footage when an existing asset works
- images that can be represented with a simple graphic

Cache:

- Sarvam audio
- start frames
- end frames
- generated host assets
- B-roll
- graphics
- memes
- final clips

Regenerate only the smallest failed asset.

---

# 27. GOOGLE VIDS ROLE

Google Vids is the finishing/editing destination.

It is not the editorial brain.

The system should prepare a Vids-ready timeline with tracks for:

```text
MAIN VIDEO
B-ROLL
EVIDENCE
MEMES
GRAPHICS
HOST
OVERLAYS
CAPTIONS
MUSIC
SFX
```

Google Vids should receive already-decided:

- clip order
- timing
- transitions
- asset paths
- audio timing
- captions
- music cues
- SFX cues

If browser automation is unavailable, generate a complete deterministic Vids-ready manifest and state exactly what remains manual.

Never claim that Google Vids performed an action unless the automation actually performed it.

---

# 28. DYNAMIC RENDERING

The renderer must operate from the shot manifest.

It must support:

- hard cuts
- short dissolves where appropriate
- match cuts
- push/slide transitions sparingly
- crop/reframe
- subtle scale movement
- pan
- masked reveals
- split screens
- overlays
- picture-in-picture
- evidence highlights
- graphic animation
- meme insertion
- music ducking
- SFX timing

Do not apply one transition preset to the entire video.

Transitions are editorial decisions.

Default should often be a clean hard cut.

---

# 29. MUSIC

Music should support narrative structure.

Use:

```text
HOOK → immediate energy
INVESTIGATION → restrained tension
EXPLANATION → low distraction
REVEAL → controlled lift
SERIOUS CONSEQUENCE → minimal / emotional
CONCLUSION → resolution
```

Music must not fight Sarvam narration.

Duck music under narration.

Avoid generic constant cinematic music across the entire video.

---

# 30. SFX

Use SFX for meaning, not decoration.

Examples:

- UI click
- notification
- cash/register sound
- impact on reveal
- whoosh for intentional motion
- subtle transition hit
- glitch only when conceptually justified

Avoid excessive whooshes.

---

# 31. CAPTIONS

Captions are optional by project profile but should be supported.

When enabled:

- sync to actual Sarvam timing
- prioritize readability
- avoid covering important evidence
- use emphasis selectively
- never turn every word into a giant animated caption

---

# 32. REFERENCE VIDEO STUDY PROTOCOL

When reference videos are supplied, do not merely say they are "cinematic".

Extract measurable/high-level traits:

```text
average shot length
shot-length range
host percentage
B-roll percentage
graphic percentage
meme/reaction frequency
evidence frequency
camera variety
close-up frequency
wide-shot frequency
visual changes per 30 sec
use of hard cuts
use of transitions
use of screenshots/documents
use of maps/timelines
music density
SFX density
hook structure
reveal timing
```

Then create a project-specific style profile.

Do not clone the reference.

The output should be:

> **informed by the editorial language of the references, but recognizably Hardik.**

---

# 33. PILOT-FIRST DEVELOPMENT

Before generating an 8–15 minute production, run a 90–120 second pilot.

Pilot should contain:

```text
HOOK
→ problem
→ evidence
→ explanation
→ meme/reaction
→ host
→ graphic
→ reveal
→ conclusion beat
```

Target approximately:

- 12–25 shots
- 3–5 Hardik shots
- 3–6 B-roll/cinematic shots
- 2–4 graphics
- 1–2 evidence shots
- 1–2 memes
- 1–2 transitions/reveals

The pilot passes only if it looks like an edited video rather than a presentation.

---

# 34. FINAL PRODUCTION GATE

Do not scale to 8–15 minutes until the pilot passes all major gates:

```text
[ ] Narration sounds natural
[ ] Shot manifest is semantically coherent
[ ] No slide-show behavior
[ ] Visual changes are meaningful
[ ] Host identity is stable
[ ] Host shots are not repetitive
[ ] B-roll is specific
[ ] Evidence is visible
[ ] Graphics explain rather than decorate
[ ] Memes have clear triggers
[ ] Veo shots are photorealistic
[ ] Continuity works where required
[ ] Music supports narration
[ ] SFX are restrained
[ ] No long static holds
[ ] No semantic visual repetition
[ ] Actual QC evidence exists
[ ] No fabricated PASS values
```

---

# 35. PROJECT DIRECTORY

Recommended structure:

```text
video-project/
│
├── project.json
├── research/
├── script/
├── audio/
│   ├── narration.wav
│   └── word_map.json
├── manifest/
│   ├── shot_manifest.json
│   └── editorial_style_profile.json
│
├── character/
│   ├── MASTER_CHARACTER.md
│   ├── references/
│   └── generated/
│
├── scenes/
│   ├── scene_001/
│   │   ├── scene.json
│   │   ├── shots/
│   │   └── last_frame.png
│   └── scene_002/
│
├── frames/
│   ├── start/
│   └── end/
│
├── veo/
├── broll/
├── evidence/
├── graphics/
├── memes/
├── captions/
├── music/
├── sfx/
├── timeline/
├── qc/
└── exports/
```

---

# 36. FAILURE RECOVERY

If one shot fails:

```text
FAILED SHOT
 ↓
IDENTIFY FAILURE TYPE
 ↓
REGENERATE ONLY FAILED ASSET
 ↓
RE-RUN LOCAL QC
 ↓
REINSERT INTO TIMELINE
```

Do not regenerate the entire video.

Failure categories:

```text
IDENTITY_FAILURE
REALISM_FAILURE
CONTINUITY_FAILURE
VISUAL_RELEVANCE_FAILURE
TIMING_FAILURE
AUDIO_FAILURE
ASSET_FAILURE
RENDER_FAILURE
EDITORIAL_RHYTHM_FAILURE
```

---

# 37. ABSOLUTE PROHIBITIONS

Never:

1. Build the whole video from presentation slides.
2. Use one visual for an entire scene by default.
3. Treat Ken Burns as sufficient editing.
4. Generate Hardik for every shot.
5. Use memes as filler.
6. Use generic B-roll when specific evidence exists.
7. Repeat the same semantic visual immediately.
8. Claim QC PASS without evidence.
9. Treat intended end frame as actual final frame.
10. regenerate unchanged assets.
11. spend Veo credits before visual planning.
12. copy the reference creators' exact style, wording, branding or identity.
13. use transitions everywhere.
14. fabricate evidence.
15. prioritize AI novelty over editorial usefulness.

---

# 38. THE SINGLE MOST IMPORTANT RULE

When deciding what happens next in the timeline, think like an editor:

> **What does the viewer need to see right now, and what should they see next so they keep watching?**

Not:

> "What asset can the AI generate?"

Not:

> "What slide should come next?"

Not:

> "How do I use Veo here?"

The correct order is:

```text
STORY
 ↓
VIEWER NEED
 ↓
EDITORIAL PURPOSE
 ↓
SHOT
 ↓
ASSET
 ↓
MOTION
 ↓
CUT
 ↓
NEXT SHOT
```

That is the architecture that turns this system from an **AI presentation generator** into an **automated YouTube video editor**.
