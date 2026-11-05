import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "Cold open")]
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            t = s[2]["t"]; chap.append((S[i], t[0] + t[1:].lower()))
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
out[0] = (0, "Cold open: an iron lung evacuation, 1945")
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""Before the vaccine, polio came back every summer, and for patients who could no longer breathe, the answer was a steel tank: the iron lung. We follow how America stopped wild polio: the first iron lung at Boston Children's in 1928, FDR and the March of Dimes, the 1954 Salk field trial with 1.8 million children, the Cutter incident, the 1961 vaccination drives, the last U.S. wild cases in 1979, and how a 1952 epidemic in Copenhagen, with one iron lung for a whole country, led to the first intensive care unit.

Chapters:
{chapters}

Sources:
WHO, Poliomyelitis fact sheet: https://www.who.int/news-room/fact-sheets/detail/poliomyelitis
CDC, Pink Book, Chapter 18: Poliomyelitis: https://www.cdc.gov/pinkbook/hcp/table-of-contents/chapter-18-poliomyelitis.html
CDC, Polio Facts (archived 2012): https://webarchive.library.unt.edu/web/20121002195009/http://www.cdc.gov/Features/PolioFacts
CDC, Historical Vaccine Safety Concerns (archived): https://webarchive.library.unt.edu/web/20170125004715/https://www.cdc.gov/vaccinesafety/concerns/concerns-history.html
California Department of Public Health, Polio: https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/Immunization/polio.aspx
Harvard Medical School, Lifesaving Breath: https://hms.harvard.edu/news/lifesaving-breath
Mass Humanities, Mass Moments, Boston Doctors Use First Iron Lung: https://www.massmoments.org/moment-details/boston-doctors-use-first-iron-lung.html
Boston Children's Hospital Archives, The "iron lung": https://bcharchives.omeka.net/exhibits/show/polio/treatment/ironlung
Kansas Historical Society, Kansapedia, Iron Lung: https://www.kansashistory.gov/kansapedia/iron-lung/18723
FDR Presidential Library & Museum, FDR and Polio: https://fdrlibrary.org/polio
Howard Markel, The day polio began losing its grip on America, PBS NewsHour (2013): https://www.pbs.org/newshour/health/the-day-polio-began-losing-its-grip-on-america
University of Michigan School of Public Health, 1955 Polio Vaccine Trial Announcement: https://sph.umich.edu/polio
University of Florida College of Medicine, Treatment of polio led to the evolution of the modern ICU: https://news.drgator.ufl.edu/2011/12/16/treatment-of-polio-led-to-the-evolution-of-the-modern-icu
Paul Warwicker, How a polio outbreak led to the invention of modern intensive care, New Statesman (2020): https://www.newstatesman.com/long-reads/2020/04/how-polio-outbreak-led-invention-modern-intensive-care
ATS Conference News, keynote by Dr. Hannah Wunsch: https://www.atsconferencenews.org/monday-keynote-speaker-shares-gripping-story-of-modern-medical-innovation-amid-polio-epidemic/

Footage: Staff Sgt. Jan Valle, U.S. Army Southern European Task Force, Africa, "US, Tanzania enhance ICU readiness with ventilator training," 2026 (training exercise); Gerardo Estrada, Brooke Army Medical Center, "Day in the Life: Respiratory Therapists," 2022 (mannequin training shots only); U.S. Naval Hospital Guam, "ICU Tour," 2026; Spc. Raekwon Jenkins, Operation Allies Welcome, "U.S. Navy Administers Immunizations," 2021 — all via DVIDS. Archival film: U.S. Army Signal Corps, "Iron Lung Evacuation, 60th General Hospital, Manila" (1945, National Archives 111-ADC-5218); "FDR at Warm Springs" (1928–1939, FDR Presidential Library); "Unconditional Surrender" (1956, National Foundation for Infantile Paralysis, Prelinger Archives); "Babies and Breadwinners" (1961, Communicable Disease Center); Universal Newsreels "Thanks for the Dimes" (1944) and 1957 Salk vaccine coverage — public domain via Internet Archive. U.S. government visual information is in the public domain; its appearance does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, NIH, CDC, WHO or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
