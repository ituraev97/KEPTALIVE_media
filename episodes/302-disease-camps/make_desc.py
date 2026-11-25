import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//3600}:{x%3600//60:02d}:{x%60:02d}" if x >= 3600 else f"{x//60}:{x%60:02d}"
chap = [(0, "Camp Thomas, 1898: the camp fever")]
names = {"THE CAMPS OF 1898": "The camps of 1898: typhoid and flies",
         "THE FIRST ORDER": "The first order: Washington and smallpox",
         "THE FORGOTTEN WAR": "The forgotten war: Mexico, 1846–48",
         "THE LARGEST EXPERIMENT": "The largest experiment: Civil War camps",
         "THE CIVILIAN ARMY": "The civilian army: volunteers and disease",
         "DID THE MOSQUITO DO IT?": "Did the mosquito do it? Yellow fever, 1900",
         "THE SHOT": "The shot: the typhoid vaccine",
         "THE SECOND ARMY": "The second army: 1918 and influenza",
         "THE SOUTH PACIFIC": "The South Pacific: malaria in World War II",
         "THE POWDER": "The powder: typhus in Naples, 1943–44",
         "TODAY": "Today: the Army and infectious disease"}
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter": chap.append((S[i], names.get(s[2]["t"], s[2]["t"].title())))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in chap)
desc = f"""Why disease often killed more U.S. soldiers than combat, explained: war medicine and military medicine history from the Revolution to today. Disease in the army, from Civil War and Spanish-American War camps (typhoid, dysentery, measles) to yellow fever, malaria, typhus and influenza, and how sanitation, vaccines and mosquito control fought back. Counts from the Congressional Research Service and the Army's own histories, with where the pattern holds and where it broke (World War II).

WAR MEDICINE · EP 3. Historic photographs, plans and films; no wounds on screen; history only.

Chapters:
{chapters}

Sources (full list: github.com/ituraev97/KEPTALIVE_media, episodes/302-disease-camps/sources.md):
Congressional Research Service RL32492, American War and Military Operations Casualties: https://www.everycrsreport.com/files/20190924_RL32492_75dc0f1f826404a4728a7a3eb43ec2f8cb67905d.html
VA, America's Wars fact sheet: https://www.va.gov/opa/publications/factsheets/fs_americas_wars.pdf
Medical Statistics in the U.S. Army, World War II (OTSG, 1975): https://collections.nlm.nih.gov/ocr/nlm:nlmuid-7607981-bk
Typhoid Board (Reed, Vaughan, Shakespeare, 1904), UVA exhibit: https://exhibits.hsl.virginia.edu/typhoid/creation
PBS American Experience, Fever: https://www.pbs.org/wgbh/americanexperience/features/fever-scourge-spanish-american-war
Nat'l Museum of Health and Medicine, To Bind Up the Nation's Wounds: https://medicalmuseum.health.mil/index.cfm/visit/exhibits/past/nationswounds/page_03
NPS, Smallpox inoculation in the Revolutionary War: https://www.nps.gov/articles/000/smallpox-inoculation-revolutionary-war.htm
NPS, Olmsted and the U.S. Sanitary Commission: https://www.nps.gov/articles/000/olmsted-and-the-united-states-sanitary-commission.htm
UVA, U.S. Army Yellow Fever Commission in Cuba: https://exhibits.hsl.virginia.edu/yellowfever/yellow-fever-commission-work/
James Lind Library, yellow fever in Havana: https://www.jameslindlibrary.org/articles/dramatic-effects-of-control-measures-on-deaths-from-yellow-fever-in-havana-cuba-in-the-early-1900s/
Preventive Medicine in WWII, Vol. VI, Malaria: https://collections.nlm.nih.gov/ocr/nlm:nlmuid-1278003RX5-mvpart
NLM, Typhus Fever and Malaria in the Mediterranean: https://profiles.nlm.nih.gov/spotlight/vv/feature/typhus

Photographs, plans and engravings (public domain, via Internet Archive): Harper's Pictorial History of the War with Spain (1899); Reed, Vaughan & Shakespeare, Typhoid Fever in U.S. Military Camps (1904); The Photographic History of the Civil War, vol. 8 (1911); Frost, Pictorial History of Mexico and the Mexican War (1862); The Mexican War and Its Heroes (1850); Kelly, Walter Reed and Yellow Fever (1906); Medical Dept. of the U.S. Army in the World War, vol. 6 (1926); Preventive Medicine in World War II, vols. 6 and 7. Each image is captioned with its own printed place and date.
Films (public domain U.S. government films via the National Archives and Internet Archive): 83rd Division, Camp Sherman, Ohio, 1917–18 (Signal Corps); "A Few Quick Facts" (U.S. Army, 1944); It's Up to You: Dengue-Yellow Fever Control and Aedes aegypti control (U.S. Public Health Service, 1945); Malaria and Mosquito Control Activities (U.S. Navy, 1943–44); War Dept. Film Bulletins 147 (1944), 195 (DDT, 1945) and 217 (Army Medical Laboratories, 1947); San Francisco parade, 1918 (Prelinger Archives, newsreel, not government). Each shot is labelled with its own year; archival film is shown as period illustration, not as the exact place or event named.
Footage via DVIDS (flu vaccination, Oct.–Nov. 2026, real events, not training): Lance Cpl. Jase Graziano, U.S. Marine Corps (AFN Iwakuni, Japan, Oct. 2, 2026); Staff Sgt. Juliana Londono, U.S. Air Force (AFN Kaiserslautern, Nov. 2026); Pfc. Donghyun Ko, U.S. Army (AFN Daegu, Camp Carroll, Korea, Oct. 26, 2026).
U.S. government visual information is in the public domain; appearance of U.S. government visual information does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Army, the U.S. Department of Defense, the National Park Service, NIH, CDC or any government agency.

#warmedicine #militaryhistory #keptalive
"""
assert len(desc) <= 4900, len(desc)
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
