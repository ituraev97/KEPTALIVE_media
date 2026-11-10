import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "Cold open: no beds in Monrovia")]
names = {"CONTACT": "How Ebola spreads", "NO BEDS": "No beds: Liberia, summer 2014", "THE CALL": "The call: Operation United Assistance",
         "TEST. BUILD. TRAIN.": "Labs, treatment units and training", "THE TURN": "What really turned the tide", "ZERO": "Counting to zero", "AFTER": "Vaccines, and the 2026 outbreak"}
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            chap.append((S[i], names.get(s[2]["t"], s[2]["t"].title())))
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""How was the 2014 Ebola outbreak stopped in Liberia? The West Africa Ebola epidemic was the largest Ebola outbreak in history, and in September 2014 Monrovia had almost no treatment beds. This medical history documentary follows Operation United Assistance, the U.S. military's mobile labs, Ebola treatment units and the Monrovia Medical Unit, and what the evidence says really turned the tide.

The U.S. military did not treat Ebola patients. Cases in Liberia were already falling before most U.S.-built units opened, and studies credit Liberian communities, safe burial teams, contact tracing and isolation. Then: the Ebola vaccine and treatments approved since 2019, and the 2026 Bundibugyo outbreak in Congo, with CDC figures. History and public-health facts only; not medical advice.

Chapters:
{chapters}

Sources:
CDC, 2014–2016 Ebola Outbreak in West Africa: https://www.cdc.gov/vhf/ebola/history/2014-2016-outbreak/index.html
CDC, Ebola Disease Basics: https://www.cdc.gov/ebola/about/index.html · Signs and Symptoms: https://www.cdc.gov/ebola/signs-symptoms/index.html
Nyenswah et al., Ebola and Its Control in Liberia, 2014–2015, Emerging Infectious Diseases (2016): https://wwwnc.cdc.gov/eid/article/22/2/15-1456
CDC MMWR, Ebola Epidemic — Liberia, March–October 2014: https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6346a10.htm
CDC MMWR, Effectiveness of Ebola Treatment Units and Community Care Centers — Liberia (2015): https://www.cdc.gov/mmwr/pdf/wk/mm64e0123a2.pdf
WHO, The Ebola outbreak in Liberia is over (2015): https://www.who.int/news/item/08-05-2015-the-ebola-outbreak-in-liberia-is-over
WHO, Liberia: a country and its capital are overwhelmed with Ebola cases (2015): https://library.alnap.org/system/files/content/resource/files/main/who-liberia-a-country-and-its-capital-are-overwhelmed-with-ebola-cases.pdf
MSF, Liberia: new Ebola centres already overwhelmed (2014): https://www.msf.org/liberia-msfs-new-ebola-management-centres-already-overwhelmed
Remarks by President Obama at the CDC, Sept. 16, 2014 (govinfo): https://www.govinfo.gov/content/pkg/PPP-2014-book2/pdf/PPP-2014-book2-doc-pg1179.pdf
U.S. Army (army.mil, 2014–2015): https://www.army.mil/article/134936 · https://www.army.mil/article/137002 · https://www.army.mil/article/143540
Navy Medicine, NMRC Ebola response in West Africa (2024): https://www.med.navy.mil/Media/News/Article/3921361/10-years-later-looking-back-on-nmrc-ebola-response-in-west-africa/
Federal Practitioner, NIH and PHS Commissioned Corps in the Ebola response (2017): https://pmc.ncbi.nlm.nih.gov/articles/PMC5708545
Stars and Stripes, 11 US Ebola treatment centers treated only 28 patients (2015): https://www.stripes.com/theaters/africa/report-11-us-ebola-treatment-centers-treated-only-28-patients-1.339857
FDA, Ebola: https://www.fda.gov/emergency-preparedness-and-response/mcm-issues/ebola
CDC, Ebola Outbreak: Current Situation (as of Nov. 6, 2026): https://www.cdc.gov/ebola/situation-summary/index.html
CDC MMWR, Bundibugyo virus — DRC and Uganda (2026): https://www.cdc.gov/mmwr/volumes/75/wr/mm7522e3.htm

Footage via DVIDS (no patients shown; TRAINING marked on screen): U.S. Army videos by Sgt. Zila Winstead, 101st Airborne Division (Monrovia Medical Unit, Tubmanburg ETU, ETU construction, redeployment); Eric Hudson, 7th MPAD (Gbediah ETU); David Greeson, 27th PAD (Senje ETU; ETU course — TRAINING; 1st Area Medical Lab); David Meyer, 27th PAD (PPE training — TRAINING); Jose Ramirez, 1st AD CAB (CH-47 to Ganta); Daniel Hosack, DoD News (Fat Cow); Carlos Gonzales, 7th MPAD (36th Engineer Brigade); U.S. Air Force video by Audrey Merrell, 7th Bomb Wing. U.S. government visual information is in the public domain; its appearance does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, NIH, CDC, WHO, Doctors Without Borders or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
