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
card("long1842.jpg", "NO. 3 · GEORGIA", [("1842", 260, MON), ("CRAWFORD", 150, GAUZE), ("LONG", 150, GAUZE)], "Ether · published only in 1849")
card("bullet.jpg", "CIVIL WAR · 1861–1865", [("BITE THE", 180, GAUZE), ("BULLET?", 220, IOD)], "Union army medical records")
card("civil80k.jpg", "UNION ARMY RECORDS", [("80,000+", 220, MON), ("WITH", 130, GAUZE), ("ANESTHESIA", 140, SCRUB)], "Only 254 recorded without")
card("speed.jpg", "SURGERY BEFORE 1846", [("THE BEST", 150, GAUZE), ("DEFENSE:", 150, GAUZE), ("SPEED", 220, IOD)], "Patients were wide awake")
print("cards ok")
