#!/usr/bin/env python3
"""Doc Cinema — ONE final encode for upload: optional film finish + 1440p master + size cap.

usage: deliver.py IN.mp4 OUT.mp4 [--height 1440] [--finish] [--grain 3] [--vignette 0.15] [--max-mb 440] [--crf 18] [--preset fast]

Why (measured 2026-11-29 on our published videos): a 1080p upload is served by YouTube at 0.7–1.3 Mbit/s, a 1440p upload
of the same picture at ~4 Mbit/s (VP9/AV1 ladder) — the 1440p master is what makes text and footage look sharp on a phone
and a TV. This replaces `look.py finish` + a separate re-encode (two encodes = softer picture and an extra hour of CPU).
Horizontal video → 2560x1440; vertical (Shorts) is left at 1080x1920. Audio is copied if it is AAC, else encoded at 256k.
--max-mb caps the file (Drive relay limit is 450 MB): bitrate ceiling = size / duration.
"""
import argparse, json, subprocess, sys

p = argparse.ArgumentParser(); p.add_argument("inp"); p.add_argument("out")
p.add_argument("--height", type=int, default=1440); p.add_argument("--finish", action="store_true")
p.add_argument("--grain", type=float, default=3); p.add_argument("--vignette", type=float, default=0.15)
p.add_argument("--max-mb", type=float, default=440); p.add_argument("--crf", type=int, default=18); p.add_argument("--preset", default="fast")
a = p.parse_args()
pr = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height",
                                         "-of", "json", a.inp]))
v = next(s for s in pr["streams"] if s["codec_type"] == "video"); au = [s for s in pr["streams"] if s["codec_type"] == "audio"]
dur = float(pr["format"]["duration"]); W, H = v["width"], v["height"]
vf = []
if a.finish:
    vf += ["eq=contrast=1.05:saturation=1.04:gamma=0.99", f"vignette=angle={0.35 + a.vignette * 2:.3f}:mode=forward:eval=init"]
if W > H and H < a.height:
    vf.append(f"scale={int(a.height * 16 / 9 // 2 * 2)}:{a.height}:flags=lanczos+accurate_rnd")
    vf.append("unsharp=5:5:0.35:5:5:0.0")          # light sharpen after the upscale (luma only)
if a.finish and a.grain > 0:
    vf.append(f"noise=alls={a.grain}:allf=t+u")     # grain LAST, at the delivery size, so it stays fine
vf.append("format=yuv420p")
kbps = int(a.max_mb * 8192 / dur) - (256 if au else 0)
cmd = ["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", a.inp, "-vf", ",".join(vf), "-c:v", "libx264", "-preset", a.preset, "-crf", str(a.crf),
       "-maxrate", f"{kbps}k", "-bufsize", f"{kbps * 2}k", "-g", "60", "-bf", "2", "-movflags", "+faststart",
       "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709"]
cmd += (["-c:a", "copy"] if au and au[0]["codec_name"] == "aac" else ["-c:a", "aac", "-b:a", "256k"]) if au else ["-an"]
r = subprocess.run(cmd + [a.out], capture_output=True, text=True)
if r.returncode:
    sys.exit(r.stderr[-800:])
o = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=width,height", "-of", "json", a.out]))
ov = next(s for s in o["streams"] if "width" in s)
print(json.dumps({"out": a.out, "size": f"{ov['width']}x{ov['height']}", "mb": round(int(o["format"]["size"]) / 1048576, 1),
                  "seconds": round(float(o["format"]["duration"]), 1), "ok": abs(float(o["format"]["duration"]) - dur) < 1}))
