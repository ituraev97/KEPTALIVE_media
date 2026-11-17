import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "120 feet under enemy waters, no doctor aboard")]
names = {"THE BOAT THAT SURVIVED": "Cavite, 1941: the boat that survived", "\"HEY DOC\"": "\"Hey Doc\": a 19-year-old falls sick",
         "THE ORDER": "The captain's order", "THE KIT": "The kit: 5 spoons and a tea strainer", "THE CLOCK": "The clock: 10:46 to 13:22",
         "STILL PITCHING": "\"Still in there pitching\"", "THE STORY": "The Pulitzer story", "TWICE MORE": "Grayback and Silversides: twice more",
         "A DEPARTMENT OF ONE": "Today: the independent duty corpsman", "AFTERWARDS": "Afterwards"}
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            chap.append((S[i], names.get(s[2]["t"], s[2]["t"].title())))
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""WWII submarine surgery with no doctor aboard: on September 11, 1942, the submarine USS Seadragon dived to 120 feet in enemy waters so that Pharmacist's Mate Wheeler Lipes, 23, could remove a shipmate's appendix on the wardroom table — with 5 bent tablespoons as retractors and a tea strainer as the ether mask.

The true story from the Navy's own records: the captain's order, the clock from 10:46 to 13:22, the Pulitzer Prize-winning newspaper story, two more submarine appendectomies before the year was out (Grayback and Silversides), and the Navy job it helped create — the independent duty corpsman. 1945 U.S. Navy archival film (not Seadragon) and 2026 U.S. Navy footage; history and public facts only.

Chapters:
{chapters}

Sources:
Naval History and Heritage Command, PhM1/c Wheeler B. Lipes and a Submerged Appendectomy: https://history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/world-war-ii-profiles/submerged-appendectomy.html
Navy Department Library, Submarine Squadron Two report to the Bureau of Medicine and Surgery (Oct. 22, 1942): https://history.navy.mil/research/library/oral-histories/wwii/oral-history-appendectomy-performed-on-fourth-war-patrol-of-ussseadragon-1942/submarine-squadron-two-report-appendectomy.html
Navy Department Library, Oral history: appendectomy on the fourth war patrol of USS Seadragon: https://history.navy.mil/research/library/oral-histories/wwii/oral-history-appendectomy-performed-on-fourth-war-patrol-of-ussseadragon-1942.html
NHHC, DANFS Seadragon (SS-194): https://history.navy.mil/research/histories/ship-histories/danfs/s/seadragon-i.html
NHHC, DANFS Grayback (SS-208): https://history.navy.mil/research/histories/ship-histories/danfs/g/grayback-i.html
NHHC, DANFS Silversides (SS-236): https://www.history.navy.mil/research/histories/ship-histories/danfs/s/silversides-i.html
BUMED via DVIDS, A brief history of the U.S. Navy Independent Duty Corpsman (2014): https://www.dvidshub.net/news/printable/149637
Navy Medicine, An undersea medical officer's tale from the Silent Service (2024): https://www.med.navy.mil/Media/News/Article/3811813/an-undersea-medical-officers-tale-from-the-silent-service/
Navy Medicine, Independent Duty Corpsman: A Department of One (2023): https://www.med.navy.mil/Media/News/Article/3332617/independent-duty-corpsman-a-department-of-one/
NIDDK (NIH), Definition & Facts for Appendicitis: https://www.niddk.nih.gov/health-information/digestive-diseases/appendicitis/definition-facts
NPR, Navy Hero to Earn Medal for 1942 Surgery at Sea (2005): https://www.npr.org/2005/02/19/4503760/navy-hero-to-earn-medal-for-1942-surgery-at-sea
The Pulitzer Prizes, George Weller of Chicago Daily News: https://www.pulitzer.org/winners/george-weller
WW2 on Deadline, Surgery under the sea: George Weller's Pulitzer-winning thriller: https://ww2ondeadline.substack.com/p/george-weller-correspondent-pulitzer-prize
Wikipedia, Wheeler Bryson Lipes: https://en.wikipedia.org/wiki/Wheeler_Bryson_Lipes

Archival film (public domain): U.S. Navy, Naval Photographic Center, 1945 — "Silent Service" (MN-9141) and supplements (NPC-3844), USS Skate film (NPC-15523), National Archives via Internet Archive. Shown as 1945 film, not USS Seadragon.
Footage via DVIDS (published Sept. 29 – Nov. 16, 2026): MC2 Nicholas A. Russell, U.S. Navy (USS Colorado, Pearl Harbor, Sept. 23); Joel Messer and Jordon Johnson, U.S. Navy (USS Washington undocking, Portsmouth Naval Shipyard, Oct. 27); PO3 Reef Rogers, U.S. Navy (USS Spruance returns to San Diego, Nov. 13); LCpl Nathan Saucier, USMC (U.S. Naval Hospital Okinawa drill, Oct. 26 — TRAINING); LCpl Tyler Bassett, USMC (Iwakuni medical drill, Oct. 23 — TRAINING).
U.S. government visual information is in the public domain; appearance of U.S. government visual information does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Navy, the U.S. Department of Defense, NIH or any government agency.

#ww2 #submarine #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
