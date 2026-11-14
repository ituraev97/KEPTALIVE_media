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





card("card_flu1918", "1918 PANDEMIC · EARLY FLU VACCINES", [("1918", 300, MON), ("WRONG GERM", 140, GAUZE), ("AIMED AT BACTERIA", 100, IOD)], "Sources: WHO · CDC")
card("card_flu1945", "FRANCIS & SALK · U. OF MICHIGAN", [("1945", 300, MON), ("INACTIVATED FLU VACCINE", 100, GAUZE), ("LICENSED FOR CIVILIANS", 90, IOD)], "Tested on the U.S. military · CDC, WHO")
card("card_flu1930", "1930s · INFLUENZA VIRUS ISOLATED", [("1930s", 300, MON), ("A VIRUS", 140, GAUZE), ("NOT BACTERIA", 120, IOD)], "Source: CDC")
card("card_97k", "LANDSTUHL · GERMANY", [("97,000+", 280, MON), ("TROOPS TREATED", 130, GAUZE), ("FROM 56 COUNTRIES", 100, IOD)], "Wounded, injured and ill · Source: U.S. Army")
card("card_56", "LANDSTUHL · MEDICAL EVACUATIONS", [("56", 320, MON), ("COUNTRIES", 140, GAUZE), ("EUROPE · AFRICA · MIDDLE EAST", 80, IOD)], "U.S. and coalition troops · Source: U.S. Army")
card("card_99", "LANDSTUHL REGIONAL MEDICAL CENTER", [("99%", 320, MON), ("SURVIVAL RATE", 130, GAUZE), ("AS REPORTED BY THE ARMY", 80, IOD)], "Source: army.mil, April 2023")
card("card_4ships", "U.S. COAST GUARD · OCT 26 – NOV 5, 2026", [("4", 320, MON), ("CRUISE SHIP MEDEVACS", 120, GAUZE), ("IN 11 DAYS", 120, IOD)], "Source: U.S. Coast Guard releases via DVIDS")
print("cards ok")
