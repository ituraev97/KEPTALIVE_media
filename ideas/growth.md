# GROWTH RULES — all channels (owner 2026-11-28)
Source: YouTube Help Center / Creator Insider (Todd Beaupré, Sep 2026) / YPP policy + our own YouTube Analytics (28 days).

## What our numbers say
- 85–97% of our views come from the **Shorts feed**; long videos get almost nothing from Home/Suggested. The fastest growth lever is turning Shorts viewers into long-video viewers and packaging long videos better.
- New channels get tested on non-subscribers in the first hour; if nobody clicks AND watches, impressions stop. One weak video does not hurt the channel — repeated ignored videos do.

## Every long video
1. The promise of the title/thumbnail is paid off in the first 30 s (show it, don't tease it). No slow intros, no logo stings longer than 2 s.
2. Length follows the story: for channels under 10k subs aim for **10–15 min**; 30–50 min episodes are not watched (retention 14% at the halfway point on NMTK).
3. Original script with a clear thesis + analysis + sources. Vary structure and visuals between episodes — YouTube's "inauthentic content" policy (Jul 2025) demonetizes whole channels for "templated, mass-produced" videos with minimal variation. No still image on screen > 6 s; use maps, diagrams, timelines, real footage.
4. Title ≤ 70 chars, the plain topic keywords (who/what) in the first 5 words; title and thumbnail complement each other, never repeat the same words.
5. Make 2–3 thumbnail variants for Test & Compare (YouTube picks the winner by WATCH-TIME share, not CTR).
6. Description: 2-line summary, chapters, sources. Tags barely matter.
7. Realistic AI reconstructions of real people/events → tick "altered or synthetic content". Plain AI narration needs no label. Never generate a real person's face with AI.

## Every Short
- Standalone: number / famous name / paradox in second 0, payoff at the end, 20–40 s. A steady daily flow matters more than volume (Shorts older than ~30 days fade).
- Cut Shorts FROM the long video and name the long topic, so the Shorts → long path exists ("related video" link is set in Studio).

## Thumbnails (all channels)
- ONE focal point a phone viewer gets in 0.5 s: a human face with a strong emotion, or one iconic object. Max 3 big words. High contrast, warm/saturated colours beat dark empty scenes.
- Not the same template every time (inauthentic-content risk) — rotate 3–4 layouts.
- Never AI-generated faces of real people; real photos only (government releases, archive), AI may only relight/extend.

## Variety & promise (all channels) — owner 2026-11-28: "the same clips and graphics keep coming out, and it is not clear what the title has to do with it"
Audit of the last 4 long videos per channel found the same problem everywhere: one stock clip cut into dozens of slices (COLD WARRANT 027: one aircraft clip = 49% of the video; RELEASED IN FULL 021: the same 5-second Capitol shot 61 times, the same Capitol clip in 17 episodes), the same document page shown 12 times (SWORN 023), the same code-generated music bed in every episode, one thumbnail template for months, the same opening line ("<Date>, twenty twenty-six.") and the same chapter names, and titles promising something that is not on screen (CW 026 "gunfire" with no gunfire shot; SWORN 024 Meng Wanzhou on the thumbnail although she was not on trial; HOTFIX "GTA 6 mode" with GTA in 4% of the footage).
## MEASURED 2026-11-29 — what our published videos actually look and sound like (owner: "sound must be good, frames sharp and not repeating")
The latest long video of 8 channels was downloaded from YouTube and measured with our own tools. Only HOTFIX and Book Plume passed.
- **Frozen picture**: COLD WARRANT 46 % of the runtime, KEPT ALIVE 45 %, LAST CONTACT 26 % (pieces up to 19 s where nothing moves). Text cards filled 15 of 24 sampled frames on COLD WARRANT — that is a slideshow, and YouTube serves it at 0.7 Mbit/s.
- **Repeats**: SWORN 19 %, NMTK 18.5 %, KEPT ALIVE 16 % (limit 15 %); the same press conference three times in one video.
- **Flat sound**: loudness range 1.5–2.5 LU on six channels (HOTFIX 5.9). Music was only ~6 dB under the voice. Nothing can be an accent when everything is equally loud.
- **Black first frame** on SWORN, COLD WARRANT, NMTK, KEPT ALIVE — frame 0 is what the Shorts feed, hover preview and autoplay show.
- **Sharpness**: REEL 41 tops out at 720p. 1080p uploads are served at 0.7–1.3 Mbit/s; the same picture uploaded as 1440p gets ~4 Mbit/s. Source footage was fetched at 720p and stretched.
- **Captions too small** for a phone on COLD WARRANT and REEL 41; a caption said "an empty cell" over a picture of a gym.

### Fixes that are now mandatory (all tools are in `tools/cinema/`)
1. **Upload master = 1440p, one encode.** Render at 1920×1080 or larger, then `python3 tools/cinema/deliver.py final.mp4 upload.mp4 --finish` (film finish + lanczos upscale to 2560×1440 + size cap 440 MB, audio untouched). Upload `upload.mp4`. Do NOT also run `look.py finish` (two encodes soften the picture). Shorts stay 1080×1920. Never deliver a long video below 1080p.
2. **Sources at 1080p.** The footage relay now delivers 1080p. Ask for the best available quality, crop only when ≥ 720 px of real height remains, never enlarge a clip more than 1.5×; a soft or tiny source is shown smaller on a designed background instead of being stretched full-frame.
3. **Moving picture, not cards.** Frozen picture ≤ 10 % of the runtime and no piece > 4 s (critique.py fails otherwise). Text/number/quote/list cards together ≤ 20 % of the runtime, each ≤ 4 s, and every card sits over moving footage or a slow-moving image, never on a flat dark background. A list of N points = N pictures. If a fact has no footage: map, document crop that pushes to the quoted line, photo with a move, timeline — rotate these, do not repeat one type back to back.
4. **Frame 0 is a picture**: the strongest shot or the key number over footage. Never black, never a fade-in from black, never a logo.
5. **Sound levels are set by the tool, relative to the voice.** `sound_design.py --used-music used_music.json --episode <id>` (commit `used_music.json`): music 17 dB under the voice while it speaks and 9 dB under it in the gaps, a chain of different tracks instead of one loop, no track from the last 4 episodes. Do not add your own music/SFX gain on top. Narration: no heavy compression (ratio ≤ 2:1), no single-pass `loudnorm` on the voice or on the final mix — loudness is normalised once, by sound_design.py. Target loudness range of the final mix ≥ 4 LU; `sound_qa.json` must show `music_under_voice_db` ≥ 13.
6. **Captions readable on a phone**: burned-in captions ≥ 4.5 % of the frame height (≥ 48 px at 1080p, ≥ 64 px at 1440p), max 2 lines, max 7 words on screen, dark plate or 3 px outline. Captions never cover a broadcaster's lower third, a source line or on-screen text of the clip — move them to the top third for that shot. A label must describe what is literally in the picture.
7. **Length**: 10–15 minutes for every channel under 10k subscribers (KEPT ALIVE and NOT MEANT TO KNOW included: their 30–45 min videos keep ~13 % of viewers at the midpoint). A longer story becomes two episodes.

**Hard gate — run on every finished long video AND Short before scheduling (both commands, on the file you will upload):**
`python3 tools/cinema/critique.py <upload.mp4> --events events.json` → must print ОК (frame 0, frozen picture, black gaps, loudness, true peak; warnings about flat sound / resolution are fixed too).

`python3 tools/cinema/variety_check.py <final.mp4> --ledger variety_ledger.json --episode <id>` (commit `variety_ledger.json`). It hashes the picture once per second: `repeat_share` ≤ 0.15 (the same clip moment/still/page shown again), `top_visual` ≤ 0.12 (one picture dominating), `cross_share` ≤ 0.10 (pictures from the previous episodes). FAIL → fix the edit (more sources, different moments) and re-run; never schedule a FAIL. Put its JSON line in the run report.
**Picture:**
- ≥ 25 distinct footage/image sources for a 10+ min video (≥ 30 for 15+ min). Order more footage early instead of stretching what you have.
- No source > 10–15% of the runtime; never wrap a clip back to its start; no round-robin over a small fixed pool; pick moments at random among unused ones.
- A clip/still used in any of the previous 5 episodes: ≤ 10 s in the new one. Generic stock (Capitol, courthouse, aircraft, city skyline, military jets): ≤ 20 s per video in total.
- Never use a source video's own title/intro/text card as b-roll, never zoom until text is cut off or blurry, never upscale a frame beyond ~150%; a soft/low-res frame is replaced, not stretched. On-screen overlays never cover faces or other text.
- The first 3 seconds are a real, striking moment with people or action (never a text card, black screen or logo).
- The same document page/photo at most twice per video — show the next page, a different crop of a different line, or another document.
- Graphics: no card type more than ~12 times or 8% of runtime; nothing holds still > 6 s.
- IN-SCENE HANDLE (owner 2026-11-29: "just write our YouTube user"): in 3D/composited scenes with a natural surface for signage — airport billboard, hangar wall, terminal screen, ground vehicle, building sign, a TV in the background — put THIS channel's YouTube @handle (listed under "This channel") as if it were a real ad: correct perspective, lighting and wear, readable at phone size for 1–3 s, about once per 3–5 minutes. NEVER on the aircraft/vehicle/person/document the story is about, never on evidence, never in a way that looks like part of the real event.
- SUPER-REALISTIC (owner 2026-11-28): every 3D model / AI picture must show THE specific thing — correct model/type and its real markings (airline livery and logo, ship name and hull number, police/army insignia, company branding, the real building). A UPS crash shows a UPS MD-11, not a white airliner. Generic white/placeholder models are banned; if it cannot be made convincingly, use real photos or footage instead.
**Sound:** never generate the music bed in code (fixed chords/seed = the same track every episode). Use `tools/cinema/library/music_*` (6 moods × several tracks), choose the mood; `sound_design.py --used-music used_music.json --episode <id>` rotates the tracks itself (nothing from the last 4 episodes) — commit `used_music.json`.
**Packaging and structure:**
- Thumbnail: rotate at least 3 layouts; never the same layout + accent colour twice in a row, never the same wording pattern within 5 episodes. Never AI-drawn documents (garbled text looks fake) — real crops only. Only show a person's face if the video is about THEM.
- Opening line and title formula: not the same pattern as the previous long video (no "<Date>, twenty twenty-six." twice in a row). Chapter titles used in the last 5 episodes are not reused.
- PROMISE: the person/object/event named in the title or shown on the thumbnail is ON SCREEN and named within the first 30 s; backstory ≤ 60 s before the promised thing. If the footage for a promised moment does not exist (e.g. "gunfire"), change the title — do not promise it.
- A remake of an old episode gets a new title, thumbnail and opening, and the old video must be hidden before the remake is scheduled.

## Voice (all channels) — owner 2026-11-28: work HARD on intonation, pace and pronunciation; every channel has its OWN voice
Engine: Chatterbox **Turbo** on the office PC / relay since 2026-11-28 (≈4.5× faster than the old Chatterbox, same quality). Never ElevenLabs for the English channels.

**Own voice per channel (never borrow another channel's voice):** use exactly the voice listed under "This channel's voice" below. Chatterbox voices are named reference clips (relay spec `"voice": "<name>"`); Kokoro fallbacks are channel-specific blends — the first (largest) voice of a blend is reserved for that channel. A new channel gets a new voice that is checked against all existing ones.

**Intonation (read the script aloud in your head before voicing):**
- Tag every paragraph with a tone: ~25% "hype" (reveals, numbers, verdicts, twists), ~15% "calm" (context, aftermath, sad facts), rest "normal". Never a whole video in one tone.
- Write for the ear: short sentences, vary sentence length, questions where the viewer would ask one, the key word at the END of the sentence. Commas where a speaker breathes; no semicolons/parentheses/colons in narration.
- Turbo understands a few sound tags — `[sigh]` `[chuckle]` `[gasp]` `[clear throat]` — at most one per minute, only where a human narrator would really do it.
- After voicing, LISTEN-CHECK by measurement: pitch variation ≥ 4 semitones, loudness range ≥ 6 LU; a flat take is re-voiced with more hype/calm contrast, not shipped.

**Pace:** long narration 150–165 wpm, Shorts 160–180 wpm. Never speed long narration up with atempo to fit a duration — cut words. No silence > 0.6 s inside narration except one deliberate beat before a reveal. Sentence gaps 0.3–0.45 s.

**Pronunciation:**
- Numbers, dates, money and units are written OUT in words in the TTS text ("twenty twenty-four", "fifty billion dollars", "forty percent").
- Every name, place, brand or foreign/rare word gets a phonetic respelling in the TTS text the first time it is unclear, e.g. `Jaquan` → `Jay-kwahn`, `Huwaitat` → `Hoo-why-tat`, `Riyadh` → `Ree-yahd`; keep the real spelling in subtitles/titles. Keep a per-channel list in `voice_lexicon.md` (word → respelling) and reuse it every episode.
- Acronyms: letters with hyphens when spelled (`F-B-I`), as a word only if people say it as a word (NASA).
- Check the Whisper QA report: any line with similarity < 0.86 or a misread name is re-voiced before rendering.

## This channel
- MEASURED 2026-11-29 on your latest long video: 45% of the runtime was a frozen picture (156 pieces, up to 18 s), repeats 16% (limit 15%), frame 0 black, loudness range 1.8 LU (flat), 43 minutes long. Next episode: 10–15 minutes, every still gets a move ≤ 4 s then a cut, no black opening.
- VARIETY FIX (audit 2026-11-28): own graphics 59% of runtime in 302 and 104 (43 stat cards / 40 quote cards) → own graphics 35–45%, no card type more than 12 times or 8% of runtime; 103 WWI showed the same 5-s window 22 times and one film = 23%; 102 top-3 sources = 77%. Cold opens run 50–119 s (RUNBOOK limit 40 s) → make > 40 s a QA failure. 103 and 104 used the same opening pattern sentence by sentence ("So imagine you are one of them… no antibiotics…") → the title formula and cold-open pattern may not repeat the previous long video. Music: pipeline/finish.py:104-139 synth D-minor score with fixed seed → tools/cinema library. Thumbnails: 3 of last 4 = the same red/yellow split layout → rotate. used_clips.json showed repeats (1029569, 1027481, 1027887) — enforce it.
- Format change: stop 40–50 min episodes (1–2 views each). Longs 10–12 min only on topics whose Short beat the channel median; 2 Shorts/day.
- Thumbnails: a real historical photo with a human face and emotion, warm palette, ≤3 words. The black-red data template looks mass-produced (inauthentic-content risk) and has too many numbers.
- IN-SCENE HANDLE: this channel's YouTube handle is @keptalivefiles — use exactly this text for in-scene signage (see Variety & promise).

## Voice
- This channel's voice: Kokoro blend am_fenrir:0.6+bm_daniel:0.4 (livelier Kokoro method) + vfx.py. Do not use any other channel's voice.
- Voice audit 2026-11-28: Kokoro am_fenrir is medium-flat (pitch 4.2–4.7). Switch to the 'livelier Kokoro' method from coldwarrant-media pipeline/tts_ep.py (commit 54a45a8, owner choice 2026-11-27): blend of voices, per-sentence synthesis, short sentences slower + longer pause, long ones quicker, ±2% jitter — measured on COLD WARRANT as lively as Chatterbox with blend am_fenrir:0.6+bm_daniel:0.4. Longs 150–160 wpm.
