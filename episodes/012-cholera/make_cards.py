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





card("card_brew", "BROAD STREET · LONDON · 1854", [("70+", 300, MON), ("BREWERY WORKERS", 120, GAUZE), ("0 SEVERE CASES", 110, IOD)], "Source: John Snow, 1855")
card("card_500", "SOHO, LONDON · 1854", [("500+", 320, MON), ("DEATHS IN 10 DAYS", 120, GAUZE), ("NEAR ONE PUMP", 100, IOD)], "Source: John Snow, 1855")
card("card_61", "SNOW'S INQUIRY · 1854", [("61", 320, MON), ("VICTIMS SAID TO HAVE", 110, GAUZE), ("DRUNK THE PUMP WATER", 110, IOD)], "Of 73 deaths near the pump · Source: John Snow, 1855")
card("card_2ft8", "40 BROAD STREET · 1855", [("2 FT 8 IN", 230, MON), ("CESSPOOL", 130, GAUZE), ("TO WELL", 130, IOD)], "Surveyor's report · UCLA Snow archive")
card("card_typh", "TYPHOID FEVER · U.S. · PER 100,000", [("1900: ~100", 190, GAUZE), ("2006: 0.1", 190, MON), ("~1,000X DROP", 120, IOD)], "Source: CDC")
card("card_1908", "JERSEY CITY, NEW JERSEY", [("1908", 300, MON), ("FIRST U.S. CITY", 120, GAUZE), ("TO ROUTINELY DISINFECT", 90, IOD)], "Routine disinfection · Source: CDC")
print("cards ok")
