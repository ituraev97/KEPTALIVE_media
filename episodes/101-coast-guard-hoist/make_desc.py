import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "A boat on fire, 50 miles out")]
names = {"FOUR SICK MARINERS": "4 sick mariners on an oil tanker", "PLASMA IN A STORM": "1944: plasma in a storm, the first helicopter lifesaving flight",
         "THE CLOCK": "The clock: range, fuel and distance", "37 DEGREES": "1983: the Marine Electric and the missing rescue swimmer",
         "DOWN THE WIRE": "Down the wire: a cruise ship medevac", "FIFTY MILES OUT": "The burning boat: 4 of 4 rescued", "ORDINARY WEEKS": "One autumn of hoists"}
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            chap.append((S[i], names.get(s[2]["t"], s[2]["t"].title())))
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""Coast Guard rescue at sea, told through real medevacs from this autumn: a 90-foot fishing boat on fire 50 miles off Alabama with 4 people aboard, 4 sick mariners hoisted off an oil tanker near Puerto Rico, and a cruise ship passenger lifted by helicopter hoist off North Carolina. When there is no ambulance at sea, the U.S. Coast Guard sends a helicopter crew down a cable.

Plus the history behind the hoist: the 1944 wartime flight that carried blood plasma through a storm after the destroyer USS Turner exploded, the 1945 rescue widely regarded as the first helicopter hoist rescue over water, and the 1983 Marine Electric sinking that gave the Coast Guard its rescue swimmers. Real U.S. Coast Guard footage; history and public facts only.

Chapters:
{chapters}

Sources:
U.S. Coast Guard releases via DVIDS (asset descriptions): videos 1026608, 1029245, 1028902, 1023702, 1024523, 1028385, 1025010, 1029116, 1028766, 1025953, 1028863 — https://www.dvidshub.net
Maritime Executive, USCG medevacs four tanker crewmembers with food poisoning (Nov. 9, 2026): https://maritime-executive.com/article/uscg-medevacs-four-tanker-crewmembers-with-food-poisoning
Marine Insight, Coast Guard airlifts four tanker crew (Nov. 10, 2026): https://www.marineinsight.com/coast-guard-airlifts-four-tanker-crew-suspected-food-poisoning-vieques/
WECT, Coast Guard aircrew airlifts passenger from cruise ship (Nov. 5, 2026): https://www.wect.com/2026/11/05/coast-guard-aircrew-airlifts-passenger-cruise-ship-off-north-carolina-coast/
Cruise Hive, Norwegian Bliss passenger airlift (Nov. 5, 2026): https://www.cruisehive.com/coast-guard-airlifts-norwegian-bliss-passenger-off-north-carolina
WKRG via Yahoo News, Four people rescued from burning boat (Oct. 15, 2026): https://www.yahoo.com/news/weather-news/articles/four-people-rescued-burning-boat-200049462.html
Blue RAM Media (Oct. 19, 2026): https://bluerammedia.com/four-people-rescued-from-burning-boat-off-dauphin-island-coast/
U.S. Coast Guard, MH-60T fact sheet: https://www.dcms.uscg.mil/Portals/10/CG-9/Acquisition%20PDFs/Factsheets/MH-60T.pdf
U.S. Coast Guard, HC-144 fact sheet (2025): https://dcms.uscg.mil/Portals/10/HC-144-Fact-Sheet-Updated%2014%20Jan%202025.pdf
Naval Air Training Command, Coast Guard community brief: https://www.cnatra.navy.mil/tw5/ht18/assets/docs/university/cg-community-brief.pdf
Naval History and Heritage Command, Frank Erickson: https://history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/world-war-ii-profiles/vignette--frank-erickson.html
U.S. Coast Guard Historian's Office, The Long Blue Line: Frank Erickson: https://www.history.uscg.mil/Research/THE-LONG-BLUE-LINE/Article/2931772/
Lockheed Martin, The Rescue That Changed Search and Rescue Forever (2026): https://lockheedmartin.com/en-us/news/features/2026/the-rescue-that-changed-search-and-rescue-forever.html
U.S. Coast Guard, The shipwreck that changed the Coast Guard forever (2025): https://www.mycg.uscg.mil/News/Article/4160041/the-shipwreck-that-changed-the-coast-guard-forever/
Seapower, Rescue swimmer program starts after tragedy at sea: https://seapowermagazine.org/rescue-swimmer-program-starts-after-tragedy-at-sea/

Footage via DVIDS (U.S. Coast Guard, published Sept. 20 – Nov. 9, 2026): PO3 Tasha Smith, USCG Heartland (fishing vessel fire, Oct. 13); Ricardo Castrodad, PADET San Juan (tanker Daibelli, Nov. 8; long-range medevac east of St. Maarten, Sept. 19); PO2 Matthew Thieme, USCG East (Norwegian Bliss, Nov. 2); Air Station Borinquen (Allure of the Seas, Sept. 24); USCG Southwest (container ship off San Francisco, Oct. 31); PO3 Nathan Bishop, Air Station Sitka (Alaska, Sept. 28); PO3 Dillon Grimsley, USCG Great Lakes (Lake Michigan, Nov. 7); USCG Southeast (South Carolina, Nov. 4); PO3 Jessica Walker, USCG Southeast (rescue swimmer hoist near Mona Island, Nov. 5 — TRAINING).
Archival film (public domain): U.S. Navy, Naval Photographic Center film 3017, Sikorsky HO3S-1 helicopter, 1947 (National Archives 76656, via Internet Archive) — shown as 1947 film, not the 1944 flight.
U.S. government visual information is in the public domain; appearance of U.S. government visual information does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Coast Guard, the U.S. Department of Defense, the Department of Homeland Security or any government agency.

#coastguard #rescue #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
