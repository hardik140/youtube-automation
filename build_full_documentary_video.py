import os
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FFMPEG_EXE = r"C:\Users\91981\AppData\Local\Programs\Python\Python312\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
MANIFEST_PATH = r"e:\youtube automation\output\upi_is_scam_production\05_VIDEO_PRODUCTION_MANIFEST.json"
CHAR_DIR = r"e:\youtube automation\output\character_assets\cropped"
MEME_BASE_DIR = r"e:\youtube automation\250+ memes 😊👍"
WORK_DIR = r"e:\youtube automation\output\upi_is_scam_production\temp_render"
FINAL_DIR = r"e:\youtube automation\output\upi_is_scam_production\final_video"

os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(FINAL_DIR, exist_ok=True)

# Colors
BG_COLOR = (13, 17, 23)        # Sleek dark tech slate
CARD_BG = (22, 27, 34)         # Elevated card
TEXT_WHITE = (240, 246, 252)
TEXT_MUTED = (139, 148, 158)
ACCENT_RED = (248, 81, 73)     # Alert red
ACCENT_BLUE = (88, 166, 255)   # Tech blue
ACCENT_GOLD = (210, 153, 34)   # Warning gold
ACCENT_GREEN = (63, 185, 80)   # Safe green

def get_font(size, bold=False):
    font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
    try:
        return ImageFont.truetype(os.path.join(r"C:\Windows\Fonts", font_name), size)
    except:
        return ImageFont.load_default()

def create_scene_frame(scene_idx, scene_data, out_image_path):
    W, H = 1920, 1080
    im = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(im)

    # 1. Subtle Background Grid & Top Banner
    draw.rectangle([0, 0, W, 80], fill=(18, 22, 29))
    draw.line([(0, 80), (W, 80)], fill=(48, 54, 61), width=2)
    
    font_top = get_font(28, bold=True)
    draw.text((60, 24), "HARDIK INVESTIGATES  |  THE UPI MONETARY & SCAM REPORT", font=font_top, fill=ACCENT_BLUE)
    
    scene_tag = f"SCENE 0{scene_idx + 1} OF 07"
    draw.text((W - 300, 24), scene_tag, font=font_top, fill=TEXT_MUTED)

    # 2. Hardik Presenter Avatar & Identity Card (Right Side)
    char_img_path = os.path.join(CHAR_DIR, "hardik_front_clean.png" if scene_idx % 2 == 0 else "hardik_34left_clean.png")
    if os.path.exists(char_img_path):
        char_img = Image.open(char_img_path).convert("RGBA")
        target_w = 420
        target_h = int(char_img.height * (target_w / char_img.width))
        char_resized = char_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        # Border & Card for Hardik
        char_x = W - target_w - 70
        char_y = 125
        draw.rectangle([char_x - 10, char_y - 10, char_x + target_w + 10, char_y + target_h + 85], fill=CARD_BG, outline=(48, 54, 61), width=3)
        im.paste(char_resized, (char_x, char_y), char_resized)
        
        # Host Badge
        badge_y = char_y + target_h + 15
        draw.text((char_x + 35, badge_y), "HARDIK • TECH INVESTIGATOR", font=get_font(22, bold=True), fill=TEXT_WHITE)
        draw.text((char_x + 55, badge_y + 30), "Host & Systems Builder", font=get_font(18), fill=ACCENT_BLUE)

    # 3. Left Content Area: Scene Topic & Visual Graphic
    content_x = 80
    content_y = 130
    content_w = W - 620

    # Main Topic Header
    scene_titles = [
        "THE 3-SECOND TRAP: HOW INNOCENTS GET FROZEN",
        "THE CASH PARADOX: ₹0.005 vs ₹600 IN COSTS",
        "ZERO-MDR CRISIS: THE ₹427 CR SUBSIDY CLIFF",
        "THE VELOCITY WEAPON: DIGITAL ARREST & MULES",
        "THE 1930 DISASTER: GUILTY UNTIL PROVEN INNOCENT",
        "THE DATA PANOPTICON: WALMART & GOOGLE MONOPOLY",
        "THE 2026 CRACKDOWN & 4 SURVIVAL RULES"
    ]
    title_text = scene_titles[min(scene_idx, len(scene_titles)-1)]
    draw.text((content_x, content_y), title_text, font=get_font(36, bold=True), fill=ACCENT_GOLD)

    # Central Infographic Panel
    panel_y = content_y + 70
    panel_h = 560
    draw.rectangle([content_x, panel_y, content_x + content_w, panel_y + panel_h], fill=CARD_BG, outline=(48, 54, 61), width=2)

    # Custom Graphics per scene
    if scene_idx == 0:
        # Scene 1: Fake Bank Alert
        draw.rectangle([content_x + 40, panel_y + 60, content_x + content_w - 40, panel_y + 200], fill=(68, 18, 22), outline=ACCENT_RED, width=3)
        draw.text((content_x + 70, panel_y + 80), "⚠️  ALERT: ALL DEBITS BLOCKED BY LAW ENFORCEMENT", font=get_font(28, bold=True), fill=ACCENT_RED)
        draw.text((content_x + 70, panel_y + 130), "DIRECTIVE: CYBER CRIME COORDINATION CENTRE (1930)", font=get_font(22), fill=TEXT_WHITE)
        
        draw.text((content_x + 70, panel_y + 250), "TRIGGER: Received ₹300 via standard UPI QR Scan", font=get_font(26, bold=True), fill=TEXT_WHITE)
        draw.text((content_x + 70, panel_y + 300), "STATUS: Life savings, salary & medical funds locked (₹0 Available)", font=get_font(24), fill=ACCENT_RED)
        draw.text((content_x + 70, panel_y + 360), "TIME TO COMPROMISE: Under 3 seconds", font=get_font(24), fill=ACCENT_GOLD)

    elif scene_idx == 1:
        # Scene 2: Cash vs UPI math
        # Cash Box
        box1_w = (content_w - 120) // 2
        draw.rectangle([content_x + 40, panel_y + 60, content_x + 40 + box1_w, panel_y + 440], fill=(20, 35, 25), outline=ACCENT_GREEN, width=3)
        draw.text((content_x + 60, panel_y + 80), "💵 PHYSICAL CASH (₹100 Note)", font=get_font(26, bold=True), fill=ACCENT_GREEN)
        draw.text((content_x + 60, panel_y + 140), "• Printing Cost: ₹1.51 (RBI SPMCIL)", font=get_font(22), fill=TEXT_WHITE)
        draw.text((content_x + 60, panel_y + 190), "• Lifespan: 3 to 4 Years", font=get_font(22), fill=TEXT_WHITE)
        draw.text((content_x + 60, panel_y + 240), "• Velocity: 300 Exchanges", font=get_font(22), fill=TEXT_WHITE)
        draw.text((content_x + 60, panel_y + 300), "COST PER TRANSACTION:", font=get_font(20, bold=True), fill=TEXT_MUTED)
        draw.text((content_x + 60, panel_y + 340), "₹0.005 (Half a Paisa!)", font=get_font(34, bold=True), fill=ACCENT_GREEN)

        # UPI Box
        box2_x = content_x + 80 + box1_w
        draw.rectangle([box2_x, panel_y + 60, box2_x + box1_w, panel_y + 440], fill=(45, 20, 20), outline=ACCENT_RED, width=3)
        draw.text((box2_x + 20, panel_y + 80), "📱 UPI DIGITAL RAIL", font=get_font(26, bold=True), fill=ACCENT_RED)
        draw.text((box2_x + 20, panel_y + 140), "• Marginal Server Fee: ₹2.00 / txn", font=get_font(22), fill=TEXT_WHITE)
        draw.text((box2_x + 20, panel_y + 190), "• Payer Bank + NPCI + Receiver", font=get_font(22), fill=TEXT_WHITE)
        draw.text((box2_x + 20, panel_y + 240), "• 300 Digital Transactions:", font=get_font(22), fill=TEXT_WHITE)
        draw.text((box2_x + 20, panel_y + 300), "CUMULATIVE PROCESSING COST:", font=get_font(20, bold=True), fill=TEXT_MUTED)
        draw.text((box2_x + 20, panel_y + 340), "₹600.00 Linear Scale!", font=get_font(34, bold=True), fill=ACCENT_RED)

    elif scene_idx == 2:
        # Scene 3: Subsidy Cliff
        draw.text((content_x + 60, panel_y + 50), "GOVERNMENT SUBSIDY ALLOCATION (ZERO-MDR DEFICIT)", font=get_font(24, bold=True), fill=ACCENT_BLUE)
        
        bars = [
            ("FY 2023-24", "₹3,500 Crore", 400, ACCENT_GREEN),
            ("FY 2024-25", "₹2,000 Crore", 230, ACCENT_GOLD),
            ("Current Year", "₹427 Crore (-88% Drop!)", 50, ACCENT_RED),
        ]
        curr_y = panel_y + 120
        for year, val, bar_len, col in bars:
            draw.text((content_x + 60, curr_y), year, font=get_font(22, bold=True), fill=TEXT_WHITE)
            draw.rectangle([content_x + 250, curr_y - 5, content_x + 250 + bar_len * 2, curr_y + 35], fill=col)
            draw.text((content_x + 270 + bar_len * 2, curr_y), val, font=get_font(22, bold=True), fill=col)
            curr_y += 80
            
        draw.text((content_x + 60, panel_y + 400), "RESULT: Banks face ₹10,000+ Cr deficit, freezing cybersecurity upgrades.", font=get_font(22), fill=TEXT_MUTED)

    elif scene_idx == 3:
        # Scene 4: Digital Arrest & Mules
        draw.text((content_x + 60, panel_y + 50), "HOW DIGITAL ARREST & MULES EXPLOIT 3-SECOND VELOCITY", font=get_font(24, bold=True), fill=ACCENT_GOLD)
        
        steps = [
            ("1. Psychological Terror", "Fake video call in staged CBI/Police uniform threatening arrest."),
            ("2. Instant Settlement", "Victim transfers funds to 'Verification Account' via UPI (Irreversible)."),
            ("3. Automated Mule Mesh", "Bots split funds across 15+ accounts within 30 seconds."),
            ("4. Real-World Collateral", "Tainted cash spent at local stores or transferred to students.")
        ]
        curr_y = panel_y + 110
        for num, desc in steps:
            draw.rectangle([content_x + 50, curr_y, content_x + content_w - 50, curr_y + 70], fill=(28, 33, 40), outline=(48, 54, 61))
            draw.text((content_x + 70, curr_y + 10), num, font=get_font(22, bold=True), fill=ACCENT_BLUE)
            draw.text((content_x + 70, curr_y + 38), desc, font=get_font(20), fill=TEXT_WHITE)
            curr_y += 90

    elif scene_idx == 4:
        # Scene 5: The 1930 Freeze Loophole
        draw.rectangle([content_x + 40, panel_y + 50, content_x + content_w - 40, panel_y + 170], fill=(50, 15, 15), outline=ACCENT_RED, width=2)
        draw.text((content_x + 60, panel_y + 70), "THE LAW (Lien Only)", font=get_font(24, bold=True), fill=ACCENT_GREEN)
        draw.text((content_x + 60, panel_y + 110), "Hold ONLY the disputed ₹500. Rest of account stays free.", font=get_font(22), fill=TEXT_WHITE)
        
        draw.rectangle([content_x + 40, panel_y + 200, content_x + content_w - 40, panel_y + 320], fill=(70, 10, 10), outline=ACCENT_RED, width=3)
        draw.text((content_x + 60, panel_y + 220), "THE REALITY (Total Account Freeze)", font=get_font(24, bold=True), fill=ACCENT_RED)
        draw.text((content_x + 60, panel_y + 260), "Banks freeze 100% of funds. Citizen forced to travel 2000 km to get police NOC.", font=get_font(22), fill=TEXT_WHITE)
        
        draw.text((content_x + 60, panel_y + 380), "• Legal Principle: Innocent until proven guilty", font=get_font(22), fill=TEXT_MUTED)
        draw.text((content_x + 60, panel_y + 420), "• UPI Enforcement: Guilty until you spend ₹30,000 on legal travel", font=get_font(22, bold=True), fill=ACCENT_RED)

    elif scene_idx == 5:
        # Scene 6: Monopoly & Surveillance
        draw.text((content_x + 60, panel_y + 50), "THE UPI DUOPOLY & BEHAVIORAL SURVEILLANCE", font=get_font(24, bold=True), fill=ACCENT_BLUE)
        
        # PhonePe Card
        draw.rectangle([content_x + 60, panel_y + 110, content_x + 500, panel_y + 270], fill=(30, 20, 50), outline=(138, 43, 226), width=2)
        draw.text((content_x + 80, panel_y + 130), "PhonePe (Walmart)", font=get_font(26, bold=True), fill=(180, 120, 255))
        draw.text((content_x + 80, panel_y + 180), "• Volume Share: 45.35%", font=get_font(24), fill=TEXT_WHITE)
        draw.text((content_x + 80, panel_y + 220), "• Value Share: 48.68%", font=get_font(24), fill=TEXT_WHITE)

        # Google Pay Card
        draw.rectangle([content_x + 540, panel_y + 110, content_x + 980, panel_y + 270], fill=(20, 30, 50), outline=ACCENT_BLUE, width=2)
        draw.text((content_x + 560, panel_y + 130), "Google Pay (Alphabet)", font=get_font(26, bold=True), fill=ACCENT_BLUE)
        draw.text((content_x + 560, panel_y + 180), "• Volume Share: 34.64%", font=get_font(24), fill=TEXT_WHITE)
        draw.text((content_x + 560, panel_y + 220), "• Value Share: 34.25%", font=get_font(24), fill=TEXT_WHITE)

        draw.text((content_x + 60, panel_y + 320), "COMBINED MARKET SHARE: 80% to 85%", font=get_font(28, bold=True), fill=ACCENT_GOLD)
        draw.text((content_x + 60, panel_y + 370), "Non-transactional data collected: GPS Coordinates, Phone IMEI, Personal Social Graph.", font=get_font(22), fill=TEXT_WHITE)

    elif scene_idx == 6:
        # Scene 7: 4 Golden Rules
        draw.text((content_x + 60, panel_y + 40), "THE BUILDER'S SURVIVAL PROTOCOL (4 RULES)", font=get_font(26, bold=True), fill=ACCENT_GREEN)
        
        rules = [
            ("RULE 1: Secondary Buffer Account", "Keep savings in account A. Connect only Account B with ₹3,000 balance to UPI."),
            ("RULE 2: 'Stranger Cash' Strict NO", "Never accept cash from a stranger to transfer via UPI QR."),
            ("RULE 3: Never Scan QR to 'Receive'", "UPI PIN is strictly to SEND money. Receiving never requires a PIN."),
            ("RULE 4: Demand Formal Lien Within 24h", "If frozen, invoke RBI 2026 SOP demanding hold strictly on disputed amount.")
        ]
        curr_y = panel_y + 90
        for title, desc in rules:
            draw.rectangle([content_x + 40, curr_y, content_x + content_w - 40, curr_y + 80], fill=(22, 35, 26), outline=ACCENT_GREEN, width=1)
            draw.text((content_x + 60, curr_y + 10), title, font=get_font(22, bold=True), fill=ACCENT_GOLD)
            draw.text((content_x + 60, curr_y + 42), desc, font=get_font(20), fill=TEXT_WHITE)
            curr_y += 100

    # 4. Bottom Subtitle Lower Third (Narration Bar)
    draw.rectangle([0, H - 150, W, H], fill=(10, 12, 16))
    draw.line([(0, H - 150), (W, H - 150)], fill=(48, 54, 61), width=2)
    
    # Subtitle Text
    sub_text = scene_data["narration_text"]
    if len(sub_text) > 130:
        sub_text = sub_text[:127] + "..."
    draw.text((60, H - 105), sub_text, font=get_font(26), fill=TEXT_WHITE)

    im.save(out_image_path)
    print(f"Rendered graphic frame: {out_image_path}")

def render_scene_video(scene_idx, scene_data, out_clip_path):
    # 1. Generate frame
    frame_path = os.path.join(WORK_DIR, f"frame_scene_{scene_idx:02d}.png")
    create_scene_frame(scene_idx, scene_data, frame_path)

    audio_path = scene_data["audio_file"]
    duration = scene_data["duration_seconds"]

    # 2. Render static image + audio to MP4 with subtle slow zoom (Ken Burns effect)
    # Using ffmpeg: zoompan filter from 1.0 to 1.05
    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1", "-i", frame_path,
        "-i", audio_path,
        "-vf", f"scale=1920:1080,zoompan=z='min(zoom+0.0003,1.04)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080",
        "-c:v", "libx264", "-tune", "stillimage", "-preset", "fast",
        "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-ar", "44100", "-ac", "2",
        "-t", str(duration),
        out_clip_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Rendered scene video clip: {out_clip_path} (Duration: {duration}s)")

def reencode_meme_video(meme_rel_path, out_clip_path):
    meme_full = os.path.join(MEME_BASE_DIR, meme_rel_path)
    if not os.path.exists(meme_full):
        print(f"Warning: Meme {meme_full} not found, skipping.")
        return False
    
    cmd = [
        FFMPEG_EXE, "-y",
        "-i", meme_full,
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1",
        "-c:v", "libx264", "-preset", "fast", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-ar", "44100", "-ac", "2",
        out_clip_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Re-encoded meme clip: {out_clip_path}")
    return True

def main():
    print("=== STARTING FULL AUTOMATED DOCUMENTARY VIDEO PRODUCTION ===")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    clips_list = []
    
    for idx, scene in enumerate(manifest["scenes"]):
        scene_clip_name = f"clip_scene_{idx:02d}.mp4"
        scene_clip_path = os.path.join(WORK_DIR, scene_clip_name)
        render_scene_video(idx, scene, scene_clip_path)
        clips_list.append(scene_clip_path)

        # Process meme cutaway if available
        meme_info = scene.get("meme_cutaway")
        if meme_info and meme_info.get("clip_file"):
            meme_file = meme_info["clip_file"]
            meme_clip_name = f"meme_scene_{idx:02d}.mp4"
            meme_clip_path = os.path.join(WORK_DIR, meme_clip_name)
            if reencode_meme_video(meme_file, meme_clip_path):
                clips_list.append(meme_clip_path)

    # Concatenate all clips using concat demuxer
    concat_txt_path = os.path.join(WORK_DIR, "concat_list.txt")
    with open(concat_txt_path, "w", encoding="utf-8") as f:
        for c in clips_list:
            # Escape path for ffmpeg concat
            escaped_path = c.replace("\\", "/")
            f.write(f"file '{escaped_path}'\n")

    final_output_video = os.path.join(FINAL_DIR, "WHY_UPI_IS_BECOMING_INDIAS_BIGGEST_FINANCIAL_NIGHTMARE.mp4")
    print("\nConcatenating all scenes and meme cutaways into master video...")
    
    concat_cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_txt_path,
        "-c", "copy",
        final_output_video
    ]
    subprocess.run(concat_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    file_size_mb = os.path.getsize(final_output_video) / (1024 * 1024)
    print("\nSUCCESS: MASTER DOCUMENTARY VIDEO READY!")
    print(f"Output: {final_output_video}")
    print(f"File Size: {file_size_mb:.2f} MB")
    print(f"Total Segments Combined: {len(clips_list)}")

if __name__ == "__main__":
    main()
