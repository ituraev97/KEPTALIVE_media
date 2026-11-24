Run notes go to RUNBOOK_NOTES.md (append there, never here). Promote a note into a rule section only if it must apply to every future run.

> **LATEST OWNER DECISIONS — read first, they override older sections below (2026-11-24)**
> - Thumbnails v6 (section "Thumbnails v6" near the end): thumb_A and thumb_B are made with `tools/thumbkit/thumbkit.py` + AI pictures from `tools/img_client.py` (request them at the START of the run); only thumb_C uses this channel's old generator. Every run must at least request the AI pictures; if they do not arrive in time, say so in the report.
> - EMOTION FIRST: every thumbnail shows a strong emotion (rage, shock, fear, disbelief) — never a calm face; the AI may only re-light a real face, never change it.
> - Promise rule + subtitles + minimal bleeps (section "Promise, clips & subtitles" at the end).
> - VOICE PACE (owner 2026-11-24: "the voice speeds up and talks too fast"): long-form narration is NEVER sped up — `speed`/`tempo`/`tempos` ≤ 1.0 for the long video (the relay now clamps long-form to 1.0 and Shorts to 1.10). Target 150–165 words per minute: budget ≈ 155 words per minute of narration when you size the script, short sentences, commas where a speaker breathes; do not cram to hit a duration — cut words instead.


# KEPT ALIVE — daily production runbook

The daily run first decides LONG or OFF (see "Long-video cadence"). **LONG run:** one long immersive documentary (40–50 min, hosted on Google Drive) for the target ET day + 4 Short candidates, of which the best are scheduled for the target day and the next day (max 2 Shorts per day, see "Shorts: cadence + hook rules"). **OFF run:** nothing but the check and a one-line report. Precedence: "Long-video cadence" > "Shorts: cadence + hook rules" > "Real footage via relay" > "Format v3" > "Format v2" > the numbered sections.
Read the Projects doc `claude/kept-alive-bible.md` first (rules, brand, voice, formats). The pipeline is a fork of CHANNEL 16;
`reference/ch16-a001-found/` shows the episode DSL (its colours/hex values are CHANNEL 16's — never copy them; use the KEPT ALIVE palette below).

## Long-video cadence — owner decision 2026-11-23 (overrides every 'one long per run/day' line)
Why: token budget. One long video every 2 days; the run in between is OFF.
1. **First step of every run (before setup, cloning or research):** Metricool `getScheduledPosts` for brand KEPT ALIVE (blogId 7806960), window = yesterday … day after tomorrow (ET). Target day = tomorrow (ET).
2. **OFF run:** if tomorrow (ET) already has its Shorts scheduled AND the previous ET day (today) or the target day (tomorrow) has a long video → do nothing else. Report one line, e.g. `OFF run 2026-11-25: long 11-24 + Shorts 11-24/11-25 already scheduled.`
3. **LONG run (every other case):** publish ONE long video on the target day (13:00 ET) AND schedule the Shorts for 2 days: the target day + the next day. Make **4 Short candidates** (s1–s4), score them (scorecard), schedule at most 2 per day at 10:00 / 18:00 ET (Shorts rules): target day 18:00 = trailer for the long, 10:00 = best other candidate; next day = the next two best, different templates. Candidates < 7/10 are not scheduled (say so in the report).
4. If the long video cannot be finished and QA'd in the run: still schedule the Shorts that passed for the target day, do NOT publish an unchecked long, report — the next run is then a LONG run again (step 2 fails because no long exists).
5. If a long video is already scheduled for the target day but its Shorts are missing (e.g. a failed run): make and schedule only the missing Shorts.
6. Weekly Shorts review ("every Monday"; Performance rules rewrite): done by the first LONG run on or after Monday; an OFF run never does it.

## Shorts: cadence + hook rules — owner decision 2026-11-23
Why (Metricool, 30 days, 10 channels, 546 Shorts): Shorts that open with a hard NUMBER, a FAMOUS NAME or a "WHY…?" PARADOX won by 5–50×; template clones posted 3–6 times a day decayed week over week (COLD WARRANT median 633 → 107, bookplume 329 → 42) — YouTube throttles mass-produced look-alike Shorts. This section overrides every older "3 Shorts a day", Shorts schedule and Shorts-count line in this file.
**KEPT ALIVE evidence (Nov 2–20):** winners = one blood / war-plague cluster: "The walking blood bank: when the donors are the blood supply" 1,403 views, "Why the military wants low titer O blood" 1,284, "What Really Killed Most Victims of the 1918 Flu" 1,230, "Why fresh whole blood needs no refrigerator" 1,230, "The Deadliest Flu in Modern History, in 3 Numbers" 1,210 (tourniquet "87% vs 0%" 542). Losers = 1 view each: "The Seat Lowered Through the Jungle Canopy", "CDC Warned of 1.4 Million Ebola Cases. Here's What Changed", "5 Spoons, No Doctor: WWII Surgery 120 Feet Underwater"; hospital ship, polio, penicillin, Ebola, anesthesia mostly 1–50. Shorts median 37 at 3.6 Shorts/day (weekly 74 → 19.5 → 39).

**Cadence (YouTube):**
- Make 4 Short candidates per LONG run (s1–s4, covering 2 days — see "Long-video cadence"), score each one (below), and schedule only those that pass — **never more than 2 a day**. KEPT ALIVE has no TikTok in Metricool, so the other candidates are NOT published anywhere (keep their spec in shorts_spec.py).
- Slots: **10:00 and 18:00 ET** (the two best existing slots, 8 h apart; 15:00 dropped). One Short only → 10:00. Two Shorts on one day must use different visual templates.
- Long-video day (every 2 days, long 13:00 ET): the 18:00 Short is a **trailer** for that long video (ends "Full story on the channel."); the 10:00 Short is the highest-scoring other candidate. The day after: the next two best candidates.

**Scorecard — schedule a Short only if it scores ≥ 7/10** (write the scores into the run report):
1. Hook (0–4): the first second has a hard number, a famous name/brand, or a paradox question — on screen AND spoken. 4 = all of them, punchy; 0 = generic explainer.
2. Payoff (0–3): the hook's promise is paid in the last 2–3 s (a reveal, a number, a twist). Viewers who feel cheated swipe → YouTube stops showing the channel.
3. Freshness (0–2): new story or new angle; never the same template as yesterday's Short.
4. Clarity (0–1): understandable with sound off.
No candidate reaches 7 → rewrite the hook/payoff of the best one and rebuild it; still < 7 → no Short that day (say so in the report).

**Hook rules:**
- Second 0: no logo, no title card, no "In 1942…" slow start — start on the most surprising sentence. On-screen hook ≤ 7 words, large, centered upper third.
- Title formulas that won: [number] + [stakes] ("The Deadliest Flu in Modern History, in 3 Numbers"); [famous name] + [unexpected fact]; "Why/How did…?" + paradox ("Why fresh whole blood needs no refrigerator"). ≤ 60 characters + #shorts.
- **Banned openers/titles:** quizzes ("Name this X in 3 seconds"), plain recaps of old events without a number or a famous name, "Here's what happened…", "Did you know…".
- **Length 20–40 s** (completion rate drives distribution); hard cap 50 s. End on the payoff, then cut — no outro card longer than 1 s; a loopable last line is a plus.
- **Template rotation:** rotate at least 3 visual templates (footage-led / number-card-led / map-or-timeline-led); never the same template two days running (check yesterday's shorts_spec.py).
- Watch-time check: a Short whose average view duration in Metricool is < 5 s after 48 h → that hook style is dead, don't repeat it.

**Weekly (every Monday):** the run reads the last 7 days of Shorts analytics in Metricool (views + average view duration), lists the top 3 / bottom 3 and writes one line "what won" into "Performance rules" below — repeat the winners' hook pattern, drop the losers'.

## Real footage via relay — owner decision 2026-11-23 (adds to Format v3 §3 and Format v2 §2)
The cloud sandbox cannot reach youtube.com. A relay on the owner's server downloads clips from YouTube (or any yt-dlp URL: archive.org, C-SPAN, …) and hands them over through Google Drive folder "FOOTAGE RELAY". Client: `tools/footage_client.py` (stdlib only; read its docstring).
1. **Find:** Drive creds are already in /tmp/drive_creds.json (Format v3 §5). Find candidate videos with the YouTube Data API (`search.list` / `videos.list`, with Projects docs `claude/yt_research.py` + key from `claude/youtube-api-key.md` (never commit the key)) — check channel, upload date and description; pick exact in/out points from the description, chapters or transcript.
2. **Request EARLY, keep working:** `clips.json` = `[{"name": "...", "src": "<youtube id or URL>", "start": "M:SS", "end": "M:SS"}]`, ≤ 40 clips, ≤ 90 s each. `python3 tools/footage_client.py request <RUN> clips.json --creds /tmp/drive_creds.json` (RUN = episode/run id, e.g. `105-2026-11-26`), then continue with research/TTS/graphics. Later: `python3 tools/footage_client.py wait <RUN> /home/claude/clips/relay --creds /tmp/drive_creds.json --timeout 1800` (run it in the background). No answer in 30 min → continue with DVIDS/archive.org as before and note it in the run report. Relay clips go through the same checks as any clip (contact sheet, `src_cuts.py`, cadence/SAR, `clips.json`, `used_clips.json` — never reuse).
3. **Priority 1 = public-domain government video:** CDC, NIH, NLM, FDA, DoD/DVIDS uploads on YouTube, military medicine channels (Army/Navy/Air Force medicine, USU, DHA, Coast Guard), official hospital/agency releases. **Priority 2 = news reports about the exact rescue/outbreak** (short excerpts, with our commentary — fair use).
4. **Never:** movies/TV dramas (medical TV series), other YouTubers, patients' faces under illness words, graphic surgery/gore/blood/wounds (hard rules §0 still apply), minors. Vaccine/treatment claims from any clip only per CDC/NIH/FDA/WHO (§0).
5. **Use:** real footage 30–50 % of runtime; ≤ ~12 s of one external clip at a time; mostly muted under narration (`mute_nat` / `MUTE`), original audio only for short key quotes (≤ 15 s, speaker named on screen); on-screen source label on every relay clip ("CDC VIDEO", "NBC NEWS · 2026", …); list all footage sources (channel, title, URL, date) in sources.md and in the description's footage credits. DVIDS stays first for fresh military medicine (Format v2 §2); the relay adds what DVIDS/archive.org do not have.

## Format v3 — owner decision 2026-11-17 (overrides v2 on length, schedule, structure and hosting of LONG videos)
Why: by 2026-11-13 the channel fell to 30–200 views/day and long videos still got 1–9 views. Similar channels that grow in our niche publish LONG immersive documentaries: Paul McAllister (125K subs) — 57-min "Horrors of Being an American Civil War Soldier" 430K views, median 47K; Explainer Medieval History (8.6K subs, started May 2026) — 50-min "What Dying From Every Medieval Disease Actually Felt Like" 485K; World at War — 45-min documentaries, median 280K; Coast Guard TV (21K, started May 2026) — 42-min episodes in numbered seasons. Long watch time also builds the 8,000 watch hours YPP needs.
1. **Schedule:** one long video every 2 days at 13:00 ET ("Long-video cadence", replaces Mon/Thu). Shorts: 1–2 a day on YouTube, every day ("Shorts: cadence + hook rules").
2. **Length & structure:** **40–50 min** (6,000–7,500 words). One big immersive theme told chronologically through 8–12 chapters (each chapter a mini-story with its own hook), never a list of dry facts. Proven title formulas (≤ 70 chars, true and sourced): "Horrors of Being a [Wounded Soldier / Navy Surgeon / Field Medic] in [War]", "What [Being Wounded at Gettysburg] Actually Felt Like", "Every [Disease That Killed More Soldiers Than Bullets], Explained", "10 Battlefield Inventions That Still Save Lives". "Horrors" is told through narration, archival illustrations, documents and graphics — the hard rules below still forbid blood, wounds, tissue and bodies on screen.
3. **Sources for 40–50 min:** real footage via the relay (see "Real footage via relay", 30–50 % of runtime), archive.org public-domain films (Army/Navy medical training films, NLM collections), Library-of-Congress-era illustrations via archive.org scans, DVIDS (fresh footage first, Format v2 §2), and our own graphics (≥ 35 % of screen time: maps, timelines, stat cards, documents). Prefer 30p/60p sources: 24p interpolation is very slow on 2 cores; at this length use crossfades/Ken-Burns on 24p archival instead of interpolation.
4. **Build time:** start the long build EARLY in the run; run every long step in the background and wait for it only as in "4. Build → Waiting for long jobs". Typical times on 2 cores: TTS ~35 min (265 lines), graphics ~35 min (in parallel), build_ep ~60 min, finish ~10 min, encode 470 MB ~75 min. Encode with `bash $P/encode.sh $EP $EP/long.mp4 470` (≤ 470 MB, preset veryfast). Unfinished long → "Long-video cadence" step 4.
5. **Hosting (long only):** Google Drive, folder "KEPT ALIVE". Credentials: Projects doc `claude/google-drive-oauth.md` (save the JSON to /tmp/drive_creds.json — NEVER into git); script: Projects doc `claude/drive_upload.py` → /home/claude/drive_upload.py. `python3 /home/claude/drive_upload.py $EP/long.mp4 --folder "KEPT ALIVE" --creds /tmp/drive_creds.json` → use its `direct` URL as the Metricool media for the long video (files > 100 MB need `direct`). Thumbnails and Shorts stay on the GitHub drop branch. After scheduling, clean up: `--cleanup-days 7 --folder "KEPT ALIVE"` (only after the older posts are published). Metricool's YouTube limit is 500 MB per file.
7. **Thumbnails v4 = the SWORN layout (owner decision 2026-11-17: "make the covers the way SWORN does") — `pipeline/thumb3.js` with `<ep>/thumb3.json`** (replaces thumb.mjs and the Format v2 thumbnail rules for long videos; thumb.mjs stays only for localized dub covers of old episodes). Run: `cd $P && node thumb3.js $EP/thumb3.json $EP $EP` → thumb_A/B/C.jpg. Examples: `ab_tests/2026-11-17-v4/*.json`.
   - Split frame with a white divider: LEFT a real frame or archival image (big face if there is one; eyes in the upper third; `"cover": true`), RIGHT a red panel with a HUGE yellow number and a white label plate (`{"number": "120 FT", "label": "UNDER ENEMY WATERS"}`) — or two real images side by side.
   - Red italic tag top-left (`"tag"`: WWII / WWI / CIVIL WAR / 1918 / OUTBREAK / TRUE STORY / TRAINING), KEPT ALIVE mark top-right (automatic).
   - At most 2 caption lines at the bottom: line1 white, line2 red or yellow; ≤ 5 words per line; the number may sit inside the line.
   - Three formats every time: **A** = image + number panel + 2 lines; **B** = question panel (`"left": {"q": ["NO","DOCTOR.","NOW","WHAT?"]}`) + face/image right, no lines; **C** = another image + another number + 2 lines (yellow line2). The strongest goes to thumb_A.
   - Archival/illustrative images that are not of the event itself carry a chip: `"chip": "1945 NAVY FILM"` / `"TRAINING"` (never pretend a 1945 film is the 1942 boat). Crop frames ABOVE our burned-in lower thirds and subtitles (top ~790 px of a 1080 frame).
   - Every word factual and sourced (the fact-checker checks thumbnail text). No gore, no patient faces under illness words.
   - QA: look at all three full size AND at 168×94 — the face/number and one word must still read; bottom-right 260×90 stays clear (duration badge).
8. **Seasons:** number the long videos as a series on the thumbnail badge and in the description ("WAR MEDICINE · EP 3") so viewers binge; end every long video by naming the next episode.

## Format v2 — owner decision 2026-11-14 (overrides anything older below; long-video length, schedule and hosting replaced by Format v3)
Why: channel data 02–10 Nov — ~13,000 of ~13,700 views came from the Shorts feed; every long video got ~3 views (no browse/suggested impressions); Shorts on war + blood, the 1918 flu, the tourniquet and smallpox got 1,000–1,400 views each, hospital-ship and polio Shorts 2–75. YouTube recommends our audience: long dramatic war documentaries (20–26 min, e.g. "They Found 250 Bodies From WWI's Lost Army", 1.2M), ER/ICU "life on a clock" stories ("SHE COULD DIE IN 2 MINUTES!", 234K), outbreaks and disasters.
1. **Topics:** every topic has a military/war angle OR an outbreak/disaster, AND a life at stake on a clock. Institutional "how X is organised" topics (hospital ships as such, polio programmes, admin) only as background inside a story. Queue: `topics.md` (season 2 at the top).
2. **Fresh footage first (owner rule 2026-11-14):** start every episode and every Short from the NEWEST DVIDS uploads: `https://api.dvidshub.net/search?api_key=KEY&q=<terms>&type[]=video&sort=date&sortdir=desc&from_date=<today-60d>T00:00:00Z&max_results=50` (queries rotate: medevac, medic, hospital, surgical, trauma, MEDEVAC hoist, Coast Guard medevac, CBRN, outbreak, field hospital, blood). Prefer REAL recent events (Coast Guard/Navy medevacs, hospital-ship missions, disaster responses, mass-casualty exercises) published in the last 30 days — a real save from this week can be the topic itself. Target ≥ 60 % of footage screen time from clips published in the last 60 days; archival film only for genuinely historical chapters. Log each clip's DVIDS publish date in sources.md. Never reuse a clip (`used_clips.json`). Then request government/news YouTube clips of the same event or topic through the relay (see "Real footage via relay").
3. **Long video = a story, not a lecture:** one real case with a protagonist (a medic, a crew, a ship, a doctor — rescuers may be named when an official release names them; patients never) told on a clock: cold open on the most dramatic verified moment ("They had 4 minutes…") → who/where → the danger escalates → the save → what it changed (history: then vs now on fresh footage) → teaser → disclaimer. (Length and structure per Format v3: 40–50 min, 8–12 chapters; the story-on-a-clock approach lives on inside each chapter.) Titles ≤ 70 chars, true and sourced.
5. **Shorts formula (from the winners):** every Short opens on a number or a contrast tied to war or an outbreak — "87% vs. 0%", "in 3 numbers", "1883 vs. now", "13 million pints", "killed more soldiers than combat". Hook text + subject on screen at 0.5 s. 20–40 s. Titles ≤ 60 chars, never two Shorts in a day with the same opening pattern. The trailer Short comes from the long's story; the other candidates may also use the freshest DVIDS real events / one war-medicine or outbreak fact each, built on footage published in the last 30 days where possible.
7. **A/B/C test on every long video (owner rule 2026-11-14):** THREE thumbnails (layouts per Format v3 §7, `thumb3.json`), each from a DIFFERENT real frame and with a DIFFERENT promise (number / emotion / question) — and THREE titles (A = the published one). Metricool gets title A + thumb_A. The drop branch carries thumb_A/B/C.jpg; `research/YYYY-MM-DD.md` and the run report list titles B and C and the thumb files so the owner can start YouTube Studio → Test & Compare (thumbnails, and titles where the channel has title testing). All three titles and texts must be true and sourced. Back catalogue A/B/C for 001–012: `ab_tests/2026-11-14/`.
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
- Relay clips (YouTube: CDC/NIH/NLM/FDA/DoD channels, news reports of the exact event) — request early, see "Real footage via relay".
- archive.org public-domain films (`advancedsearch.php`, mediatype:movies) for OUTBREAK / FIRST; check each item's rights; credit "ARCHIVAL FILM · YEAR · STUDIO".
- Never use a clip already in `used_clips.json`. Contact sheet every 3–5 s with timestamps; skip injuries/blood/patients' faces.
- `python3 pipeline/src_cuts.py /home/claude/clips ID` (internal cuts; builder avoids flash fragments). Add `box` to `clips.json` for 4:3 sources.
- Check real cadence: some "60p" DVIDS files are 24p/25p content (e.g. 923203, 923212) — set `"src_fps": "24000/1001"` (or "25") for that id in `clips.json`; build/shorts then motion-interpolate from the true rate. Some shots inside such files are still uneven: if motion_check flags them, swap the shot. Interview/museum clips with speech: list them in `META["mute_nat"]`. `META["training"]` = clip ids that get the on-screen TRAINING EXERCISE badge.

## 3. Research + script
- `episodes/NNN-slug/episode.py`: `LINES = [(spoken, shots, opts)]` — same DSL as the reference. opts: `kind` (calm|punch|tense|slow|drive|question), `tag` (place · date lower third), `gap`. Numbers as words in `spoken`; hard terms respelled + `DISPLAY` map.
- 6,000–7,500 words → 40–50 min (Format v3 §2). Structure: cold open ≤ 40 s on the most dramatic verified moment → title → 8–12 chronological chapters, each a mini-story with its own hook → "what changed" → name the next episode → disclaimer line → end card.
- Graphics (`pipeline/graphics.mjs`): title, chapter, stat, callcard, steps, cards3, map, timeline, list, doc, end. Colours: Night #0A1214, Panel #13242A, Gauze #EEF2EF, Scrub #2BB3A3 (accent, ONE word), Monitor #6CF29A (numbers/data), Iodine #F2B33D (hook only), Steel #8A9AA0. Graphics animate 0–2.4 s, then hold still.
- `shorts_spec.py`: 4 Short candidates (20–40 s each; only those passing the scorecard get scheduled, max 2/day over 2 days), Shorts hook rules + Format v2 §5, own narration, hook ≤ 1.5 s, CTA "FOLLOW FOR MORE REAL MEDICINE". Shorts-only fallback ("Long-video cadence" step 5): an episode folder `episodes/sNNN-slug/` with only shorts_spec.py + sources.md (build only the per-line TTS/graphics/clips shorts.py needs, never a long video).
- Fact-check agent (separate) on episode.py + shorts_spec.py + sources.md → fix → only then TTS.

## 4. Build
```bash
EP=/home/claude/keptalive_media/episodes/NNN-slug; P=/home/claude/keptalive_media/pipeline; CL=/home/claude/clips
W=/home/claude/keptalive_media/tools/waitfor.sh
bg() { n=$1; shift; setsid nohup bash -c "$*; echo EXIT \$?" > $EP/$n.log 2>&1 < /dev/null & echo $! > $EP/$n.pid; }
bg tts   "python3 $P/tts_ep.py $EP"      # am_fenrir + processing (vfx.py) — the channel voice, do not change
bash $W $EP/tts.log "^speech seconds:|^EXIT |Traceback" 540 $(cat $EP/tts.pid)
bg gfx   "cd $P && python3 make_gspec.py $EP && node graphics.mjs $EP/gspec.json $EP/gfx"   # may run in parallel with tts
bash $W $EP/gfx.log "^EXIT |Error" 540 $(cat $EP/gfx.pid)
bg build "python3 $P/build_ep.py $EP $CL"
bash $W $EP/build.log "^done [0-9]|^EXIT |Traceback" 540 $(cat $EP/build.pid)
python3 $P/motion_check.py $EP/video_raw.mp4 $EP/timing.json $CL/clips.json > $EP/mc.log; tail -n 15 $EP/mc.log   # must report "issues 0"
bg finish "python3 $P/finish.py $EP $CL"  # subtitles, lower thirds, score, SFX, -14 LUFS
bash $W $EP/finish.log "^audio \+ subs done|^EXIT |Traceback" 540 $(cat $EP/finish.pid)
bg encode "bash $P/encode.sh $EP $EP/long.mp4 470"   # ≤ 470 MB, long is hosted on Google Drive (Format v3 §5)
bash $W $EP/encode.log "^EXIT " 540 $(cat $EP/encode.pid)
bg shorts "python3 $P/shorts.py $EP $CL" # 4 Short candidates from shorts_spec.py (prints "sN <sec> s -> <file>" per Short)
bash $W $EP/shorts.log "^EXIT |Traceback" 540 $(cat $EP/shorts.pid)
cd $P && node thumb3.js $EP/thumb3.json $EP $EP   # thumb_A + thumb_B + thumb_C (Format v3 §7)
```
**Waiting for long jobs (token rule, owner decision 2026-11-23):** every step that can run > 1 min (TTS, graphics, build_ep, finish, encode, shorts, excerpt/minterpolate jobs, footage_client `wait` — regex `^EXIT |"clips"|timeout`) runs via `setsid nohup … > <log> 2>&1 < /dev/null &` with a pid file (the `bg` helper above; it appends `EXIT <code>`), and is waited for ONLY with `bash tools/waitfor.sh <log> "<done-or-error regex>" 540 <pid>`. It prints DONE / EXITED / WAITING + the last 3 log lines; repeat the same call while it prints WAITING. Never `cat`, `tail -f`, `sleep`-loop or re-read a big log to poll; after DONE/EXITED read at most `tail -n 20` or `grep -E "WARN|MOVE|Error" <log> | head -30`. EXIT ≠ 0 or Traceback → read the error lines, fix, rerun. Run independent jobs in parallel and wait on the longest one. Never let a foreground command run past 10 minutes (it kills the job; see QA on aborted builds).

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
- Branch = weekday of the ET publish date (`drop-mon` … `drop-sun`): orphan commit with ONLY that day's files (thumb_A/B/C.jpg on the long day — long.mp4 itself goes to Drive, Format v3 §5 — plus that day's 1–2 scheduled sN.mp4), force-push. A LONG run fills two branches: the target day's and the next day's (its Shorts). URL `https://raw.githubusercontent.com/ituraev97/KEPTALIVE_media/drop-XXX/<file>`. Video never on `main`.
- Metricool brand **KEPT ALIVE**, blogId **7806960** (YouTube UCa7qKTXkXc0yXmKJkBTFa9Q, brand timezone Asia/Tashkent — send `publicationDate` with timezone America/New_York).
  - Long (one every 2 days, "Long-video cadence"; media = Google Drive `direct` URL): 13:00 ET, `youtubeData`: type "video", madeForKids false, category "EDUCATION", isAiGeneratedContent false, tags (10–15), title ≤ 70 chars.
  - Shorts: 10:00 and 18:00 ET (1–2 per day, every day — only candidates that passed the scorecard; on the long day 18:00 = trailer for the long; a LONG run schedules the target day and the next day), type "short", same flags, title ends with "#shorts".
  - Description = `templates/description.txt` filled (summary, chapters, sources, disclaimers, footage credits).
- Verify with getScheduledPosts that all posts exist: target day = long + 1–2 Shorts, next day = 1–2 Shorts. Then commit `episode.py`, `shorts_spec.py`, `sources.md`, `thumb3.json`, `youtube_description.txt`, updated `used_clips.json`, `clips.json`, `topics.md` to `main` and push.
- Shorts: `MUTE = [clip ids]` in shorts_spec.py replaces natural sound with silence for those sources (interviews, narrated archival films) — the Short otherwise mixes the clip's own audio under the narration.
- YouTube description must stay under 5,000 characters (005 first draft was 5,024) — check `make_desc.py` output.
- Interlaced archive.org MPEG-2 (e.g. Combat Bulletin): convert with `fieldmatch,yadif=deint=interlaced,decimate` to clean 24p; 60p archive.org MP4s of silent film (111-ADC) -> `fps=24`. Add a silent audio track (`anullsrc`) so shorts.py/finish.py can read audio.
- Known bad frames: 963638 has a duplicated frame at ~16.67 s (motion_check REPEAT) — avoid 12.7–18.1 s; 857891 cuts at 4.9 s to a donor with a blood-filled line — keep shots before 4.6 s; 917871 ~216 s and ~89 s show red-stained dressings/tubing — avoid.

## Lessons from past runs (distilled 2026-11-23)
Full per-run notes (006–s018): RUNBOOK_NOTES.md — read it only when a lesson below points there.
1. Before using ANY DVIDS / archive.org / NARA clip id, `grep -n <id> RUNBOOK_NOTES.md` (known duplicate frames, moulage blood, cadaver labs, name straps, slates, memorial photos, bad windows).
2. Check reuse by id: `used_clips.json` is a list of dicts → `{str(x['id']) for x in json.load(...)}`; also check against the Shorts of the last 2 runs.
3. Run `src_cuts.py` on every new clip BEFORE build_ep/shorts.py; it still misses some jump cuts, whip pans, flashes and wipes — check frames at each shot's start AND end; motion_check finds the rest → move the shot.
4. Telecined / 24p / 29.41p / "29/1" / bobbed "60p" archival film: pre-cut short excerpts once to clean 30p (`decimate=cycle=5` where every 5th frame repeats, then `framerate=fps=30` or `minterpolate=fps=30`; interlaced: `fieldmatch,yadif=deint=interlaced,decimate`; 4:3: crop active picture, `setsar=1`) + `anullsrc`, then use the excerpts as clips.
5. Excerpts and push-in clips must be longer than the longest line that uses them (build_ep silently renders short segments) — after every build compare each seg's frame count with timing.json.
6. NARA silent films open with a slate: never start a shot before ~3.5 s. Crop burned-in timecodes/captions out of the excerpt.
7. Anamorphic or 4:3-in-1080 files (check SAR): pre-scale once to square pixels (`scale=…,setsar=1`, even width) and replace the clip file.
8. Static shots of 29.97p DVIDS files and phone footage (~10–12 fps) carry duplicate frames → motion_check REPEAT: prefer shots with camera/subject motion.
9. Fresh DVIDS B-roll shots are ~2–4 s: plan 2–3 shots per line inside one source shot. DVIDS often ships a vertical 1080x1920 original (files[0]) — use it for Shorts.
10. 9:16 Shorts: first shot = steady close-up (fast motion in a medium shot reads as JUMP); for hoist-cam set `cx` so the operator is in the crop.
11. Old-film flicker / hand-crank hitches that motion_check reports as JUMP: verify a few by eye, log them in `<ep>/archival_flicker_points.json` and pass them via `/home/claude/clips/clips_mc.json` (builder clips.json unchanged).
12. motion_check on a Short needs `shorts/sN/timing.json` + clips.json; check the voice pitch on `shorts/sN/voice.wav` (~120–135 Hz), not on the final mix.
13. Stills: Wikimedia (upload.*), Met, LoC, Wellcome are blocked from the cloud — use archive.org (`/download/<id>/page/n<leaf>_w1600.jpg`, find a caption's leaf via `_hocr_pageindex.json.gz` + `_hocr_searchtext.txt.gz`; PDFs via `pdftoppm` / `pdfimages -j`; render fold-out plates alone).
14. Photos/cards as clips: render a 20 s push-in (`zoompan` on a 7680-wide canvas, step 0.0002–0.0003); a Ken-Burns "in" still longer than ~9.1 s hits the zoom cap → use "pan". Portrait/square stills (aspect < 1): pre-pad onto a 3840x2160 blurred, darkened copy of themselves; trim printed body text from book scans; check faces are not cut at the eyes.
15. tts_ep.py caches by line NUMBER: when inserting lines, rename `vo/raw_NN.wav` to the new indices (match by text) and delete `vo/l_*.wav`.
16. Changing the shot count of a line re-renders every later segment (~10 min) — to shorten, cut words, not shots. A Short over 40 s: cut words. ~90–96 spoken words ≈ 36–40 s incl. CTA.
17. graphics.mjs re-renders the whole spec: for 1–2 changed graphics pass a filtered gspec JSON. Always pass absolute episode paths.
18. `stat` graphics count up leading numbers with separators: prefix years with a zero-width space (`&#8203;1965`). DISPLAY replacements: longest phrases first (`sorted(DISPLAY, key=lambda x: -len(x[0]))`).
19. Shorts layout: HUD `label` must be true over the WHOLE Short; credit line ≤ ~70 chars; card footers ≤ ~40 chars; card content between ~30 % and ~55 % of the height, rows ≤ ~600 px of 2160; Pillow card fonts have no "→" (write "TO"); long-form doc `source` ≤ ~30 chars.
20. Contact sheets: after `fps=1/N`, drawtext `%{eif\:t\:d}` already gives source seconds; `fps=1/8` shows content ~4 s after the stamp; `-ss` before `-i` with `ass=` restarts subtitle time — none of these are sync errors.
21. DVIDS titles can be wrong: trust the burned-in slate at 0–4 s and burned-in sensor dates over the title/description, and say so in sources.md.
22. Archival footage not of the event: tag it ("NOT <SHIP>", "PLANT/LOCATION NOT IDENTIFIED", chip "1945 NAVY FILM") and keep it off named-place lines. Historical stories cannot reach 60 % fresh footage: put fresh clips on the "today" chapter and say so in the report.
23. Fact-check traps: data from another country presented as American; merged events; case series that include other populations ("Union Army records", not "Union soldiers"); different counts are never "the same count"; "no less than N" → "N+"; "gunshot" not "bullets" when fragments are included; quotes first printed later → "as reported"; thumbnail lines must name the population.
24. People: only rescuers named in official releases, official histories or published memoirs may be named; private letter-writers are anonymised.
25. Training clips: scan for moulage/role-player blood (face too) and cadaver labs before use; keep wide or equipment-centred shots.

## Performance rules
Rewritten every Monday (Tashkent) from Metricool analytics, last 28 days. Max 8 rules, each backed by ≥ 3 videos. Never changes schedules, AI-label settings, medical-safety or owner content rules (those are recommendations in the run report).
1. The SUBJECT decides a Short: blood / bleeding, the tourniquet, the flu that hit soldiers, smallpox, a war wound and its fix — 22 Shorts, median 297 views; every other subject — 47 Shorts, median 25. Pick each Short from that family or give it a famous name / paradox hook (Shorts hook rules).
2. Institutions, programmes, ships and labs die in the feed: hospital ships, polio, Ebola response, penicillin production, labs, "a hospital in 72 hours", robots — 24 Shorts, median 17 (all others 44). Use them only as background inside a war/body story.
3. Put a war word in the title (army, soldier, troops, military, combat, WWI/WWII, Korea, D-Day, Civil War, medic): 30 Shorts with one, median 52.5; 39 without, median 25.
4. A number alone does not lift a weak subject: 39 Shorts with a digit, median 37; 30 without, median 38. "In 3 Numbers" — 4 Shorts, median 22.5 (only the 1918 flu one won). Numbers work on a strong subject.
5. Death odds on a war wound are this month's best number hook: "31 of 34 Died. Then the Coast Guard Got Rescue Swimmers" 309, "An Estimated 4 in 5 Died of This WWI Wound. Then: a Splint" 183, "Bleeding Linked to 9 in 10 Potentially Survivable War Deaths" 124 — the three best of Nov 16–20.
6. Present-day ship and cruise medevacs without a war or death-odds angle do not travel: "4 Cruise Ships, 11 Days" 14, "No Ambulance at Sea: 4 Sick Crew, 1 Helicopter" 34, "A Helicopter Deck on a Hospital Ship" 6, "How Medevac Crews Rescue Where They Can't Land" 4. Use such fresh rescues as the "today" shot inside a history Short instead.
7. Shorts are watched for ~4 s (median average view duration 4 s, 69 Shorts): the on-screen hook and the first spoken sentence must carry the payoff.
8. Long videos still get no reach: 13 long videos in the export (Nov 2–18), median 5 views, median average view duration 20 s; 93 % of all views come from the Shorts feed, 5 % from search. The 40-min documentaries (EP 1 Nov 19, EP 2 Nov 23) are not in the export yet — judge them once ≥ 3 are in; until then every Short points to the newest long via "Related video".
- Dropped: the 10:00 ET slot rule (since Nov 7: 10:00 ET median 40, 15:00 36, 18:00 36 — no slot effect once topic is equal).
- Not enough data yet: 40-min documentaries, thumbnails/A-B-C winners (not in Metricool), Short length, famous-name hooks (first one: s018 Desmond Doss, 2026-11-24).
- Changelog: 2026-11-09 — section created (weekly review 1). 2026-11-16 — weekly review 2 (54 videos). 2026-11-23 — weekly review 3 (uploads 2026-10-26..11-20: 69 Shorts, 13 long): rules 5, 6 new (death odds; present-day ship medevacs); slot rule dropped; rules 1–4, 7, 8 updated with new numbers. Weekly Shorts median: Nov 2–8 74 → Nov 9–15 19.5 → Nov 16–20 39.

## Thumbnails v5 — illustrated cut-out from REAL images (owner decision 2026-11-23)
Owner: "bright and illustrated-looking, like the top drama channels — but faces must not be distorted". This section overrides the **thumb_A** part of the earlier thumbnail rules; thumb_B and thumb_C keep the current generator, so YouTube Studio → Test & Compare measures the new style against the old one. All earlier content rules stay in force: lawful image sources, every word true and sourced, fact-check of the thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

- Tool: `tools/thumbkit/thumbkit.py` (header = full spec). Setup once per run: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"` (downloads a 176 MB cut-out model on first use; if that fails the tool still works with a soft oval mask — say so in the report).
- It cuts the subject out of a real photo or video frame, adds a white sticker outline, a coloured glow and a rim light, washes the background in colour and sets 2–3 huge Anton words + an optional yellow sticker. Only pixel filters — no AI redraw, faces stay exactly as photographed. NEVER feed it an AI-generated image of a real person.
- Spec (`<ep>/thumbkit.json`, a list → thumb.jpg, thumb_B.jpg… — for this channel set "out":"thumb_A.jpg"):
  `[{"out":"thumb_A.jpg","layout":"solo","people":[{"src":"photo_or_clip","t":12.4,"crop":[x,y,w,h],"tint":"warm","kind":"person"}],"line1":"$250M","line2":"VANISHED","sticker":"SMALL FACT","brand":{"accent":"<channel colour>","sticker":"#FFD400","border":false}}]`
  - `layout`: "solo" (subject right, words left) or "versus" (two REAL sides of the same dispute, words centre — never pair people who are not part of the same story).
  - `kind`: "person" or "object" (boat, drug bundle, document, product, building, aircraft…).
  - `crop`: generous box around head + shoulders (face ≈ 35–50 % of its height) in source pixels; the subject must be ≥ 360 px tall in the source (the tool warns otherwise — find a bigger image).
  - `tint`: warm | cold | toxic | gold. `brand.accent` = the channel's main colour from the current generator.
- After rendering, LOOK at thumb_A at 320 px wide: words readable, face not covered, outline clean (no chunks of background). If the cut-out is bad (busy background, hands lost), use the current generator for A and say so in the report.

## Thumbnails v6 — YouTube-AI style: AI picture + real text/documents (owner decision 2026-11-23)
Owner: "make them like the thumbnails YouTube Studio's AI draws — bright, illustrated, with brands". This section overrides the **thumb_A and thumb_B** parts of the earlier thumbnail rules; thumb_C keeps the current generator, so YouTube Studio → Test & Compare measures the new style. Earlier content rules stay: lawful image sources, every word true and sourced, fact-check of thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

0. **EMOTION FIRST (owner 2026-11-24):** every thumbnail must show a strong emotion at first glance (rage, shock, fear, disbelief) — never a calm or smiling face. Pick the PEAK real frame/photo, let the AI dramatize light/smoke/contrast while keeping the exact face and expression; if no emotional real frame exists, put the emotion into the scene (fire, sirens, red stamp). Details: STYLE.md "EMOTION FIRST".
1. Read `tools/thumbkit/STYLE.md` — templates learned from YouTube's own AI thumbnails: doc (documentary split), evidence/fraud (object + real document + stamp), ntsb (full-bleed reconstruction + telemetry HUD + red circle), mugshot (real face + seized items, soft seam), versus, solo. Pick the template that fits this channel's examples.
2. AI pictures (free, FLUX.2 klein on the owner's office PC) via Drive "IMG RELAY" — request EARLY in the run (≈ 12 min per picture, longer while the PC voices — at most 3 pictures per run):
   `python3 tools/img_client.py request <ID> plates.json --creds /tmp/drive_creds.json` then later `python3 tools/img_client.py wait <ID> <ep>/plates --creds /tmp/drive_creds.json --timeout 2400`.
   plates.json = `[{"name":"plate_A.png","prompt":"cinematic photo of ..., dramatic side light, dark background, high detail","w":1280,"h":720,"seed":1}, ...]` (max 6). The AI paints ONLY pictures — NEVER ask it for text, documents, logos-as-evidence. Real people: send their REAL lawful photo as `"ref"` (edit mode: "same person, same expression, re-lit with red and blue police lights, sharp, cinematic") — never generate a real person from text.
   No answer in time → build A/B with real frames (thumbkit solo/versus) and say so in the report.
3. Compose with `tools/thumbkit/thumbkit.py <ep>/thumbkit.json` (setup: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"`; header lists every layout and overlay: tag, ribbon, hud, circle, path, stamp, bignum, pill, label, band). Text, numbers, stamps and the REAL document crop are drawn by thumbkit — documents come only from the real source (PDF page → `doc`, `highlights` boxes in its pixels).
4. LOOK at every thumb at full size and at 320 px: AI picture has no garbage text/extra fingers/melted objects, faces unchanged, words readable. Bad picture → new seed/prompt (one retry), otherwise fall back to the real-frame layout.

## Promise, clips & subtitles (owner decision 2026-11-24 — lesson from HOTFIX comments: "baited by title, talks about it for 2 seconds", "censors so much you can't tell what he's saying", "ai slop")
- **Promise rule:** the moment the title + thumbnail promise (the arrest, the verdict, the crash, the confession, the number) must appear IN FULL within the first 60 s — the real clip/document/audio, not a 2-second tease — and that story takes ≥ 25 % of the runtime. The title describes what the video is mostly about; never sell one moment that only pays off near the end. Shorts: the hook's promise is paid by the last 3 s.
- **Original audio is always subtitled:** every bodycam/court/interview/stream clip gets burned-in subtitles (word-timed from faster-whisper or the official transcript), big and high-contrast, so viewers understand it on a phone with bad speakers.
- **Bleep only the f-word, c-word and slurs**, exactly the word length (±0.03 s); milder swearing stays audible; the subtitle shows the bleeped word as f***. No swearing at all in the first 15 s (advertiser rules). Gore/violence rules of this runbook stay as they are.
- **Against the "AI slop" impression:** open on real footage/real voices, not narration over stock; real material (clips, documents, photos) ≥ 30 % of the runtime; the narrator states clear judgements ("this is where it went wrong"), no filler or repeated recaps; length follows the story — a tight 12-minute video beats a padded 25.
- Check before publishing: watch the first 60 s — is the promise delivered? Read 3 random subtitled clips with the sound off — are they understandable?
