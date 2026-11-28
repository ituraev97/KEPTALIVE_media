# s020 cards: number cards (s1, Table 115) + page crops (s1 table, s2 pages 51). Both from Army Medical Dept. in the World War (public domain, U.S. government):
#  s1: Internet Archive item WW1ArmyMedDeptHistV15-2 (vol. XV pt 2, Medical and Casualty Statistics, 1925), printed p.1024 = leaf 1036 (leaf = printed page + 12)
#  s2: Internet Archive item WW1ArmyMedDeptHistV11-1 (vol. XI Surgery pt 1, 1927), printed p.51 = leaf 83 (leaf = printed page + 32)
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
F = "/root/.fonts/"; S = "/home/claude/work/stills"
CLIPS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/clips"
def font(n, s): return ImageFont.truetype(F + n, s)
NIGHT, GAUZE, SCRUB, MON, IOD, STEEL, PANEL = "#0A1214", "#EEF2EF", "#2BB3A3", "#6CF29A", "#F2B33D", "#8A9AA0", "#13242A"
W, H = 3840, 2160; CX = W // 2; COL = int(H * 9 / 16)
os.makedirs("cards", exist_ok=True); os.makedirs(S, exist_ok=True); os.makedirs(CLIPS, exist_ok=True)
def scan(item, leaf, tag):
    f = f"{S}/{tag}{leaf}.jpg"
    if not os.path.exists(f) or os.path.getsize(f) < 50000:
        subprocess.run(["curl", "-sL", "-o", f, f"https://archive.org/download/{item}/page/n{leaf}_w1600.jpg"], check=True)
    return f
def pushin(name, jpg):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", jpg, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                    "-filter_complex", "[0:v]scale=7680:-2,zoompan=z='1+0.0003*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=600:s=1920x1080:fps=30,format=yuv420p[v]",
                    "-map", "[v]", "-map", "1:a", "-t", "20", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "aac", f"{CLIPS}/{name}.mp4"], check=True)
def frame(d): d.rectangle([CX - COL // 2, 0, CX + COL // 2, H], fill=PANEL)
def tail(d, kicker, foot):
    d.rectangle([CX - 160, 1600, CX + 160, 1614], fill=SCRUB)
    for txt, yy, fn, sz, col in ((foot, 1690, "SourceSans3-SemiBold.ttf", 56, GAUZE), (kicker, 1790, "MartianMono-Medium.ttf", 40, STEEL)):
        fnt = font(fn, sz)
        while d.textlength(txt, font=fnt) > COL - 200: sz -= 2; fnt = font(fn, sz)
        d.text((CX, yy), txt, font=fnt, fill=col, anchor="mm")
def card(name, kicker, rows, foot):
    im = Image.new("RGB", (W, H), NIGHT); d = ImageDraw.Draw(im); frame(d)
    tot = sum(int(sz * 1.02) for _, sz, _ in rows); y = 950 - tot // 2
    for txt, size, col in rows:
        fnt = font("SairaCondensed-ExtraBold.ttf", size)
        while d.textlength(txt, font=fnt) > COL - 90: size -= 4; fnt = font("SairaCondensed-ExtraBold.ttf", size)
        d.text((CX, y + size // 2), txt, font=fnt, fill=col, anchor="mm"); y += int(size * 1.02)
    tail(d, kicker, foot); im.save(f"cards/{name}.jpg", quality=94); pushin(name, f"cards/{name}.jpg")
def page(name, path, fb, kicker, foot):
    src = Image.open(path).convert("RGB"); w, h = src.size
    im = src.crop((int(fb[0]*w), int(fb[1]*h), int(fb[2]*w), int(fb[3]*h)))
    tw = COL - 80; im = im.resize((tw, int(im.height * tw / im.width)), Image.LANCZOS)
    can = Image.new("RGB", (W, H), NIGHT); d = ImageDraw.Draw(can); frame(d)
    y0 = 300 + (1200 - im.height) // 2
    can.paste(im, (CX - tw // 2, max(y0, 360))); tail(d, kicker, foot)
    can.save(f"cards/{name}.jpg", quality=94); pushin(name, f"cards/{name}.jpg")
T115 = scan("WW1ArmyMedDeptHistV15-2", 1036, "t")
P51 = scan("WW1ArmyMedDeptHistV11-1", 83, "sg")
# ---- s1 case fatality by region (Table 115, p.1024: deaths / admissions, battle injuries, gas excepted, 1917-18)
card("card_43", "ARMY BATTLE WOUNDS, 1917–18 · ABDOMEN AND PELVIS", [("43%", 380, MON), ("DIED", 130, GAUZE), ("1,536 OF 3,546 ADMITTED DIED", 75, IOD)], "Army medical reports, 1925")
page("pg_t115", T115, (0.04, 0.085, 0.99, 0.385), "TABLE 115 · CASE FATALITY BY REGION · P. 1024", "Total column: 7.73% · all regions", )
card("card_regions", "CASE FATALITY · ARMY BATTLE WOUNDS (GAS EXCEPTED) · 1917–18", [("HEAD  14%", 190, GAUZE), ("CHEST  24%", 190, IOD), ("SPINE  56%", 190, MON)], "Army medical reports, 1925")
card("card_limbs", "CASE FATALITY · ARMY BATTLE WOUNDS (GAS EXCEPTED) · 1917–18", [("ARMS  4%", 230, GAUZE), ("LEGS  7%", 230, IOD)], "Army medical reports, 1925")
card("card_all", "CASE FATALITY · ARMY BATTLE WOUNDS (GAS EXCEPTED) · 1917–18", [("8%", 380, MON), ("ALL REGIONS TOGETHER", 100, GAUZE), ("7.73 PER 100 ADMITTED", 75, IOD)], "Army medical reports, 1925")
card("card_weapon", "ABDOMEN AND PELVIS · CASE FATALITY BY MISSILE (RIFLE BALL, SHELL ONLY)", [("RIFLE BALL  33%", 175, GAUZE), ("SHELL  45%", 175, MON)], "Army medical reports, 1925")
# ---- s2 hemorrhage estimate (vol. XI Surgery, p.51)
card("card_80", "ARMY SURGERY HISTORY · BATTLEFIELD DEATHS", [("80–85%", 300, MON), ("PRIMARY HEMORRHAGE", 105, GAUZE), ("ESTIMATED, NOT COUNTED", 80, IOD)], "Army Medical Dept., vol. XI, 1927")
page("pg_hem", P51, (0.06, 0.322, 0.86, 0.406), "VOL. XI · SURGERY · P. 51", "“probably safe in estimating”")
page("pg_lack", P51, (0.06, 0.234, 0.86, 0.325), "VOL. XI · SURGERY · P. 51", "“lack of observation and lack of records”")
card("card_80b", "ARMY SURGERY HISTORY · BATTLEFIELD DEATHS", [("80–85%", 300, MON), ("FROM BLEEDING", 120, GAUZE), ("AN ESTIMATE", 100, IOD)], "Army Medical Dept., vol. XI, 1927")
print("cards ok")
