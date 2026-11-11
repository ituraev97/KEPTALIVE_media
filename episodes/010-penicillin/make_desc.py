import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "Cold open: how was penicillin discovered?")]
names = {"THE WOUNDS": "World War I: infected wounds", "THE DISH": "1928: Fleming's contaminated dish", "THE TEAM": "Oxford: Florey, Chain and Heatley",
         "THE CANTALOUPE": "Peoria: the moldy cantaloupe and mass production", "D-DAY": "D-Day: 2.3 million doses", "THE WARNING": "Fleming's warning and antibiotic resistance"}
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            chap.append((S[i], names.get(s[2]["t"], s[2]["t"].title())))
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""How was penicillin discovered? By accident: in September 1928, Alexander Fleming returned to his London lab and found a mold that stopped bacteria from growing. This penicillin history documentary follows the first antibiotic to be mass-produced from Fleming's dish to Howard Florey, Ernst Chain and Norman Heatley in Oxford, the moldy cantaloupe of Peoria, Illinois, and the 2.3 million doses ready before D-Day.

Then: how penicillin works (it breaks the bacterial cell wall), Fleming's 1945 Nobel lecture warning about resistance, and what the CDC and WHO say about antibiotic resistance today, ahead of World AMR Awareness Week (Nov. 18–24, 2026). History and public-health facts only.

Chapters:
{chapters}

Sources:
American Association of Immunologists, Alexander Fleming: https://www.aai.org/About/History/Notable-Members/Nobel-Laureates/AlexanderFleming
PBS NewsHour, The real story behind the world's first antibiotic: https://pbs.org/newshour/health/the-real-story-behind-the-worlds-first-antibiotic
National WWII Museum, Penicillin fact sheet: https://www.nationalww2museum.org/sites/default/files/2017-07/penicillin-fact-sheet.pdf
Science History Institute, Howard Florey and Ernst Chain: https://www.sciencehistory.org/education/scientific-biographies/howard-walter-florey-and-ernst-boris-chain
University of Oxford, 75 years of penicillin in people: https://ox.ac.uk/node/213547
Smithsonian Magazine, the "penicillin girls": https://www.smithsonianmag.com/smithsonian-institution/pencillin-girls-made-one-worlds-most-life-saving-discoveries-possible-180985449/
USDA ARS, Penicillin: opening the era of antibiotics: https://www.ars.usda.gov/midwest-area/peoria-il/national-center-for-agricultural-utilization-research/docs/penicillin-opening-the-era-of-antibiotics/
USDA ARS, The enduring mystery of "Moldy Mary": https://scientificdiscoveries.ars.usda.gov/tellus/stories/articles/enduring-mystery-moldy-mary
UW–Madison CALS, D-Day and the penicillin project: https://news.cals.wisc.edu/2017/06/05/d-day-invasion-was-bolstered-by-uw-madison-penicillin-project
American Chemical Society (via EurekAlert), Pfizer deep-tank fermentation landmark: https://www.eurekalert.org/news-releases/491868
Nobel Prize, Fleming's Nobel Lecture (Dec. 11, 1945): https://www.nobelprize.org/prizes/medicine/1945/fleming/lecture/
Live Science, the threat of superbugs was known from the first antibiotic: https://www.livescience.com/health/viruses-infections-disease/how-could-it-have-been-allowed-to-happen-the-threat-of-superbugs-was-known-from-the-first-antibiotic-but-weve-failed-to-stop-it
Abraham & Chain, Nature 146:837 (1940): https://www.nature.com/articles/146837a0
StatPearls, Penicillin: https://statpearls.com/point-of-care/26891
CDC, Antimicrobial resistance facts and stats: https://www.cdc.gov/antimicrobial-resistance/data-research/facts-stats/index.html
UN News, WHO report on antibiotic resistance (Oct. 2025): https://news.un.org/en/story/2025/10/1166087
WHO, World AMR Awareness Week 2026: https://www.who.int/campaigns/world-amr-awareness-week/world-amr-awareness-week-2026

Archival film (public domain, National Archives via Internet Archive): United News newsreels "Penicillin Drug Saves Allied Lives" (1944, 208-UN-113) and "Penicillin and Plasma Save Lives" (1944, 208-UN-1008) — plants and locations not identified; U.S. Coast Guard film "Embarkation: Normandy Invasion of Europe" (1944, Naval Photographic Center 10769); U.S. Navy film of landing craft and the landing in France, June 5–6, 1944 (NPC 4360); U.S. Army film "2d Hospital Set Up, Normandy, France" (July 28, 1944).

Footage via DVIDS: Walter Reed Army Institute of Research videos by Tyra Breaux (Multidrug-Resistant Organism Repository and Surveillance Network; Experimental Therapeutics, 2023); U.S. Navy video by MC3 Mariterese Merrique, Naval Medical Center San Diego (Microbiology Laboratory, 2021). U.S. government visual information is in the public domain; appearance of U.S. government visual information does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, NIH, CDC, WHO, USDA or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
