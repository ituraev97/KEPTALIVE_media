import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json"))
S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "The golden hour")]
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            chap.append((S[i], s[2]["t"].capitalize()))
# YouTube: first 0:00, each >= 10 s
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
out[0] = (0, "Cold open: a Dustoff crew in training")
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""What is the "golden hour" in trauma care, and how do military medevac crews race it? We follow Army Dustoff, National Guard and Air Force crews in training, from the 9-line radio call to the hoist, and look at where the idea came from: R Adams Cowley's "golden hour", helicopter evacuation in Korea and Vietnam, the Pentagon's 2009 60-minute rule for Afghanistan, and what the research does and doesn't show.

Chapters:
{chapters}

Sources:
Kotwal RS et al., "The Effect of a Golden Hour Policy on the Morbidity and Mortality of Combat Casualties," JAMA Surgery (online Sept. 30, 2015) — via JAMA Network release: https://sciencedaily.com/releases/2015/09/150930140123.htm
HealthDay, U.S. combat deaths declined under 'Golden Hour Policy': https://www.healthday.com/health-news/general-health/u-s-combat-deaths-declined-under-golden-hour-policy-study-703685.html
Newgard CD et al., Ann Emerg Med 2010;55:235-246 — via JEMS: https://www.jems.com/ems-training/ems-intervals-associated-morta/
EMS1, How the "death lab" evolved into a modern trauma system: https://www.ems1.com/trauma/articles/how-the-death-lab-evolved-into-a-modern-trauma-system-L5PhfJiEE93gKwPQ/
U.S. Army, Army helicopters in Korea, 1950 to '53: https://www.army.mil/article/177302/army_helicopters_in_korea_1950_to_53
U.S. Army, evolution of Army Aviation's MedEvac mission: https://www.army.mil/article/197320
U.S. Army, 7ATC's Safety Focus: 9-Line Medevac: https://www.army.mil/article/189003/7atcs_safety_focus_9_line_medevac
Texas Tech Vietnam Center, Dustoff exhibit: https://www.vietnam.ttu.edu/exhibits/dustoff/beginning.php and https://www.vietnam.ttu.edu/exhibits/dustoff/mystique.php
Army Technology, HH-60M MEDEVAC Black Hawk: https://www.army-technology.com/projects/sikorsky-hh-60m-medevac-black-hawk-helicopter/
DARPA, The Live Chain (DVIDS): https://www.dvidshub.net/video/993660

Footage (DVIDS, public domain): U.S. Army videos by Sgt. Vincent Levelev, 82nd Combat Aviation Brigade (training); Alejandro Pena, Alaska National Guard (training); Elizabeth Hackbarth, 305th Mobile Public Affairs Detachment (training); Spc. Janean Carr, 101st Airborne Division (training); Pfc. David Connors, Rhode Island National Guard (training); Pfc. Yunseong Jang, 8th Army (training); Staff Sgt. Uriah Clites, 109th MPAD (training); Staff Sgt. Josiah Meece, 165th Airlift Wing (training); Sgt. Olivia Cowart, 25th Combat Aviation Brigade (training); Jorge Gomez, Irwin Army Community Hospital (interview); Katie Lange, Defense Media Activity (includes Vietnam-era archival footage). U.S. government visual information is in the public domain; its appearance does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, NIH, CDC or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(desc[:1500]); print(len(desc), "chars")
