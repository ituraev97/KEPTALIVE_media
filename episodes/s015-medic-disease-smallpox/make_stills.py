# s015: branded cards + archival stills as 20 s push-in clips (1920x1080, 30p, silent audio) for shorts.py.
# Stills: The Photographic History of the Civil War, vol. 7 (1911; Internet Archive millersphotographic07franrich, NOT_IN_COPYRIGHT) page scans,
#         Gilbert Stuart, George Washington (Athenaeum portrait, 1796; Internet Archive, Public Domain Mark). Pages in /home/claude/stills15.
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps
Image.MAX_IMAGE_PIXELS = None
F = "/root/.fonts/"; S = "/home/claude/stills15"
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

# ---- s1 Woodson (health.mil 2024-06-04; army.mil 277628)
card("card_shrapnel", "OMAHA BEACH · JUNE 6-7, 1944", [("WOUNDED", 230, IOD), ("BY MORTAR SHRAPNEL", 104, GAUZE), ("KEPT WORKING", 150, MON)], "Sources: health.mil · army.mil")
card("card_200", "CPL. WAVERLY WOODSON · 320TH BARRAGE BALLOON BN.", [("200+", 320, MON), ("CASUALTIES CARED FOR", 104, GAUZE), ("IN 30 HOURS UNDER FIRE", 96, IOD)], "Historical commission, via army.mil")
card("card_dsc", "ALMOST 80 YEARS AFTER D-DAY", [("DSC", 300, MON), ("DISTINGUISHED SERVICE CROSS", 92, GAUZE), ("JUNE 3, 2024 · POSTHUMOUS", 92, IOD)], "Source: army.mil")
# ---- s2 Civil War disease (NPS Death and Dying; American Battlefield Trust)
card("card_2x", "CIVIL WAR · 1861-1865", [("2 : 1", 320, MON), ("DISEASE VS. BATTLE WOUNDS", 96, GAUZE), ("SOLDIERS' DEATHS", 110, IOD)], "Source: National Park Service")
card("card_620", "SOLDIERS WHO DIED · CIVIL WAR", [("620,000", 270, MON), ("ESTIMATED DEATHS", 120, GAUZE), ("ABOUT 2 IN 3 FROM DISEASE", 96, IOD)], "NPS · American Battlefield Trust")
card("card_measles", "CIVIL WAR CAMPS · AS RECALLED BY JOHN B. GORDON", [("“COUNTRY BOYS", 170, GAUZE), ("WHO HAD NEVER HAD", 120, GAUZE), ("THE MEASLES”", 170, IOD)], "Source: American Battlefield Trust")
still("st_fieldhosp", "p272.jpg", (54, 1958, 2666, 3480))      # Field hospital, 2nd Div., II Corps, Brandy Station, Va.
still("st_genhosp", "p219.jpg", (65, 190, 2693, 1795))         # U.S. General Hospital, Jeffersonville, Ind.
still("st_nelson", "p219.jpg", (98, 2475, 2693, 3700))         # Mountain convalescent camp, Camp Nelson, Ky.
still("st_eastwards", "p292.jpg", (15, 300, 2600, 1475))       # East wards, convalescent camp, Alexandria, 1864
still("st_fairoaks", "p266.jpg", (60, 90, 2660, 2290))         # Farm-house hospital after Fair Oaks, June 1862
# ---- s3 smallpox 1777 (NPS smallpox-inoculation article; American Battlefield Trust)
card("card_canada", "CONTINENTAL ARMY · WINTER 1775-76", [("CANADA", 260, MON), ("SMALLPOX RAVAGED", 130, GAUZE), ("THE AMERICAN ARMY", 120, IOD)], "Source: American Battlefield Trust")
card("card_quote", "GEORGE WASHINGTON · FEB. 6, 1777", [("“MORE TO DREAD", 150, GAUZE), ("FROM IT THAN FROM", 120, GAUZE), ("THE SWORD", 170, IOD), ("OF THE ENEMY”", 140, IOD)], "Letter on inoculating the troops")
card("card_inoc", "1700s METHOD · NOT TODAY'S VACCINE", [("INOCULATION", 210, MON), ("SMALLPOX IN A SMALL CUT", 100, GAUZE), ("RISKY · USUALLY MILDER", 96, IOD)], "Source: National Park Service")
card("card_late", "INOCULATED IN SECRET", [("LATE 1777", 250, MON), ("SMALLPOX IN THE ARMY", 110, GAUZE), ("SUBSTANTIALLY REDUCED", 104, IOD)], "Source: National Park Service")
still("st_gw", "gw_athenaeum.jpg", (0, 0, 5157, 6701), tone=False)       # Gilbert Stuart, 1796 (Athenaeum portrait)
still("st_gw2", "gw_athenaeum.jpg", (700, 600, 4457, 4600), tone=False)  # same portrait, closer
print("stills ok")
