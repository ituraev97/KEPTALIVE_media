# KEPT ALIVE — daily production runbook

One run = ONE publish day in America/New_York. **Long-video days (Mon / Wed / Fri ET):** one long story (15–18 min) + 3 Shorts. **Other days (Tue / Thu / Sat / Sun):** 3 Shorts only. See "Format v2" below — it overrides older lines in this file.
Read the Projects doc `claude/kept-alive-bible.md` first (rules, brand, voice, formats). The pipeline is a fork of CHANNEL 16;
`reference/ch16-a001-found/` shows the episode DSL (its colours/hex values are CHANNEL 16's — never copy them; use the KEPT ALIVE palette below).

## Format v2 — owner decision 2026-11-14 (overrides anything older below)
Why: channel data 02–10 Nov — ~13,000 of ~13,700 views came from the Shorts feed; every long video got ~3 views (no browse/suggested impressions); Shorts on war + blood, the 1918 flu, the tourniquet and smallpox got 1,000–1,400 views each, hospital-ship and polio Shorts 2–75. YouTube recommends our audience: long dramatic war documentaries (20–26 min, e.g. "They Found 250 Bodies From WWI's Lost Army", 1.2M), ER/ICU "life on a clock" stories ("SHE COULD DIE IN 2 MINUTES!", 234K), outbreaks and disasters.
1. **Topics:** every topic has a military/war angle OR an outbreak/disaster, AND a life at stake on a clock. Institutional "how X is organised" topics (hospital ships as such, polio programmes, admin) only as background inside a story. Queue: `topics.md` (season 2 at the top).
2. **Fresh footage first (owner rule 2026-11-14):** start every episode and every Short from the NEWEST DVIDS uploads: `https://api.dvidshub.net/search?api_key=KEY&q=<terms>&type[]=video&sort=date&sortdir=desc&from_date=<today-60d>T00:00:00Z&max_results=50` (queries rotate: medevac, medic, hospital, surgical, trauma, MEDEVAC hoist, Coast Guard medevac, CBRN, outbreak, field hospital, blood). Prefer REAL recent events (Coast Guard/Navy medevacs, hospital-ship missions, disaster responses, mass-casualty exercises) published in the last 30 days — a real save from this week can be the topic itself. Target ≥ 60 % of footage screen time from clips published in the last 60 days; archival film only for genuinely historical chapters. Log each clip's DVIDS publish date in sources.md. Never reuse a clip (`used_clips.json`).
3. **Long video = a story, not a lecture:** one real case with a protagonist (a medic, a crew, a ship, a doctor — rescuers may be named when an official release names them; patients never) told on a clock: cold open on the most dramatic verified moment ("They had 4 minutes…") → who/where → the danger escalates → the save → what it changed (history: then vs now on fresh footage) → teaser → disclaimer. 2,300–2,700 words → 15–18 min. Titles ≤ 70 chars with stakes + a number or a clock ("He Had 4 Minutes to Stop the Bleeding", "The Outbreak That Shut Down an Army Camp"), true and sourced. Mon / Wed / Fri only, 13:00 ET.
4. **Thumbnails (long):** 2–4 HUGE words of stakes ("4 MINUTES TO LIVE", "247 MILES OUT"), real frame close-up of a rescuer/aircraft/object (never a patient's face, never gore), red Alarm #E5383B circle and/or arrow on the key detail (`thumb.json` → `"ring":{...,"color":"alarm"}`, `"arrow":{"x1":..,"y1":..,"x2":..,"y2":..}`), `badge` with the format. Test at 168×94.
5. **Shorts formula (from the winners):** every Short opens on a number or a contrast tied to war or an outbreak — "87% vs. 0%", "in 3 numbers", "1883 vs. now", "13 million pints", "killed more soldiers than combat". Hook text + subject on screen at 0.5 s. 20–40 s. Titles ≤ 60 chars, never two Shorts in a day with the same opening pattern. Long days: the 3 Shorts come from that story. Shorts-only days: 3 Shorts on the freshest DVIDS real events / one war-medicine or outbreak fact each, built on footage published in the last 30 days where possible.
6. **Shorts → long video:** every Short's description says "Full story on the channel." and the run report lists, for each Short, which long video should be set as its YouTube "Related video" (the owner sets it manually in YouTube Studio — Metricool cannot).

## 0. Hard rules (medical channel)
- Education and history only: how medicine works and how it was done. NO treatment advice, dosages, diagnoses, "cure", supplements, fear bait, "doctors hide".
- Vaccines, treatments, prevention: only the position of CDC / NIH / FDA / WHO. YouTube's medical misinformation policy = strikes.
- No blood, open wounds, tissue or bodies on screen. Surgery only in wide shots. No patient names; no faces of patients under words about illness. No self-harm cases.
- Footage must never pretend to be a different event: training footage is labelled TRAINING; a 2024 exercise is never "Afghanistan 2010".
- Every fact from a page actually opened (CDC, NIH, NLM, FDA, DoD, peer-reviewed papers, DVIDS descriptions) → `sources.md`. Disputed or modelled numbers say "estimated" and name who estimated. Associations are not causes.
- Independent fact-check by a SEPARATE agent before TTS. Fix everything it flags. (The test Short needed 4 fixes: "from the call, not from injury", subset sizes, author affiliation, "estimate".)
- Every video ends with: "For education only. This is not medical advice. If you have a health concern, talk to a doctor." Description carries the independence line (see `templates/description.txt`).
- Inauthentic-content guard: rotate formats, own graphics ≥ 35% of screen time, never reuse a clip (`used_clips.json`), no two days on the same topic.

## 1. Setup (fresh container)
```bash
# add_repo owner=ituraev97 repo=KEPTALIVE_media access=push first
git clone --depth 1 https://github.com/ituraev97/KEPTALIVE_media /home/claude/keptalive_media
cd /home/claude/keptalive_media/pipeline && npm i          # Playwright is preinstalled globally (/opt/npm-tools)
pip install --break-system-packages kokoro-onnx soundfile scipy fonttools brotli librosa
mkdir -p /home/claude/tts && cd /home/claude/tts && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
python3 /home/claude/keptalive_media/pipeline/install_fonts.py   # must print the 3 exact family names (fixes broken @fontsource names)
mkdir -p /home/claude/clips && cp /home/claude/keptalive_media/clips.json /home/claude/clips/
```

## 2. Pick the topic and footage
- Next topic: first unchecked line of season 2 in `topics.md`, unless the fresh-DVIDS scan (Format v2 §2) finds a stronger real event from the last 30 days — then add it as a new line and use it. Mark it done with the date when published.
- DVIDS API (key in the scheduled-task prompt): `https://api.dvidshub.net/search?api_key=KEY&q=<terms>&type[]=video&sort=date&sortdir=desc&from_date=<today-60d>T00:00:00Z` (newest first) → `https://api.dvidshub.net/asset?api_key=KEY&id=video:ID` → download the 1920x1080 file (`files[].src`) to `/home/claude/clips/ID.mp4`. Prefer 30p/60p; 24p must be motion-interpolated (see build).
- archive.org public-domain films (`advancedsearch.php`, mediatype:movies) for OUTBREAK / FIRST; check each item's rights; credit "ARCHIVAL FILM · YEAR · STUDIO".
- Never use a clip already in `used_clips.json`. Contact sheet every 3–5 s with timestamps; skip injuries/blood/patients' faces.
- `python3 pipeline/src_cuts.py /home/claude/clips ID` (internal cuts; builder avoids flash fragments). Add `box` to `clips.json` for 4:3 sources.
- Check real cadence: some "60p" DVIDS files are 24p/25p content (e.g. 923203, 923212) — set `"src_fps": "24000/1001"` (or "25") for that id in `clips.json`; build/shorts then motion-interpolate from the true rate. Some shots inside such files are still uneven: if motion_check flags them, swap the shot. Interview/museum clips with speech: list them in `META["mute_nat"]`. `META["training"]` = clip ids that get the on-screen TRAINING EXERCISE badge.

## 3. Research + script
- `episodes/NNN-slug/episode.py`: `LINES = [(spoken, shots, opts)]` — same DSL as the reference. opts: `kind` (calm|punch|tense|slow|drive|question), `tag` (place · date lower third), `gap`. Numbers as words in `spoken`; hard terms respelled + `DISPLAY` map.
- 2,300–2,700 words → 15–18 min (Format v2 §3). Structure: cold open ≤ 40 s on the most dramatic verified moment → title → 5–7 chapters that escalate toward the save → "what changed" → teaser → disclaimer line → end card.
- Graphics (`pipeline/graphics.mjs`): title, chapter, stat, callcard, steps, cards3, map, timeline, list, doc, end. Colours: Night #0A1214, Panel #13242A, Gauze #EEF2EF, Scrub #2BB3A3 (accent, ONE word), Monitor #6CF29A (numbers/data), Iodine #F2B33D (hook only), Steel #8A9AA0. Graphics animate 0–2.4 s, then hold still.
- `shorts_spec.py`: 3 Shorts (20–40 s each), formula from Format v2 §5, own narration, hook ≤ 1.5 s, CTA "FOLLOW FOR MORE REAL MEDICINE". Shorts-only days: an episode folder `episodes/sNNN-slug/` with only shorts_spec.py + sources.md (build only the per-line TTS/graphics/clips shorts.py needs, never a long video).
- Fact-check agent (separate) on episode.py + shorts_spec.py + sources.md → fix → only then TTS.

## 4. Build
```bash
EP=/home/claude/keptalive_media/episodes/NNN-slug; P=/home/claude/keptalive_media/pipeline; CL=/home/claude/clips
python3 $P/tts_ep.py $EP                 # am_fenrir + processing (vfx.py) — the channel voice, do not change
cd $P && python3 make_gspec.py $EP && node graphics.mjs $EP/gspec.json $EP/gfx
nohup python3 $P/build_ep.py $EP $CL > $EP/build.log 2>&1 &   # long; poll the log
python3 $P/motion_check.py $EP/video_raw.mp4 $EP/timing.json $CL/clips.json   # must report 0 issues
python3 $P/finish.py $EP $CL             # subtitles, lower thirds, score, SFX, -14 LUFS
bash $P/encode.sh $EP $EP/long.mp4 95    # < 100 MB for GitHub
python3 $P/shorts.py $EP $CL             # 3 Shorts from shorts_spec.py
cd $P && node thumb.mjs $EP/thumb.json $EP   # thumb_A + thumb_C
```
Long steps (build/finish/encode/shorts) through nohup + polling; never let a foreground command run past 10 minutes.

## 5. QA (do not skip)
- motion_check 0 issues (long and each Short). Contact sheet every 8 s: no gore, no overlaps, subtitles inside frame.
- Listen check: voice must be MALE (am_fenrir). `ffmpeg -i long.mp4 -af ebur128 -f null -` ≈ −14 LUFS.
- Thumbnail at 168×94 still reads; bottom-right corner empty.
- Shorts HUD `label`: max ~50 characters per line; split longer labels into two lines with `\\N` (one long line runs off the frame).
- Check every surgery shot in the 9:16 crop too: a medium 16:9 shot becomes a close-up of the operating field after cropping — use only room-wide shots.
- Never kill build_ep.py mid-run and reuse seg/: a segment cut off mid-write keeps a valid .key and gets reused (truncated -> timing drift, motion_check GFX-DRIFT everywhere). After an aborted build, compare each seg's frame count with timing.json and delete short ones. Changing the number of shots in a line shifts all later seg indices (full re-render) - keep shot counts when patching.
- Check DVIDS "Day in the Life"-style clips for burned-in caption text inside the shot window (e.g. 861320 after 99.5 s).
- Archival (non-DVIDS) Shorts: set `credit=` in shorts_spec.py so the on-screen footage line does not say "via DVIDS".
- Avoid edited "wrap-up" montages (1-second cuts, baked-in titles) — the builder cannot place a shot inside them.

## 6. Upload + schedule
- Branch = weekday of the ET publish date (`drop-mon` … `drop-sun`): orphan commit with ONLY that day's files (long.mp4 on long days, s1..s3.mp4, thumb_A.jpg, thumb_C.jpg), force-push. URL `https://raw.githubusercontent.com/ituraev97/KEPTALIVE_media/drop-XXX/<file>`. Video never on `main`.
- Metricool brand **KEPT ALIVE**, blogId **7806960** (YouTube UCa7qKTXkXc0yXmKJkBTFa9Q, brand timezone Asia/Tashkent — send `publicationDate` with timezone America/New_York).
  - Long (Mon / Wed / Fri only): 13:00 ET, `youtubeData`: type "video", madeForKids false, category "EDUCATION", isAiGeneratedContent false, tags (10–15), title ≤ 70 chars.
  - Shorts: 10:00, 15:00, 18:00 ET (3 per day, every day), type "short", same flags, title ends with "#shorts".
  - Description = `templates/description.txt` filled (summary, chapters, sources, disclaimers, footage credits).
- Verify with getScheduledPosts that all posts exist for the day (4 on long days, 3 on Shorts-only days). Then commit `episode.py`, `shorts_spec.py`, `sources.md`, `thumb.json`, `youtube_description.txt`, updated `used_clips.json`, `clips.json`, `topics.md` to `main` and push.
- Shorts: `MUTE = [clip ids]` in shorts_spec.py replaces natural sound with silence for those sources (interviews, narrated archival films) — the Short otherwise mixes the clip's own audio under the narration.
- YouTube description must stay under 5,000 characters (005 first draft was 5,024) — check `make_desc.py` output.
- Interlaced archive.org MPEG-2 (e.g. Combat Bulletin): convert with `fieldmatch,yadif=deint=interlaced,decimate` to clean 24p; 60p archive.org MP4s of silent film (111-ADC) -> `fps=24`. Add a silent audio track (`anullsrc`) so shorts.py/finish.py can read audio.
- Known bad frames: 963638 has a duplicated frame at ~16.67 s (motion_check REPEAT) — avoid 12.7–18.1 s; 857891 cuts at 4.9 s to a donor with a blood-filled line — keep shots before 4.6 s; 917871 ~216 s and ~89 s show red-stained dressings/tubing — avoid.
- 006 (2026-11-07): NARA silent films on archive.org (111-H-1179/1454/1540) start with a NARA slate (0–3 s) — never start a shot before ~3.5 s. 24p/29p silent film: cut short excerpts first and pre-interpolate them to 30p once (`minterpolate` at 960x720, ~11 s CPU per 1 s), then use the excerpts as 30p clips — the build is then fast and motion_check stays at 0. 29.97p DVIDS clips can carry a duplicated frame (1027481 ~16.7 s) — move the shot if motion_check reports REPEAT.
- Photos as Shorts footage: render a 12 s push-in mp4 (`zoompan` on a 7680-wide canvas, d=360) and use it like a clip; keep shots before ~11 s (zoom reaches its max -> REPEAT).
- Shorts credit line must stay ≤ ~70 characters (longer runs off both edges). Pyin on the final Short mix reads ~70–90 Hz because of the score; check the voice stem `shorts/sN/voice.wav` (should be ~120–135 Hz).
- `motion_check.py` on Shorts needs `shorts/sN/timing.json` + clips.json, otherwise every cut is reported as JUMP.

- 007 (2026-11-08): src_cuts misses some jump-cuts — 111605 (~59.1 s, ~121.2 s), 886668 (~61.1 s), NARA 111-M-489 excerpts arm_officers (~2.3 s) and arm_field (~18.7 s): motion_check finds them; move the shot. In 9:16 Shorts fast hand/body motion in a medium shot reads as JUMP — prefer steady close-ups for the first shot. 949268 (Vicenza hemorrhage lane) has moulage blood — never use. 610820 opens with third-party memorial photos (0–8 s) — never use. Wikimedia Commons API rate-limits the cloud (send a User-Agent, sleep between calls); archive.org NLM book scans (pdftoppm on the item PDF) are a reliable public-domain illustration source. Long-form doc graphics: keep `source` short (≤ ~30 chars) or the stamp covers it.

- 008 (2026-11-09): `stat` graphics count up any leading number and add thousands separators — a year like 1965 renders as "1,965". Prefix years with a zero-width space (`a="&#8203;1965"`). DISPLAY replacements run in list order: put longer phrases first ("eighteen forty-two" before "eighteen forty"), or end the list with `DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))`. graphics.mjs re-renders the whole spec (~6 min); for one or two changed graphics, pass a filtered gspec JSON. Wikimedia Commons API, Met, LoC and Wellcome are blocked or rate-limited from the cloud; archive.org book scans (pdftoppm) worked for every still. Own text cards for Shorts: keep content between ~30% and ~55% of the height (hook above, captions at ~62–70%). 385923 has a duplicated frame at ~16.7 s and a dissolve at ~7.5 s — use 8.2–15.5 only. 1026809 ~13–15 s shows a red "fire" sticker on a manikin — avoid. Fact-check found that "Gentlemen, this is no humbug" was first printed in 1859 — always label it "as reported".

- 009 (2026-11-10): 2014 DVIDS SD files are anamorphic (720x480 with SAR 40:33 or 5000:4219; 1440x1080 SAR 4:3) — build_ep crops storage pixels, so people look stretched. Pre-scale them once to square-pixel 1920x1080 (`scale=1920:1080,setsar=1`) and replace the clip file. Contact sheets: drawtext `%{eif\:t\:d}` already gives source seconds after `fps=1/N` (do not multiply). Static DVIDS shots of 29.97p files (374379 sign 4–14 s, Tubmanburg 15–25 s; 372199 48–58 s and ~100 s; 375113 ~150 s) carry duplicated frames -> motion_check REPEAT: prefer shots with camera/subject motion. Card push-ins for Shorts must be longer than the longest line (render 20 s, zoom step 0.0003): a 12 s card under a 12.3 s line shifts every later cut (motion_check JUMP inside segments). DVIDS clip titles can be wrong (382681 "ETU Training B-Roll" is actually ETU construction near Senje) — trust the burned-in slate at 0–4 s and say so in sources.md. graphics.mjs and build paths: pass absolute episode paths.

- 010 (2026-11-11): United News 1944 newsreels on archive.org (gov.archives.arc.*) are telecined NTSC MPEG-2: `fieldmatch,yadif=deint=interlaced,decimate,scale=960:720,setsar=1` + minterpolate to 30p (~14 min CPU for 75 s on 2 cores); NPC-4360 has a burned-in timecode at ~75–82% height — crop `920:518:180:0`. The Shorts HUD `label` is shown for the WHOLE Short: write it so it is true over every shot (cards + film), not just one clip. Pillow card fonts have no "→" glyph (renders as a symbol) — use "TO". The fact-checker flagged unidentified newsreel labs under Oxford/Peoria/Brooklyn narration: tag archival production footage "PLANT/LOCATION NOT IDENTIFIED" and keep it off named-place lines.

- 011 (2026-11-12): NARA 111-ADC Korean War films on archive.org (e.g. 111-adc-9535) are 720x480 SAR 10:11 "60p" made from bobbed telecined film (every 5th frame near-duplicate): cut short excerpts with `fps=24,scale=656:480,setsar=1,minterpolate=fps=30` (+ anullsrc) and use the excerpts (mash_a..d); fps=30 on the original gives judder. Excerpts can still carry an interpolation JUMP (mash_c ~10.3 s) — motion_check on the Short finds it. archive.org FB-173 (War Dept. Film Bulletin "The Evacuation Hospital", 1945) is a washed-out copy with ~6 unique frames/s — unusable (description usable as a source). DVIDS 810388 ends with a "READY NOW" slate after ~105 s (a long shot from 99 s ran into black); 1000528 has a duplicated frame at ~116.8 s and moulage casualties at ~125–135 s; 999435 is almost all moulage wounds (only the 0–3 s triage sign and ~104 s sterilizers are clean); 996410 is 25p (auto-interpolated, slow) with cuts every ~3 s. Contact sheets with `fps=1/8` show content from ~4 s after the stamped time, and `-ss` before `-i` with `ass=` restarts subtitle time at 0 — don't mistake either for sync errors. Shot-count changes in one line re-render every later segment (~10 min).

- 012 (2026-11-14): Wellcome book scans on archive.org (e.g. Snow 1855, b28985266) render fast with pdftoppm except fold-out plates — render plate pages alone (`-f N -l N`, r=150) in the background; 16:9 crops of plates as 20 s push-in clips (`zoompan` on 7680 canvas, step 0.0002–0.0003) work in both long-form and Shorts and give motion_check 0. NLM "Purification of Water" (1943, archive.org PurificationOfWater1943) is 29.41 fps telecine with a duplicate every 5th frame: excerpt with `decimate=cycle=5,scale=960:720,minterpolate=fps=30`. NLM has transcripts for many films (collections.nlm.nih.gov/transcript/nlm:nlmuid-…-vid) — use them as the film's own source. DVIDS 672418 is 671211 with a DoD bug (duplicate, skip). 1002024 ~238 s gives a motion_check JUMP (cut detector misses it) — use 218 or 225.7. 24p DVIDS shots cost ~2.5–5 min each in build_ep when CPU is shared: run Shorts in parallel only after the archival/graphics prep is done. Encode (2-pass x265, 10.4 min) takes ~35 min on 2 cores.

- s013 (2026-11-15, Shorts-only): run `src_cuts.py` on every new clip BEFORE shorts.py — without "cuts" in clips.json shorts.py cannot avoid fragments and motion_check reports every source cut as JUMP. Fresh DVIDS B-roll shots are only ~2.3–4 s long (1027903, 1028444): plan 2–3 shots per line inside one source shot each. Coast Guard cruise-ship medevac videos are often 4:3 anamorphic inside 1920x1080 (1029322 SAR 10:11, 1028920 SAR 8:9) — pre-scale to square pixels (even width: 1746 / 1706). For hoist-cam clips set cx so the USCG helmet/operator is in the 9:16 crop at 0.5 s (1027649: cx 0.15). Card footers ≤ ~40 characters (longer runs out of the 9:16 column). 1028444 (LRMC MASCAL DECON): 0–8 s burned-in name strap, 16.7–23.3 s crowded beds with role-players, ≥36 s red-marked litter — avoid.

## Performance rules
Rewritten every Monday (Tashkent) from Metricool analytics, last 28 days. Max 8 rules, each backed by ≥ 3 videos. Never changes schedules, AI-label settings, medical-safety or owner content rules (those are recommendations in the run report).
1. Shorts titles name ONE concrete, specific thing — a superlative ("The Only…"), a nickname/term ("…Called 'Dustoff'", "The 9-Line Radio Call"), or a year/object ("…Made in 1955"). These 4 Shorts: median 400 views; the 4 generic ones ("Inside the Army's…", "How Medevac Crews…", "The Rule That…"): median 12.5 views.
2. No Short title opens with "Inside…" or a vague "How crews…": the 3 Shorts built that way got 62, 3 and 1 views.
3. Shorts are watched for seconds, not to the end (median average view duration 6.5 s across all 8 measured Shorts; best 11 s): the first spoken sentence and the hook text must carry the payoff; nothing slow before it.
- Not enough data yet (Metricool returns only the 10 videos published Nov 2–3; Nov 4+ uploads not in the connector): long videos (2 measured, 1 view each), publishing slots (≤ 2 videos per slot), thumbnails and lengths — no rule until ≥ 3 videos each.
- Changelog: 2026-11-09 — section created (weekly review 1; data 2026-10-12..11-09, 10 videos: 8 Shorts, 2 long).
