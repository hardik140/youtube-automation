# 🎬 Hardik — AI YouTube Video Factory & Automation Engine

> **End-to-End Automated YouTube Production Pipeline**  
> Frame-First • Master Character Identity • Multi-Angle Consistency • Sarvam AI TTS • Meme Placement • Automated 1080p Video Compilation

---

## 📌 Overview

This repository contains the complete automated video production system tailored for **Hardik's YouTube Channel** (Investigative Documentary, Tech, Systems Architecture, and Business Explainer content).

It combines structured AI agent skills, a permanent master character reference system, Indian voiceover generation (Sarvam AI), an intelligent meme selection taxonomy, and automated Python/FFmpeg video rendering.

---

## 🚀 Key Features & Architecture

```text
RESEARCH & KNOWLEDGE
       ↓
VIRAL SCRIPT ENGINE (Hooks, Open Loops, Stakes)
       ↓
MASTER CHARACTER IDENTITY LOCK (Permanent 10-Angle Visual Consistency)
       ↓
SARVAM AI AUDIO GENERATION (Persistent Caching & Timing Authority)
       ↓
MEME INTELLIGENCE PLACEMENT (248 Catalogued Clips)
       ↓
AUTOMATED VIDEO COMPILATION (1080p Motion Graphics, Subtitles, Concat)
       ↓
HIGH-CTR TITLES, THUMBNAILS & METADATA PACKAGING
```

### 1. Master Character Identity Lock
- Anchored by [Master_Character_Identity_Reference.pdf](./Master_Character_Identity_Reference.pdf) and [CHARACTER_IDENTITY_LOCK.md](./CHARACTER_IDENTITY_LOCK.md).
- **Core Law**: *Identity is immutable; scene variables are mutable.*
- 10-camera-angle photographic reference sheet providing spatial and facial consistency across all image models and video renders.

### 2. Sarvam AI Voiceover Engine
- Implemented in [sarvam_audio_service.py](./sarvam_audio_service.py).
- High-fidelity Indian English and Hindi speech synthesis (`bulbul:v3` / `aditya` voice).
- **Smart Credit-Saving Cache**: `{project_id}_{scene_id}_{voice}_{hash}.wav` prevents burning API credits on unchanged text.
- **Timing Authority**: Auto-measures WAV duration to establish exact cut pacing for video scenes.

### 3. Meme Intelligence & Cutaway System
- Documented in [MEME_INTELLIGENCE_GUIDE.md](./MEME_INTELLIGENCE_GUIDE.md).
- Taxonomy mapping narrative tension, surprise, corporate greed, and irony directly to video meme templates.

### 4. Automated Video Compiler
- Script: [build_full_documentary_video.py](./build_full_documentary_video.py).
- Generates 1920x1080 presentation frames using Pillow, applies smooth Ken Burns zoompan camera motion, overlays character badges and subtitles, and merges meme cutaways into a final master MP4 video.

### 5. Production Showcase: The UPI Scam Documentary
Full case study and production artifacts inside [`output/upi_is_scam_production/`](./output/upi_is_scam_production/):
- **01_COMPREHENSIVE_RESEARCH_BRIEF.md**: Mathematical proof of Cash amortization (₹0.005/txn) vs. UPI Linear Cost (₹2/txn), Zero-MDR subsidy collapse, and 2026 Supreme Court / RBI MuleHunter.AI updates.
- **02_HIGH_CTR_TITLE_PACKAGES.md**: 10 scored title concepts.
- **03_THUMBNAIL_PACKAGING_SYSTEM.md**: 3 viral compositions with prompt locks.
- **04_MASTER_VIRAL_SCRIPT.md**: Full 12–14 minute script with camera cues and meme triggers.
- **05_VIDEO_PRODUCTION_MANIFEST.json**: Scene-by-scene manifest with character prompts and audio blocks.
- **06_YOUTUBE_DESCRIPTION_AND_METADATA.md**: Chapters, helplines (1930), and pinned comment.

---

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.10+
- FFmpeg (or `imageio-ffmpeg`)
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/hardik140/youtube-automation.git
cd youtube-automation

# Install required dependencies
pip install yt-dlp Pillow imageio-ffmpeg PyMuPDF python-dotenv
```

### Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Add your Sarvam AI API Key:
```env
SARVAM_API_KEY=your_sarvam_api_key_here
```

---

## ⚡ Usage

### 1. Test Sarvam AI Voiceover
```bash
python sarvam_audio_service.py
```

### 2. Build Full Documentary Video
```bash
python build_full_documentary_video.py
```

### 3. Batch Download Reference Videos in 480p
```bash
python download_videos.py
```

---

## 📂 Repository Structure

```text
├── .agents/                          # Custom Antigravity / Claude Agent Skills
│   ├── rules/                        # Permanent workspace rules & identity locks
│   └── skills/                       # Installed production skills
├── output/                           # Production deliverables & character assets
│   ├── character_assets/             # Cropped master character portraits
│   └── upi_is_scam_production/       # Complete UPI documentary package & manifest
├── my research/                      # In-depth research papers & raw notes
├── build_full_documentary_video.py   # Full automated video rendering pipeline
├── download_videos.py                # Multi-URL 480p video downloader
├── sarvam_audio_service.py           # Sarvam AI TTS caching & timing module
├── CHARACTER_IDENTITY_LOCK.md        # Main onscreen explainer prompt lock
├── MEME_INTELLIGENCE_GUIDE.md        # 248 video meme decision guide
├── Master_Character_Identity_Reference.pdf # Visual reference master sheet
├── .env.example                      # Template for API keys
└── README.md                         # Project documentation
```

---

## 📜 License
MIT License. Created for Hardik's YouTube Automation Channel.
