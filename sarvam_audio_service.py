"""
Sarvam AI Audio Service for Hardik AI Video Factory
Implements caching, narration block generation, and duration measurement as specified in Section 23 of HARDIK_AI_VIDEO_FACTORY_MASTER_SKILL.md.
"""

import os
import json
import base64
import hashlib
import wave
import urllib.request
import urllib.error
from pathlib import Path

DEFAULT_VOICE = "aditya"  # Options: 'aditya', 'shubh', 'anand', 'rahul', 'kabir', etc.
DEFAULT_MODEL = "bulbul:v3"

def get_sarvam_api_key():
    key = os.getenv("SARVAM_API_KEY")
    if not key:
        env_file = Path(__file__).resolve().parent / ".env"
        if env_file.exists():
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("SARVAM_API_KEY="):
                        key = line.strip().split("=", 1)[1].strip().strip('"').strip("'")
                        break
    if not key:
        raise ValueError("SARVAM_API_KEY not found in environment or .env file.")
    return key

def get_audio_duration_wav(file_path):
    """Calculates duration in seconds from a WAV file header."""
    try:
        with wave.open(str(file_path), 'r') as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            return round(frames / float(rate), 2)
    except Exception:
        return None

def generate_sarvam_audio(
    text: str,
    project_id: str = "project",
    scene_id: str = "scene_01",
    speaker: str = DEFAULT_VOICE,
    target_language_code: str = "hi-IN",
    output_dir: str = "output/audio",
    pitch: float = 0.0,
    pace: float = 1.0,
    model: str = DEFAULT_MODEL
):
    """
    Generates narration audio via Sarvam AI with persistent disk caching.
    Filename pattern: {project_id}_{scene_or_block}_{voice_id}_{text_hash}.wav
    """
    api_key = get_sarvam_api_key()
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    text_hash = hashlib.sha256(f"{text}_{speaker}_{pace}_{target_language_code}".encode("utf-8")).hexdigest()[:10]
    filename = f"{project_id}_{scene_id}_{speaker}_{text_hash}.wav"
    dest_file = out_path / filename

    # Cache hit check
    if dest_file.exists() and dest_file.stat().st_size > 0:
        duration = get_audio_duration_wav(dest_file)
        return {
            "cached": True,
            "file_path": str(dest_file),
            "filename": filename,
            "duration_seconds": duration,
            "speaker": speaker
        }

    # API Request
    url = "https://api.sarvam.ai/text-to-speech"
    headers = {
        "api-subscription-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": [text],
        "target_language_code": target_language_code,
        "speaker": speaker,
        "pitch": pitch,
        "pace": pace,
        "model": model
    }

    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            audios = data.get("audios", [])
            if not audios:
                raise RuntimeError("No audio returned by Sarvam AI.")
            
            # Base64 decode audio
            audio_bytes = base64.b64decode(audios[0])
            with open(dest_file, "wb") as f:
                f.write(audio_bytes)
            
            duration = get_audio_duration_wav(dest_file)
            return {
                "cached": False,
                "file_path": str(dest_file),
                "filename": filename,
                "duration_seconds": duration,
                "speaker": speaker
            }
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode("utf-8")
        raise RuntimeError(f"Sarvam AI HTTP {e.code}: {error_msg}")

if __name__ == "__main__":
    print("Testing Sarvam Audio Service...")
    res = generate_sarvam_audio(
        text="हार्दिक के ऑटोमेशन स्टूडियो में आपका स्वागत है।",
        project_id="hardik_demo",
        scene_id="intro",
        speaker="aditya",
        target_language_code="hi-IN"
    )
    print("Audio result:", res)
