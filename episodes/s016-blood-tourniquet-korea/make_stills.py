# s016: branded cards + archival stills as 20 s push-in clips (1920x1080, 30p, silent audio) for shorts.py.
# Stills: U.S. Army photo, 1st Mobile Army Surgical Hospital, Korea, March 10, 1951 (frame of DVIDS 1029263, Military Health System, 2026-11-09; cropped above its caption).
#         Gilbert Stuart, George Washington (Athenaeum portrait, 1796; Internet Archive, Public Domain Mark). Pages in /home/claude/stills15.
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps
Image.MAX_IMAGE_PIXELS = None
F = "/root/.fonts/"; S = "/home/claude/stills16"
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


# ---- s1 Robertson 1917 blood depot (KUMC; National Archives UK blog; Proto; History.com)
card("card_ice", "WWI · WESTERN FRONT · 1917", [("BLOOD", 280, MON), ("STORED ON ICE", 140, GAUZE), ("FOR WOUNDED SOLDIERS", 100, IOD)], "U.S. Army doctor Oswald H. Robertson")
card("card_typeo", "ONLY ONE DONOR GROUP", [("TYPE O", 280, MON), ("COULD SAFELY BE GIVEN", 100, GAUZE), ("TO MOST SOLDIERS", 120, IOD)], "Sources: KUMC · Proto (MGH)")
card("card_bottles", "GLASS BOTTLES · WWI", [("CITRATE", 220, MON), ("SO IT WOULD NOT CLOT", 100, GAUZE), ("+ DEXTROSE TO HELP IT KEEP", 100, IOD)], "Sources: KUMC · National Archives (UK)")
card("card_ammo", "SHIPPING CONTAINERS", [("AMMO BOXES", 220, MON), ("PACKED WITH", 110, GAUZE), ("SAWDUST AND ICE", 130, IOD)], "Source: KUMC WWI archives")
card("card_26", "STORED ON ICE", [("UP TO", 100, IOD), ("26", 330, MON), ("DAYS", 150, GAUZE)], "Source: National Archives (UK)")
card("card_cambrai", "BATTLE OF CAMBRAI · 1917", [("THE FIRST", 150, GAUZE), ("BLOOD DEPOT", 200, MON), ("PRECURSOR OF THE BLOOD BANK", 86, IOD)], "Sources: Proto (MGH) · KUMC")
# ---- s2 Vietnam -> TCCC -> tourniquets (Butler & Blackbourne, J Trauma 2012; Butler, JSOM 2015; Task & Purpose 2025)
card("card_74", "U.S. SOLDIERS KILLED IN ACTION · VIETNAM", [("7.4%", 330, MON), ("DIED OF BLEEDING", 120, GAUZE), ("FROM AN ARM OR LEG ALONE", 92, IOD)], "193 of 2,600 KIA studied · JSOM 2015")
card("card_atls", "STANDARD TRAUMA COURSE (ATLS)", [("TOURNIQUETS", 200, MON), ("DISCOURAGED", 190, IOD)], "As quoted in Butler, JSOM 2015")
card("card_1996", "MILITARY MEDICINE · AUGUST 1996", [("1996", 300, MON), ("TACTICAL COMBAT", 120, GAUZE), ("CASUALTY CARE", 130, GAUZE)], "Butler, Hagmann, Butler")
card("card_2005", "ARMY SURGEON GENERAL · MARCH 2005", [("2005", 300, MON), ("TOURNIQUETS ORDERED", 110, GAUZE), ("FOR SOLDIERS DEPLOYING", 100, IOD), ("TO IRAQ & AFGHANISTAN", 100, IOD)], "Source: J Trauma 2012 (Butler)")
card("card_lives", "ESTIMATE · 2009 (KRAGH)", [("1,000-2,000", 220, MON), ("U.S. LIVES SAVED", 130, GAUZE), ("BY BATTLEFIELD TOURNIQUETS", 86, IOD)], "Source: J Trauma 2012 (Butler)")
# ---- s3 Korea H-13 (army.mil 177302, 2016; centennialofflight.net; Harrison, Korean J Med Hist 2023)
card("card_1951", "FIRST ARMY AERIAL MEDEVAC MISSIONS", [("JAN. 3", 250, MON), ("1951", 200, GAUZE), ("KOREA", 150, IOD)], "Source: army.mil")
card("card_18000", "ARMY AVIATORS · H-13", [("18,000", 280, MON), ("OF 23,000 CASUALTIES", 110, GAUZE), ("FLOWN TO MASH UNITS", 110, IOD)], "Source: army.mil (2016)")
card("card_rate", "DEATH RATE BEFORE REACHING CARE", [("4.5%", 180, STEEL), ("WWII", 90, GAUZE), ("2.5%", 220, MON), ("KOREA", 100, IOD)], "Evacuated patients · army.mil")
still("st_h13", "h13_57.png", (230, 195, 1690, 780), tone=False)    # 1st MASH, Korea, March 10, 1951: H-13 with litter outside
still("st_h13b", "h13_57.png", (230, 195, 1250, 780), tone=False)   # same photo, left side
print("stills ok")
