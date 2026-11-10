# Branded 16:9 cards whose content sits in the central 9:16 column (for Shorts), KEPT ALIVE palette.
from PIL import Image, ImageDraw, ImageFont
F = "/root/.fonts/"
def font(n, s): return ImageFont.truetype(F + n, s)
NIGHT, GAUZE, SCRUB, MON, IOD, STEEL, PANEL = "#0A1214", "#EEF2EF", "#2BB3A3", "#6CF29A", "#F2B33D", "#8A9AA0", "#13242A"
W, H = 3840, 2160; CX = W // 2; COL = int(H * 9 / 16)  # 1215 px column
def card(out, kicker, rows, foot):
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
    im.save(out, quality=94)
card("card_week.jpg", "LIBERIA · 2014", [("UP TO", 150, GAUZE), ("A WEEK", 220, IOD), ("FOR A RESULT", 130, GAUZE)], "Confirming an Ebola case")
card("card_hours.jpg", "NAVY MOBILE LABS · 2014", [("7 DAYS", 180, STEEL), ("NOW", 110, GAUZE), ("<4 HOURS", 220, MON)], "Source: Navy Medicine")
card("card_hcw.jpg", "LIBERIA · 2014–2015", [("378", 260, MON), ("HEALTH WORKERS", 130, GAUZE), ("INFECTED", 150, IOD)], "192 died · Emerging Infectious Diseases")
card("card_14m.jpg", "CDC MODEL · SEPT. 2014", [("1.4", 260, IOD), ("MILLION", 170, GAUZE), ("CASES?", 150, GAUZE)], "An estimate without more action")
card("card_burial.jpg", "LIBERIA · SAFE BURIALS", [("<10", 200, STEEL), ("TO 54", 200, MON), ("BURIAL TEAMS", 130, GAUZE)], "August to Oct. 5, 2014 · CDC MMWR")
card("card_paper.jpg", "LIBERIA · CONTACT TRACING", [("PAPER", 200, IOD), ("AND", 110, GAUZE), ("EXCEL", 200, GAUZE)], "Emerging Infectious Diseases, 2016")
card("card_iso.jpg", "LIBERIA · ISOLATION", [("~9,000", 220, MON), ("CASES", 140, GAUZE), ("PREVENTED", 140, SCRUB)], "Liberia, Sept. 23–Oct. 31, 2014 · CDC estimate")
print("cards ok")
