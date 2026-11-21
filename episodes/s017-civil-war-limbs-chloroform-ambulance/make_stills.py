# s017: branded cards + Civil War stills (Miller, Photographic History of the Civil War, 1911, vols. 2/7, public domain via Internet Archive)
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


# ---- s1 limbs and amputation (MSH Surgical Vol. 2/3, 1883; battlefields.org Backus; NMCWM Slawson)
card("card_71", "UNION GUNSHOT WOUNDS TREATED · 1861-65", [("71%", 330, MON), ("HIT AN ARM", 120, GAUZE), ("OR A LEG", 120, IOD)], "Medical & Surgical History (1883)")
card("card_minie", "THE MINIE BALL", [(".58", 300, MON), ("CALIBER", 120, GAUZE), ("SOFT LEAD", 130, IOD)], "Springfield rifle-musket ball, 500 grains")
card("card_why", "NO ANTIBIOTICS · NO GERM THEORY", [("AMPUTATION", 190, MON), ("OFTEN THE BEST CHANCE", 96, GAUZE), ("OF SURVIVAL", 120, IOD)], "Source: Nat. Museum of Civil War Medicine")
card("card_29980", "UNION ARMY · RECORDED", [("29,980", 280, MON), ("AMPUTATIONS", 140, GAUZE), ("ABOUT 1 IN 4 DIED", 110, IOD)], "26.3% · Medical & Surgical History")
card("card_site", "DEATH RATE BY SITE", [("3%", 170, MON), ("HAND & FINGERS", 90, GAUZE), ("83%", 190, IOD), ("HIP", 100, GAUZE)], "Medical & Surgical History (1883)")
still("st_surgeons", "medical_directors_army_cumberland_1863.jpg", (0, 0, 2587, 1412))
# ---- s2 anaesthesia (MSH Surgical Vol. 3, 1883; Chisolm 1861 via HistoryNet; Cutter & Clarke, Mil Med 2014)
card("card_80000", "UNION CASES WITH ANESTHESIA", [("AT LEAST", 110, IOD), ("80,000", 300, MON)], "Medical & Surgical History (1883)")
card("card_254", "NO ANESTHETIC GIVEN", [("ONLY", 120, GAUZE), ("254", 320, MON), ("CASES", 130, IOD)], "Medical & Surgical History (1883)")
card("card_chloro", "WHERE THE DRUG WAS RECORDED", [("3 IN 4", 260, MON), ("CHLOROFORM", 150, GAUZE)], "76.2% of 8,900 cases · MSH 1883")
card("card_cone", "SURGEON'S MANUAL · 1861", [("A FOLDED", 130, GAUZE), ("CLOTH CONE", 200, MON), ("+ A SMALL SPONGE", 110, IOD)], "J. Julian Chisolm (Confederate manual)")
card("card_myth", "MILITARY MEDICINE · 2014", [("\"BITE THE", 170, GAUZE), ("BULLET\"?", 170, GAUZE), ("A MYTH", 220, MON)], "Cutter & Clarke, Military Medicine 2014")
still("st_irwine", "surgeon_irwine_tent_1863.jpg", (0, 0, 2620, 1382))   # Army of the Potomac surgeons at a tent, 1863 (Miller 7)
# ---- s3 ambulance corps (Gillett, Army Medical Dept 1818-1865, CMH; Official Records III/2; Letterman 1866; 13 Stat. 20; NPS)
card("card_24h", "SECOND BULL RUN · AUGUST 1862", [("24+ HOURS", 230, MON), ("WOUNDED LEFT", 120, GAUZE), ("UNATTENDED", 130, IOD)], "Source: Gillett, U.S. Army CMH")
card("card_drivers", "HIRED AMBULANCE DRIVERS", [("\"SCARED AND", 150, GAUZE), ("RAN AWAY\"", 170, MON), ("\"A FEW GOT DRUNK\"", 110, IOD)], "Official Records, Series III, Vol. II")
card("card_1864", "AMBULANCE CORPS ACT", [("MARCH 11", 200, MON), ("1864", 200, GAUZE), ("ALL UNION ARMIES", 110, IOD)], "13 Stat. 20")
still("st_letterman", "letterman_and_staff_1862.jpg", (0, 0, 2030, 1507))
still("st_bridge", "antietam_burnside_bridge.jpg", (0, 300, 1880, 1700))
still("st_smith", "after_antietam_smiths_farm_hospital.jpg", (0, 0, 2613, 1349))   # field hospital at Smith's farm, Keedysville, after Antietam (Miller 7)
print("stills ok")
