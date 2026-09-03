# Pilot Video Production Audit: UPI Scam Investigation

> **Project ID:** `upi_scam_documentary_01`  
> **Source of Truth:** [`output/upi_is_scam_production/05_VIDEO_PRODUCTION_MANIFEST.json`](file:///e:/youtube%20automation/output/upi_is_scam_production/05_VIDEO_PRODUCTION_MANIFEST.json)  
> **Host Identity:** Hardik ([`CHARACTER_IDENTITY_LOCK.md`](file:///e:/youtube%20automation/CHARACTER_IDENTITY_LOCK.md))  
> **Voice:** Sarvam AI (`aditya`, `bulbul:v3`)  
> **Target Output:** 1080p Full Documentary Video (`pilot/final/pilot_video.mp4`)

---

## 1. Inventory of Existing Assets

| Asset Category | Location | Status | Action in Pilot |
| :--- | :--- | :--- | :--- |
| **Video Manifest** | `output/upi_is_scam_production/05_VIDEO_PRODUCTION_MANIFEST.json` | Complete (7 scenes) | Source of truth; expanded into 28 visual beats |
| **Master Script** | `output/upi_is_scam_production/04_MASTER_VIRAL_SCRIPT.md` | Complete (~13 min) | Provides narrative context & caption baseline |
| **Narration Audio** | `output/upi_is_scam_production/audio/*.wav` (7 files) | Verified & Measured (133.4s) | Copied into `pilot/audio/` as timing authority |
| **Character Identity** | `Master_Character_Identity_Reference.pdf` | 10-angle reference sheet | Base identity for all Hardik frames |
| **Character Crops** | `output/character_assets/cropped/hardik_front_clean.png`, `hardik_34left_clean.png` | Verified high-res | Used for start/end frames & host scenes |
| **Meme Catalog** | `MEME_INTELLIGENCE_GUIDE.md` | 248 catalogued video memes | Selection authority for emotional cutaways |
| **Meme Video Files** | `250+ memes 😊👍` (6 specific files) | 100% verified | Re-encoded to 1080p 30fps stereo in `pilot/memes/selected/` |
| **FFmpeg Binary** | `imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe` | Functional 7.1 build | Standalone rendering & concatenation engine |
| **Pipeline Tools** | `pipeline/*.py` | Modular Phase 3–6 scripts | Executed to build beats, manifests, and QC |

---

## 2. Gap Analysis & What Must Be Generated

1. **Multi-Beat Expansion**: The 7 scenes must be expanded into 25–35 visual beats (`pilot/pilot_manifest.json`) so visual changes happen every 2–5 seconds.
2. **Frame-First Start & End Anchors**: Each scene requires a dedicated `start_frame.png` and `end_frame.png` with physical continuity.
3. **Veo 3 Prompts**: Production-ready Veo 3 camera and lighting prompts for each scene (`veo_prompt.txt`).
4. **Last Frame Continuity Extractions**: Actual extracted final frame (`last_frame.png`) using `pipeline/extract_last_frame.py` to link to the next scene.
5. **Captions**: Standard `captions.srt` and `captions.vtt` synchronized with Sarvam AI audio.
6. **Audio Mix**: Royalty-free tension background score ducked at -16dB under voiceover, plus SFX (whoosh, alert drop).
7. **Google Vids Manifest**: Standardized 8-track `google_vids_manifest.json` for UI assembly.
8. **Automated QC Suite**: Output reports in `pilot/qc/`.

---

## 3. Credit Optimization & Reuse Guarantee

* **Sarvam AI Voice Credits Used:** **0** (All 7 scene audio files are reused directly from cache).
* **AI Image Credits Conserved:** Master character reference portraits from PDF are composited with scene-specific data graphics, avoiding hundreds of redundant generations.
* **Meme Reuse:** 100% local video clips from `250+ memes 😊👍`.
