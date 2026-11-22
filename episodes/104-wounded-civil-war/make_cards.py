# 104 Shorts (Mon 2026-11-23): branded cards + Civil War stills (Miller 1911, public domain via Internet Archive) as 20 s push-ins.
# as 20 s push-in clips (1920x1080, 30p, silent audio) for shorts.py.
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps
Image.MAX_IMAGE_PIXELS = None
F = "/root/.fonts/"; S = "/home/claude/work/stills301"
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


# ---- s1 pyemia / no germ theory (MSHWR Surgical vol. 3, 1883; W. W. Keen via NMCWM; Lister 1867)
card("card_71of", "PYEMIA AFTER GUNSHOT WOUNDS · UNION ARMY RECORDS", [("71", 300, MON), ("OF 2,818", 170, GAUZE), ("RECOVERED", 130, IOD)], "Medical & Surgical History (1883)")
card("card_coats", "UNION SURGEON W. W. KEEN, REMEMBERING", [("\"OLD BLOOD-", 150, GAUZE), ("STAINED COATS\"", 150, GAUZE), ("\"VETERANS OF A HUNDRED FIGHTS\"", 90, IOD)], "W. W. Keen, 1918")
card("card_sponges", "NO GERM THEORY IN SURGERY YET", [("SPONGES", 220, MON), ("REUSED", 160, GAUZE), ("WASHED IN TAP WATER", 100, IOD)], "W. W. Keen · via NMCWM")
card("card_remedies", "ESTABLISHED PYEMIA · ARMY'S VERDICT, 1883", [("\"ALL REMEDIES", 150, GAUZE), ("WERE FOUND", 150, GAUZE), ("INEFFECTIVE\"", 170, MON)], "Medical & Surgical History (1883)")
card("card_1867", "JOSEPH LISTER, ANTISEPTIC SURGERY", [("1867", 300, MON), ("TWO YEARS", 130, GAUZE), ("AFTER THE WAR", 130, IOD)], "Lister, The Lancet, 1867")
still("st_ward", "armory_square_ward_k.jpg", (0, 0, 2585, 1061))     # Ward K, Armory Square hospital, Washington (Miller 7)
# ---- s2 bullets vs blades (MSHWR Surgical, 1883; Civil War Monitor estimate)
card("card_922", "SABRE AND BAYONET WOUNDS · UNION RECORDS", [("922", 330, MON), ("RECORDED", 130, GAUZE)], "Medical & Surgical History (1883)")
card("card_245790", "GUNSHOT WOUNDS · UNION RECORDS", [("245,790", 270, MON), ("RECORDED", 130, GAUZE), ("FEWER THAN 1 IN 200: BLADES", 90, IOD)], "Medical & Surgical History (1883)")
card("card_hollow", "THE MINIE BALL", [("SOFT LEAD", 190, MON), ("HOLLOW BASE", 150, GAUZE), ("JUST OVER AN OUNCE", 100, IOD)], "Springfield ball, .58 cal., 500 grains")
card("card_76", "ESTIMATE · CIVIL WAR MONITOR", [("~3 IN 4", 260, MON), ("BATTLEFIELD INJURIES", 110, GAUZE), ("FROM THE MINIE BALL", 100, IOD)], "Estimated 76% · Civil War Monitor")
still("st_knaps", "antietam_knaps_battery.jpg", (0, 0, 2000, 674))   # Knap's battery after Antietam, Sept. 1862 (Miller 2)
# ---- s3 diarrhea and dysentery (MSHWR Medical vol. 1, 1870; McGill Osler Library)
card("card_44558", "UNION DEATHS · DIARRHEA AND DYSENTERY", [("44,558", 280, MON), ("DIED", 150, GAUZE)], "Medical & Surgical History (1870)")
card("card_44238", "UNION · KILLED IN BATTLE", [("44,238", 280, IOD), ("AT LEAST · ARMY RECORDS", 100, GAUZE)], "Medical & Surgical History (1870)")
card("card_million", "RECORDED CASES · UNION ARMY", [("WELL OVER", 140, GAUZE), ("1 MILLION", 240, MON)], "Medical & Surgical History (1879)")
card("card_fevers", "CAMP FEVERS · TYPHOID, TYPHUS AND OTHERS", [("40,000+", 260, MON), ("MORE DEATHS", 140, GAUZE)], "Medical & Surgical History (1870)")
still("st_recruits", "kentucky_recruits_tent_camp.jpg", (0, 0, 2705, 1183))   # Kentucky recruits' camp, 1861 (Miller 7)
still("st_eastwards", "east_wards_convalescent_camp_1864.jpg", (0, 0, 2562, 1070))   # convalescent camp, Alexandria, 1864 (Miller 7)
print("cards ok")
