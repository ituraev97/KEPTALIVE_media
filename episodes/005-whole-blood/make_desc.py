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
out[0] = (0, "Cold open: the bank that walks")
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""When stored blood runs out far from a hospital, the military turns to an old idea: the walking blood bank, where prescreened donors are the blood supply. We follow whole blood from Oswald Robertson's 1917 ice chest, through World War II, Korea and Vietnam, to the 1970s switch to components and its return with the Rangers' ROLO program, the Navy's Valkyrie, low titer O whole blood and civilian air ambulances.

Chapters:
{chapters}

Sources:
MedlinePlus (NIH/NLM), Blood: https://medlineplus.gov/blood.html
NHLBI, Types of Blood Transfusions (archived): https://webarchive.library.unt.edu/eot2008/20080917140215/http:/www.nhlbi.nih.gov/health/dci/Diseases/bt/bt_types.html
Nobel Prize, Karl Landsteiner, facts: https://www.nobelprize.org/prizes/medicine/1930/landsteiner/facts
Nobel Prize, Speed read: Blood relations: https://nobelprize.org/prizes/medicine/1930/speedread
Eve Meinhardt, 'Walking blood banks' fill gap for medical care in field environment, army.mil (2019): https://www.army.mil/article/224502/walking_blood_banks_fill_gap_for_medical_care_in_field_environment
Maj. Tony Mayne, Ranger whole blood program wins an Army's Greatest Innovation Award, army.mil (2017): https://www.army.mil/article/184219/ranger_whole_blood_program_wins_an_armys_greatest_innovation_award
Jessica Pellegrini (ASBP), ASBP's low titer Type O whole blood helps save lives on the battlefield: https://www.keesler.af.mil/News/Article-Display/Article/1206400/
Sgt. Sarah Stegall, Valkyrie: emergency fresh whole blood transfusion enhances 15th MEU medical capabilities, marines.mil (2021): https://www.marines.mil/News/News-Display/Article/2489777/valkyrie-emergency-fresh-whole-blood-transfusion-enhances-15th-meu-medical-capa/
Cpl. Juan Torres, U.S. Navy, ADF participate in Valkyrie emergency fresh whole blood transfusion training, DVIDS (2024): https://dvidshub.net/news/472274/us-navy-adf-participate-valkyrie-emergency-fresh-whole-blood-transfusion-training
LCpl Talan Werner, 2nd Marine Logistics Group hosts walking blood bank training, DVIDS (2026): https://www.dvidshub.net/news/560832/2nd-marine-logistics-group-hosts-walking-blood-bank-training-enhanced-battlefield-care
Curtis Hill, Navy medical personnel aboard MCB Camp Pendleton train on walking blood bank operations, DVIDS (2026): https://www.dvidshub.net/news/565066/navy-medical-personnel-aboard-mcb-camp-pendleton-train-walking-blood-bank-operations-nhcp
Proto Magazine (Mass General), The Blood Depot (2017): https://protomag-dev.partners.org/?p=13318
Elizabeth Yuko, How World War I Spurred the Invention of Blood Banks, History.com (2024): https://history.com/news/how-world-war-i-spurred-the-invention-of-blood-banks
Review, Trauma Surgery & Acute Care Open, vol. 11, e002278: https://tsaco.bmj.com/content/11/2/e002278
Armed Services Blood Program, Talking Points (archived 2016): https://webarchive.library.unt.edu/web/20161019064551/http:/www.militaryblood.dod.mil/press/Documents/Print_Talking_Points.pdf
Mayo Clinic, A reemerging role for whole blood in modern trauma care (2022): https://mayoclinic.org/medical-professionals/trauma/news/a-reemerging-role-for-whole-blood-in-modern-trauma-care/mac-20531706

Footage via DVIDS (training marked): U.S. Army video by Sgt. Samantha Hill (Combined Resolve 25-2, Germany, 2025, training), Spc. Wesley Richardson, 204th PAD (Keris Strike 26, Malaysia, 2026, training), Pvt. Oshon Trowbridge (10th Mountain Division, Fort Drum, 2025, training), Sgt. Adrianne Lopez (368th Field Hospital, 2025, training), Staff Sgt. Marie Alth (ASBP blood drive, Kelley Barracks, Germany, 2023); U.S. Marine Corps video by Lance Cpl. Deja Rogers (Camp Pendleton, 2024, training), Lance Cpl. Talan Werner (JTS Valkyrie course, Camp Lejeune, 2026, training), Cpl. Migel A. Reynosa (Valkyrie training, Darwin, Australia, 2024, training); U.S. Navy video by Petty Officer 2nd Class Jason Isaacs (ASBB Center Okinawa, 2022) and Seaman Vincent Dettlaff (walking blood bank screening, Diego Garcia, 2026); Defense Health Agency video by Sara Barger (ASBP blood drive, Norfolk, Va., 2022). Archival film: "Combat Bulletin No. 35" (1945, War Department / Army Pictorial Service) and U.S. Army Signal Corps "Blood Bank Story, Tokyo, Japan" (1950, National Archives 111-ADC-8650) — public domain via Internet Archive. U.S. government visual information is in the public domain; its appearance does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, the Armed Services Blood Program, NIH, CDC or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
