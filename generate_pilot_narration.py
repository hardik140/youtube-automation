import os
import re
import json
import wave
import subprocess
from pathlib import Path
from sarvam_audio_service import generate_sarvam_audio, get_audio_duration_wav

FFMPEG = r"C:\Users\91981\AppData\Local\Programs\Python\Python312\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

def main():
    script_text = Path("script/narration.txt").read_text(encoding="utf-8")

    # Split into natural sentences
    sentences = [s.strip() for s in re.split(r"(?<=[.!?।])\s+", script_text) if s.strip()]

    # Group sentences into chunks <= 400 chars
    chunks = []
    current = ""
    for s in sentences:
        if len(current) + len(s) + 1 <= 400:
            current = (current + " " + s).strip()
        else:
            if current:
                chunks.append(current)
            current = s
    if current:
        chunks.append(current)

    print(f"Split script into {len(chunks)} chunks:")
    chunk_wavs = []
    chunk_metadata = []
    time_cursor = 0.0

    for i, c in enumerate(chunks):
        wav = generate_sarvam_audio(
            text=c,
            project_id="controlled_pilot",
            scene_id=f"chunk_{i+1:02d}",
            output_dir="audio/chunks"
        )
        try:
            with wave.open(str(wav), "rb") as wf:
                d = round(wf.getnframes() / float(wf.getframerate()), 2)
        except Exception as err:
            print(f"Error reading {wav}: {err}")
            d = 0.0
        chunk_metadata.append({
            "chunk_id": f"chunk_{i+1:02d}",
            "text": c,
            "file": wav,
            "start_time": round(time_cursor, 2),
            "end_time": round(time_cursor + d, 2),
            "duration": d
        })
        time_cursor += d
        print(f"  Chunk {i+1} audio: {wav} ({d}s)")

    # Concat with ffmpeg
    concat_file = Path("audio/chunks/concat.txt")
    with open(concat_file, "w", encoding="utf-8") as f:
        for w in chunk_wavs:
            p = Path(w).resolve().as_posix()
            f.write(f"file '{p}'\n")

    master_narration = Path("audio/narration.wav")
    subprocess.run([
        FFMPEG, "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(master_narration)
    ], check=True)

    total_dur = get_audio_duration_wav(master_narration)
    print(f"\nMASTER NARRATION AUDIO CREATED: {master_narration} (Duration: {total_dur}s)")

    timing_manifest = {
        "audio_file": str(master_narration.resolve()),
        "total_duration_seconds": total_dur,
        "chunks_count": len(chunks),
        "chunks": chunk_metadata
    }
    Path("audio/timing.json").write_text(json.dumps(timing_manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Wrote audio/timing.json successfully.")

if __name__ == "__main__":
    main()
