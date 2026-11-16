# Branded 16:9 cards whose content sits in the central 9:16 column (for Shorts), KEPT ALIVE palette.
# Then renders each card as a 20 s push-in mp4 (+ silent audio) into the clips dir, usable like a clip.
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont
F = "/root/.fonts/"
CLIPS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/clips"
def font(n, s): return ImageFont.truetype(F + n, s)
NIGHT, GAUZE, SCRUB, MON, IOD, STEEL, PANEL = "#0A1214", "#EEF2EF", "#2BB3A3", "#6CF29A", "#F2B33D", "#8A9AA0", "#13242A"
W, H = 3840, 2160; CX = W // 2; COL = int(H * 9 / 16)  # 1215 px column
def card(name, kicker, rows, foot):
    # layout keeps clear of the Shorts hook (top ~28%) and caption band (~58-70%)
    im = Image.new("RGB", (W, H), NIGHT); d = ImageDraw.Draw(im)
    d.rectangle([CX - COL // 2, 0, CX + COL // 2, H], fill=PANEL)
    tot = sum(int(sz * 1.02) for _, sz, _ in rows); y = 900 - tot // 2
    for txt, size, col in rows:
        fnt = font("SairaCondensed-ExtraBold.ttf", size)
        d.text((CX, y + size // 2), txt, font=fnt, fill=col, anchor="mm"); y += int(size * 1.02)
    d.rectangle([CX - 160, 1600, CX + 160, 1614], fill=SCRUB)
    d.text((CX, 1690), foot, font=font("SourceSans3-SemiBold.ttf", 56), fill=GAUZE, anchor="mm")
    d.text((CX, 1790), kicker, font=font("MartianMono-Medium.ttf", 44), fill=STEEL, anchor="mm")
    im.save(f"cards/{name}.jpg", quality=94)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", f"cards/{name}.jpg", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                    "-filter_complex", "[0:v]scale=7680:-2,zoompan=z='1+0.0003*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=600:s=1920x1080:fps=30,format=yuv420p[v]",
                    "-map", "[v]", "-map", "1:a", "-t", "20", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "aac", f"{CLIPS}/{name}.mp4"], check=True)
import os; os.makedirs("cards", exist_ok=True)
card("card_9in10", "IRAQ & AFGHANISTAN · 2001-2011", [("9 IN 10", 280, MON), ("POTENTIALLY SURVIVABLE", 100, GAUZE), ("LINKED TO BLEEDING", 110, IOD)], "Eastridge et al., J Trauma 2012")
card("card_87", "4,596 U.S. BATTLEFIELD DEATHS", [("87%", 320, MON), ("DIED BEFORE REACHING", 100, GAUZE), ("A MEDICAL FACILITY", 100, IOD)], "Iraq & Afghanistan, 2001-2011")
card("card_70k", "AMERICAN EXPEDITIONARY FORCES · WWI", [("70,522", 280, MON), ("GAS CASES", 150, GAUZE), ("REPORTED", 110, IOD)], "Source: U.S. Army Heritage Center")
card("card_31", "AMERICAN EXPEDITIONARY FORCES · WWI", [("31%", 320, MON), ("OF ALL AEF CASUALTIES", 100, GAUZE), ("WERE GAS CASES", 110, IOD)], "31.49% · U.S. Army Heritage Center")
card("card_1221", "OF 70,522 U.S. GAS CASES · WWI", [("1,221", 300, MON), ("DIED", 150, GAUZE), ("MOST FROM MUSTARD GAS", 90, IOD)], "Source: U.S. Army Heritage Center")
card("card_decon", "WWI MUSTARD GAS · BEFORE THE HOSPITAL", [("STEP 1", 240, MON), ("UNIFORM OFF", 130, GAUZE), ("BATH · NEW CLOTHES", 100, IOD)], "Source: Army Nurse Corps Association")
card("card_prize", "DARPA TRIAGE CHALLENGE · FINALS 2026", [("$1.5M", 300, MON), ("GRAND PRIZE", 140, GAUZE), ("ROBOSCOUT · U. OF MARYLAND", 76, IOD)], "$3.8M in total prizes · Source: DARPA")
print("cards ok")
