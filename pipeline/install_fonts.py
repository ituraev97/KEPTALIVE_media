#!/usr/bin/env python3
"""Install the KEPT ALIVE fonts for libass/ffmpeg subtitles (~/.fonts) with clean family names.
@fontsource ships instances of variable fonts whose internal names are wrong (e.g. 'Source Sans 3 ExtraLight SemiBold'),
so names are rewritten to exactly what finish.py / shorts.py ask for."""
import os, subprocess
from fontTools.ttLib import TTFont
NM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "node_modules/@fontsource")
FONTS = [("saira-condensed/files/saira-condensed-latin-800-normal.woff2", "Saira Condensed ExtraBold", "SairaCondensed-ExtraBold"),
         ("source-sans-3/files/source-sans-3-latin-600-normal.woff2", "Source Sans 3 SemiBold", "SourceSans3-SemiBold"),
         ("martian-mono/files/martian-mono-latin-500-normal.woff2", "Martian Mono", "MartianMono-Medium")]
out = os.path.expanduser("~/.fonts"); os.makedirs(out, exist_ok=True)
for src, fam, ps in FONTS:
    f = TTFont(os.path.join(NM, src)); f.flavor = None
    n = f["name"]
    for nid in (16, 17, 21, 22): n.removeNames(nameID=nid)
    for rec in list(n.names):
        if rec.nameID == 1: rec.string = fam
        elif rec.nameID == 2: rec.string = "Regular"
        elif rec.nameID == 4: rec.string = fam
        elif rec.nameID == 6: rec.string = ps
    f.save(os.path.join(out, ps + ".ttf"))
subprocess.run(["fc-cache", "-f"], check=True)
for _, fam, _ in FONTS:
    print(fam, "->", subprocess.run(["fc-match", fam, "family"], capture_output=True, text=True).stdout.strip())
