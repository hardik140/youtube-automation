# 🎬 Hardik — Editorial AI YouTube Video Factory

> **Shot/Beat-first automated YouTube production system**  
> Editorial Intelligence • Photorealistic Hardik • Multi-Angle Identity • Frame-First Veo • Sarvam AI • Evidence/B-roll • Memes • Dynamic Rendering • Google Vids • Automated QC

---

## 📌 Overview

This repository contains Hardik's automated YouTube production system for investigative documentaries, explainers, technology, business, AI, systems and current-affairs content.

The production architecture has been rebuilt around an **editorial video-editor model**, not a presentation/slideshow model. The primary production skill is:

```text
.agents/skills/hardik-editorial-video-factory/SKILL.md
```

That skill is the single source of truth for video-production decisions. Superseded video-factory and visual-director skills have been removed to prevent conflicting instructions.

---

## 🧠 Primary Architecture

```text
TOPIC
  ↓
RESEARCH
  ↓
SCRIPT / STORY
  ↓
SARVAM NARRATION AUDIO
  ↓
EDITORIAL DIRECTOR
  ↓
SHOT / BEAT MANIFEST
  ↓
VISUAL DECISION ENGINE
  ↓
EXISTING ASSETS / GRAPHICS / MEMES / B-ROLL / HOST / VEO
  ↓
FRAME ANCHORS FOR VEO WHEN REQUIRED
  ↓
VEO GENERATION
  ↓
ACTUAL LAST-FRAME EXTRACTION
  ↓
CONTINUITY ENGINE
  ↓
DYNAMIC TIMELINE
  ↓
GOOGLE VIDS FINISHING
  ↓
VISUAL QC + EDITORIAL QC
  ↓
FINAL YOUTUBE VIDEO
```

### Core production rule

> **Narration → editorial intent → shot decision → asset → motion → cut → next shot**

A scene is only a chapter/grouping. The actual production unit is a **shot/beat**, normally around 0.8–7 seconds depending on editorial purpose.

The system must actively prevent:

- static slideshow output
- one image held for an entire narration block
- zoom-only motion pretending to be editing
- repetitive Hardik shots
- repetitive graphics
- irrelevant B-roll
- random meme insertion
- unnecessary Veo generation
- QC reports that claim PASS without actually evaluating the condition

---

## 🎯 Target Channel Profile

- Platform: YouTube
- Aspect ratio: 16:9
- Delivery: 1080p minimum; 4K when source assets support it
- Typical duration: 8–15 minutes
- Languages: Hindi / Hinglish / English
- Voice: Sarvam AI
- Host: Hardik
- Host representation: photorealistic AI-generated Hardik
- Memes: enabled
- Music: enabled
- SFX: enabled

The visual language should feel like a modern Indian explainer/documentary: conversational, investigative, energetic, evidence-led, cinematic where useful, and humorous when the story earns it.

Reference creators/videos may inform **general editorial mechanics only**. Do not copy wording, scripts, catchphrases, branding, voice, thumbnails or distinctive identity.

---

## 🧍 Master Character Identity

Authoritative files:

- [CHARACTER_IDENTITY_LOCK.md](./CHARACTER_IDENTITY_LOCK.md)
- [Master_Character_Identity_Reference.pdf](./Master_Character_Identity_Reference.pdf)
- `character/MASTER_CHARACTER.md` when present

Core law:

> **Identity is immutable; scene variables are mutable.**

Lock:

- facial identity
- skin characteristics
- hair identity
- facial-hair pattern
- age appearance
- body proportions
- recognizable facial landmarks

Allow scene-specific changes to:

- clothing
- environment
- pose
- camera
- lighting
- expression
- accessories

For important Veo shots, generate deliberate **start and end frame images** from the master identity plus the relevant multi-angle references. The generated video's **actual extracted last frame**, not the intended end frame, is the continuity authority for the next shot.

---

## 🎙️ Sarvam Audio

Sarvam is the narration timing authority.

The workflow generates narration before final visual timing, measures the actual audio duration, and uses word/phrase/block timing when available.

The repository includes `sarvam_audio_service.py` for voice generation and caching. Existing audio should be reused whenever the narration input has not changed.

---

## 😂 Meme Intelligence

Meme selection is editorial, not decorative.

The canonical guide is:

- [MEME_INTELLIGENCE_GUIDE.md](./MEME_INTELLIGENCE_GUIDE.md)

Memes are selected from the available library using:

```text
narration trigger
→ story beat
→ emotion
→ scenario
→ meme taxonomy
→ candidate ranking
→ exact timing
→ trim
→ insert
```

A meme must have a clear narrative reason to exist and should normally be brief.

---

## 🎥 Visual Asset Strategy — Low Credit First

The system should prefer the cheapest credible visual that communicates the idea:

```text
1. Existing reusable asset
2. Existing footage / B-roll
3. Screenshot / document / photograph
4. Programmatic graphic
5. Existing meme
6. Reusable Hardik still/cutout
7. New AI image
8. Veo video
```

Veo is reserved for visuals where motion, performance, cinematic composition or continuity materially improves the story.

---

## 📊 Editorial QC

Before export, evaluate at minimum:

- narration/visual relevance
- shot density
- visual variety
- semantic repetition
- host overuse
- graphic overuse
- static holds
- meme relevance and timing
- evidence usage
- continuity where required
- photorealism and identity consistency
- audio/visual synchronization
- transitions
- music/SFX balance
- resolution/aspect ratio

QC must never fabricate a PASS. If a condition cannot actually be evaluated, report `NOT_EVALUATED` rather than pretending it passed.

A pilot cut should be validated before scaling to an 8–15 minute production.

---

## 📂 Repository Structure

```text
├── .agents/
│   ├── rules/
│   │   └── character-identity.md
│   └── skills/
│       ├── hardik-editorial-video-factory/   # PRIMARY video skill
│       ├── hardik-thumbnail-creation/         # thumbnail-only skill
│       ├── hardik-youtube-description/        # description-only skill
│       ├── hardik-youtube-title-engine/       # title/packaging skill
│       ├── meme-intelligence-guide/           # meme taxonomy skill
│       └── viral-documentary-script-engine/   # scriptwriting skill
│
├── output/
├── character/
├── research/
├── script/
├── manifest/
├── scenes/
├── ppt/
├── memes/
├── broll/
├── music/
├── sfx/
├── timeline/
├── qc/
├── exports/
│
├── CHARACTER_IDENTITY_LOCK.md
├── MEME_INTELLIGENCE_GUIDE.md
├── Master_Character_Identity_Reference.pdf
├── PHASE_3_6_IMPLEMENTATION.md
├── sarvam_audio_service.py
└── README.md
```

---

## 🛠️ Setup

Prerequisites:

- Python 3.10+
- FFmpeg (or `imageio-ffmpeg`)
- Git

Install the core dependencies as required by the active implementation.

Configure Sarvam through `.env` using the repository's environment template.

---

## ⚠️ Important Migration Note

The repository previously contained separate legacy video-factory and visual-director skills. Those duplicated the newer editorial architecture and could cause an AI coding agent to follow conflicting instructions. They have intentionally been removed.

**Use `hardik-editorial-video-factory/SKILL.md` as the authoritative video-production skill.**

The specialized title, description, thumbnail, meme and script skills remain because they represent distinct production functions rather than duplicate video-rendering instructions.

---

## 📜 License

MIT License. Created for Hardik's YouTube Automation Channel.
