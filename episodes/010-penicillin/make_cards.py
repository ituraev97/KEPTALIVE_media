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
card("card_hunt.jpg", "PEORIA, ILLINOIS · 1943", [("THE", 120, GAUZE), ("MOLD", 220, IOD), ("HUNT", 220, GAUZE)], "Produce markets · USDA ARS")
card("card_cantaloupe.jpg", "STRAIN NRRL 1951", [("MOLDY", 170, GAUZE), ("CANTALOUPE", 200, IOD), ("PEORIA MARKET", 110, GAUZE)], "Parent of all commercial strains · USDA ARS")
card("card_vats.jpg", "PEORIA · FROM JULY 1941", [("DEEP", 200, GAUZE), ("VATS", 220, MON), ("CORN STEEP LIQUOR", 100, GAUZE)], "Air pumped in · USDA ARS")
card("card_20.jpg", "JULY 1943", [("$20", 300, IOD), ("A DOSE", 170, GAUZE)], "Penicillin · USDA ARS")
card("card_055.jpg", "JULY 1943 TO 1946", [("$20", 140, STEEL), ("THREE YEARS LATER", 90, GAUZE), ("55¢", 300, MON)], "Per dose · USDA ARS")
card("card_12.jpg", "ALEXANDER FLEMING · 1928", [("12", 300, MON), ("YEARS", 170, GAUZE), ("KEPT THE MOLD", 110, GAUZE)], "Source: National WWII Museum")
card("card_2000.jpg", "OXFORD · EARLY 1940s", [("2,000", 260, MON), ("LITERS", 170, GAUZE), ("FOR ONE CASE", 120, IOD)], "Of mold fluid · PBS NewsHour")
print("cards ok")
