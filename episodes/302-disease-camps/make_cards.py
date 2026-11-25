# EP 3 (302) Shorts: archival stills + number cards as 20 s push-in clips (1920x1080, 30p, silent audio) for shorts.py.
# Pattern copied from s018-doss-coastguard-koningsdam/make_cards.py. usage: python3 make_cards.py [clips_dir]   (cards/ is written next to this file's cwd)
# Stills: /home/claude/work/stills302 (index.json has captions/years). All numbers: /home/claude/work/facts302.md (+ factcheck.md wording).
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter, ImageEnhance
Image.MAX_IMAGE_PIXELS = None
F = "/root/.fonts/"; S = "/home/claude/work/stills302"
CLIPS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/clips"
ONLY = set(sys.argv[2:])
def font(n, s): return ImageFont.truetype(F + n, s)
NIGHT, GAUZE, SCRUB, MON, IOD, STEEL, PANEL = "#0A1214", "#EEF2EF", "#2BB3A3", "#6CF29A", "#F2B33D", "#8A9AA0", "#13242A"
W, H = 3840, 2160; CX = W // 2; COL = int(H * 9 / 16)
os.makedirs("cards", exist_ok=True)
def pushin(name, jpg):
    subprocess.run(["nice", "-n", "19", "ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", jpg, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                    "-filter_complex", "[0:v]scale=7680:-2,zoompan=z='1+0.0003*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=600:s=1920x1080:fps=30,format=yuv420p[v]",
                    "-map", "[v]", "-map", "1:a", "-t", "20", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "aac", f"{CLIPS}/{name}.mp4"], check=True)
def want(name): return not ONLY or name in ONLY
def frame(name, kicker, foot, draw_body):
    im = Image.new("RGB", (W, H), NIGHT); d = ImageDraw.Draw(im)
    d.rectangle([CX - COL // 2, 0, CX + COL // 2, H], fill=PANEL)
    draw_body(d)
    d.rectangle([CX - 160, 1600, CX + 160, 1614], fill=SCRUB)
    for txt, yy, fn, sz, col in ((foot, 1690, "SourceSans3-SemiBold.ttf", 56, GAUZE), (kicker, 1790, "MartianMono-Medium.ttf", 40, STEEL)):
        fnt = font(fn, sz)
        while d.textlength(txt, font=fnt) > COL - 60: sz -= 2; fnt = font(fn, sz)
        d.text((CX, yy), txt, font=fnt, fill=col, anchor="mm")
    im.save(f"cards/{name}.jpg", quality=94); pushin(name, f"cards/{name}.jpg")
def card(name, kicker, rows, foot, bar=None):
    if not want(name): return
    def body(d):
        tot = sum(int(sz * 1.02) for _, sz, _ in rows); y = 900 - tot // 2 - (60 if bar else 0)
        for txt, size, col in rows:
            fnt = font("SairaCondensed-ExtraBold.ttf", size)
            while d.textlength(txt, font=fnt) > COL - 90: size -= 4; fnt = font("SairaCondensed-ExtraBold.ttf", size)
            d.text((CX, y + size // 2), txt, font=fnt, fill=col, anchor="mm"); y += int(size * 1.02)
        if bar:  # (share_of_first, color_first, color_second, label_first, label_second) horizontal split bar under the rows
            share, c1, c2, l1, l2 = bar; bw = COL - 160; x0 = CX - bw // 2; yb = y + 60
            d.rectangle([x0, yb, x0 + int(bw * share), yb + 90], fill=c1); d.rectangle([x0 + int(bw * share), yb, x0 + bw, yb + 90], fill=c2)
            f2 = font("MartianMono-Medium.ttf", 40); d.text((x0, yb + 130), l1, font=f2, fill=c1, anchor="lm"); d.text((x0 + bw, yb + 130), l2, font=f2, fill=c2, anchor="rm")
    frame(name, kicker, foot, body)
def still(name, src, box=None, mode="land", cy=0.46, tone=False):
    """landscape: whole picture fitted to the 9:16 column width over a blurred copy of itself; portrait: fitted by height (0.62 H), centred low so faces clear the hook text."""
    if not want(name): return
    im = Image.open(f"{S}/{src}").convert("RGB")
    if box: im = im.crop(box)
    if tone: im = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1).convert("RGB")
    bg = ImageOps.fit(im, (W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(70)); bg = ImageEnhance.Brightness(bg).enhance(0.35)
    if mode == "land": s = (COL - 70) / im.width
    else: s = 0.62 * H / im.height
    fg = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, int(H * cy) - fg.height // 2) if mode == "land" else ((W - fg.width) // 2, int(H * 0.55) - fg.height // 2))
    bg.save(f"cards/{name}.jpg", quality=94); pushin(name, f"cards/{name}.jpg")

# ================= s1 TRAILER: Spanish-American War, number-card-led =================
card("card_sa_nums", "CRS · U.S. DEATHS · SPANISH-AMERICAN WAR", [("385", 210, MON), ("BATTLE DEATHS", 90, GAUZE), ("2,061", 210, IOD), ("OTHER DEATHS", 90, GAUZE)], "Congressional Research Service, RL32492")
card("card_sa_note", "NOTE ON THE DATA · CRS", [("MAY 1 TO AUG. 31, 1898", 100, GAUZE), ("THE DATA COVER ONLY", 80, STEEL), ("THESE MONTHS", 80, STEEL), ("RECORDS INCOMPLETE", 120, IOD), ("IN MANY CASES", 100, IOD)], "Congressional Research Service, RL32492")
card("card_sa_typhoid", "TYPHOID · 1898 · A DIFFERENT COUNT", [("20,700", 230, MON), ("OF 171,000 PERSONNEL", 90, GAUZE), ("CAUGHT TYPHOID", 90, GAUZE), ("OVER 1,500 DIED", 140, IOD)], "PBS American Experience, \"Fever\"")
card("card_sa_ratio", "OTHER DEATHS PER BATTLE DEATH", [("5.4 TO 1", 300, MON), ("2,061 OTHER · 385 BATTLE", 90, GAUZE), ("OUR ARITHMETIC", 80, IOD)], "Spanish-American War · CRS data")
still("st_sa_camp", "sf_camp_bay_district.jpg", box=(0, 0, 1859, 735))
still("st_sa_plan", "typhoid_report_plan_rough_plot_camp.jpg", box=(110, 60, 2800, 2160))
still("st_sa_dock", "tampa_dock_loading_transport.jpg")
still("st_sa_daiquiri", "daiquiri_camp_view_a.jpg")

# ================= s2: Reed / Camp Lazear, archival-photo-led =================
card("card_havana462", "HAVANA · AVERAGE 1890 TO 1900", [("462", 300, MON), ("YELLOW FEVER", 110, GAUZE), ("DEATHS A YEAR", 110, IOD)], "James Lind Library")
card("card_reed_q", "WALTER REED · LETTER · SEPT. 7, 1900", [("\"DID THE", 170, GAUZE), ("MOSQUITO", 190, MON), ("DO IT?\"", 170, GAUZE)], "Source: Univ. of Virginia exhibit")
card("card_havana_last", "HAVANA · LAST DEATH UNDER U.S. OCCUPATION", [("SEPT. 28, 1901", 180, MON), ("LAST YELLOW FEVER", 100, GAUZE), ("DEATH IN HAVANA", 100, GAUZE), ("UNDER AMERICAN RULE", 90, IOD)], "James Lind Library")
still("st_reed", "reed_1901_portrait.jpg", mode="port")
still("st_lazear_camp", "camp_lazear_view.jpg", box=(70, 0, 1516, 791))
still("st_lazear_clothes", "camp_lazear_fomites_building.jpg")

# ================= s3: WWII, film-led (+ cards) =================
card("card_ww2_adm", "U.S. ARMY · 1942 TO 1945 · MEDICAL STATISTICS", [("14,998,369", 190, MON), ("MEDICAL ADMISSIONS", 80, GAUZE), ("FOR DISEASE", 80, GAUZE), ("723,560", 190, IOD), ("FOR BATTLE WOUNDS", 80, GAUZE)], "Cases, not men · includes minor ones")
card("card_earlier", "OTHER DEATHS VS BATTLE DEATHS · CRS", [("EARLIER WARS", 110, IOD), ("MEXICAN  11,550 VS 1,733", 80, GAUZE), ("CIVIL WAR (UNION)  224,097 VS 140,414", 80, GAUZE), ("SPANISH-AMER.  2,061 VS 385", 80, GAUZE), ("WORLD WAR I  63,114 VS 53,402", 80, GAUZE)], "Other deaths first · all services")
card("card_ww2_battle", "U.S. ARMY DEATHS · THROUGH DEC. 1945", [("229,823", 260, MON), ("BATTLE DEATHS", 120, GAUZE)], "Medical Statistics in WWII (1975)")
card("card_ww2_dis", "U.S. ARMY DEATHS · THROUGH DEC. 1945", [("14,904", 260, IOD), ("DISEASE DEATHS", 120, GAUZE), ("THE OLD RULE BROKE", 90, MON)], "Medical Statistics in WWII (1975)")

# ================= s4: Mexican War, map/illustration + bar cards =================
card("card_mex_ratio", "MEXICAN WAR 1846 TO 1848 · CRS", [("ABOUT 7 TO 1", 230, MON), ("11,550 OTHER DEATHS", 90, IOD), ("1,733 BATTLE DEATHS", 90, GAUZE), ("OUR ARITHMETIC: 6.7 TO 1", 70, STEEL)], "Congressional Research Service, RL32492")
card("card_mex_split", "MEXICAN WAR · ALL U.S. DEATHS · CRS", [("13,283", 250, GAUZE), ("DEATHS IN ALL", 100, GAUZE)], "Congressional Research Service, RL32492", bar=(11550 / 13283, IOD, MON, "OTHER 11,550", "BATTLE 1,733"))
card("card_mex_note", "NOTE ON THE DATA · CRS", [("DATA BEFORE WORLD WAR I", 90, GAUZE), ("ARE BASED ON", 90, GAUZE), ("INCOMPLETE RECORDS", 110, IOD), ("IN MANY CASES", 100, IOD)], "Congressional Research Service, RL32492")
card("card_mex_pay", "OUR ARITHMETIC · 11,550 OF 13,283", [("ABOUT 87%", 230, MON), ("OF MEXICAN WAR DEATHS", 90, GAUZE), ("WERE OTHER DEATHS", 100, IOD)], "Congressional Research Service, RL32492")
still("st_mex_monterrey", "mex_frost_bishops_palace_monterey.jpg", box=(520, 258, 2392, 1362))
still("st_mex_vcmap", "mex_siege_vera_cruz_map.jpg", box=(30, 30, 1506, 1072))
still("st_mex_city", "mex_lippard_city_of_mexico.jpg", box=(0, 0, 2207, 1440))
print("cards ok")
