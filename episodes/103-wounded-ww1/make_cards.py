# Branded 16:9 cards whose content sits in the central 9:16 column (for Shorts), KEPT ALIVE palette,
# plus 20 s push-ins of archival stills. Renders each as a 20 s mp4 (+ silent audio) into the clips dir.
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont
F = "/root/.fonts/"
CLIPS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/clips"
def font(n, s): return ImageFont.truetype(F + n, s)
NIGHT, GAUZE, SCRUB, MON, IOD, STEEL, PANEL = "#0A1214", "#EEF2EF", "#2BB3A3", "#6CF29A", "#F2B33D", "#8A9AA0", "#13242A"
W, H = 3840, 2160; CX = W // 2; COL = int(H * 9 / 16)
def push(img, name):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", img, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                    "-filter_complex", "[0:v]scale=7680:-2,zoompan=z='1+0.0003*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=600:s=1920x1080:fps=30,format=yuv420p[v]",
                    "-map", "[v]", "-map", "1:a", "-t", "20", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "aac", f"{CLIPS}/{name}.mp4"], check=True)
def card(name, kicker, rows, foot):
    im = Image.new("RGB", (W, H), NIGHT); d = ImageDraw.Draw(im)
    d.rectangle([CX - COL // 2, 0, CX + COL // 2, H], fill=PANEL)
    tot = sum(int(sz * 1.02) for _, sz, _ in rows); y = 900 - tot // 2
    for txt, size, col in rows:
        d.text((CX, y + size // 2), txt, font=font("SairaCondensed-ExtraBold.ttf", size), fill=col, anchor="mm"); y += int(size * 1.02)
    d.rectangle([CX - 160, 1600, CX + 160, 1614], fill=SCRUB)
    d.text((CX, 1690), foot, font=font("SourceSans3-SemiBold.ttf", 56), fill=GAUZE, anchor="mm")
    d.text((CX, 1790), kicker, font=font("MartianMono-Medium.ttf", 44), fill=STEEL, anchor="mm")
    im.save(f"cards/{name}.jpg", quality=94); push(f"cards/{name}.jpg", name)
os.makedirs("cards", exist_ok=True)
card("card_flu", "U.S. ARMY IN FRANCE · 1918", [("340,000", 250, MON), ("IN HOSPITAL: FLU", 104, GAUZE), ("227,000", 250, MON), ("IN HOSPITAL: WOUNDS", 96, IOD)], "Sources: National Guard · Byerly, PHR 2010")
card("card_45k", "U.S. SOLDIERS · BY THE END OF 1918", [("45,000", 280, MON), ("DEAD OF FLU", 130, GAUZE), ("AND PNEUMONIA", 110, GAUZE), ("NEARLY AS MANY AS COMBAT", 72, IOD)], "Source: National Guard Bureau")
card("card_blood", "U.S. ARMY · 1917", [("22", 330, MON), ("UNITS OF BLOOD", 120, GAUZE), ("STORED ON ICE", 110, GAUZE), ("THE FIRST BLOOD BANK", 84, IOD)], "Sources: Stanford Blood Center · NLM")
card("card_80", "THIGH-BONE FRACTURES · 1914–15", [("4 IN 5", 280, MON), ("DIED", 140, GAUZE), ("EARLY-WAR ESTIMATE", 90, GAUZE), ("COL. SIR HENRY GRAY", 80, IOD)], "Source: J. Special Operations Medicine, 2014")
card("card_156", "ARRAS · 1917 · 1,009 MEN", [("15.6%", 280, MON), ("DIED", 140, GAUZE), ("SPLINT IN WIDE USE", 104, GAUZE), ("ABOUT 1 IN 6", 90, IOD)], "Source: Gray 1919 · via JSOM 2014")
for k, f in [("stl_thomas_bed", "splint_thomas_leg_splint_application_fig11"), ("stl_thomas_str", "splint_thomas_halfring_stretcher_transport_fig13"), ("stl_cantigny", "v8_p296_regimental_aid_station_cantigny_1918")]:
    push(f"/home/claude/work/stills16/{f}.jpg", k)
print("cards ok")
