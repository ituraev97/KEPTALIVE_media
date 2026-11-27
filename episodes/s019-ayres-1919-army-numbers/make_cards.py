# s019 cards: number cards + page crops of Ayres, "The War with Germany: A Statistical Summary" (U.S. War Dept., 1919; 2nd ed.),
# Internet Archive item warwithgermanyst01unit (public domain, U.S. government). Page leaf = printed page + 5.
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
def frame(d):
    d.rectangle([CX - COL // 2, 0, CX + COL // 2, H], fill=PANEL)
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
def page(name, leaf, fb, kicker, foot, head=None):
    """crop fb=(x0,y0,x1,y1) fractions of the scan, fit to the column width, on the panel."""
    src = Image.open(f"{S}/ay{leaf}.jpg").convert("RGB"); w, h = src.size
    im = src.crop((int(fb[0]*w), int(fb[1]*h), int(fb[2]*w), int(fb[3]*h)))
    tw = COL - 80; im = im.resize((tw, int(im.height * tw / im.width)), Image.LANCZOS)
    can = Image.new("RGB", (W, H), NIGHT); d = ImageDraw.Draw(can); frame(d)
    y0 = 300 + (1200 - im.height) // 2
    if head:
        fnt = font("SairaCondensed-ExtraBold.ttf", 100); d.text((CX, 260), head, font=fnt, fill=IOD, anchor="mm")
    can.paste(im, (CX - tw // 2, max(y0, 360))); tail(d, kicker, foot)
    can.save(f"cards/{name}.jpg", quality=94); pushin(name, f"cards/{name}.jpg")
SRC = "U.S. WAR DEPT. · AYRES, THE WAR WITH GERMANY · 1919"
# ---- s1 flu
card("card_rate5", "ARMY DISEASE DEATH RATE · TO SEPT. 14, 1918", [("5", 380, MON), ("DEATHS PER 1,000", 120, GAUZE), ("MEN A YEAR", 120, GAUZE), ("FROM DISEASE", 120, IOD)], "Army summary, 1919")
page("pg_d56", 132, (0.04, 0.19, 0.97, 0.79), "DIAGRAM 56 · DEATHS PER 1,000 SOLDIERS EACH WEEK", "U.S. troops, 1918–19", head=None)
card("card_316", "TROOPS IN THE U.S. · SEPT. 14–NOV. 8, 1918", [("316,089", 230, MON), ("FLU CASES", 130, GAUZE), ("53,449", 230, MON), ("PNEUMONIA CASES", 120, IOD)], "Reported by the Army")
card("card_40k", "ARMY PNEUMONIA DEATHS · WHOLE WAR", [("40,000+", 250, MON), ("PNEUMONIA DEATHS", 120, GAUZE), ("~25,000", 230, IOD), ("FROM THE FLU PANDEMIC", 100, GAUZE)], "Army's word: \"probably\"")
# ---- s2 wounded
page("pg_sum67", 135, (0.10, 0.593, 0.94, 0.643), "ARMY SUMMARY, 1919 · ITEMS 6 AND 7", "The War with Germany", head=None)
card("card_med", "ARMY MEDICAL CORPS · WWI", [("2,089", 250, MON), ("MEDICAL OFFICERS AT WAR'S START", 85, GAUZE), ("+31,251", 250, IOD), ("PHYSICIANS COMMISSIONED", 85, GAUZE)], "Army summary, 1919")
card("card_2of100", "ARMY SUMMARY · ITEM 1", [("2", 380, MON), ("OF EVERY 100", 120, GAUZE), ("SOLDIERS AND SAILORS", 100, GAUZE), ("KILLED OR DIED OF DISEASE", 85, IOD)], "Served in the war with Germany")
card("card_85", "ARMY SUMMARY, 1919 · P. 122", [("~85%", 300, MON), ("OF MEN SENT TO HOSPITAL", 85, GAUZE), ("FOR INJURIES", 110, GAUZE), ("RETURNED TO DUTY", 110, IOD)], "American Expeditionary Forces")
card("card_7pct", "AMERICAN EXPEDITIONARY FORCES · TABLE 10", [("7%", 380, MON), ("DIED OF WOUNDS", 120, GAUZE), ("AS A SHARE OF THE WOUNDED", 70, IOD), ("14,720 OF 205,690", 80, STEEL)], "Army summary, 1919")
# ---- s3 ladder
card("card_110", "DISEASE DEATHS PER 1,000 MEN A YEAR", [("110", 380, MON), ("MEXICAN WAR", 130, GAUZE), ("1846–48", 90, STEEL)], "Army summary, 1919")
card("card_65", "DISEASE DEATHS PER 1,000 MEN A YEAR", [("65", 380, MON), ("CIVIL WAR (NORTH)", 120, GAUZE), ("1861–65", 90, STEEL)], "Army summary, 1919")
card("card_26", "DISEASE DEATHS PER 1,000 MEN A YEAR", [("26", 380, MON), ("SPANISH WAR", 130, GAUZE), ("1898", 90, STEEL)], "Army summary, 1919")
card("card_19", "DISEASE DEATHS PER 1,000 MEN A YEAR", [("19", 380, MON), ("OVERSEAS FORCES", 120, GAUZE), ("WORLD WAR I · TO NOV. 11, 1918", 62, STEEL)], "Army summary, 1919")
page("pg_d54", 129, (0.04, 0.24, 0.97, 0.715), "DIAGRAM 54 · DISEASE AND BATTLE DEATHS PER 1,000", "Mexican War to WWI", head=None)
# ---- s4 totals / typhoid
card("card_115", "ARMY DEATHS, WWI · MARINES ATTACHED INCLUDED", [("115,660", 250, MON), ("DEATHS IN THE ARMY", 110, GAUZE)], "Army summary, 1919")
page("pg_d53", 128, (0.05, 0.54, 0.97, 0.815), "DIAGRAM 53 · TOTAL DEATHS", "50% disease · 43% battle · 7% other", head=None)
card("card_2x", "OVERSEAS FORCES · WWI", [("2×", 380, MON), ("BATTLE LOSSES", 120, GAUZE), ("VS. DEATHS FROM DISEASE", 85, IOD)], "Army summary, 1919")
card("card_typh", "TYPHOID FEVER · WWI ARMY · TO MAY 1, 1919", [("2,328", 250, MON), ("CASES REPORTED", 110, GAUZE), ("227", 250, IOD), ("DEATHS", 110, GAUZE)], "Army summary, 1919")
page("pg_p125", 130, (0.07, 0.527, 0.90, 0.632), "ARMY SUMMARY, 1919 · P. 125", "Typhoid, vaccination, sanitation", head=None)
print("cards ok")
