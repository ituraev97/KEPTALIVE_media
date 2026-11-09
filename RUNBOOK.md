# KEPT ALIVE — daily production runbook

One run = one long video (10–12 min, English, US audience) + 6 vertical Shorts, all for ONE publish day in America/New_York.
Read the Projects doc `claude/kept-alive-bible.md` first (rules, brand, voice, formats). The pipeline is a fork of CHANNEL 16;
`reference/ch16-a001-found/` shows the episode DSL (its colours/hex values are CHANNEL 16's — never copy them; use the KEPT ALIVE palette below).

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
- Next topic: first unchecked line of `topics.md` (formats rotate: THE SAVE / OUTBREAK / HOW IT WORKS / FIRST). Mark it done with the date when published.
- DVIDS API (key in the scheduled-task prompt): `https://api.dvidshub.net/search?api_key=KEY&q=<terms>&type[]=video` → `https://api.dvidshub.net/asset?api_key=KEY&id=video:ID` → download the 1920x1080 file (`files[].src`) to `/home/claude/clips/ID.mp4`. Prefer 30p/60p; 24p must be motion-interpolated (see build).
- archive.org public-domain films (`advancedsearch.php`, mediatype:movies) for OUTBREAK / FIRST; check each item's rights; credit "ARCHIVAL FILM · YEAR · STUDIO".
- Never use a clip already in `used_clips.json`. Contact sheet every 3–5 s with timestamps; skip injuries/blood/patients' faces.
- `python3 pipeline/src_cuts.py /home/claude/clips ID` (internal cuts; builder avoids flash fragments). Add `box` to `clips.json` for 4:3 sources.
- Check real cadence: some "60p" DVIDS files are 24p/25p content (e.g. 923203, 923212) — set `"src_fps": "24000/1001"` (or "25") for that id in `clips.json`; build/shorts then motion-interpolate from the true rate. Some shots inside such files are still uneven: if motion_check flags them, swap the shot. Interview/museum clips with speech: list them in `META["mute_nat"]`. `META["training"]` = clip ids that get the on-screen TRAINING EXERCISE badge.

## 3. Research + script
- `episodes/NNN-slug/episode.py`: `LINES = [(spoken, shots, opts)]` — same DSL as the reference. opts: `kind` (calm|punch|tense|slow|drive|question), `tag` (place · date lower third), `gap`. Numbers as words in `spoken`; hard terms respelled + `DISPLAY` map.
- 1,500–1,800 words → 10–12 min. Structure: cold open ≤ 40 s → title → 5–6 chapters → "what changed" → teaser → disclaimer line → end card.
- Graphics (`pipeline/graphics.mjs`): title, chapter, stat, callcard, steps, cards3, map, timeline, list, doc, end. Colours: Night #0A1214, Panel #13242A, Gauze #EEF2EF, Scrub #2BB3A3 (accent, ONE word), Monitor #6CF29A (numbers/data), Iodine #F2B33D (hook only), Steel #8A9AA0. Graphics animate 0–2.4 s, then hold still.
- `shorts_spec.py`: 6 Shorts (25–55 s each), one fact or moment per Short from the day's topic, own narration, hook ≤ 1.5 s, CTA "FOLLOW FOR MORE REAL MEDICINE".
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
python3 $P/shorts.py $EP $CL             # 6 Shorts from shorts_spec.py
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
- Branch = weekday of the ET publish date (`drop-mon` … `drop-sun`): orphan commit with ONLY that day's files (long.mp4, short1..6.mp4, thumb_A.jpg), force-push. URL `https://raw.githubusercontent.com/ituraev97/KEPTALIVE_media/drop-XXX/<file>`. Video never on `main`.
- Metricool brand **KEPT ALIVE**, blogId **7806960** (YouTube UCa7qKTXkXc0yXmKJkBTFa9Q, brand timezone Asia/Tashkent — send `publicationDate` with timezone America/New_York).
  - Long: 13:00 ET, `youtubeData`: type "video", madeForKids false, category "EDUCATION", isAiGeneratedContent false, tags (10–15), title ≤ 70 chars.
  - Shorts: 08:00, 10:00, 12:00, 15:00, 18:00, 21:00 ET, type "short", same flags, title ends with "#shorts".
  - Description = `templates/description.txt` filled (summary, chapters, sources, disclaimers, footage credits).
- Verify with getScheduledPosts that all 7 posts exist for the day. Then commit `episode.py`, `shorts_spec.py`, `sources.md`, `thumb.json`, `youtube_description.txt`, updated `used_clips.json`, `clips.json`, `topics.md` to `main` and push.
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

## Performance rules
Rewritten every Monday (Tashkent) from Metricool analytics, last 28 days. Max 8 rules, each backed by ≥ 3 videos. Never changes schedules, AI-label settings, medical-safety or owner content rules (those are recommendations in the run report).
1. Shorts titles name ONE concrete, specific thing — a superlative ("The Only…"), a nickname/term ("…Called 'Dustoff'", "The 9-Line Radio Call"), or a year/object ("…Made in 1955"). These 4 Shorts: median 400 views; the 4 generic ones ("Inside the Army's…", "How Medevac Crews…", "The Rule That…"): median 12.5 views.
2. No Short title opens with "Inside…" or a vague "How crews…": the 3 Shorts built that way got 62, 3 and 1 views.
3. Shorts are watched for seconds, not to the end (median average view duration 6.5 s across all 8 measured Shorts; best 11 s): the first spoken sentence and the hook text must carry the payoff; nothing slow before it.
- Not enough data yet (Metricool returns only the 10 videos published Nov 2–3; Nov 4+ uploads not in the connector): long videos (2 measured, 1 view each), publishing slots (≤ 2 videos per slot), thumbnails and lengths — no rule until ≥ 3 videos each.
- Changelog: 2026-11-09 — section created (weekly review 1; data 2026-10-12..11-09, 10 videos: 8 Shorts, 2 long).
