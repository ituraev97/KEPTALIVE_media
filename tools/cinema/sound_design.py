#!/usr/bin/env python3
"""Doc Cinema — automatic sound design for a LONG documentary (any length), built from real recordings.

usage:
  sound_design.py --voice narration.wav --events events.json --library LIB_DIR --out OUT_DIR
                  [--ambience amb_desert] [--music music_tension] [--seed 7] [--beat-align]
                  [--used-music used_music.json --episode ID]     # never the same track as the last 4 episodes
                  [--music-under 17] [--music-open 9]             # dB under the voice: while it speaks / in the gaps

events.json — the "event log" the pipeline writes while building the edit (times in seconds of the final video):
  {"duration": 812.4, "events": [
     {"t": 0.0,   "type": "open"},                 # cold open: ambience + music start
     {"t": 41.2,  "type": "chapter"},              # chapter card / big scene change → whoosh (peak on t) + music lift
     {"t": 95.0,  "type": "reveal", "strength": 1},# key reveal → 4–8 s riser ending 0.3 s BEFORE t, short near-silence, impact ON t
     {"t": 130.4, "type": "number"},               # number/stat pops on screen → small hit
     {"t": 150.0, "type": "doc"},                  # document/paper on screen → paper
     {"t": 151.2, "type": "stamp"}, {"t": 170.0, "type": "photo"}, {"t": 200.0, "type": "glitch"},
     {"t": 260.0, "type": "cut", "ambience": "amb_ocean"}   # place change → ambience crossfade (starts 0.4 s early)
  ]}
Five layers (atmosphere, actions, movement, accents, music). 2026-11-29 (measured on published videos: music was only 6 dB
under the voice, library files differed by 6 dB, one 4-minute track was looped 3–4 times, the beat-align seam clicked):
  - EVERY level is now set relative to the measured voice level, and every library file is level-matched first;
  - music sits --music-under dB below the voice while it speaks and --music-open dB below it in the gaps (chapter cards);
  - the bed is a chain of DIFFERENT tracks of the mood (3 s crossfades), a track repeats only when all were played;
  - tracks used in the last 4 episodes (--used-music) are skipped.
Writes OUT/mix.wav, OUT/stems/{voice,music,ambience,sfx}.wav, OUT/sound_qa.json (+ waveform/spectrum PNGs), OUT/credits.txt.
"""
import argparse, json, os, random, subprocess
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve, resample_poly

SR = 48000
p = argparse.ArgumentParser()
p.add_argument("--voice", required=True); p.add_argument("--events", required=True)
p.add_argument("--library", required=True); p.add_argument("--out", required=True)
p.add_argument("--ambience", default="amb_room"); p.add_argument("--music", default="music_documentary")
p.add_argument("--seed", type=int, default=None, help="default: derived from the episode id / voice length, so episodes differ")
p.add_argument("--beat-align", action="store_true", help="start the first track where its accents best hit reveals/chapters")
p.add_argument("--used-music", default=None, help="json ledger of tracks used per episode (kept next to the channel repo)")
p.add_argument("--episode", default=None)
p.add_argument("--music-under", type=float, default=17.0); p.add_argument("--music-open", type=float, default=9.0)
p.add_argument("--amb-under", type=float, default=26.0)
A = p.parse_args()
os.makedirs(os.path.join(A.out, "stems"), exist_ok=True)
LIB = json.load(open(os.path.join(A.library, "library.json")))
used = []


def db(x):
    return 10 ** (x / 20)


def load(path):
    tmp = path + f".{os.getpid()}.tmp.wav"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", path, "-ac", "2", "-ar", str(SR), tmp], check=True)
    a, _ = sf.read(tmp, dtype="float32"); os.remove(tmp)
    return a if a.ndim == 2 else np.stack([a, a], 1)


def level(x):
    """Gated RMS in dBFS: 100 ms frames, the quiet 30 % ignored (so pauses do not count)."""
    m = x.mean(1) if x.ndim == 2 else x
    h = SR // 10
    if len(m) < h:
        return 20 * np.log10(np.sqrt(np.mean(m ** 2)) + 1e-9)
    fr = np.sqrt(np.mean(m[: len(m) // h * h].reshape(-1, h) ** 2, axis=1))
    fr = np.sort(fr)[int(len(fr) * 0.3):]
    return 20 * np.log10(np.sqrt(np.mean(fr ** 2)) + 1e-9)


def to_level(x, target_db):
    return x * db(target_db - level(x))


def to_peak(x, target_db):
    return x * db(target_db) / (np.abs(x).max() + 1e-9)


def cands(role):
    return [e for e in LIB if e["role"] == role] or [e for e in LIB if e["role"].startswith(role.split("_")[0])]


def pick(role):
    c = cands(role)
    if not c:
        return None
    e = c[rng.randrange(len(c))]
    used.append(e)
    return load(os.path.join(A.library, e["file"]))


def vary(x, pitch=0.045, gain_db=1.5):
    f = 1 + rng.uniform(-pitch, pitch)
    y = resample_poly(x, 1000, int(round(1000 * f)), axis=0).astype(np.float32)  # faster/slower = pitch shift
    return y * db(rng.uniform(-gain_db, gain_db))


def hp(x, f):
    return sosfilt(butter(2, f, "high", fs=SR, output="sos"), x, axis=0).astype(np.float32)


def place(track, clip, start):
    s = int(start * SR)
    if s < 0:
        clip = clip[-s:]; s = 0
    e = min(len(track), s + len(clip))
    if e > s:
        track[s:e] += clip[: e - s]


def mavg(x, n):
    """Centred moving average in O(N) (a plain convolution with a 0.3–0.8 s kernel takes tens of minutes on a 15-minute track)."""
    c = np.cumsum(np.concatenate([[0.0], x.astype(np.float64)]))
    h = n // 2; i = np.arange(len(x))
    lo = np.clip(i - h, 0, len(x)); hi = np.clip(i - h + n, 0, len(x))
    return ((c[hi] - c[lo]) / n).astype(np.float32)


def xjoin(a, b, xfade):
    """Equal-power crossfade of b onto the end of a."""
    xf = min(int(xfade * SR), len(a) // 3, len(b) // 3)
    fi = np.sqrt(np.linspace(0, 1, xf))[:, None]
    return np.concatenate([a[:-xf], a[-xf:] * fi[::-1] + b[:xf] * fi, b[xf:]]).astype(np.float32)


def loop_to(x, n, xfade=2.0):
    out = x.copy()
    while len(out) < n:
        out = xjoin(out, x, xfade)
    return out[:n].astype(np.float32)


ev = json.load(open(A.events))
voice = load(A.voice)
dur = max(ev.get("duration", 0), len(voice) / SR)
rng = random.Random(A.seed if A.seed is not None else f"{A.episode}|{len(voice)}|{round(dur, 1)}")
N = int(dur * SR) + SR
voice = np.pad(voice, ((0, max(0, N - len(voice))), (0, 0)))[:N]
VL = level(voice)                                             # the reference: everything below is relative to the voice
VPK = float(np.percentile(np.abs(voice), 99.9)) + 1e-9
music = np.zeros((N, 2), np.float32); amb = np.zeros((N, 2), np.float32); sfx = np.zeros((N, 2), np.float32)
events = sorted(ev["events"], key=lambda e: e["t"])

# ---- ambience: continuous, crossfades at place changes (start 0.4 s early), level-matched ----
cuts = [(0.0, A.ambience)] + [(e["t"] - 0.4, e["ambience"]) for e in events if e.get("type") == "cut" and e.get("ambience")]
for i, (t0, role) in enumerate(cuts):
    t1 = cuts[i + 1][0] + 2.0 if i + 1 < len(cuts) else dur
    bed = pick(role)
    if bed is None or t1 - t0 < 3.2:
        continue
    seg = loop_to(to_level(hp(bed, 100), VL - A.amb_under), int((t1 - t0) * SR))
    f = int(1.5 * SR); seg[:f] *= np.linspace(0, 1, f)[:, None]; seg[-f:] *= np.linspace(1, 0, f)[:, None]
    place(amb, seg, t0)

# ---- music: a chain of different tracks of the mood, never one track looped ----
ledger = {"episodes": []}
if A.used_music and os.path.exists(A.used_music):
    ledger = json.load(open(A.used_music))
recent = {f for e in ledger["episodes"][-4:] if e.get("id") != A.episode for f in e.get("tracks", [])}
pool = cands(A.music)
fresh = [e for e in pool if e["file"] not in recent] or pool
rng.shuffle(fresh)
# a mood with few tracks borrows from its neighbours before anything repeats
NEAR = {"music_tension": ["music_investigative", "music_somber"], "music_investigative": ["music_tension", "music_documentary"],
        "music_documentary": ["music_investigative", "music_calm"], "music_somber": ["music_calm", "music_tension"],
        "music_calm": ["music_documentary", "music_somber"], "music_drive": ["music_tension", "music_documentary"]}
extra = [e for r_ in NEAR.get(A.music, []) for e in LIB if e["role"] == r_ and e["file"] not in recent]
rng.shuffle(extra)
order = fresh + extra + [e for e in pool if e not in fresh]
tracks_used = []
if order:
    chain = None; k = 0
    while chain is None or len(chain) < N:
        e = order[k % len(order)]; k += 1
        x = to_level(load(os.path.join(A.library, e["file"])), VL - A.music_open)
        if chain is None and A.beat_align:
            mono = np.abs(x).mean(1); hopn = SR // 100
            env = mono[: len(mono) // hopn * hopn].reshape(-1, hopn).mean(1)
            onset = np.clip(np.diff(env, prepend=env[0]), 0, None); onset /= onset.max() + 1e-9
            targets = [q["t"] for q in events if q.get("type") in ("reveal", "chapter") and q["t"] * 100 < len(onset) - 3000]
            best, best_sc = 0, -1.0
            for off in range(0, min(3000, max(1, len(onset) // 3)), 5):
                sc = sum(onset[max(0, int(t * 100 + off) - 10): int(t * 100 + off) + 10].max(initial=0) for t in targets)
                if sc > best_sc:
                    best, best_sc = off, sc
            x = x[best * hopn:]                                   # trim the head, no wrap-around seam
            print(f"beat-align: first track starts {best / 100:.2f}s in, score {best_sc:.2f}/{len(targets)}")
        used.append(e); tracks_used.append(e["file"])
        chain = x if chain is None else xjoin(chain, x, 3.0)
    music = chain[:N].copy()
    f = int(2 * SR); music[:f] *= np.linspace(0, 1, f)[:, None]; music[-int(3 * SR):] *= np.linspace(1, 0, int(3 * SR))[:, None]

# ---- event sounds: levels relative to the voice peaks ----
pre_silence = []
for e in events:
    t, typ, s = e["t"], e.get("type"), float(e.get("strength", 0.7))
    if typ == "chapter":
        w = pick("whoosh")
        if w is not None:
            w = vary(to_peak(w, 0)); pk = int(np.argmax(np.abs(w).mean(1)))
            place(sfx, w * VPK * db(-9 + 4 * s), t - pk / SR)        # the PEAK of the whoosh lands on the transition
    elif typ == "reveal":
        r = pick("riser"); im = pick("impact")
        if r is not None:
            r = to_peak(r[-int(6 * SR):], 0)                          # keep the END of a riser — that is where it climaxes
            f = min(len(r), int(0.4 * SR)); r[:f] *= np.linspace(0, 1, f)[:, None]
            place(sfx, r * VPK * db(-11), t - 0.3 - len(r) / SR)
        pre_silence.append((t - 0.3, t))
        if im is not None:
            place(sfx, vary(to_peak(im, 0), 0.03) * VPK * db(-1 + 2 * s), t)   # the loudest sound of the section
    elif typ in ("number", "doc", "stamp", "photo", "glitch", "hit"):
        role = {"number": "hit_small", "doc": "paper", "stamp": "stamp", "photo": "camera", "glitch": "glitch", "hit": "hit_small"}[typ]
        c = pick(role)
        if c is not None:
            place(sfx, vary(to_peak(c, 0)) * VPK * db(-11 + 4 * s), t)

# one shared room: short early-reflection reverb on the SFX bus
ir_len = int(0.35 * SR); ir = np.zeros(ir_len, np.float32); ir[0] = 1
for d, g in ((0.011, .35), (0.019, .28), (0.031, .2), (0.047, .14), (0.071, .09), (0.11, .05)):
    ir[int(d * SR)] += g
sfx = np.stack([fftconvolve(sfx[:, c], ir)[:N] for c in range(2)], 1).astype(np.float32)

# ---- ducking: music drops to --music-under while the voice speaks; near-silence before reveals ----
win = int(0.3 * SR)
venv = mavg(np.abs(voice).mean(1), win)
vgate = np.clip(venv / (np.percentile(venv[venv > 0], 60) + 1e-9), 0, 1) if venv.any() else np.zeros(N)
# hold the duck through short pauses (0.8 s) so the bed does not pump between sentences
hold = int(0.8 * SR)
vgate = np.clip(mavg((vgate > 0.25).astype(np.float32), hold) * 2.0, 0, 1)
senv = mavg(np.abs(sfx).mean(1), win)
sgate = np.clip(senv / (senv.max() * 0.3 + 1e-9), 0, 1)
duck = max(0.0, A.music_under - A.music_open)
gain = db(-duck * vgate - 4 * sgate)
for a, b in pre_silence:
    i0, i1 = int(max(0, a - 0.15) * SR), int(b * SR)
    gain[i0:i1] *= db(-14); amb[i0:i1] *= db(-8)
music *= gain[:, None]

stems = {"voice": voice, "music": music, "ambience": amb, "sfx": sfx}
for k, v in stems.items():
    sf.write(os.path.join(A.out, "stems", f"{k}.wav"), v, SR)
mix = voice + music + amb + sfx
mix /= max(1.0, float(np.abs(mix).max()) / 0.95)
raw = os.path.join(A.out, "_mix_raw.wav"); sf.write(raw, mix.astype(np.float32), SR)

# two-pass loudness to −14 LUFS / −1 dBTP (linear gain: keeps the dynamics we built)
m = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", raw, "-af", "loudnorm=I=-14:TP=-1:LRA=11:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True).stderr
js = json.loads(m[m.rindex("{"): m.rindex("}") + 1])
af = (f"loudnorm=I=-14:TP=-1:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:"
      f"measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
out = os.path.join(A.out, "mix.wav")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", raw, "-af", af, "-ar", str(SR), out], check=True)
os.remove(raw)

# ---- QA without ears ----
qa = {}
r = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
tail = r[r.rfind("Summary:"):]
qa["ebur128"] = " ".join(tail.split())[:300]
r = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", out, "-af", "silencedetect=n=-50dB:d=1.0", "-f", "null", "-"], capture_output=True, text=True).stderr
qa["silences_over_1s"] = r.count("silence_start")
y, _ = sf.read(out, dtype="float32")
qa["clipped_samples"] = int((np.abs(y) > 0.999).sum())
sp = vgate > 0.9
if sp.any() and music.any():
    ms = music[sp]; qa["music_under_voice_db"] = round(float(VL - 20 * np.log10(np.sqrt(np.mean(ms ** 2)) + 1e-9)), 1)
    if qa["music_under_voice_db"] < 13:
        qa["warning"] = "music is less than 13 dB under the voice — it will fight the narration on a phone"
qa["music_tracks"] = tracks_used
hits = []
for e in events:
    if e.get("type") in ("reveal", "number", "chapter"):
        i = int(e["t"] * SR); seg = np.abs(sfx[max(0, i - SR // 10): i + SR // 5]).mean(1)
        hits.append(round(float(seg.max()) if len(seg) else 0, 3))
qa["event_peaks_min"] = min(hits) if hits else None
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-filter_complex", "showwavespic=s=1800x240:split_channels=0", "-frames:v", "1", os.path.join(A.out, "wave.png")])
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-lavfi", "showspectrumpic=s=1800x400:legend=0", os.path.join(A.out, "spectrum.png")])
json.dump(qa, open(os.path.join(A.out, "sound_qa.json"), "w"), indent=1)
if A.used_music:
    ledger["episodes"] = [e for e in ledger["episodes"] if e.get("id") != A.episode][-11:] + [{"id": A.episode, "tracks": tracks_used}]
    json.dump(ledger, open(A.used_music, "w"), indent=1)
with open(os.path.join(A.out, "credits.txt"), "w") as f:
    seen = set()
    for e in used:
        if e["license"] == "by" and e["id"] not in seen:
            seen.add(e["id"]); f.write(f"\"{e['title']}\" by {e['creator']} — CC BY — {e['source']}\n")
print(json.dumps(qa, ensure_ascii=False))
