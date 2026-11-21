# 104 — preparation status (run of 2026-11-21 for Mon 2026-11-23, WAR MEDICINE · EP 2)
Done in the prep run (container-local, NOT in git — redo if the container is fresh):
- Stills: 169 public-domain images in /home/claude/work/stills301 (captions in stills_index.json). Rebuild with stills_scripts/ (m7spec/m2spec/msspec/mdspec/hwspec/pspec + cut.py + build_index.py; they download archive.org leaves `page/n<leaf>_w1600.jpg`). episode.py reads S301 = /home/claude/work/stills301/<key>.jpg.
- TTS: vo/raw_01..265.wav (am_fenrir, tts_ep.py, ~60 min with other jobs) — raw speech 38.15 min + gaps 2.31 = ~40.5 min. Voice f0 ~131 Hz (male).
- Graphics: make_gspec.py -> gspec.json (148 graphics) -> graphics.mjs -> gfx/ (~45 min while TTS ran).
- Clips (download from DVIDS asset API files[2] into /home/claude/clips, then src_cuts.py): 753958 (2020, 29.97p), 1030224 (59.94p), 1028671 (23.976p), 1030410 (29.97p), 1030600 (25p). Shot times already fitted inside src_cuts windows; 1030224 REPEAT near 61.7 s avoided.
- Thumbnails: thumb3.json (img/ = copies of stills301 ambulance_drill_after_antietam, after_antietam_smiths_farm_hospital, medical_directors_army_cumberland_1863) -> thumb_A/B/C.jpg checked at full size and 168x94.
Fact-check: factcheck.md (38 required fixes, all applied before TTS).
Build day: build_ep.py -> seg frame-count check vs timing.json -> motion_check 0 -> finish.py -> contact sheet every 8 s -> encode.sh 470 -> Drive -> Metricool 13:00 ET Mon. Description: templates/description.txt (+ make_desc.py from 103 as model), chapters from timing.json.
