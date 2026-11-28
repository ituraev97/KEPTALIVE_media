#!/usr/bin/env python3
"""Doc Cinema — ONE command before scheduling a long video (2026-11-29).

usage: finalize.py FINAL.mp4 --episode ID [--events events.json] [--ledger variety_ledger.json] [--out upload.mp4]
                   [--no-finish] [--vignette 0.15] [--grain 3] [--max-mb 440]
Does, in order:  deliver.py (film finish + 2560x1440 master, one encode)  →  critique.py  →  variety_check.py.
Prints one JSON line {"upload": ..., "verdict": "PASS"|"FAIL", "fails": [...], "warnings": [...]} and exits 1 on FAIL.
Schedule ONLY the file named in "upload", and only on PASS. On FAIL fix the edit and run again.
Shorts (vertical): pass --no-finish; they are checked, not upscaled.
"""
import argparse, json, os, subprocess, sys

H = os.path.dirname(os.path.abspath(__file__))
p = argparse.ArgumentParser(); p.add_argument("final"); p.add_argument("--episode", required=True)
p.add_argument("--events"); p.add_argument("--ledger", default="variety_ledger.json"); p.add_argument("--out")
p.add_argument("--no-finish", action="store_true"); p.add_argument("--vignette", default="0.15"); p.add_argument("--grain", default="3")
p.add_argument("--max-mb", default="440")
a = p.parse_args()
out = a.out or os.path.splitext(a.final)[0] + ".upload.mp4"
res = {"upload": out, "fails": [], "warnings": []}
cmd = [sys.executable, f"{H}/deliver.py", a.final, out, "--max-mb", a.max_mb, "--vignette", a.vignette, "--grain", a.grain]
r = subprocess.run(cmd + ([] if a.no_finish else ["--finish"]), capture_output=True, text=True)
if r.returncode:
    res["fails"].append("deliver failed: " + (r.stderr or r.stdout)[-300:])
else:
    res["deliver"] = json.loads(r.stdout.strip().splitlines()[-1])
    cj = out + ".critique.json"
    subprocess.run([sys.executable, f"{H}/critique.py", out, "--out", cj] + (["--events", a.events] if a.events else []), capture_output=True, text=True)
    if os.path.exists(cj):
        c = json.load(open(cj)); res["fails"] += c.get("fail", []); res["warnings"] += c.get("warn", [])
        res["frozen_share"] = c.get("frozen_share"); res["lra"] = c.get("lra"); res["lufs"] = c.get("lufs")
    else:
        res["fails"].append("critique did not run")
    v = subprocess.run([sys.executable, f"{H}/variety_check.py", out, "--ledger", a.ledger, "--episode", a.episode], capture_output=True, text=True)
    try:
        vj = json.loads(v.stdout.strip().splitlines()[-1]); res["fails"] += vj.get("fails", [])
        res["repeat_share"] = vj.get("repeat_share"); res["cross_share"] = vj.get("cross_share")
    except Exception:
        res["fails"].append("variety_check did not run: " + v.stderr[-200:])
res["verdict"] = "FAIL" if res["fails"] else "PASS"
print(json.dumps(res, ensure_ascii=False))
sys.exit(1 if res["fails"] else 0)
