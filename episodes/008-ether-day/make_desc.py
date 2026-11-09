import json, importlib.util
sp = importlib.util.spec_from_file_location("e", "episode.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
T = json.load(open("timing.json")); S = T["starts"]
def mmss(x): x = int(x); return f"{x//60}:{x%60:02d}"
chap = [(0, "Cold open: surgery before anesthesia")]
names = {"AWAKE": "Awake: surgery before 1846", "LAUGHING GAS": "Laughing gas: Davy, Long and Wells", "NO HUMBUG": "October 16, 1846: Ether Day",
         "THE FIGHT FOR CREDIT": "The fight for credit", "TO THE BATTLEFIELD": "To the battlefield: Civil War to today", "UNDER": "What anesthesia does today"}
for i, (txt, shots, o) in enumerate(E.LINES):
    for s in shots:
        if s[0] == "g:chapter":
            chap.append((S[i], names.get(s[2]["t"], s[2]["t"].title())))
out = []
for t, n in chap:
    if out and t - out[-1][0] < 10: continue
    out.append((t, n))
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""What was surgery like before anesthesia? Patients were awake, and a surgeon's best defense against pain was speed. This medical history documentary tells how anesthesia was discovered: from Humphry Davy's laughing gas and Crawford Long's ether to Horace Wells and Ether Day, October 16, 1846, when William Morton gave ether at Massachusetts General Hospital in Boston.

Then the fight over who discovered anesthesia, how chloroform and ether reached Civil War surgery (no, most soldiers did not "bite the bullet"), the nurse anesthetists of the World Wars, and what general, regional and local anesthesia do today, according to the National Library of Medicine.

Chapters:
{chapters}

Sources:
National Park Service, National Historic Landmark nomination, Ether Dome: https://npgallery.nps.gov/GetAsset/fe6d94f0-71a6-4766-8644-d28aff02b855
Paul S. Russell, MD Museum (MGH): https://www.russellmuseum.org/?p=2758
Wood Library-Museum of Anesthesiology, History of anesthesia: https://www.woodlibrarymuseum.org/history-of-anesthesia/
Wood Library-Museum, Horace Wells: https://www.woodlibrarymuseum.org/museum/horace-wells-plaque/
Hektoen International, "Gentlemen, this is no humbug" (2020): https://hekint.org/2020/11/23/gentlemen-this-is-no-humbug/
Hektoen International, Robert Liston: https://hekint.org/2019/06/13/robert-liston-the-fastest-knife-in-town/
UCL Bloomsbury Project, Robert Liston: https://www.ucl.ac.uk/bloomsbury-project/articles/individuals/liston_robert.htm
Science Museum (London), surgery and anaesthesia: https://www.sciencemuseum.org.uk/objects-and-stories/surgery
S. J. Snow, OUPblog (2009): https://blog.oup.com/2009/01/anaesthesia/
Britannica, Anesthetics through history: https://www.britannica.com/science/anesthetic/Anesthetics-through-history
Smithsonian NMAH, W. T. G. Morton papers: https://sova.si.edu/record/nmah.ac.0118
National Museum of Civil War Medicine: https://www.civilwarmed.org/anesthesia-2/
Gaceta Médica de México (1997), ether at Veracruz 1847: https://anmm.org.mx/bgmm/1864_2007/1997-133-5-473-474.pdf
AANA, Profiles of nurse anesthetists: https://www.aana.com/about-us/history/aana-archives/profiles-of-nurse-anesthetists/
U.S. Army Medical Department Office of Medical History, WWII training: https://achh.army.mil/history/book-wwii-medtrain-ch4/
MedlinePlus (NLM), General anesthesia: https://medlineplus.gov/ency/article/007410.htm · Anesthesia: https://medlineplus.gov/anesthesia.html
American Society of Anesthesiologists, anesthesia risks: https://www.asahq.org/madeforthismoment/anesthesia-101/types-of-anesthesia/anesthesia-risks/
WFSA, World Anaesthesia Day 2026: https://wfsahq.org/news/world-anaesthesia-day-2026-before-during-and-beyond-surgery/

Illustrations (public domain, via Internet Archive): A. J. Keller, "The First Public Demonstration of Surgical Anaesthesia, Boston, October 16, 1846", the MGH engraving of 1846–47 and the portrait of J. C. Warren, from "The Semi-Centennial of Anaesthesia" (Massachusetts General Hospital, 1897); title pages of H. Wells, "A History of the Discovery of the Application of Nitrous Oxide Gas, Ether, and Other Vapors, to Surgical Operations" (1847, NLM copy) and of W. T. G. Morton's "Statements, Supported by Evidence" (1853, Library of Congress copy).

Footage via DVIDS (TRAINING marked on screen): U.S. Army Medical Department (MEDVID-TV) video by Gloria Grider (Army Graduate Program in Anesthesia Nursing, 2016 — TRAINING); U.S. Air Force video by Ryan J. Law and A1C Johnathon Wines, 88th Air Base Wing (OR team training, Wright-Patterson AFB, 2017 — TRAINING); Brooke Army Medical Center video by Gerardo Estrada (OR Stand-Up Training Day, 2026 — TRAINING); U.S. Navy video by Sara Eshleman (USNS Comfort post-anesthesia care unit, New York, 2020); U.S. Navy video by Lt. Cmdr. Jesse Ehrenfeld, NATO Role 3 Multinational Medical Unit (Kandahar, Afghanistan, 2015); U.S. Navy video by Justin Ontiveros (USNS Mercy, Pacific Partnership 2024-1). U.S. government visual information is in the public domain; appearance of U.S. government visual information does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, NIH, CDC, Massachusetts General Hospital or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
