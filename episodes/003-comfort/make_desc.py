import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "Cold open: New York, 2020")]
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            t = s[2]["t"]; chap.append((S[i], t.title().replace("'S", "'s")))
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""How do you build a hospital that can sail anywhere, and switch it on in five days? USNS Comfort is a converted supertanker with a 1,000-bed hospital, 12 operating rooms and its own oxygen plants. We follow it from the Gulf War and 9/11 to the Haiti earthquake, Hurricane Maria, its month in New York in 2020, and the 79-day Continuing Promise 2025 mission that treated 12,616 patients in six countries.

Chapters:
{chapters}

Sources:
U.S. Navy Fact File, Hospital Ships (T-AH): https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2232638/hospital-ships-t-ah/
USNS Comfort Fact Sheet (U.S. Navy, archived): https://webarchive.library.unt.edu/web/20170118222511/http://www.med.navy.mil/sites/usnscomfort/Documents/USNSComfortFactSheet%5B1%5D.pdf
USNS Comfort Fact Sheet, Operation Unified Response (archived): https://webarchive.library.unt.edu/web/20130215151515/http://bogota.usembassy.gov/root/pdfs/factsheet-operationunifiedresponse-usnscomfort.pdf
U.S. Navy, USNS Comfort departs NYC (2020): https://www.navy.mil/Press-Office/News-Stories/Article/2283797/usns-comfort-departs-nyc-prepared-for-future-tasking-military-relief-efforts-co/
U.S. Navy, USNS Comfort completes hurricane relief mission in Puerto Rico (2017): https://www.navy.mil/Press-Office/News-Stories/Article/2253626/usns-comfort-completes-hurricane-relief-mission-in-puerto-rico/
U.S. Navy, USNS Comfort returns home after Continuing Promise 2025: https://www.navy.mil/Press-Office/News-Stories/display-news/Article/4277657/usns-comfort-returns-home-after-continuing-promise-2025/
U.S. Navy, USNS Comfort departs Grenada during Continuing Promise 2025: https://www.navy.mil/Press-Office/News-Stories/display-news/Article/4225308/usns-comfort-departs-grenada-during-continuing-promise-2025/
DVIDS, USNS Comfort departs Colón, Panama (2025): https://www.dvidshub.net/news/502070/usns-comfort-departs-colon-panama
A. Sobocinski (BUMED historian), Remembering USS Relief (AH-1): https://usnhistory.navylive.dodlive.mil/Recent/Article-View/Article/2686718/remembering-uss-relief-ah-1-the-navys-floating-fortress-of-health

Footage (all via DVIDS, no training footage): U.S. Navy video by MC1 Scott Bigley (New York arrival and departure, 2020), MC1 Jason Pastrick (loading at Norfolk, 2020), MC1 Joshua Sheppard (departing Norfolk, 2020), MC2 Joshua M. Tolbert (return to Norfolk, 2020), MC2 Jonas Womack (supply offload, Dominican Republic, 2025), MC2 Deven Fernandez (medical site set-up, Dominican Republic, 2025), MC2 Rylin Paul (medical site, Costa Rica, 2025), javan r johnson / Fleet Public Affairs Center Norfolk (helicopters, Colombia, 2018); U.S. Army video by Staff Sgt. Richard Colletta (San Juan, Puerto Rico, 2017), Spc. Ethan McCubbins (flight operations, 2025), Cpl./Sgt. William Hunter (surgery aboard, Colón, Panama, and hospital tour, Trinidad, 2025 — wide shots only); U.S. Air Force video by Senior Airman Christopher Bermudez (Miami, 2025). U.S. government visual information is in the public domain; its appearance does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, the U.S. Navy, NIH, CDC or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
