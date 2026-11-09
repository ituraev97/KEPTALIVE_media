# KEPT ALIVE · FIRST 008 — Ether Day: What Surgery Was Like Before Anesthesia, and the Day It Changed
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts) | I(image key, kb="in"|"pan")
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  Historical narration (before 1900) is shown ONLY with period illustrations/documents and our own graphics — never modern footage.
#  Modern footage appears only where the narration is about anesthesia today or the modern military, with its real place/date:
#   640595 = U.S. Army Graduate Program in Anesthesia Nursing (USAGPAN) overview, AMEDD/MEDCOE 2016 — classroom + simulation lab -> TRAINING
#   531459 = 88th Medical Group OR team practising procedures, Wright-Patterson AFB, Ohio, June 2017 -> TRAINING
#   1026809 = Operating Room Stand-Up Training Day, Brooke Army Medical Center, Texas, Oct 2026 (manikins) -> TRAINING
#   745407 = USNS Comfort prepares its post-anesthesia care unit (empty beds), New York City, March 31, 2020 (real, no patients)
#   385923 = Physician anesthesiologists at the NATO Role 3 Multinational Medical Unit, Kandahar, Afghanistan, 2015 (real; staff only, no patient shots)
#   905268 = Surgery aboard USNS Mercy, Pacific Partnership 2024-1 (real; instrument tables and microscope only, no operative field)
#  Stills (public domain): keller = A. J. Keller, "The First Public Demonstration of Surgical Anaesthesia, Boston, October 16, 1846",
#   in "The Semi-Centennial of Anaesthesia" (MGH, 1897); mgh1846 = engraving "Massachusetts General Hospital, Boston, 1846-7" (same book);
#   warren = portrait of John Collins Warren (same book); wells1847 = title page, Horace Wells, "A History of the Discovery of the Application
#   of Nitrous Oxide Gas, Ether, and Other Vapors, to Surgical Operations" (Hartford, 1847; NLM copy); morton1853 = title page, "Statements,
#   Supported by Evidence, of Wm. T. G. Morton… on his claim to the discovery of the anaesthetic properties of ether" (Washington, 1853; LoC copy).
#  No patient is named. No blood, wounds or operative field on screen.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)
CASE = "FIRST · 008"
S = "<span style=\"color:#2BB3A3\">{}</span>"
KEL = ("\"THE FIRST PUBLIC DEMONSTRATION OF SURGICAL ANAESTHESIA\"", "ILLUSTRATION BY A. J. KELLER · PUBLISHED 1897 · MGH")
MGH = ("MASSACHUSETTS GENERAL HOSPITAL, BOSTON · 1846–47", "ENGRAVING · \"THE SEMI-CENTENNIAL OF ANAESTHESIA\" · 1897")
WAR = ("JOHN COLLINS WARREN · SURGEON", "PORTRAIT · \"THE SEMI-CENTENNIAL OF ANAESTHESIA\" · 1897")
WEL = ("HORACE WELLS · HARTFORD · 1847", "TITLE PAGE · NATIONAL LIBRARY OF MEDICINE COPY")
MOR = ("MORTON'S CLAIM TO THE U.S. SENATE · 1853", "TITLE PAGE · LIBRARY OF CONGRESS COPY")
GPAN = ("ARMY GRADUATE PROGRAM IN ANESTHESIA NURSING", "SIMULATION TRAINING · U.S. ARMY MEDICAL DEPARTMENT · 2016")
WPAFB = ("OPERATING ROOM TEAM TRAINING", "WRIGHT-PATTERSON AFB, OHIO · 2017 · 88TH MEDICAL GROUP")
BAMC = ("OPERATING ROOM TRAINING DAY", "BROOKE ARMY MEDICAL CENTER, TEXAS · OCT. 2026")
COM = ("POST-ANESTHESIA CARE UNIT · USNS COMFORT", "NEW YORK CITY · MARCH 2020 · U.S. NAVY")
KAN = ("PHYSICIAN ANESTHESIOLOGISTS · NATO ROLE 3 HOSPITAL", "KANDAHAR, AFGHANISTAN · 2015")
MER = ("SURGICAL TEAM ABOARD USNS MERCY", "PACIFIC PARTNERSHIP 2024-1 · SOLOMON ISLANDS · 2023 · U.S. NAVY")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Before anesthesia, surgery was done on patients who were wide awake. A surgeon's best weapon against pain was speed.",
  [G("stat", a="AWAKE", b="SURGERY BEFORE ANESTHESIA", c="PATIENTS WERE CONSCIOUS · SOURCE: SCIENCE MUSEUM, LONDON")], dict(kind="punch")),
 ("Then, on a Friday morning in October, eighteen forty-six, in a Boston hospital, a dentist named William Morton gave a patient ether vapor to breathe.",
  [I("mgh1846", kb="pan")], dict(tag=MGH, kind="tense")),
 ("After about five minutes, the patient was asleep. The surgeon removed a growth from his neck. Afterward, the patient said it felt as if his neck had been scraped. But it hadn't hurt.",
  [I("keller", kb="in")], dict(tag=KEL, kind="calm")),
 ("The surgeon turned to the doctors watching, and, according to an account published years later, said:",
  [I("warren", kb="in")], dict(tag=WAR, kind="slow", gap=0.3)),
 ("Gentlemen, this is no humbug.",
  [G("quote", q="Gentlemen, this is no humbug.", w="JOHN COLLINS WARREN · OCTOBER 16, 1846 · AS REPORTED — FIRST PRINTED IN 1859")], dict(kind="punch", gap=0.8)),
 ("This is the story of how surgery stopped hurting. Why it took so long. Who fought over the credit. And how it reached the battlefield.",
  [I("keller", kb="pan")], dict(tag=KEL, kind="question", gap=0.4)),
 ("Ether Day. The day surgery stopped hurting.",
  [G("title", kicker=CASE, title="ETHER " + S.format("DAY"), sub="THE DAY SURGERY STOPPED HURTING", size=210)], dict(kind="slow", gap=2.4)),

 # ---------------- I. AWAKE ----------------
 ("To understand what changed, start with what surgery was like before.",
  [G("chapter", case="BEFORE 1846", n="I", t="AWAKE")], dict(gap=1.0, kind="calm")),
 ("An operation was the last resort. Surgeons had to operate on conscious patients, who might be writhing in agony. And pain was not the only danger. Blood loss and infection made every operation life-threatening.",
  [G("cards3", kicker="SURGERY BEFORE 1846", title="THREE DANGERS",
     cards=[dict(h="PAIN", t="The patient was awake"), dict(h="BLOOD LOSS", t="Could be fatal", size=96), dict(h="INFECTION", t="No antiseptics yet", size=96)],
     footer="SOURCES: SCIENCE MUSEUM, LONDON · S. J. SNOW, OUPBLOG, 2009")], dict(kind="calm")),
 ("Doctors had a few ways to dull the senses. Alcohol. Opium. In earlier centuries, plants like henbane. British sailors were given rum before an emergency amputation.",
  [G("list", kicker="BEFORE ANESTHESIA", title="WHAT DOCTORS HAD",
     items=["Alcohol", "Opium", "Plants such as henbane", "Rum, for sailors facing an amputation"],
     footer="SOURCES: SCIENCE MUSEUM, LONDON · BRITANNICA")], dict(kind="calm")),
 ("None of it was reliable. So surgeons worked as fast as they could.",
  [G("stat", a="SPEED", b="THE SURGEON'S BEST DEFENSE AGAINST PAIN", c="SOURCE: SCIENCE MUSEUM, LONDON")], dict(kind="punch", gap=0.5)),
 ("In London, the surgeon Robert Liston was famous for the speed with which he could amputate a limb. Even a busy surgeon like him performed only two or three operations a month.",
  [G("doc", header="LONDON · 1830s–1840s", title="ROBERT LISTON", body="Famous for \"the speed and decisiveness with which he could amputate a limb before the discovery of anaesthetics.\"",
     source="SOURCE: UCL BLOOMSBURY PROJECT", stamp="FASTEST KNIFE")], dict(kind="calm")),
 ("Between eighteen thirty-five and eighteen forty, he performed sixty-six amputations. Ten of those patients died.",
  [G("phases", kicker="ROBERT LISTON · 1835–1840", title="HIS AMPUTATION RECORD", left=dict(label="AMPUTATIONS", num="66", desc="PERFORMED"),
     right=dict(label="PATIENTS WHO DIED", num="10", desc="ABOUT 15%"), active=1, footer="SOURCE: HEKTOEN INTERNATIONAL, 2019")], dict(kind="calm")),
 ("You may have heard that one of his operations killed three people at once. Historians call that story apocryphal. There is no good evidence it happened.",
  [G("stat", a="MYTH", b="THE \"300% MORTALITY\" OPERATION", c="CALLED APOCRYPHAL · SOURCE: AMERICAN COLLEGE OF SURGEONS POSTER, 2016")], dict(kind="calm", gap=0.5)),
 ("Patients left their own accounts. In eighteen eleven, an English writer had an operation in Paris with only a wine cordial to steady her.",
  [G("doc", header="PARIS · SEPTEMBER 30, 1811", title="A PATIENT'S LETTER", body="An operation without anesthesia. Only a wine cordial was given beforehand. She wrote about it months later, in a letter to her sister.",
     source="SOURCES: BC MEDICAL JOURNAL, 2013 · OUPBLOG, 2009")], dict(kind="calm")),
 ("She remembered how it began. Her room was entered, without warning, by seven men in black. And she remembered the glitter of polished steel.",
  [G("quote", q="…my room, without previous message, was entered by 7 Men in black… the glitter of polished Steel.", w="LETTER, 1812 · VIA NYU MEDICAL HUMANITIES")], dict(kind="tense")),
 ("Months later, she wrote to her sister about it. She called it a terror that surpasses all description. And she added: I dare not revise, nor read. The recollection is still so painful.",
  [G("quote", q="…a terror that surpasses all description… I dare not revise, nor read, the recollection is still so painful.", w="LETTER, 1812 · QUOTED IN S. J. SNOW, OUPBLOG, 2009")], dict(kind="slow", gap=0.8)),

 # ---------------- II. LAUGHING GAS ----------------
 ("And yet, a clue had been there for decades.",
  [G("chapter", case="1800–1845", n="II", t="LAUGHING GAS")], dict(gap=1.0, kind="calm")),
 ("In eighteen hundred, the English chemist Humphry Davy wrote that nitrous oxide appeared capable of destroying physical pain. He suggested it might be used during surgical operations.",
  [G("quote", q="As nitrous oxide in its extensive operation appears capable of destroying physical pain…", w="HUMPHRY DAVY · 1800 · VIA THE WOOD LIBRARY-MUSEUM OF ANESTHESIOLOGY")], dict(kind="calm")),
 ("For decades, almost no one followed up. Instead, nitrous oxide became laughing gas. At shows and parties, people passed it around in bladders and inhaled it for fun.",
  [G("doc", header="1800s · PUBLIC ENTERTAINMENT", title="LAUGHING GAS", body="Nitrous oxide was passed around in bladders and inhaled at shows and parties.",
     source="SOURCES: BRITANNICA · WOOD LIBRARY-MUSEUM", stamp="SHOWTIME")], dict(kind="calm")),
 ("Why the delay? Historians still debate it. But the result was clear. For nearly half a century, the implications of Davy's findings for surgery were ignored.",
  [G("stat", a="46", b="YEARS FROM DAVY'S SUGGESTION TO ETHER DAY", c="1800 → 1846 · SOURCES: WOOD LIBRARY-MUSEUM · BRITANNICA")], dict(kind="slow", gap=0.4)),
 ("In Georgia, on March thirtieth, eighteen forty-two, a country doctor named Crawford Long used ether while removing growths from a patient's neck.",
  [G("timeline", kicker="THE RACE TO ANESTHESIA", title="EARLY ATTEMPTS",
     events=[dict(y="1800", t="Davy: nitrous oxide may stop pain"), dict(y="1842", t="Long: ether in Georgia"), dict(y="1844", t="Wells: laughing gas, Hartford"), dict(y="1846", t="Morton: ether in Boston")],
     footer="SOURCES: WOOD LIBRARY-MUSEUM · BRITANNICA")], dict(kind="calm")),
 ("But Long didn't publish his results until eighteen forty-nine. Today, America's National Doctors' Day falls on March thirtieth, in honor of that operation. It was first observed in Georgia in nineteen thirty-three, and was first recognized by Congress in nineteen ninety.",
  [G("stat", a="MARCH 30", b="NATIONAL DOCTORS' DAY", c="HONORS CRAWFORD LONG'S 1842 ETHER ANESTHETIC · SOURCE: WOOD LIBRARY-MUSEUM")], dict(kind="calm", gap=0.5)),
 ("In December eighteen forty-four, a dentist in Hartford, Connecticut, named Horace Wells went to a laughing gas show.",
  [I("wells1847", kb="in")], dict(tag=WEL, kind="calm")),
 ("The next day, he breathed the gas himself, while a colleague pulled one of his teeth. He felt no pain.",
  [G("doc", header="HARTFORD · DECEMBER 1844", title="A PAINLESS EXTRACTION", body="Wells inhaled nitrous oxide while a dental colleague extracted one of his own teeth.",
     source="SOURCE: WOOD LIBRARY-MUSEUM OF ANESTHESIOLOGY")], dict(kind="punch")),
 ("In January eighteen forty-five, Wells tried a demonstration in Boston, arranged with the surgeon John Collins Warren. The patient cried out. The demonstration was judged a failure. A humbug.",
  [G("stat", a="HUMBUG", b="WELLS' BOSTON DEMONSTRATION · JANUARY 1845", c="JUDGED A FAILURE · SOURCES: WOOD LIBRARY-MUSEUM · BRITANNICA")], dict(kind="tense", gap=0.5)),
 ("One man who knew Wells well was his former partner. A dentist named William Morton.",
  [I("mgh1846", kb="in")], dict(tag=MGH, kind="slow", gap=0.6)),

 # ---------------- III. NO HUMBUG ----------------
 ("Remember those names. Davy, in eighteen hundred. Long, in eighteen forty-two. Wells, in eighteen forty-four. Each came close. Each, for different reasons, did not change surgery. The next man would.",
  [G("timeline", kicker="CLOSE, BUT NOT YET", title="BEFORE ETHER DAY",
     events=[dict(y="1800", t="Davy suggests nitrous oxide"), dict(y="1842", t="Long uses ether, doesn't publish"), dict(y="1844", t="Wells: laughing gas"), dict(y="1846", t="?")],
     footer="SOURCES: WOOD LIBRARY-MUSEUM · BRITANNICA")], dict(kind="slow", gap=0.6)),
 ("Morton turned to a different chemical. Ether.",
  [G("chapter", case="OCTOBER 16, 1846", n="III", t="NO HUMBUG")], dict(gap=1.0, kind="calm")),
 ("On Friday, October sixteenth, eighteen forty-six, Morton was invited to an operation at ten in the morning, in the hospital's operating amphitheater. The surgeon was John Collins Warren.",
  [G("callcard", kicker="MASSACHUSETTS GENERAL HOSPITAL · BOSTON", title="OCTOBER 16, 1846",
     rows=[["10:00 A.M.", "Operation in the surgical amphitheater"], ["SURGEON", "John Collins Warren"], ["ETHER GIVEN BY", "William T. G. Morton, dentist"]],
     footer="SOURCE: NATIONAL PARK SERVICE, NATIONAL HISTORIC LANDMARK NOMINATION")], dict(kind="calm")),
 ("Morton went to the patient, took his hand, and told him he would feel no pain.",
  [I("keller", kb="pan")], dict(tag=KEL, kind="slow")),
 ("The patient breathed in the vapor. In about five minutes, he was asleep. Warren operated to remove the growth.",
  [G("steps", kicker="OCTOBER 16, 1846", title="WHAT HAPPENED", items=[["BREATHE", "Ether vapor"], ["SLEEP", "About five minutes"], ["OPERATE", "Growth removed from the neck"], ["WAKE", "\"Scraped\" — but no pain"]],
     footer="SOURCES: NATIONAL PARK SERVICE · PAUL S. RUSSELL, MD MUSEUM, MGH")], dict(kind="drive")),
 ("When it was over, the patient said he had felt his neck being scraped. But it hadn't hurt.",
  [I("keller", kb="in")], dict(tag=KEL, kind="calm")),
 ("Warren, the story goes, turned to the room. Gentlemen, this is no humbug. Some historians doubt he ever said it. But the room had seen what it had seen.",
  [I("warren", kb="pan")], dict(tag=WAR, kind="punch", gap=0.8)),
 ("The room still exists. It was the hospital's operating amphitheater from eighteen twenty-one to eighteen sixty-seven. Today it's called the Ether Dome.",
  [I("mgh1846", kb="pan")], dict(tag=MGH, kind="calm")),
 ("It sits on the fourth floor of the hospital's Bulfinch Building. It was named a National Historic Landmark in nineteen sixty-five, and it's still used for meetings and lectures.",
  [G("stat", a="&#8203;1965", b="THE ETHER DOME · NATIONAL HISTORIC LANDMARK", c="STILL USED FOR MEETINGS AND LECTURES · SOURCES: MGH · PAUL S. RUSSELL, MD MUSEUM")], dict(kind="calm", gap=0.6)),

 # ---------------- IV. THE FIGHT FOR CREDIT ----------------
 ("The news spread fast. And so did the arguments.",
  [G("chapter", case="1846–1868", n="IV", t="THE FIGHT FOR CREDIT")], dict(gap=1.0, kind="calm")),
 ("On November eighteenth, eighteen forty-six, the surgeon Henry Jacob Bigelow published an account of Morton's work.",
  [G("timeline", kicker="AFTER ETHER DAY", title="1846",
     events=[dict(y="OCT 16", t="Ether Day, Boston"), dict(y="NOV 12", t="Patent issued: \"Letheon\""), dict(y="NOV 18", t="Bigelow publishes"), dict(y="DEC 21", t="Liston, London")],
     footer="SOURCES: HEKTOEN INTERNATIONAL · SMITHSONIAN · UCLH")], dict(kind="calm")),
 ("A few days later, the physician and writer Oliver Wendell Holmes suggested, in a letter to Morton, a word for the new state. Anaesthesia. And an adjective to go with it: anaesthetic.",
  [G("stat", a="ANAESTHESIA", b="A NEW WORD · OLIVER WENDELL HOLMES · NOVEMBER 1846", c="SOURCES: WOOD LIBRARY-MUSEUM · HEKTOEN INTERNATIONAL")], dict(kind="slow")),
 ("Morton had tried to keep his secret. At first, he would not even reveal what his substance was. He called it Letheon, and he was granted a patent on it. The patent was later revoked, and he never received any royalties.",
  [G("doc", header="U.S. PATENT NO. 4,848 · NOVEMBER 12, 1846", title="\"LETHEON\"", body="Morton disguised ether under a new name. The patent was later revoked; he never received royalties.",
     source="SOURCES: SMITHSONIAN · SCIENCE MUSEUM GROUP", stamp="REVOKED")], dict(kind="calm")),
 ("The news crossed the Atlantic. On December twenty-first, eighteen forty-six, at University College Hospital in London, Robert Liston performed the first recorded major operation under ether in Europe.",
  [G("doc", header="LONDON · DECEMBER 21, 1846", title="ETHER REACHES EUROPE", body="The first recorded major operation under ether in Europe, at University College Hospital.",
     source="SOURCE: UNIVERSITY COLLEGE LONDON HOSPITALS")], dict(kind="calm")),
 ("Liston, the fastest knife in London, asked the audience to time him, even with his patient asleep. Afterward, he reportedly told the room: This Yankee dodge beats mesmerism hollow.",
  [G("quote", q="This Yankee dodge beats mesmerism hollow.", w="ROBERT LISTON · LONDON · DECEMBER 21, 1846 · AS REPORTED")], dict(kind="punch")),
 ("A year later, in Scotland, the obstetrician James Young Simpson began using another anesthetic. Chloroform.",
  [G("stat", a="&#8203;1847", b="CHLOROFORM · JAMES YOUNG SIMPSON", c="SOURCES: WOOD LIBRARY-MUSEUM · BRITANNICA")], dict(kind="calm", gap=0.5)),
 ("Back in America, a bitter fight began over who deserved the credit. Morton. His former partner, Horace Wells. The chemist Charles Jackson, who shared Morton's patent. And Crawford Long, in Georgia.",
  [I("morton1853", kb="in")], dict(tag=MOR, kind="tense")),
 ("Boston physicians petitioned Congress to reward the discoverer. Bills were introduced. None passed. The dispute was never clearly resolved.",
  [G("cards3", kicker="WHO DISCOVERED ANESTHESIA?", title="THE CLAIMANTS",
     cards=[dict(h="LONG", t="Ether · 1842 · published 1849"), dict(h="WELLS", t="Nitrous oxide · 1844"), dict(h="MORTON", t="Ether · public demonstration, 1846")],
     footer="DISPUTE \"NEVER CLEARLY RESOLVED\" · SOURCE: SMITHSONIAN NMAH ARCHIVES")], dict(kind="calm")),
 ("Morton spent his last years in controversy and lawsuits. He died in eighteen sixty-eight, at the age of forty-eight.",
  [I("morton1853", kb="pan")], dict(tag=MOR, kind="slow", gap=0.8)),

 # ---------------- V. TO THE BATTLEFIELD ----------------
 ("Anesthesia didn't stay in the hospital for long.",
  [G("chapter", case="1847–TODAY", n="V", t="TO THE BATTLEFIELD")], dict(gap=1.0, kind="calm")),
 ("Within six months of Ether Day, it had gone to war. In March eighteen forty-seven, during the Mexican-American War, an American surgeon named Edward Barton gave ether for an amputation at Veracruz.",
  [G("doc", header="VERACRUZ, MEXICO · MARCH 1847", title="ETHER GOES TO WAR", body="Dr. Edward Barton administers ether for an amputation during the Mexican-American War.",
     source="SOURCE: GACETA MÉDICA DE MÉXICO, 1997")], dict(kind="calm")),
 ("Fourteen years later came the Civil War. And with it, a myth that lasts to this day. That wounded soldiers bit a bullet, or were simply given alcohol, because there was nothing else.",
  [G("stat", a="MYTH", b="\"BITE THE BULLET\"", c="SOURCE: AMERICAN BATTLEFIELD TRUST")], dict(kind="tense")),
 ("The Union army's own medical records tell a different story. At least eighty thousand operations were done with anesthesia. Only two hundred fifty-four were recorded without it.",
  [G("phases", kicker="UNION ARMY · 1861–1865", title="SURGERY IN THE CIVIL WAR", left=dict(label="WITH ANESTHESIA", num="80,000+", desc="OPERATIONS"),
     right=dict(label="RECORDED WITHOUT", num="254", desc="OPERATIONS"), active=0, footer="SOURCE: NATIONAL MUSEUM OF CIVIL WAR MEDICINE")], dict(kind="punch")),
 ("In the field, chloroform was used most often. Ether, in about fourteen percent of cases. And William Morton himself served in Union field hospitals, as one of the war's only dedicated anesthetists.",
  [G("callcard", kicker="NATIONAL MUSEUM OF CIVIL WAR MEDICINE", title="ANESTHESIA, 1861–1865",
     rows=[["CHLOROFORM", "Used most often in the field"], ["ETHER", "About 14% of cases"], ["W. T. G. MORTON", "Gave anesthesia in Union field hospitals"]],
     footer="SOURCE: CIVILWARMED.ORG")], dict(kind="calm", gap=0.5)),
 ("The World Wars made one specialist essential. The nurse anesthetist. In World War One, nurse anesthetist Sophie Winton served with Mobile Hospital Number One in France.",
  [G("doc", header="FRANCE · WORLD WAR I", title="SOPHIE WINTON", body="Nurse anesthetist assigned to Mobile Hospital No. 1, in the Château-Thierry area.",
     source="SOURCES: AANA ARCHIVES · J CLIN ANESTH, 2016")], dict(kind="calm")),
 ("In World War Two, the Army estimated it needed two thousand four hundred ninety-five nurse anesthetists. Only two hundred seventy-three were on duty. More than two thousand would have to be recruited, or trained in new six-month courses.",
  [G("phases", kicker="U.S. ARMY · WORLD WAR II", title="NURSE ANESTHETISTS", left=dict(label="NEEDED (ESTIMATED)", num="2,495", desc="FOR ARMY UNITS"),
     right=dict(label="ON DUTY", num="273", desc="REPORTED"), active=1, footer="SOURCE: ARMY MEDICAL DEPARTMENT, OFFICE OF MEDICAL HISTORY")], dict(kind="drive")),
 ("One Army nurse anesthetist, Mildred Clark, was at Schofield Barracks in Hawaii during the attack on Pearl Harbor. She later became the first nurse anesthetist to be appointed Chief of the Army Nurse Corps.",
  [G("doc", header="HAWAII · DECEMBER 7, 1941", title="MILDRED CLARK", body="Nurse anesthetist at Schofield Barracks during Pearl Harbor; later the first nurse anesthetist appointed Chief of the Army Nurse Corps.",
     source="SOURCE: AANA ARCHIVES")], dict(kind="calm")),
 ("Today, the Army trains its own nurse anesthetists, in the U.S. Army Graduate Program in Anesthesia Nursing. In twenty eleven, U.S. News and World Report ranked it the best nurse anesthesia program in the country.",
  [C(640595, 132.2), C(640595, 268.0)], dict(tag=GPAN, kind="calm")),
 ("Military anesthesiologists work in combat hospitals. This team was at the NATO hospital in Kandahar, Afghanistan, in twenty fifteen.",
  [C(385923, 8.2), G("stat", a="ROLE 3", b="NATO MULTINATIONAL MEDICAL UNIT · KANDAHAR", c="2015 · PHYSICIAN ANESTHESIOLOGISTS · SOURCE: DVIDS")], dict(tag=KAN, kind="calm")),
 ("And in twenty twenty, aboard the Navy hospital ship Comfort in New York, a recovery unit stood ready for patients waking up after surgery.",
  [C(745407, 13.6)], dict(tag=COM, kind="calm", gap=0.6)),

 # ---------------- VI. HOW IT WORKS TODAY ----------------
 ("So what does anesthesia actually do today?",
  [G("chapter", case="TODAY", n="VI", t="UNDER")], dict(gap=1.0, kind="question")),
 ("According to the National Library of Medicine, general anesthesia puts you into a deep, sleep-like state, so you do not feel pain during surgery, and you don't remember the procedure.",
  [C(531459, 39.0, mode="fill"), C(531459, 75.0, mode="fill")], dict(tag=WPAFB, kind="calm")),
 ("It's not the only kind. Local anesthesia numbs a small area, like a tooth. Regional anesthesia numbs a larger area, like an arm or a leg. And sedation makes a patient relaxed, or sleepy.",
  [G("steps", kicker="MEDLINEPLUS · NATIONAL LIBRARY OF MEDICINE", title="TYPES OF ANESTHESIA",
     items=[["LOCAL", "A small area, like a tooth"], ["REGIONAL", "A larger area, like an arm or leg"], ["GENERAL", "The whole body"], ["SEDATION", "Relaxed or sleepy"]],
     footer="SOURCE: MEDLINEPLUS.GOV/ANESTHESIA")], dict(kind="drive")),
 ("During general anesthesia, blood pressure, pulse and breathing are monitored continuously. Most often, the anesthesia is given by a doctor called an anesthesiologist. Sometimes, by a nurse anesthetist.",
  [C(640595, 400.0), C(640595, 409.6)], dict(tag=GPAN, kind="calm")),
 ("Training never stops. Operating teams rehearse and review together, so the real day goes right.",
  [C(1026809, 20.8), C(1026809, 30.5)], dict(tag=BAMC, kind="calm")),
 ("The American Society of Anesthesiologists says surgery and anesthesia are safer today than ever before.",
  [G("stat", a="SAFER", b="THAN EVER BEFORE", c="SOURCE: AMERICAN SOCIETY OF ANESTHESIOLOGISTS")], dict(kind="slow", gap=0.6)),

 # ---------------- WHAT CHANGED ----------------
 ("Before eighteen forty-six, a surgeon raced the patient's pain, and the patient was awake for every second.",
  [I("keller", kb="pan")], dict(tag=KEL, kind="slow")),
 ("After one Friday morning in Boston, patients could sleep. And today, surgical teams like this one can take their time.",
  [C(905268, 82.0)], dict(tag=MER, kind="slow")),
 ("Within a year, the news had crossed an ocean. Within fifteen years, it was in field hospitals across a nation at war. And it began with a dentist, a surgeon, and a patient who said it didn't hurt.",
  [I("mgh1846", kb="in")], dict(tag=MGH, kind="slow", gap=0.6)),
 ("Every year on October sixteenth, the anniversary of Ether Day, anesthesiologists around the world mark World Anaesthesia Day. This October was the hundred and eightieth anniversary.",
  [G("stat", a="180", b="YEARS SINCE ETHER DAY · OCTOBER 16, 1846", c="WORLD ANAESTHESIA DAY · SOURCE: WORLD FEDERATION OF SOCIETIES OF ANAESTHESIOLOGISTS")], dict(kind="calm", gap=0.9)),
 ("If this story surprised you, subscribe. Next time on Kept Alive: penicillin. The mold that went to war.",
  [G("stat", a="NEXT", b="PENICILLIN: THE MOLD THAT WENT TO WAR", c="KEPT ALIVE · FIRST")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · FIRST 008", stamp="ETHER DAY")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("eighteen forty-six", "1846"), ("twenty twenty", "2020"), ("nineteen thirty-three", "1933"), ("nineteen ninety", "1990"), ("twenty eleven", "2011"), ("fifteen years", "15 years"), ("eighteen thirty-five", "1835"), ("eighteen forty", "1840"), ("sixty-six", "66"), ("Ten of those", "10 of those"),
 ("eighteen eleven", "1811"), ("eighteen hundred", "1800"), ("March thirtieth", "March 30"), ("eighteen forty-two", "1842"), ("eighteen forty-nine", "1849"),
 ("eighteen forty-four", "1844"), ("eighteen forty-five", "1845"), ("October sixteenth", "October 16"), ("eighteen twenty-one", "1821"), ("eighteen sixty-seven", "1867"),
 ("nineteen sixty-five", "1965"), ("November eighteenth", "November 18"), ("December twenty-first", "December 21"), ("eighteen sixty-eight", "1868"), ("forty-eight", "48"),
 ("eighteen forty-seven", "1847"), ("eighty thousand", "80,000"), ("two hundred fifty-four", "254"), ("fourteen percent", "14%"),
 ("two thousand four hundred ninety-five", "2,495"), ("More than two thousand", "More than 2,000"), ("six-month", "6-month"), ("two hundred seventy-three", "273"), ("twenty fifteen", "2015"), ("hundred and eightieth", "180th"),
 ("Kept Alive", "KEPT ALIVE"), ("Number One", "No. 1"), ("five minutes", "5 minutes"), ("Fourteen years", "14 years"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · FIRST",
    title="Ether Day",
    voice="am_fenrir",
    imgs={"keller": "/home/claude/imgs/keller.c.jpg", "mgh1846": "/home/claude/imgs/mgh1846.c.jpg", "warren": "/home/claude/imgs/warren.c.jpg",
          "wells1847": "/home/claude/imgs/wells1847.c.jpg", "morton1853": "/home/claude/imgs/morton1853.c.jpg"},
    mute_nat=["640595", "531459", "1026809", "745407", "385923", "905268"],
    training=["640595", "531459", "1026809"],
    credit=("Footage: U.S. Army, U.S. Air Force, U.S. Navy via DVIDS (public domain); training footage marked TRAINING."
            r"\NIllustrations: \"The Semi-Centennial of Anaesthesia\" (MGH, 1897); Wells, 1847 (NLM copy); Morton, 1853 (Library of Congress copy) — via Internet Archive."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, NIH or CDC."
            r"\NFor education only. This is not medical advice."),
)

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))  # longest first: 'eighteen forty' must not pre-empt 'eighteen forty-two'
