import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//3600}:{x%3600//60:02d}:{x%60:02d}" if x >= 3600 else f"{x//60}:{x%60:02d}"
chap = [(0, "The 12-hour clock: wounded in 1918")]
names = {"OVER THERE": "Over there: medics among the first casualties", "WHAT HITS YOU": "What hit them: shells, gas, bullets",
         "TWO SAFETY PINS": "Two safety pins: the packet, the bearers, the aid station", "THE SPLINT": "The Thomas splint: an estimated 4 in 5 to 1 in 6",
         "THE ROAD BACK": "The road back: Model T ambulances and jammed roads", "TRIAGE": "Triage and shock", "BLOOD ON ICE": "Blood on ice: the first blood bank",
         "GAS": "Gas", "THE TABLE": "The table: surgery without antibiotics", "THE INVISIBLE WOUND": "The invisible wound: shell shock",
         "THE OTHER ENEMY": "The other enemy: the 1918 flu, and the nurses", "THE LONG WAY HOME": "The long way home"}
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter": chap.append((S[i], names.get(s[2]["t"], s[2]["t"].title())))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in chap)
desc = f"""What being wounded in WWI actually felt like for an American soldier in 1918 — step by step, from the moment a shell fragment hit him to the day he came home. World War 1 medicine without antibiotics: stretcher bearers, Model T ambulances, triage, the Thomas splint, the first blood bank, poison gas, the 12-hour clock, shell shock and the 1918 flu.

WAR MEDICINE · EP 1. Told from the U.S. Army's own medical records, with U.S. Army Signal Corps films from 1917–1919 (National Archives) and Army photographs. No wounds on screen; history only.

Chapters:
{chapters}

Sources:
Army Medical Department (AMEDD), Medical Operations (ch. 4): https://medcoeckapwstorprd01.blob.core.usgovcloudapi.net/achh/chapter4_9849.pdf
AMEDD, Army Nurse Corps history, ch. 3 and ch. 4: https://medcoeckapwstorprd01.blob.core.usgovcloudapi.net/pfw-images/dbimages/ATC%20ch%204%20pt%201.pdf
Univ. of Kansas Medical Center, WWI military medical operations essays: https://www.kumc.edu/school-of-medicine/academics/departments/history-and-philosophy-of-medicine/archives/wwi.html
C. E. Heller, Chemical Warfare in World War I (Leavenworth Paper 10, 1984): https://apps.dtic.mil/sti/tr/pdf/ADA189331.pdf
Congressional Research Service, RL32492: https://www.everycrsreport.com/reports/RL32492.html
National Park Service, The U.S. and the First World War: https://www.nps.gov/wwim/wwioverview.htm
Library of Congress, Meuse-Argonne: https://www.loc.gov/exhibitions/world-war-i-american-experiences/about-this-exhibition/over-there/meuse-argonne/
ABMC, Caring for the Sick and Wounded: https://abmc.gov/news-events/news/caring-sick-and-wounded-establishing-first-us-army-medical-units-france-and-england
Byerly, Public Health Reports 2010: https://pmc.ncbi.nlm.nih.gov/articles/PMC2862337
National Guard, Flu killed 45,000 U.S. soldiers: https://www.nationalguard.mil/News/Article-View/Article/1616713/flu-outbreak-killed-45000-us-soldiers-during-world-war-i
U.K. National Archives, Thomas splint / blood transfusion: https://blog.nationalarchives.gov.uk/thomas-splint · https://blog.nationalarchives.gov.uk/three-men-saved-countless-lives-blood-transfusion-first-world-war
J. Special Operations Medicine 2014: https://www.jsomonline.com/Flipbook/Journals/1402-Summer/files/basic-html/page60.html
Stanford Blood Center, first blood bank: https://stanfordbloodcenter.org/100th-anniversary-first-blood-bank/
NLM Circulating Now, Gassed: https://circulatingnow.nlm.nih.gov/2017/10/04/gassed
Army Nurse Corps Association: https://e-anca.org/History/Topics-in-ANC-History/Contributions-of-the-US-Army-Nurse-Corps-in-WWI
National WWI Museum and Memorial: https://www.theworldwar.org/learn/educator-resource/bespoke-bodies-educators-guide-digital-timeline
Full source list: github.com/ituraev97/KEPTALIVE_media (episodes/103-wounded-ww1/sources.md)

Archival film (public domain): U.S. Army Signal Corps, 1917–1919, RG 111 Historical Films (111-H-1445, 1181, 1212, 1299, 1405, 1367, 1360, 1357, 1327, 1419, 1421, 1364), U.S. National Archives, via Internet Archive; "Gas Alarm" (111-H-1121) is a 1918 British anti-gas TRAINING film; Ford Film Collection 200-FC-45 (National Archives). Ambulance footage from 111-H-1212 shows American volunteer drivers serving with the French Army.
Photographs and drawings: The Medical Department of the U.S. Army in the World War, Vols. II and VIII (GPO, 1925–27); Manual of Splints and Appliances (U.S. Army, 1917).
Footage via DVIDS (published Nov. 12–17, 2026): Sgt. Josefina Garcia, 7th MPAD (E3B testing, Fort Hood, Nov. 7, 2026 — TRAINING); Sgt. Elijah Campbell, 21st TSC (519th Hospital Center CBRN training, Landstuhl — TRAINING); MC2 Sylvie Carafiol, AFN Sasebo (Red Cross blood drive, Sasebo, Oct. 21, 2026).
U.S. government visual information is in the public domain; appearance of U.S. government visual information does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Army, the U.S. Department of Defense, NIH, CDC or any government agency.

#ww1 #warmedicine #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
