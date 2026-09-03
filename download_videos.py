import os
import sys
import yt_dlp

FFMPEG_PATH = r"C:\Users\91981\AppData\Local\Programs\Python\Python312\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
DOWNLOAD_DIR = r"e:\youtube automation\downloaded_videos"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

urls = [
    "https://youtu.be/l1kEAAFDVpw?si=M208YSiibrVL_K2L",
    "https://youtu.be/54oQFGJ-xAI?si=38Gsqve7ya-iPR6a",
    "https://youtu.be/BlGyAH5NSKQ?si=GIso92IXNNefX0Wz",
    "https://youtu.be/2Mzn5VGW3hY?si=lebE7VW_zVO6x9qv",
    "https://youtu.be/bzbsJGMVHxQ?si=FoSZsUhy4M5qY2ST",
    "https://youtu.be/TTGczb8uLA0?si=ybN0Km1HVuwS7u8h"
]

ydl_opts = {
    'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]/best',
    'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s [%(id)s].%(ext)s'),
    'ffmpeg_location': FFMPEG_PATH,
    'merge_output_format': 'mp4',
    'noplaylist': True,
    'ignoreerrors': True,
    'quiet': False,
    'no_warnings': False
}

print(f"Starting download of {len(urls)} videos in 480p to '{DOWNLOAD_DIR}'...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for idx, url in enumerate(urls, 1):
        print(f"\n[{idx}/{len(urls)}] Processing: {url}")
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {e}")

print("\nAll downloads finished! Checking directory contents:")
for f in os.listdir(DOWNLOAD_DIR):
    fp = os.path.join(DOWNLOAD_DIR, f)
    size_mb = os.path.getsize(fp) / (1024 * 1024)
    print(f" - {f} ({size_mb:.2f} MB)")
