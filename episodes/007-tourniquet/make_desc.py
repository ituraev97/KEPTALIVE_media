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
out[0] = (0, "Cold open: 87% vs 0%")
chapters = "\n".join(f"{mmss(t)} {n}" for t, n in out)
desc = f"""How does a tourniquet work, and why did military doctors fear it for most of the 20th century? A tourniquet squeezes an arm or leg until the artery inside is pressed shut. This medical history documentary follows the tourniquet from the siege of Besançon and Esmarch's 1883 first aid book to the U.S. Army.

In 1916 a British army surgeon wrote that he was "inclined to think" tourniquets were "an invention of the Evil One," and for decades Army medics were taught it was a last resort. Then Tactical Combat Casualty Care (TCCC), the Combat Application Tourniquet and a 2006 Army study in Baghdad changed military medicine, and the Stop the Bleed campaign brought bleeding control to the public. This video explains history and how the device works; it is not training.

Chapters:
{chapters}

Sources:
Kragh et al., Historical review of emergency tourniquet use to stop bleeding, American Journal of Surgery (2012): https://www.east.org/content/documents/MilitaryResources/TCCC/TCCC%20Kragh%20Historical%20Rev%20of%20Emerg%20TQs%20AM%20J%20Surg%202012.pdf
Maher, Innovations from the Battlefield: Tourniquets, Journal of Military and Veterans' Health (2020): https://jmvh.org/?p=5942
Butler, The U.S. Military Experience with Tourniquets and Hemostatic Dressings, Journal of Special Operations Medicine (2015): https://jsomonline.org/wp-content/uploads/2024/02/20154149Butler.pdf
Kragh et al., Survival with emergency tourniquet use to stop bleeding in major limb trauma, Annals of Surgery (2009), abstract: https://www.naemt.org/docs/default-source/education-documents/tccc/tccc-updates_092017/tccc-reference-materials/07-tccc-key-publications-(abstracts)/kragh-survival-with-emerg-tourniquets-ann-surg-2009.pdf
Holcomb et al., Causes of death in U.S. Special Operations Forces 2001–2004, Annals of Surgery (2007), abstract: https://www.naemt.org/docs/default-source/education-documents/tccc/tccc-updates_092017/tccc-reference-materials/07-tccc-key-publications-(abstracts)/holcomb-sof-causes-of-death-ann-surg-2007.pdf
Eastridge et al., Death on the battlefield (2001–2011), J Trauma Acute Care Surg (2012): https://scholar.usuhs.edu/en/publications/death-on-the-battlefield-2001-2011-implications-for-the-future-of/
Wall et al., Getting Tourniquets Right = Getting Tourniquets Tight, JSOM (2019): https://jsomonline.org/?p=12388
DVIDS, New tourniquet being issued to Soldiers in Iraq, Afghanistan (July 2005): https://www.dvidshub.net/news/printable/2431
U.S. Air Force, BMT Tactical Combat Casualty Care course (2020): https://www.af.mil/News/Article-Display/Article/2099306
STOP THE BLEED, Our Story (American College of Surgeons): https://www.stopthebleed.org/our-story/
News-Medical, Stop the Bleed surpasses one million trained (2019): https://www.news-medical.net/news/20190908/Stop-the-Bleed-program-surpasses-one-million-mark-in-training-people-to-control-major-bleeding.aspx
STAT via PBS NewsHour, Do tourniquets save lives after mass shootings? (2016): https://www.pbs.org/newshour/health/theyre-simple-and-cheap-but-do-tourniquets-save-lives-after-mass-shootings
King et al., Tourniquet use at the Boston Marathon bombing (2015), ASPR TRACIE summary: https://asprtracie.hhs.gov/technical-resources/resource/458/tourniquet-use-at-the-boston-marathon-bombing-lost-in-translation
Esmarch, Early Aid in Injuries and Accidents (1883), NLM copy: https://archive.org/details/29420280R.nlm.nih.gov

Footage (all TRAINING, via DVIDS): U.S. Marine Corps video by Lance Cpl. Daniel A. Wulz (CAT instruction, Regional Command Southwest, Afghanistan, 2011); U.S. Army video by Christopher Coyer, U.S. Army Training Support Center (Basic Combat Training, Fort Jackson, S.C.); U.S. Air Force video by Courtney Richardson, 944th Fighter Wing (TCCC, Gila Bend, Ariz.); AFN Benelux video by Christina Carter (TCCC, Chièvres Air Base, Belgium, 2026); U.S. Air Force video by Airman 1st Class Tiffany Del Oso, 325th Fighter Wing (Stop the Bleed, Tyndall AFB); U.S. Air Force video by Olivia Grooms, Nellis AFB (Stop the Bleed, Las Vegas, 2018); U.S. Air Force video by Sarayuth Pinthong, 502d Air Base Wing (BMT TCCC, 2020). Archival film: War Department Training Film No. 71, "The Medical Service with Infantry in Combat" (National Archives 111-M-489, via Internet Archive). Illustration: Esmarch, 1883 (National Library of Medicine copy). U.S. government visual information is in the public domain; its appearance does not imply or constitute endorsement.

For education only. This is not medical advice. If you have a health concern, talk to a doctor.

KEPT ALIVE is an independent channel and is not affiliated with or endorsed by the U.S. Department of Defense, NIH, CDC, the American College of Surgeons or any government agency.

#medicine #medicalhistory #keptalive
"""
open("youtube_description.txt", "w").write(desc)
print(chapters); print(len(desc), "chars")
