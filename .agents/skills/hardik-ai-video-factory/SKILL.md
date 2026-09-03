---
name: hardik-ai-video-factory
description: >-
  End-to-end automated YouTube video production pipeline for Hardik's channel. Covers research, titles, hooks, scripts, scene breakdown, video manifest, character consistency, frame prompts, audio narration, PPT/slide integration, meme placement, and editing automation.
---

# HARDIK — AI VIDEO FACTORY
## Master Claude Skill for Automated YouTube Video Production
### Frame-First • Master Character • Multi-Angle • Veo 3 • Sarvam AI • PPT • Memes • B-roll • Automated Editing

Version: 2.0

---

# 0. PURPOSE

This skill turns a video topic into a production-ready YouTube video while minimizing manual work and unnecessary AI-credit usage.

Core pipeline:

```text
RESEARCH
   ↓
TITLE + HOOK
   ↓
SCRIPT
   ↓
SCENE BREAKDOWN
   ↓
VIDEO MANIFEST
   ↓
CHARACTER IDENTITY SYSTEM
   ↓
SCENE VISUAL DESCRIPTION
   ↓
FRAME IMAGE GENERATION
   ↓
START FRAME + END FRAME
   ↓
SARVAM AI VOICE
   ↓
VEO 3 VIDEO
   ↓
LAST-FRAME EXTRACTION
   ↓
NEXT SCENE START FRAME
   ↓
PPT / MEME MATCHING / B-ROLL / GRAPHICS
   ↓
CAPTIONS
   ↓
GOOGLE VIDS EDITING
   ↓
REMOTION / FFMPEG FALLBACK
   ↓
QC
   ↓
FINAL EXPORT
```

The goal is NOT to make something that merely looks AI-generated.

> **Produce a professional YouTube video that feels like Hardik made it, while AI and automation operate behind the scenes.**

The system must optimize for:
- strong storytelling
- high viewer retention
- high visual quality
- recognizable Hardik identity
- photorealistic character representation
- natural voice delivery
- visual variety
- strategic humor
- scene-to-scene continuity
- low AI-credit consumption
- reusable assets
- selective regeneration
- deterministic automation whenever AI is unnecessary

Never generate an entire long video in one expensive AI call.

---

# 1. HARDIK CREATOR PROFILE

Hardik is a:

> **Young Indian builder + investigator + explainer**

He is not primarily a traditional news anchor.

He should feel like someone who:
- investigates unusual systems
- discovers hidden mechanisms
- breaks down complicated subjects
- explores technology and AI
- investigates businesses and brands
- explains real-world problems
- experiments with things himself
- asks questions ordinary viewers would ask
- connects technology, business, society and everyday life

Potential content:
- AI and Agentic AI
- technology
- startups and business
- entrepreneurship
- science
- history
- mysteries
- India
- current affairs
- geopolitics
- internet culture
- scams/investigations
- interesting real-world systems

Creator positioning:

> **Hardik finds the interesting story behind things and explains what is actually going on.**

Desired personality:
- intelligent
- curious
- skeptical when investigating
- serious when appropriate
- excited when discovering something
- confident but not arrogant
- approachable
- modern
- young
- investigative
- humorous when useful

Avoid making Hardik look like:
- a politician
- a TV news anchor
- permanently angry
- overly aggressive
- artificially muscular
- unrealistically glamorous
- a generic influencer
- permanently shocked
- an artificial CGI avatar

Expression must match the story.

Never make the creator look like a generic AI influencer.

---

# 2. MASTER ARCHITECTURE

The **Video Manifest** is the source of truth for the complete production.

It controls:
- research references
- title
- hook
- scenes
- narration
- durations
- visual types
- character state
- clothing
- PPT usage
- meme usage
- B-roll
- transitions
- continuity
- captions
- music
- SFX
- asset paths
- prompts
- generation status
- QC status
- cost tracking

Everything downstream reads from the manifest.

---

# 3. COMPLETE PRODUCTION PIPELINE

```text
USER TOPIC
   ↓
1. RESEARCH
   ↓
2. TITLE + HOOK
   ↓
3. SCRIPT
   ↓
4. SCENE BREAKDOWN
   ↓
5. VIDEO MANIFEST
   ↓
6. CHARACTER IDENTITY LOAD
   ↓
7. VISUAL PLAN
   ↓
8. PPT / PRESENTATION ASSETS
   ↓
9. SARVAM AI VOICE
   ↓
10. START/END FRAME IMAGE GENERATION
   ↓
11. VEO 3 SCENE GENERATION
   ↓
12. LAST-FRAME EXTRACTION
   ↓
13. NEXT-SCENE CONTINUITY
   ↓
14. MEMES / B-ROLL / GRAPHICS
   ↓
15. CAPTIONS
   ↓
16. TIMELINE ASSEMBLY
   ↓
17. QUALITY CONTROL
   ↓
18. FINAL EXPORT
```

Important architectural rule:

> **Frame generation happens BEFORE Veo 3 video generation.**

---

# 4. STAGE 1 — RESEARCH

Understand the story before writing.

Identify:
- central question
- background
- key facts
- timeline
- people/entities
- locations
- statistics
- primary sources
- secondary sources
- competing explanations
- surprising details
- contradictions
- stakes
- visual opportunities
- meme opportunities
- story beats
- possible reveals

Research output:

```json
{
  "topic": "",
  "target_audience": "",
  "central_question": "",
  "core_story": "",
  "key_facts": [],
  "timeline": [],
  "entities": [],
  "statistics": [],
  "examples": [],
  "surprising_details": [],
  "competing_explanations": [],
  "counterarguments": [],
  "interesting_hooks": [],
  "story_angles": [],
  "visual_opportunities": [],
  "meme_opportunities": [],
  "sources": []
}
```

Never fabricate:
- statistics
- quotes
- sources
- dates
- names
- allegations
- scientific conclusions
- historical facts

Clearly distinguish:
- confirmed
- strongly supported
- disputed
- alleged
- unknown

## Credit-efficient research

Prefer:

```text
SEARCH
 ↓
COLLECT SOURCES
 ↓
EXTRACT RELEVANT INFORMATION
 ↓
ONE STRONG REASONING/SYNTHESIS CALL
```

Avoid:

```text
SEARCH
 ↓
SUMMARIZE EVERY PAGE
 ↓
SUMMARIZE SUMMARIES
 ↓
REWRITE AGAIN
 ↓
WRITE SCRIPT
```

---

# 5. STAGE 2 — TITLE + HOOK

Before writing the final script, identify:
- central mystery
- contradiction
- stakes
- strongest reveal
- strongest question
- emotional trigger
- thumbnail possibility

Hook mechanisms:
- mystery
- contradiction
- stakes
- hidden mechanism
- surprising question
- unexpected result
- personal experiment
- evidence

The title must never promise something the video does not deliver.

The hook should make the viewer think:

> **"Wait… why?"**

Do not manufacture controversy.

---

# 6. STAGE 3 — SCRIPT

Write for video, not for reading.

Default structure:

```text
HOOK
 ↓
CONTEXT
 ↓
QUESTION
 ↓
STORY DEVELOPMENT
 ↓
ESCALATION
 ↓
REVEAL
 ↓
IMPLICATION
 ↓
CONCLUSION
 ↓
CTA
```

The script must contain:
- narration
- scene intent
- visual intent
- emotion
- on-screen text
- presentation requirement
- meme opportunity
- transition type
- character requirement
- continuity requirement

Do not write one giant paragraph and reverse-engineer visuals afterward.

---

# 7. SCENE-FIRST SCRIPTING

Every script is divided into scenes.

Example:

```json
{
  "scene_id": 1,
  "type": "HOOK",
  "duration_target": 7,
  "narration": "...",
  "visual_goal": "...",
  "emotion": "curious",
  "on_screen_text": "...",
  "visual_mode": "CHARACTER",
  "meme": false,
  "ppt": false
}
```

Supported scene types:
- HOOK
- CHARACTER
- EXPLANATION
- CINEMATIC
- PPT
- GRAPHIC
- B-ROLL
- MEME
- SCREEN_RECORDING
- QUOTE
- TIMELINE
- MAP
- DATA
- TRANSITION
- CONCLUSION
- CTA

The scene breakdown must be detailed enough that another automated system can generate the scene without asking for basic clarification.

---

# 8. VIDEO MANIFEST

Recommended structure:

```json
{
  "project": {
    "id": "",
    "title": "",
    "language": "English",
    "aspect_ratio": "16:9",
    "target_duration": 600
  },
  "creator": {
    "character_id": "hardik_main",
    "master_description": "character/MASTER_CHARACTER.md",
    "reference_pack": "character/references/"
  },
  "audio": {
    "provider": "sarvam",
    "voice_id": "",
    "music_profile": "",
    "sfx_profile": ""
  },
  "scenes": []
}
```

Scene structure:

```json
{
  "scene_id": 1,
  "start": 0,
  "duration": 7,

  "narration": {
    "text": "",
    "audio_file": ""
  },

  "visual": {
    "type": "CHARACTER",
    "scene_description": "",
    "prompt": "",
    "reference_files": [],
    "camera": "",
    "motion": "",
    "location": "",
    "lighting": "",
    "emotion": "",
    "clothing": ""
  },

  "frame_plan": {
    "required": true,
    "start_frame": "",
    "end_frame": "",
    "previous_last_frame": "",
    "continuity_mode": "CONTINUOUS"
  },

  "presentation": {
    "enabled": false,
    "asset": ""
  },

  "meme": {
    "enabled": false,
    "asset": "",
    "duration": 0
  },

  "broll": {
    "enabled": false,
    "asset": ""
  },

  "captions": {
    "enabled": true
  },

  "transition": {
    "type": "CONTINUOUS",
    "use_previous_last_frame": true
  },

  "status": {
    "voice": "pending",
    "start_frame": "pending",
    "end_frame": "pending",
    "visual": "pending",
    "edit": "pending",
    "qc": "pending"
  }
}
```

---

# 9. MASTER CHARACTER IDENTITY SYSTEM

This is mandatory for Hardik's videos.

Create and permanently maintain:

```text
character/
└── MASTER_CHARACTER.md
```

The master description should contain:

```text
IDENTITY
FACE
HAIR
SKIN
BODY
FACIAL PROPORTIONS
EYES
EYEBROWS
NOSE
LIPS
JAW
FACIAL HAIR
AGE APPEARANCE
BODY PROPORTIONS
DEFAULT EXPRESSIONS
POSTURE
PERSONALITY
REALISM REQUIREMENTS
MULTI-ANGLE REFERENCES
NEGATIVE CONSTRAINTS
```

The user provides:
1. master text description
2. multi-angle reference images

The system treats these as the canonical identity source.

Do NOT rewrite the entire master description manually into every prompt.

Instead:

```text
MASTER_CHARACTER.md
+
relevant reference images
+
scene-specific description
=
scene character prompt
```

---

# 10. MULTI-ANGLE REFERENCE PACK

Recommended structure:

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

Use the minimum number of references required for the scene.

Do not unnecessarily send every reference image to every generation.

Reference selection should depend on:
- camera angle
- framing
- pose
- lighting
- face visibility

---

# 11. ULTRA-REALISM STANDARD

The character is NOT an AI avatar.

Target:

> **Photorealistic representation of the creator with stable facial identity across scenes.**

Prioritize:
- realistic skin texture
- natural facial proportions
- realistic eyes
- natural hair
- realistic hands
- physically plausible lighting
- realistic fabric
- natural shadows
- real-world lens characteristics
- cinematic but believable depth of field
- natural body movement
- realistic facial expressions
- realistic skin imperfections
- physically believable reflections
- natural perspective

Avoid:
- plastic skin
- CGI appearance
- beauty-filter appearance
- over-smoothed skin
- artificial symmetry
- doll-like eyes
- distorted hands
- face warping
- identity drift
- excessive sharpening
- unrealistic skin pores
- fake cinematic haze
- unnatural body proportions

The final result should look like:

> **A real camera captured Hardik in a real environment.**

Not:

> **An AI character pretending to be Hardik.**

---

# 12. CLOTHING SYSTEM

Identity is locked.

Clothing is NOT locked.

This is important.

The system must preserve:
- face
- hairstyle
- body proportions
- recognizable identity

But may change:
- T-shirt
- shirt
- jacket
- hoodie
- kurta
- formal wear
- casual wear
- layers
- colors
- accessories

Clothing must be selected based on:
- topic
- environment
- scene emotion
- narrative context
- continuity

Never keep the exact same clothing throughout an entire channel simply for consistency.

However:

> **Do not change clothing halfway through a continuous physical moment unless the story explicitly indicates a change.**

---

# 13. FRAME-FIRST VIDEO GENERATION SYSTEM

This is the defining architecture.

For every Veo scene that requires AI video:

```text
SCENE DESCRIPTION
       ↓
MASTER CHARACTER
       +
MULTI-ANGLE REFERENCES
       +
SCENE-SPECIFIC CLOTHING
       +
ENVIRONMENT
       +
CAMERA
       +
LIGHTING
       ↓
START FRAME IMAGE
       +
END FRAME IMAGE
       ↓
QC
       ↓
VEO 3
```

The video model should NOT be responsible for inventing Hardik's appearance from scratch.

---

# 14. START FRAME GENERATION

Every continuous Veo scene should have a deliberate starting frame.

Start frame includes:
- Hardik identity
- correct reference angle
- scene-specific clothing
- environment
- camera framing
- pose
- facial expression
- lighting
- composition
- visual story state

Example:

```json
{
  "frame": "start",
  "character": "hardik_main",
  "reference_angles": ["three_quarter_right"],
  "clothing": "dark charcoal overshirt over white t-shirt",
  "location": "modern technology laboratory",
  "camera": "medium close-up, 50mm lens",
  "expression": "skeptical curiosity",
  "pose": "standing beside a display",
  "lighting": "natural window light with soft practical lights"
}
```

---

# 15. END FRAME GENERATION

The end frame is not optional for important continuous scenes.

It must define:
- final pose
- final expression
- final camera state
- final environment state
- final character position
- final clothing state
- final visual composition

The end frame should be designed as a bridge into the next scene whenever continuity is required.

Example:

```json
{
  "frame": "end",
  "character": "hardik_main",
  "pose": "turning toward the screen",
  "expression": "surprised realization",
  "camera": "slightly wider medium shot",
  "environment": "same laboratory",
  "continuity_target": "scene_002_start"
}
```

---

# 16. VEO 3 INPUT ARCHITECTURE

For each Veo scene:

```text
START FRAME
     +
SCENE MOTION / ACTION PROMPT
     +
END FRAME / END-STATE INTENT
     +
MASTER CHARACTER REFERENCE
     ↓
VEO 3
     ↓
VIDEO
```

The scene prompt should specify:
- subject
- action
- environment
- camera
- movement
- lighting
- emotion
- physical realism
- continuity
- constraints

Prompt template:

```text
SUBJECT:
[Hardik / object / environment]

ACTION:
[what happens during the shot]

ENVIRONMENT:
[where the scene occurs]

CAMERA:
[shot size + lens feel + camera movement]

LIGHTING:
[realistic lighting description]

EMOTION:
[performance]

MOTION:
[natural physical movement]

STYLE:
[photorealistic cinematic documentary]

CONTINUITY:
[how the shot must begin/end]

CHARACTER:
Use the canonical Hardik identity and supplied multi-angle references.

CONSTRAINTS:
No identity drift, no facial distortion, no unnatural hands,
no plastic skin, no CGI appearance, no clothing change unless specified.
```

Do not overprompt.

Prioritize:
1. identity
2. action
3. camera
4. environment
5. continuity
6. realism

---

# 17. LAST-FRAME CONTINUITY ENGINE

After every continuous Veo scene:

```text
video_N.mp4
      ↓
extract final frame
      ↓
last_frame_N.png
```

Then:

```text
last_frame_N.png
      +
scene_N+1 requirements
      ↓
scene_N+1_start_frame.png
      ↓
Veo 3
```

Canonical flow:

```text
SCENE 01
 ↓
START FRAME 01
 ↓
VEO 3
 ↓
VIDEO 01
 ↓
LAST FRAME 01
 ↓
START FRAME 02
 ↓
VEO 3
 ↓
VIDEO 02
 ↓
LAST FRAME 02
 ↓
START FRAME 03
 ↓
...
```

This should be used whenever the next shot visually continues the previous shot.

---

# 18. CONTINUITY MODES

## CONTINUOUS

Use when:
- same character
- same environment
- same physical moment
- same visual sequence

```json
{
  "type": "CONTINUOUS",
  "use_previous_last_frame": true
}
```

## HARD_CUT

Use for:
- unrelated B-roll
- meme
- new location
- major time jump
- completely new visual concept

```json
{
  "type": "HARD_CUT",
  "use_previous_last_frame": false
}
```

## PRESENTATION

Character → PPT or PPT → character.

Do not fake physical continuity where none exists.

## RETURN_TO_CHARACTER

Reload the appropriate canonical character references.

---

# 19. END-FRAME VS ACTUAL-LAST-FRAME

The intended end frame and the generated video's actual last frame are different assets.

Store both:

```text
intended_end_frame.png
actual_last_frame.png
```

After Veo generation:

```text
actual_last_frame
        ↓
compare with intended_end_frame
        ↓
QC
```

If the actual final frame differs significantly, determine whether:
- the scene is still visually acceptable
- the next scene can adapt
- only the next start frame needs regeneration
- the Veo scene itself must be regenerated

Do NOT automatically regenerate the whole chain.

---

# 20. VISUAL PLANNING

Choose the cheapest suitable visual method:

```text
1. Existing reusable asset
2. Programmatic graphic
3. Existing PPT/slide
4. Stock/B-roll library
5. Meme library
6. Character image/reference
7. AI image
8. AI video
```

Never use AI video when a static/programmatic visual does the job.

Examples:

```text
Statistic → chart
Timeline → programmatic timeline
Comparison → slide/table
Simple explanation → diagram
Historical event → archive/B-roll
Character performance → AI video
```

---

# 21. NOTEBOOKLM / PRESENTATION LAYER

NotebookLM or another presentation-generation system may be used for presentation-style visuals.

It is NOT the backbone.

The backbone is:

```text
VIDEO MANIFEST
```

Presentation assets are replaceable outputs.

Useful presentation visuals:
- timelines
- comparisons
- charts
- maps
- flow diagrams
- quotes
- historical context
- technical architecture
- statistics
- before/after
- process explanations

If a PPT is unnecessary, skip it.

---

# 22. PPT DESIGN

Slides must be:
- simple
- readable at 1080p
- high contrast
- low text density
- strongly hierarchical
- animation-friendly
- consistent with Hardik's visual identity

Avoid:
- paragraphs
- tiny text
- generic corporate templates
- unnecessary decoration
- excessive bullet points

Rule:

> **One slide = one primary idea.**

---

# 23. SARVAM AI VOICE

Use Sarvam AI for narration.

Workflow:

```text
APPROVED NARRATION
      ↓
GROUP LOGICAL NARRATION BLOCKS
      ↓
SARVAM TTS
      ↓
AUDIO FILES
      ↓
MEASURE ACTUAL DURATION
      ↓
UPDATE MANIFEST TIMING
```

Do not generate every sentence separately.

Group logical narration blocks.

Cache successful audio.

Recommended filename:

```text
{project_id}_{scene_or_block}_{voice_id}_{text_hash}.wav
```

If exact:
- text
- voice
- settings

already exist:

```text
CACHE HIT
 ↓
REUSE
```

---

# 24. VOICE TIMING

Voice duration is the timing authority for narration-driven scenes.

After generation:
1. measure actual duration
2. update scene duration
3. adjust visual timing
4. recalculate timeline
5. regenerate only visuals whose constraints are violated

Never assume TTS duration.

Never regenerate the voice merely because a visual failed.

---

# 25. MEME ENGINE

Memes support retention.

Use for:
- comic relief
- reaction
- emphasis
- irony
- absurdity
- failure
- surprise
- cultural recognition

Avoid memes during serious emotional moments unless intentionally appropriate.

Baseline:

```text
0–2 memes per minute
```

Adjust according to topic.

Memes should never interrupt the core story unnecessarily.

---

# 26. REUSABLE MEME LIBRARY

```text
memes/
├── reaction/
├── shocked/
├── confused/
├── laughing/
├── failure/
├── success/
├── money/
├── technology/
├── sarcasm/
├── india/
└── generic/
```

Metadata:

```json
{
  "id": "",
  "emotion": "confused",
  "use_cases": [
    "unexpected_result",
    "contradiction"
  ],
  "duration_range": [1.5, 3.0],
  "safe_for_serious_content": false
}
```

Prefer reuse over generation.

---

# 27. B-ROLL ENGINE

Priority:

```text
Existing relevant B-roll
 ↓
Stock/library footage
 ↓
AI image
 ↓
AI video
```

Use AI video only when motion materially improves storytelling.

---

# 28. GRAPHICS ENGINE

Generate simple graphics programmatically:
- arrows
- timelines
- counters
- charts
- maps
- labels
- lower thirds
- diagrams
- comparison tables

Do not spend expensive generative credits on basic graphics.

---

# 29. CAPTION ENGINE

Use approved narration whenever possible.

```text
APPROVED SCRIPT
+
VOICE TIMING
+
SCENE TIMING
 ↓
CAPTION TIMELINE
 ↓
SRT / ASS / REMOTION
```

Do not unnecessarily retranscribe identical narration with another AI model.

---

# 30. CHARACTER VS PRESENTATION BALANCE

Hardik remains the recognizable anchor.

Starting guideline:

```text
30–50% character
20–35% B-roll/cinematic visuals
10–25% graphics/PPT
5–15% memes/reactions
```

These are flexible guidelines.

Do not make the entire video:
- a PPT
- a talking head
- AI cinematic filler

Visual changes must serve the story.

---

# 31. VISUAL RHYTHM

Possible sequence:

```text
Character
 ↓
B-roll
 ↓
Graphic
 ↓
Character
 ↓
Meme
 ↓
PPT
 ↓
Character
 ↓
Cinematic visual
```

Do not create random visual noise.

Every visual change needs a storytelling reason.

---

# 32. RETENTION-BASED VISUAL RULES

New fact → visual proof

Statistic → graphic

Surprise → reaction / camera change / meme

Explanation → PPT / diagram

Emotional moment → close-up / cinematic B-roll

Historical event → archive / map / timeline

Joke → meme/reaction

Major reveal → visual escalation

---

# 33. STORY STATE

Maintain:

```json
{
  "current_location": "",
  "current_character_clothing": "",
  "current_emotion": "",
  "current_time_period": "",
  "known_entities": [],
  "visual_style": "",
  "camera_state": "",
  "character_position": ""
}
```

Before each scene:

```text
READ STORY STATE
      ↓
READ PREVIOUS FRAME
      ↓
GENERATE SCENE
      ↓
UPDATE STORY STATE
```

This reduces continuity errors.

---

# 34. COST / CREDIT OPTIMIZATION

This is a top-level requirement.

## Rule 1 — Generate once, reuse forever

Reuse:
- character references
- master character description
- memes
- intro/outro
- music
- SFX
- captions style
- transitions
- templates

## Rule 2 — Cache generation inputs

Hash:

```text
model
prompt
reference images
settings
duration
aspect ratio
seed if supported
```

Example:

```text
generation_hash = SHA256(all_generation_inputs)
```

If cache exists:

```text
CACHE HIT → REUSE
```

## Rule 3 — Regenerate only failures

If Scene 7 fails:

```text
Scene 7 failed
 ↓
repair Scene 7
 ↓
replace Scene 7
 ↓
rebuild final timeline
```

Never regenerate the entire video.

## Rule 4 — Cheapest suitable method

```text
Existing asset? → reuse
Programmatic graphic? → code
PPT sufficient? → PPT
Static visual? → image
Motion required? → video
Character performance required? → AI video
```

## Rule 5 — One model per job

Do not ask five models to rewrite the same output without a clear reason.

## Rule 6 — Selective references

Do not send all multi-angle references to every image/video generation call.

Use only the references needed for the camera/view.

## Rule 7 — Separate image and video failures

If a start frame is wrong:

```text
regenerate start frame
```

Do not regenerate Veo until the frame is approved.

If Veo is wrong but frame is correct:

```text
regenerate Veo only
```

If the final frame is wrong:

```text
adapt next start frame OR regenerate current scene
```

---

# 35. ASSET CACHE / FOLDER STRUCTURE

```text
video-project/
├── project.json
├── research/
├── script/
├── manifest/
│
├── character/
│   ├── MASTER_CHARACTER.md
│   ├── references/
│   │   ├── front.jpg
│   │   ├── left.jpg
│   │   ├── right.jpg
│   │   ├── three_quarter_left.jpg
│   │   ├── three_quarter_right.jpg
│   │   ├── profile_left.jpg
│   │   ├── profile_right.jpg
│   │   └── fullbody.jpg
│   └── generated/
│
├── scenes/
│   ├── scene_001/
│   │   ├── scene.json
│   │   ├── narration.txt
│   │   ├── voice.wav
│   │   ├── start_frame.png
│   │   ├── intended_end_frame.png
│   │   ├── veo_prompt.txt
│   │   ├── video.mp4
│   │   ├── actual_last_frame.png
│   │   ├── caption.ass
│   │   └── qc.json
│   ├── scene_002/
│   └── scene_003/
│
├── ppt/
├── memes/
│   ├── library/
│   ├── index/
│   ├── metadata/
│   └── extracted/
├── broll/
├── captions/
├── music/
├── sfx/
├── frames/
├── cache/
├── timeline/
├── qc/
└── exports/
```

---

# 36. SCENE GENERATION STATE MACHINE

Each scene should have:

```text
PLANNED
 ↓
VOICE_READY
 ↓
START_FRAME_READY
 ↓
END_FRAME_READY
 ↓
FRAME_QC_PASS
 ↓
VEO_READY
 ↓
VIDEO_READY
 ↓
LAST_FRAME_EXTRACTED
 ↓
CONTINUITY_QC
 ↓
SCENE_QC_PASS
 ↓
EDIT_READY
```

If a stage fails, restart only that stage.

---

# 37. FAILURE RECOVERY

The pipeline must be restartable.

If it stops after Scene 18:

```text
RESUME
 ↓
READ MANIFEST
 ↓
CHECK EXISTING ASSETS
 ↓
SKIP COMPLETED STAGES
 ↓
CONTINUE FROM FIRST INCOMPLETE STAGE
```

Never restart from the beginning unless explicitly requested.

---

# 38. IDEMPOTENCY

Running generation twice must not regenerate everything.

Example:

```text
Research exists ✓
Script exists ✓
Manifest exists ✓
Voice exists ✓
Start frame exists ✓
End frame exists ✓
Scene video exists ✓
Last frame exists ✓
Scene 8 missing ✗
```

Only Scene 8 should be generated.

---

# 39. QUALITY CONTROL

QC must occur at:
1. research
2. script
3. start frame
4. end frame
5. Veo video
6. continuity
7. final edit

## Frame QC

Check:
- face identity
- facial proportions
- hair
- skin realism
- hands
- body proportions
- clothing
- environment
- lighting
- composition
- unwanted artifacts

## Video QC

Check:
- identity consistency
- natural movement
- realistic hands
- realistic facial movement
- no morphing
- no object teleportation
- no environment distortion
- no unwanted clothing changes
- correct duration
- correct framing

## Technical QC

Check:
- resolution
- FPS
- duration
- audio
- corrupted frames
- aspect ratio
- black frames

## Content QC

Check:
- narration matches visuals
- scenes are ordered correctly
- captions exist
- no missing assets
- no unintended silence
- PPT content matches narration
- meme timing is correct

---

# 40. QC OUTPUT

Scene:

```json
{
  "scene_id": 7,
  "status": "PASS",
  "checks": {
    "video_valid": true,
    "audio_valid": true,
    "duration_valid": true,
    "start_frame_valid": true,
    "end_frame_valid": true,
    "continuity_valid": true,
    "character_valid": true,
    "captions_valid": true
  }
}
```

Failure:

```json
{
  "status": "FAIL",
  "failed_checks": [
    "character_consistency"
  ],
  "action": "REGENERATE_VISUAL_ONLY"
}
```

Repair only the failed component.

---

# 41. AI VS CODE

Use AI for:
- research reasoning
- story structure
- creative writing
- visual interpretation
- character performance
- cinematic generation
- visual ideation
- frame image generation

Use code for:
- file management
- hashing
- caching
- timing
- frame extraction
- image comparison
- subtitles
- joining
- encoding
- QC
- metadata
- folder structure
- timeline generation
- asset validation

This separation improves:
- cost
- reliability
- speed
- reproducibility

---

# 42. EDITING ENGINE

Recommended architecture:

```text
VIDEO ASSETS
AUDIO
PPT
MEMES
B-ROLL
CAPTIONS
MUSIC
SFX
 ↓
TIMELINE JSON
 ↓
REMOTION / FFMPEG
 ↓
FINAL VIDEO
```

FFmpeg:
- encoding
- joining
- trimming
- audio mixing
- frame extraction
- basic transitions

Remotion:
- captions
- motion graphics
- animated graphics
- branded layouts
- programmatic compositions

---

# 43. TIMELINE

Example:

```json
{
  "timeline": [
    {
      "scene": 1,
      "video": "scene_01/video.mp4",
      "audio": "scene_01/voice.wav",
      "caption": "scene_01/caption.ass",
      "music": "music_a.wav",
      "sfx": []
    }
  ]
}
```

The editor reads the timeline instead of manually assembling every scene.

---

# 44. MUSIC + SFX

Use reusable licensed music.

Profiles:
- cinematic investigation
- technology
- suspense
- documentary
- emotional
- energetic
- light comedy
- neutral explainer

Duck music under narration.

Reusable SFX:
- whoosh
- impact
- pop
- click
- notification
- glitch
- bass hit
- transition
- typing
- money
- error
- success

SFX should emphasize moments, not play constantly.

---

# 45. EXPORTS

Produce:

```text
final_master.mp4
final_youtube.mp4
preview.mp4
captions.srt
captions.ass
thumbnail.jpg
metadata.json
```

Metadata:

```json
{
  "title": "",
  "description": "",
  "tags": [],
  "chapters": [],
  "hashtags": [],
  "sources": []
}
```

This allows title, thumbnail and description skills to connect to the video factory.

---

# 46. MASTER ORCHESTRATION

```python
def create_video(topic):

    project = create_project(topic)

    research = research_topic(topic)
    save(research)

    packaging = generate_title_and_hook(research)

    script = generate_script(
        research=research,
        packaging=packaging
    )
    save(script)

    manifest = create_video_manifest(
        research=research,
        script=script,
        packaging=packaging
    )
    save(manifest)

    load_master_character()
    generate_visual_plan(manifest)
    generate_ppt_assets(manifest)
    generate_sarvam_voice(manifest)

    for scene in manifest.scenes:

        ensure_voice(scene)

        if scene.requires_ai_video:

            if not cache_exists(scene.start_frame):
                generate_start_frame(scene)

            if not cache_exists(scene.end_frame):
                generate_end_frame(scene)

            run_frame_qc(scene)

            if not frame_qc_passed(scene):
                repair_frames(scene)
                continue

            previous_frame = get_previous_last_frame(scene)

            if not cache_exists(scene.video):

                generate_veo_video(
                    scene=scene,
                    start_frame=scene.start_frame,
                    end_frame=scene.end_frame,
                    previous_frame=previous_frame
                )

            extract_actual_last_frame(scene)

            run_continuity_qc(scene)

        elif scene.visual.type == "PPT":
            use_ppt_asset(scene)

        elif scene.visual.type == "MEME":
            select_meme(scene)

        elif scene.visual.type in PROGRAMMATIC_TYPES:
            create_programmatic_visual(scene)

        else:
            use_existing_or_stock_asset(scene)

        run_scene_qc(scene)

        if scene.qc.failed:
            repair_scene(scene)

    timeline = build_timeline(manifest)

    final_video = render(timeline)

    run_final_qc(final_video)

    if qc_passed:
        export(final_video)
    else:
        repair_failed_components()
```

---

# 47. HUMAN APPROVAL GATES

Recommended during early development:

```text
Research → approve story angle
Title + Thumbnail → approve packaging
Script → approve narrative
First frames → approve visual identity
First Veo scenes → approve realism
Final QC → export
```

After the pipeline is stable:

```text
FULL AUTO MODE
```

can be enabled.

---

# 48. VIDEO LENGTH

Do not force every topic into the same duration.

Determine length from:
- story complexity
- number of facts
- narrative arc
- audience
- retention needs

Estimate:

```text
required narration
 ↓
audio duration
 ↓
scene count
 ↓
visual-generation budget
```

Never pad the script just to hit a duration.

---

# 49. HARDIK VISUAL LANGUAGE

Long-term goal:

> Someone should eventually see a video frame and think: **"This looks like a Hardik investigation."**

Recommended visual identity:
- clean cinematic photography
- investigative compositions
- strong creator presence
- modern typography
- selective red/yellow accents
- realistic objects
- evidence-driven visuals
- restrained but expressive face
- clear storytelling
- premium documentary feel

Do not copy another creator's exact visual identity.

Use underlying storytelling mechanics while developing Hardik's own recognizable language.

---

# 50. THUMBNAIL/VIDEO BRAND CONNECTION

The video factory should be compatible with the thumbnail skill.

Thumbnail identity can use:
- creator cutout
- controlled expression
- evidence highlights
- arrows
- circles
- warning symbols
- bold typography
- strong contrast

But video frames should prioritize natural cinematic realism rather than artificial thumbnail exaggeration.

Thumbnail style and video style should feel like the same creator.

---

# 51. FINAL MASTER RULES

1. Story first.
2. Never fabricate research.
3. Manifest is the source of truth.
4. Generate scenes, not entire long videos.
5. Frame-first generation is mandatory for important Veo scenes.
6. Start and end frames are visual anchors.
7. Use the master Hardik character description.
8. Use multi-angle references intelligently.
9. Preserve identity, not stagnant clothing.
10. Aim for photorealistic live-action appearance.
11. Use previous last frame when continuity makes sense.
12. Do not force continuity across memes, PPT or hard cuts.
13. Sarvam generates approved narration.
14. Voice and video remain separate until editing.
15. Reuse assets whenever possible.
16. Cache every deterministic generation.
17. Never regenerate successful scenes.
18. Use programmatic graphics instead of AI when possible.
19. Use memes strategically.
20. Do not make every scene cinematic.
21. Do not make every scene a talking head.
22. Captions should come from approved narration whenever possible.
23. Editing should be deterministic.
24. QC should repair only failed components.
25. Pipeline must be resumable.
26. Pipeline must be idempotent.
27. Minimize AI credits without damaging storytelling.
28. Never sacrifice important character consistency merely to save credits.
29. Clothing can change between logical scenes.
30. Clothing must remain consistent within continuous shots.
31. Actual generated last frames must be checked.
32. The next scene should adapt to actual continuity when practical.
33. Every visual change must have a storytelling reason.
34. AI should handle creativity; code should handle coordination.
35. The automation should disappear behind the quality of the final video.

---


36. Google Vids is the preferred automated editing layer when suitable.
37. The meme folder is a reusable knowledge base, not merely a storage folder.
38. Use the supplied meme-reference file to understand contextual meme relevance.
39. Never randomly select a meme; score relevance against narration and story beat.
40. If no meme is sufficiently relevant, use no meme.
41. Resolve meme assets from the catalog and manifest instead of manually searching during editing.

---

# 52. ONE-SENTENCE SYSTEM RULE

> **Use AI for creativity, code for coordination, reusable assets for cost efficiency, a master character identity for visual consistency, frame-first generation for Veo continuity, and a Video Manifest to keep the entire production system synchronized.**


# 26A. GOOGLE VIDS EDITING ENGINE

For the automated editing stage, use **Google Vids** as the preferred editing/orchestration environment when it provides the required automation and integrations.

The purpose of Google Vids in this system is to make the final assembly smoother and reduce repetitive manual editing.

Google Vids should receive the already-approved production assets from the Video Manifest:

```text
VEO SCENES
+
SARVAM VOICE
+
PPT / PRESENTATION
+
MEMES
+
B-ROLL
+
CAPTIONS
+
MUSIC
+
SFX
+
TIMING / TRANSITIONS
        ↓
GOOGLE VIDS
        ↓
ASSEMBLED VIDEO
        ↓
QC
        ↓
FINAL EXPORT
```

### Important

Google Vids is an **editing/assembly layer**, not the source of truth.

The Video Manifest remains the source of truth for:
- scene order
- timing
- narration
- visual assets
- meme placement
- B-roll placement
- transitions
- captions
- music
- SFX
- continuity

The editing layer must not silently change the story.

If Google Vids cannot perform a required deterministic operation reliably, use a programmatic fallback such as FFmpeg/Remotion for that operation.

---

# 26B. MEME LIBRARY + INTELLIGENT MEME EXTRACTION

Create a permanent reusable meme library.

The user may provide:
1. a folder containing meme images/GIFs/videos
2. a reference/index file explaining which meme is relevant in which situation

The automation must treat both as a **Meme Knowledge Base**.

Recommended structure:

```text
memes/
├── library/
│   ├── meme_001.mp4
│   ├── meme_002.gif
│   ├── meme_003.jpg
│   └── ...
│
├── index/
│   └── meme_relevance.md
│
├── metadata/
│   └── meme_catalog.json
│
└── extracted/
```

The reference file may describe:
- meme meaning
- emotional context
- suitable situations
- unsuitable situations
- tone
- reaction
- timing
- cultural context
- example narration
- recommended placement

Example:

```text
MEME: confused_reaction_01
Meaning: viewer/character does not understand what is happening
Use when:
- explaining a confusing mechanism
- unexpected technical behavior
- contradictory information
Emotion: confusion
Tone: humorous
Best duration: 1–2.5 sec
Avoid:
- serious emotional sections
- sensitive subjects
```

---

# 26C. MEME MATCHING ENGINE

Do NOT randomly select memes.

For every scene, analyze:

```text
Narration
+
Scene meaning
+
Emotion
+
Story beat
+
Humor opportunity
+
Meme knowledge base
+
Timing
+
Topic sensitivity
        ↓
Meme relevance score
        ↓
Best matching meme
```

Suggested scoring:

```text
semantic relevance       30%
emotional relevance      25%
story-beat relevance     20%
humor/tone fit           15%
timing fit                5%
cultural/context fit      5%
```

The exact weighting can be adjusted after observing real videos.

Only insert a meme when the relevance score is sufficiently high.

If no meme is a strong match:

```text
NO MEME
```

is the correct decision.

Do not force a meme just to hit a quota.

---

# 26D. MEME EXTRACTION FROM USER-PROVIDED FILES

If the user provides a file containing meme references, examples, screenshots, descriptions, timestamps, categories or usage guidance:

```text
READ MEME REFERENCE FILE
        ↓
EXTRACT MEME RULES
        ↓
MAP RULES TO LIBRARY ASSETS
        ↓
CREATE / UPDATE meme_catalog.json
        ↓
USE CATALOG DURING SCENE PLANNING
```

If the supplied file is itself a video containing multiple memes, extract usable meme segments where technically appropriate.

Store:

```json
{
  "id": "meme_001",
  "file": "library/meme_001.mp4",
  "type": "reaction",
  "meaning": "confusion",
  "emotions": ["confused", "surprised"],
  "use_cases": [
    "unexpected_result",
    "technical_confusion"
  ],
  "avoid_cases": [
    "serious_loss",
    "sensitive_topic"
  ],
  "duration": 2.1,
  "source": "",
  "notes": ""
}
```

Never duplicate the same physical asset unnecessarily.

Use references to the original asset.

---

# 26E. MEME EXTRACTION WORKFLOW

```text
USER MEME FOLDER
       ↓
SCAN FILES
       ↓
IDENTIFY FILE TYPES
       ↓
EXTRACT VIDEO/GIF METADATA
       ↓
READ MEME REFERENCE FILE
       ↓
CLASSIFY MEMES
       ↓
GENERATE meme_catalog.json
       ↓
DEDUPLICATE
       ↓
CREATE SEARCHABLE MEME INDEX
       ↓
READY FOR VIDEO PRODUCTION
```

For video memes, store:
- source file
- start time
- end time
- duration
- frame rate
- resolution
- category
- emotion
- meaning
- recommended usage
- restrictions

For GIF/image memes, store:
- file
- dimensions
- format
- category
- emotion
- meaning
- recommended usage

---

# 26F. MEME PLACEMENT IN THE VIDEO MANIFEST

A scene may contain:

```json
{
  "meme": {
    "enabled": true,
    "asset_id": "confused_reaction_01",
    "start_offset": 4.2,
    "duration": 1.8,
    "placement": "picture_in_picture",
    "reason": "Narration reaches an intentionally confusing contradiction.",
    "relevance_score": 0.91
  }
}
```

Or:

```json
{
  "meme": {
    "enabled": false,
    "reason": "No meme has sufficient semantic or tonal relevance."
  }
}
```

This makes meme selection explainable and automatable.

---

# 26G. MEME PLACEMENT RULES

Use memes to:
- release tension
- emphasize absurdity
- react to surprising information
- make technical explanations accessible
- create cultural recognition
- reinforce a joke
- punctuate a reveal

Do not use memes:
- randomly
- after every sentence
- during every transition
- when the topic is sensitive
- when they distract from evidence
- when they weaken credibility
- merely because a meme exists

The meme must support the narration.

Rule:

> **The story decides whether a meme is needed; the meme library decides which meme fits.**

---

# 26H. GOOGLE VIDS + MEME AUTOMATION

The editor should receive meme placements from the manifest rather than manually searching the meme folder.

```text
VIDEO MANIFEST
      ↓
MEME ASSET IDS
      ↓
MEME CATALOG
      ↓
RESOLVE FILE PATHS
      ↓
GOOGLE VIDS
      ↓
INSERT AT MANIFEST TIMESTAMP
```

If the same meme is used multiple times:
- reuse the same source asset
- trim only when required
- do not regenerate it

---

# 26I. MEME QUALITY CONTROL

Before final export, verify:
- correct meme selected
- meme meaning matches narration
- meme starts at the correct time
- meme duration is appropriate
- meme does not cover important information
- meme does not obscure captions
- meme resolution is acceptable
- meme audio does not overpower narration
- meme does not break scene continuity
- meme does not violate the tone of the topic

If the meme fails QC:

```text
remove meme
OR
replace with better-matching library asset
```

Do not regenerate the whole scene.

---

# 26J. UPDATED EDITING PIPELINE

The preferred final editing flow is:

```text
RESEARCH
   ↓
SCRIPT
   ↓
VIDEO MANIFEST
   ↓
PPT
   ↓
SARVAM VOICE
   ↓
START FRAME
   ↓
END FRAME
   ↓
VEO 3
   ↓
LAST FRAME
   ↓
NEXT START FRAME
   ↓
...
   ↓
MEME MATCHING ENGINE
   ↓
B-ROLL SELECTION
   ↓
CAPTIONS
   ↓
GOOGLE VIDS ASSEMBLY
   ↓
MUSIC + SFX
   ↓
TRANSITIONS
   ↓
QC
   ↓
FINAL EXPORT
```

The final editor must load:
1. scene videos
2. narration
3. captions
4. PPT assets
5. matched memes
6. B-roll
7. music
8. SFX
9. transition instructions
10. brand graphics

This extends the existing final-assembly requirements, which already call for loading scene videos, narration, captions, PPT, memes and B-roll before rendering and QC. fileciteturn14file0L39-L57

---

# 26K. UPDATED LOW-CREDIT RULE

The meme system must also be credit-efficient.

Never use an AI model to create a meme when:
- an appropriate library meme already exists
- a simple reaction can be reused
- an existing clip can be trimmed
- a programmatic graphic is better

Preferred order:

```text
Existing exact meme
        ↓
Existing similar meme
        ↓
Existing B-roll/reaction
        ↓
Programmatic reaction/graphic
        ↓
AI-generated visual
```

The system should maintain a high-quality meme library precisely so repeated productions do not repeatedly spend AI credits on the same type of comedic reaction.

---

