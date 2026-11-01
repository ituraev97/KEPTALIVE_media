"""KEPT ALIVE voice: Kokoro am_fenrir + processing (owner's choice 02.11.2026, sample "B fenrir").
Pitch down 4% (duration kept), warm low end, cut boxiness, presence, gentle compression, short room echo."""
import subprocess, tempfile, os, numpy as np, soundfile as sf
VOICE = "am_fenrir"
CHAIN = ("asetrate={sr96},aresample={sr},atempo=1.0417,highpass=f=60,equalizer=f=120:t=q:w=1:g=3,"
         "equalizer=f=380:t=q:w=1.2:g=-2.5,equalizer=f=3000:t=q:w=1.4:g=2,equalizer=f=7500:t=q:w=1:g=-2,"
         "acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2,aecho=0.85:0.5:28|51:0.1|0.06")
def process(a, sr):
    with tempfile.TemporaryDirectory() as d:
        i, o = os.path.join(d, "i.wav"), os.path.join(d, "o.wav")
        sf.write(i, np.asarray(a, dtype=np.float32), sr)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", i, "-af", CHAIN.format(sr96=int(sr * 0.96), sr=sr), "-ar", str(sr), o], check=True)
        b, _ = sf.read(o, dtype="float32")
    return b
