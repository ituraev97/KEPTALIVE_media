# s018 Shorts (Tue 2026-11-24): Desmond Doss portrait (The AMEDD Historian no. 1, 2013, public domain mark, archive.org TheAMEDDHistorianIssue1.1)
# + one distance card for the Koningsdam medevac,
# as 20 s push-in clips (1920x1080, 30p, silent audio) for shorts.py.
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps
Image.MAX_IMAGE_PIXELS = None
F = "/root/.fonts/"; S = "/home/claude/work/stills"
CLIPS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/clips"
def font(n, s): return ImageFont.truetype(F + n, s)
NIGHT, GAUZE, SCRUB, MON, IOD, STEEL, PANEL = "#0A1214", "#EEF2EF", "#2BB3A3", "#6CF29A", "#F2B33D", "#8A9AA0", "#13242A"
W, H = 3840, 2160; CX = W // 2; COL = int(H * 9 / 16)
os.makedirs("cards", exist_ok=True)
def pushin(name, jpg):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", jpg, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                    "-filter_complex", "[0:v]scale=7680:-2,zoompan=z='1+0.0003*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=600:s=1920x1080:fps=30,format=yuv420p[v]",
                    "-map", "[v]", "-map", "1:a", "-t", "20", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "aac", f"{CLIPS}/{name}.mp4"], check=True)
def card(name, kicker, rows, foot):
    im = Image.new("RGB", (W, H), NIGHT); d = ImageDraw.Draw(im)
    d.rectangle([CX - COL // 2, 0, CX + COL // 2, H], fill=PANEL)
    tot = sum(int(sz * 1.02) for _, sz, _ in rows); y = 900 - tot // 2
    for txt, size, col in rows:
        fnt = font("SairaCondensed-ExtraBold.ttf", size)
        while d.textlength(txt, font=fnt) > COL - 90: size -= 4; fnt = font("SairaCondensed-ExtraBold.ttf", size)
        d.text((CX, y + size // 2), txt, font=fnt, fill=col, anchor="mm"); y += int(size * 1.02)
    d.rectangle([CX - 160, 1600, CX + 160, 1614], fill=SCRUB)
    for txt, yy, fn, sz, col in ((foot, 1690, "SourceSans3-SemiBold.ttf", 56, GAUZE), (kicker, 1790, "MartianMono-Medium.ttf", 40, STEEL)):
        fnt = font(fn, sz)
        while d.textlength(txt, font=fnt) > COL - 60: sz -= 2; fnt = font(fn, sz)
        d.text((CX, yy), txt, font=fnt, fill=col, anchor="mm")
    im.save(f"cards/{name}.jpg", quality=94); pushin(name, f"cards/{name}.jpg")
def still(name, src, box, fill_h=True, tone=True):
    im = Image.open(f"{S}/{src}").convert("RGB").crop(box)
    if tone: im = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1).convert("RGB")
    can = Image.new("RGB", (W, H), NIGHT)
    s = H / im.height; im = im.resize((int(im.width * s), H), Image.LANCZOS)
    if im.width > W: x0 = (im.width - W) // 2; im = im.crop((x0, 0, x0 + W, H))
    can.paste(im, ((W - im.width) // 2, 0)); can.save(f"cards/{name}.jpg", quality=94); pushin(name, f"cards/{name}.jpg")



# ---- s1 Desmond Doss: Cpl. Doss wearing the Medal of Honor, 1945 (The AMEDD Historian no. 1, p. 6; image extracted from the PDF)
still("st_doss", "doss_amedd.jpg", (0, 0, 727, 1024), tone=False)
still("st_doss_face", "doss_amedd.jpg", (60, 0, 727, 700), tone=False)
# ---- s2 Koningsdam medevac (DVIDS 1030654 description)
card("card_80mi", "COAST GUARD MEDEVAC · NOV. 20, 2026", [("~80", 300, MON), ("MILES", 170, GAUZE), ("OFF SAN DIEGO", 120, IOD)], "Cruise ship Koningsdam")
# ---- s3 red cross in the Pacific (National Museum of the Pacific War, 2024; Forrestal 1945 as quoted there)
card("card_target", "NATIONAL MUSEUM OF THE PACIFIC WAR", [("\"AN INTENTIONAL", 150, GAUZE), ("EFFORT TO TARGET", 150, GAUZE), ("AMERICAN CORPSMEN\"", 130, MON)], "Japanese forces, WWII Pacific")
card("card_forrestal", "NAVY SECRETARY JAMES FORRESTAL · 1945", [("\"SNIPER'S BULLETS", 140, GAUZE), ("WERE AIMED AT", 140, GAUZE), ("THE BRASSARDS", 150, MON), ("ON YOUR ARMS\"", 130, IOD)], "As quoted by the Pacific War museum")
print("cards ok")
