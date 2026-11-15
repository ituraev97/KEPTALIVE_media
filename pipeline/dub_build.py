#!/usr/bin/env python3
"""Build a dubbed audio track for a KEPT ALIVE episode.
usage: dub_build.py <episode_dir> <lang> <out_dir>
Reads <out_dir>/script.txt (one translated line per original LINE), synthesizes each line with dub_tts.py,
fits it into its original timeline slot (speed up to 1.2), rebuilds the episode's score + SFX without the English
voice (same code as pipeline/finish.py), mixes at -14 LUFS, exports <out_dir>/<ep>_<lang>.mp3 of exact video length."""
import json, os, re, subprocess, sys, importlib.util, io, contextlib
import numpy as np, soundfile as sf
from scipy.signal import resample_poly
sys.path.insert(0, "/home/claude"); import dub_tts   # Projects doc claude/dub_tts.py saved as /home/claude/dub_tts.py
EP, LANG, OUT = map(os.path.abspath, sys.argv[1:4]); LANG = os.path.basename(sys.argv[2])
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
LINES = E.LINES
T = json.load(open(os.path.join(EP, "timing.json"))); S, V, TOTAL = T["starts"], T["vdur"], T["total"]
SR = 48000
lines = [l.strip() for l in open(os.path.join(OUT, "script.txt"), encoding="utf-8") if l.strip()]
assert len(lines) == len(LINES), f"{len(lines)} lines vs {len(LINES)} in episode"
os.makedirs(os.path.join(OUT, "lines"), exist_ok=True)
log = {"lang": LANG, "lines": [], "engine_fallback": False}

import hashlib
def synth(text, speed):
    key = hashlib.md5(f"{LANG}|{speed}|{text}".encode()).hexdigest()[:16]
    cf = os.path.join(OUT, "lines", key + ".wav")
    if os.path.exists(cf):
        a, _ = sf.read(cf, dtype="float32"); return a
    a = _synth(text, speed); sf.write(cf, a, SR); return a
def _synth(text, speed):
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        a, sr = dub_tts.run(LANG, text, None, speed)
    if "falling back" in err.getvalue(): log["engine_fallback"] = True; print(err.getvalue().strip(), file=sys.stderr)
    a = resample_poly(a, SR, sr) if sr != SR else a
    nz = np.where(np.abs(a) > 0.01)[0]
    return a[: nz[-1] + int(0.05 * SR)] if len(nz) else a

voice = np.zeros(int(TOTAL * SR) + SR, np.float32)
for i, txt in enumerate(lines):
    slot = (S[i + 1] if i + 1 < len(S) else TOTAL - 0.3) - S[i] - 0.12
    sp = 1.0; a = synth(txt, sp); d = len(a) / SR
    if d > slot:
        sp = min(1.2, round(d / slot * 1.03, 3)); a = synth(txt, sp); d = len(a) / SR
    over = round(d - slot, 2) if d > slot else 0
    log["lines"].append({"n": i + 1, "speed": sp, "dur": round(d, 2), "slot": round(slot, 2), "over": over})
    i0 = int(S[i] * SR); voice[i0:i0 + len(a)] += a[: len(voice) - i0]
    print(f"{LANG} {i+1:02d} speed {sp} dur {d:.1f}/{slot:.1f}" + (f"  OVER {over}" if over else ""), flush=True)

# light voice EQ like dub_tts FX (no loudnorm here; the mix is normalised)
sf.write(os.path.join(OUT, "voice_raw.wav"), voice, SR)
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", os.path.join(OUT, "voice_raw.wav"), "-af",
                "highpass=f=75,equalizer=f=140:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1.4:g=1.5,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2",
                os.path.join(OUT, "voice.wav")], check=True)
voice, _ = sf.read(os.path.join(OUT, "voice.wav"), dtype="float32")

# ---- score + SFX from finish.py (between the SCORE and VOICE + NAT markers), ducked under the dubbed voice ----
src = open("/home/claude/keptalive_media/pipeline/finish.py").read()
code = src[src.index("# ---------------- SCORE"): src.index("# ---------------- VOICE + NAT")]
from scipy.signal import butter, sosfilt, fftconvolve
g = dict(np=np, butter=butter, sosfilt=sosfilt, fftconvolve=fftconvolve, S=S, V=V, TOTAL=TOTAL, SR=SR, LINES=LINES, T=T)
exec(code, g)
music, fx, N = g["music"], g["fx"], g["N"]
vv = np.zeros(N, np.float32); vv[: min(N, len(voice))] = voice[:N]
venv = np.convolve(np.abs(vv), np.ones(int(.3 * SR)) / int(.3 * SR), mode="same")
music = music * (1 - 0.55 * np.clip(venv / (venv.max() * .12 + 1e-9), 0, 1))
sf.write(os.path.join(OUT, "music.wav"), (music / max(1e-9, np.abs(music).max()) * .5).astype(np.float32), SR)
sf.write(os.path.join(OUT, "fx.wav"), (fx / max(1e-9, np.abs(fx).max()) * .6).astype(np.float32), SR)
sf.write(os.path.join(OUT, "voice.wav"), (vv / max(1e-9, np.abs(vv).max()) * .9).astype(np.float32), SR)
name = f"{os.path.basename(EP).split('-')[0]}_{LANG}"
out = os.path.join(OUT, f"{name}.mp3")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", os.path.join(OUT, "voice.wav"), "-i", os.path.join(OUT, "music.wav"), "-i", os.path.join(OUT, "fx.wav"),
    "-filter_complex", "[0:a]aformat=channel_layouts=stereo[v];[1:a]aformat=channel_layouts=stereo,volume=0.42[m];[2:a]aformat=channel_layouts=stereo,volume=0.6[f];"
    "[v][m][f]amix=inputs=3:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11",
    "-t", f"{TOTAL:.3f}", "-ar", "48000", "-b:a", "192k", out], check=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], capture_output=True, text=True).stdout)
log.update(file=out, duration=round(dur, 3), video=round(TOTAL, 3), max_speed=max(l["speed"] for l in log["lines"]),
           overflows=[l for l in log["lines"] if l["over"]])
json.dump(log, open(os.path.join(OUT, "build_log.json"), "w"), indent=1)
print("DONE", out, dur, "max speed", log["max_speed"], "overflows", len(log["overflows"]), "fallback", log["engine_fallback"])
