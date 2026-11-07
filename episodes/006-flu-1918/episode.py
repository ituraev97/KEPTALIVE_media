# KEPT ALIVE · OUTBREAK 006 — The Flu That Went to War (1918)
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts) | I(image key, kb="in"|"pan")
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  wwi_* = excerpts of U.S. Army Signal Corps film "Infantry Training" (covers 1918-1919; NARA 111-H-1179, compiled 1937). Generic camp scenes,
#          never presented as Camp Funston or as flu patients.
#  ship_* = U.S. Army Signal Corps "Embarkation of Troops for the United States, April and May 1919" (St. Nazaire; NARA 111-H-1454).
#          Troops going HOME in 1919 -> always captioned 1919 and introduced as "what the troopships looked like".
#  rc_* = U.S. Army Signal Corps "Welfare Activities: Red Cross [1918-1919]" (NARA 111-H-1540). Wounded scenes NOT used.
#  Photos (public domain): funston = "Emergency hospital during influenza epidemic, Camp Funston, Kansas" (National Museum of Health and Medicine, NCP 1603);
#          masks_boston / seattle_police / seattle_rc = NARA 165-WW-269B series "Medical Department - Influenza Epidemic 1918". Patients not named.
#  Modern (DVIDS, NOT training): 1027481 Camp Carroll flu drive, Korea, Oct. 2026; 1027887 SHOTEX, MCAS Iwakuni, Japan, Oct. 2026;
#          942620 flu shots, Grissom ARB, Ind., Nov. 2024; 767473 USAFSAM epidemiology lab, Wright-Patterson AFB, Aug. 2020 (not the NIH study lab).
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)
CASE = "OUTBREAK · 006"
S = "<span style=\"color:#2BB3A3\">{}</span>"
FUNSTON = [-96.79, 39.06]; DEVENS = [-71.61, 42.54]; UPTON = [-72.87, 40.87]; STL = [-90.20, 38.63]; PHL = [-75.16, 39.95]
ARCH = ("ARCHIVAL FILM · 1918–1919 · U.S. ARMY SIGNAL CORPS", "\"INFANTRY TRAINING\" · NATIONAL ARCHIVES 111-H-1179")
SHIPS = ("ARCHIVAL FILM · 1919 · TROOPS BOARD TRANSPORTS, ST. NAZAIRE", "U.S. ARMY SIGNAL CORPS · NATIONAL ARCHIVES 111-H-1454")
RC = ("ARCHIVAL FILM · 1918–1919 · U.S. ARMY SIGNAL CORPS", "\"WELFARE ACTIVITIES: RED CROSS\" · NATIONAL ARCHIVES 111-H-1540")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("By the end of nineteen eighteen, influenza, and the pneumonia that came with it, had killed about forty-five thousand American soldiers.",
  [I("funston", kb="in")], dict(tag=("EMERGENCY HOSPITAL DURING THE INFLUENZA EPIDEMIC", "CAMP FUNSTON, KANSAS · 1918 · NATIONAL MUSEUM OF HEALTH AND MEDICINE"), kind="tense")),
 ("American combat deaths in the entire war were fifty-three thousand, four hundred two.",
  [G("phases", kicker="U.S. ARMY · WORLD WAR I", title="THE FLU VS. COMBAT", left=dict(label="DIED OF INFLUENZA AND PNEUMONIA · BY END OF 1918", num="~45,000", desc="AMERICAN SOLDIERS"),
     right=dict(label="COMBAT DEATHS · WHOLE WAR", num="53,402", desc="AMERICANS"), active=0, footer="SOURCE: NATIONAL GUARD BUREAU, 2018")], dict(kind="punch", gap=0.7)),
 ("CDC calls it the most severe pandemic in recent history. An estimated five hundred million people infected. At least fifty million dead, worldwide.",
  [G("cards3", kicker="THE 1918 PANDEMIC", title="THE MOST SEVERE IN RECENT HISTORY",
     cards=[dict(h="500M", t="people infected", s="ESTIMATED · ABOUT ONE-THIRD OF THE WORLD"), dict(h="50M+", t="deaths worldwide", s="ESTIMATED · AT LEAST"), dict(h="675,000", t="deaths in the U.S.", s="ABOUT", size=96)],
     footer="SOURCE: CDC, 1918 PANDEMIC (H1N1 VIRUS)")], dict(kind="calm")),
 ("And in the United States, CDC says, it was first identified in military personnel.",
  [C("wwi_march", 1.0), C("wwi_march", 8.5)], dict(tag=ARCH, kind="slow")),
 ("This is how the deadliest flu in modern history went to war, and what medicine learned from it.",
  [C("wwi_barracks", 1.0)], dict(kind="question", gap=0.6)),
 ("The flu that went to war.",
  [G("title", kicker=CASE, title="THE FLU THAT<br>WENT TO " + S.format("WAR"), sub="1918 · THE U.S. ARMY AND THE PANDEMIC", size=170)], dict(kind="slow", gap=2.6)),

 # ---------------- I. THE CAMPS ----------------
 ("It started with an army being built in a hurry.",
  [G("chapter", case="1918", n="I", t="THE CAMPS")], dict(gap=1.1, kind="calm")),
 ("When America entered the First World War, more than four million recruits were mobilized. About thirty training camps were thrown up fast. Some held up to fifty thousand men, in crowded barracks.",
  [C("wwi_train", 0.5), C("wwi_barracks", 7.0)], dict(tag=ARCH, kind="drive")),
 ("One of them was Camp Funston, at Fort Riley, Kansas. At its peak, it processed nearly fifty-six thousand troops on their way to France.",
  [G("map", map=dict(useUS=True, rings=[dict(ll=FUNSTON, r=34, n=3, d=0.5)], cities=[dict(ll=FUNSTON, name="CAMP FUNSTON", sub="FORT RILEY, KANSAS", d=0.3, color="#6CF29A")]),
     kicker="KANSAS · 1918", title="A CAMP OF 56,000", footer="SOURCE: MILITARY.COM, 2026 · NATIONAL GUARD BUREAU, 2018")], dict(kind="calm")),
 ("In early March, nineteen eighteen, the first influenza cases were identified there. CDC counts more than one hundred cases. Within three weeks, a National Guard history says, eleven hundred of the camp's fifty-six thousand two hundred twenty-two troops were sick.",
  [G("stat", a="1,100", b="SICK WITHIN THREE WEEKS · OF 56,222 TROOPS AT CAMP FUNSTON", c="FIRST CASES: MARCH 1918 · SOURCES: CDC · NATIONAL GUARD BUREAU, 2018")], dict(kind="punch", gap=0.6)),
 ("In the weeks that followed, thousands of soldiers there came down with influenza. Thirty-eight died.",
  [I("funston", kb="pan")], dict(tag=("EMERGENCY HOSPITAL DURING THE INFLUENZA EPIDEMIC", "CAMP FUNSTON, KANSAS · 1918 · NATIONAL MUSEUM OF HEALTH AND MEDICINE"), kind="calm")),
 ("Where the virus came from is still debated. CDC says there is no universal consensus. One theory, from medical historians, points to rural Haskell County, Kansas, where a local doctor reported severe flu early that year. Young men from that county trained at Camp Funston.",
  [G("callcard", kicker="ONE THEORY · NOT SETTLED", title="HASKELL COUNTY, KANSAS",
     rows=[["JAN.–FEB. 1918", "A LOCAL DOCTOR, LORING MINER, SEES SEVERE FLU"], ["MARCH 1918", "HE ALERTS THE U.S. PUBLIC HEALTH SERVICE"], ["THE LINK", "YOUNG MEN FROM THE COUNTY TRAIN AT CAMP FUNSTON"]],
     footer="SOURCES: CDC · NATIONAL GUARD BUREAU, 2018")], dict(kind="calm")),
 ("CDC says the mass movement of troops helped spread the flu around the world. Within weeks, camps in Georgia reported cases. By the end of April, twenty-four of the Army's thirty-six main camps had reported outbreaks. And influenza reached Brest, in France, a major port for American troops.",
  [C("wwi_drill", 1.0), C("wwi_rows", 2.0)], dict(tag=ARCH, kind="drive")),
 ("And the troops kept moving. In March alone, eighty-four thousand American soldiers sailed for France. On one Atlantic crossing, the Fifteenth Cavalry reported thirty-six influenza cases, and six deaths.",
  [G("stat", a="84,000", b="AMERICAN TROOPS SAILED FOR FRANCE IN MARCH 1918 ALONE", c="15TH U.S. CAVALRY: 36 FLU CASES, 6 DEATHS ON ONE CROSSING · SOURCE: MILITARY.COM, 2026")], dict(kind="drive")),
 ("That first wave was widespread. But the worst was still coming.",
  [C("wwi_rows", 10.0)], dict(kind="slow", gap=0.7)),

 # ---------------- II. A MISLEADING NAME ----------------
 ("The world would call it the Spanish flu. The name is a misnomer.",
  [G("chapter", case="1918", n="II", t="A MISLEADING NAME")], dict(gap=1.1, kind="calm")),
 ("Nations fighting the war suppressed press coverage of the outbreak, to protect morale. Spain was neutral. Its newspapers reported the illness freely, including that King Alfonso the Thirteenth had fallen sick. So it looked as if the flu had started, or was at its worst, in Spain.",
  [G("doc", header="WARTIME PRESS · 1918", title="WHY \"SPANISH\"?", body="Warring nations suppressed news of the outbreak to protect morale. Neutral Spain reported it openly, including that King Alfonso XIII had fallen sick.",
     source="SOURCES: MILITARY.COM, 2026 · HISTORY.COM", stamp="NEUTRAL SPAIN")], dict(kind="calm")),
 ("Basically, it gets called the Spanish flu because the Spanish media did their job.",
  [G("quote", q="Basically, it gets called the 'Spanish flu' because the Spanish media did their job.", w="LORA VOGT · NATIONAL WWI MUSEUM AND MEMORIAL · VIA HISTORY.COM")], dict(kind="slow", gap=0.8)),

 # ---------------- III. THE SECOND WAVE ----------------
 ("In the fall of nineteen eighteen, the flu came back.",
  [G("chapter", case="1918", n="III", t="THE SECOND WAVE")], dict(gap=1.1, kind="tense")),
 ("CDC says this highly fatal second wave was responsible for most of the American deaths in the pandemic.",
  [G("timeline", kicker="CDC · THREE WAVES", title="MARCH 1918 TO SUMMER 1919",
     events=[dict(y="SPRING 1918", t="First wave · Camp Funston"), dict(y="FALL 1918", t="Second wave · most U.S. deaths"), dict(y="1919", t="Third wave · winter and spring")],
     footer="SOURCE: CDC, 1918 PANDEMIC INFLUENZA: THREE WAVES")], dict(kind="calm")),
 ("At Camp Devens, Massachusetts, influenza appeared in September. By the end of the month, fourteen thousand soldiers there were sick. Seven hundred fifty-seven died.",
  [G("map", map=dict(useUS=True, rings=[dict(ll=DEVENS, r=34, n=3, d=0.5)], cities=[dict(ll=DEVENS, name="CAMP DEVENS", sub="MASS.", d=0.3, color="#6CF29A")]),
     kicker="MASSACHUSETTS · SEPTEMBER 1918", title="CAMP DEVENS: 14,000 SICK BY END OF SEPT. · 757 DIED", footer="SOURCES: NATIONAL GUARD BUREAU, 2018 · MISSOURI MEDICINE, 2018")], dict(kind="tense")),
 ("At Camp Upton, on Long Island, the commander shut the camp to civilian visitors, and ended soldiers' leave. By the time the epidemic there ended, on October twenty-second, six thousand one hundred thirty-one soldiers had been hospitalized. Four hundred four had died.",
  [G("callcard", kicker="LONG ISLAND, N.Y. · FALL 1918", title="CAMP UPTON",
     rows=[["SEPT. 13", "INFLUENZA APPEARS"], ["RESPONSE", "NO CIVILIAN VISITORS · SOLDIERS' LEAVE ENDED"], ["BY OCT. 22", "6,131 HOSPITALIZED · 404 DEAD"]],
     footer="SOURCE: NATIONAL GUARD BUREAU, 2018")], dict(kind="calm")),
 ("In upstate New York, Camp Syracuse had no hospital, and only three ambulances. It counted two thousand two hundred eighty-nine flu cases. Two hundred eight soldiers died. In the city of Syracuse, about nine hundred residents died by the end of the epidemic.",
  [G("callcard", kicker="NEW YORK · FALL 1918", title="CAMP SYRACUSE",
     rows=[["THE CAMP", "NO HOSPITAL · ONLY THREE AMBULANCES"], ["SOLDIERS", "2,289 FLU CASES · 208 DIED"], ["THE CITY", "ABOUT 900 SYRACUSE RESIDENTS DIED"]],
     footer="SOURCE: NATIONAL GUARD BUREAU, 2018")], dict(kind="calm")),
 ("With so many doctors and nurses serving in the military, CDC says, there were shortages of medical personnel across the country. In Missouri, roughly half of the state's doctors were serving in the military. In October, the Army stopped taking in new draftees until the epidemic ended.",
  [C("wwi_barracks", 4.0), C("wwi_drill", 7.0)], dict(tag=ARCH, kind="calm")),
 ("But the war still needed men. The Army's Surgeon General recommended halting troop shipments to France. President Wilson declined. General Pershing wanted reinforcements. And they sailed.",
  [C("wwi_train", 6.0), C("wwi_rows", 13.0)], dict(tag=ARCH, kind="drive")),
 ("These Army films, from nineteen nineteen, show what those troopships looked like. Soldiers packed shoulder to shoulder, for a crossing of ten to fourteen days.",
  [C("ship_deck", 1.0), C("ship_rail", 1.0), C("ship_lifeboats", 2.0)], dict(tag=SHIPS, kind="calm")),
 ("Healthy soldiers often fell sick on the way. One sailor counted fifteen burials at sea, from a single ship, in one day.",
  [C("ship_lifeboats", 11.5)], dict(tag=SHIPS, kind="slow", gap=0.8)),

 # ---------------- IV. OVER THERE ----------------
 ("In France, the flu met the war.",
  [G("chapter", case="1918", n="IV", t="OVER THERE")], dict(gap=1.1, kind="calm")),
 ("In nineteen eighteen, the American Expeditionary Forces hospitalized three hundred forty thousand soldiers for influenza. Two hundred twenty-seven thousand were hospitalized for battle wounds.",
  [G("phases", kicker="AMERICAN EXPEDITIONARY FORCES · 1918", title="HOSPITALIZED IN EUROPE", left=dict(label="FOR INFLUENZA", num="340,000", desc="SOLDIERS"),
     right=dict(label="FOR BATTLE WOUNDS", num="227,000", desc="SOLDIERS"), active=0, footer="SOURCES: NATIONAL GUARD BUREAU, 2018 · MILITARY.COM, 2026")], dict(kind="punch")),
 ("In October, during the Meuse-Argonne offensive, one thousand four hundred fifty-one Americans died of the flu. The Third Infantry Division evacuated more soldiers from the front with influenza than with combat wounds.",
  [C("rc_front", 1.0), C("rc_front", 9.0)], dict(tag=RC, kind="tense")),
 ("The other side noticed. On October seventeenth, the German general Erich Ludendorff said the Americans were suffering severely from influenza.",
  [G("quote", q="The Americans are suffering severely from influenza.", w="GEN. ERICH LUDENDORFF, ON THE AMERICANS · OCT. 17, 1918 · AS QUOTED BY THE NATIONAL GUARD BUREAU")], dict(kind="slow")),
 ("Much of the care fell to nurses. By the Armistice, the Army Nurse Corps had reached an estimated peak of more than twenty-one thousand.",
  [C("rc_nurses", 1.0), C("rc_nurses", 8.0)], dict(tag=RC, kind="calm")),
 ("Historians estimate that more than two hundred American nurses died during the war. Most of those deaths are attributed to influenza, or complications like pneumonia.",
  [G("stat", a="200+", b="AMERICAN NURSES WHO DIED DURING THE WAR · ESTIMATED", c="MOSTLY INFLUENZA OR PNEUMONIA · SOURCE: ARLINGTON NATIONAL CEMETERY")], dict(kind="slow")),
 ("Back home, Red Cross workers made masks for soldiers in camp.",
  [I("masks_boston", kb="pan")], dict(tag=("RED CROSS WORKERS MAKE MASKS FOR SOLDIERS IN CAMP", "BOSTON, MASS. · 1918 · NATIONAL ARCHIVES 165-WW-269B"), kind="calm", gap=0.7)),

 # ---------------- V. WHAT KILLED THEM ----------------
 ("And doctors noticed something strange about who was dying.",
  [G("chapter", case="1918", n="V", t="WHAT KILLED THEM")], dict(gap=1.1, kind="question")),
 ("CDC says mortality was high in children under five, in adults twenty to forty, and in people sixty-five and older. The high death rate among healthy people aged twenty to forty was a unique feature of this pandemic.",
  [G("cards3", kicker="WHO DIED · 1918", title="A UNIQUE FEATURE",
     cards=[dict(h="&lt; 5", t="young children", s="HIGH MORTALITY"), dict(h="20–40", t="healthy adults", s="UNIQUE TO THIS PANDEMIC"), dict(h="65+", t="older adults", s="HIGH MORTALITY")],
     footer="SOURCE: CDC, 1918 PANDEMIC (H1N1 VIRUS)")], dict(kind="calm")),
 ("And the camps were full of young men, an age group usually less affected by seasonal flu.",
  [C("wwi_march", 6.0)], dict(tag=ARCH, kind="slow")),
 ("And in nineteen eighteen, there was no vaccine against influenza, and no antibiotics to treat the bacterial infections that followed.",
  [G("list", kicker="CDC · 1918", title="WHAT DOCTORS DID NOT HAVE", items=["No flu vaccine", "No antibiotics for the infections that followed", "Only isolation, quarantine, hygiene, disinfectants and fewer gatherings"],
     footer="SOURCE: CDC, 1918 PANDEMIC (H1N1 VIRUS)")], dict(kind="calm")),
 ("Ninety years later, NIH scientists examined lung tissue from fifty-eight soldiers who died of influenza at U.S. military bases in nineteen eighteen and nineteen nineteen. The tissue had been preserved in paraffin blocks. They also reviewed more than eight thousand autopsy reports.",
  [G("callcard", kicker="NIH · 2008", title="58 SOLDIERS, 90 YEARS LATER",
     rows=[["THE SAMPLES", "LUNG TISSUE FROM 58 SOLDIERS · U.S. MILITARY BASES · 1918–19"], ["PRESERVED", "IN PARAFFIN BLOCKS"], ["ALSO", "8,398 AUTOPSIES REVIEWED · 15 COUNTRIES"]],
     footer="SOURCE: NIH NEWS RELEASE, AUG. 2008 · MORENS ET AL., J INFECT DIS")], dict(kind="calm")),
 ("Their conclusion. Most victims died of bacterial pneumonia, following infection with the influenza virus. The virus damaged the lungs, and bacteria did much of the killing.",
  [G("stat", a="MOST", b="VICTIMS DIED OF BACTERIAL PNEUMONIA FOLLOWING THE FLU", c="SOURCE: NIH, 2008 · \"PREDOMINANT ROLE OF BACTERIAL PNEUMONIA\"")], dict(kind="punch", gap=0.8)),

 ("The researchers drew a lesson for the future. Pandemic planning, they said, should include stockpiles of antibiotics and bacterial vaccines, alongside flu vaccines and antiviral drugs.",
  [G("list", kicker="NIH · 2008", title="THE LESSON FOR PLANNERS", items=["Influenza vaccines", "Antiviral drugs", "Stockpiles of antibiotics", "Bacterial vaccines"], footer="SOURCE: NIH NEWS RELEASE, AUG. 2008")], dict(kind="calm", gap=0.7)),
 # ---------------- VI. THE HOME FRONT ----------------
 ("At home, cities had to fight it without a vaccine or antibiotics.",
  [G("chapter", case="1918", n="VI", t="THE HOME FRONT")], dict(gap=1.1, kind="calm")),
 ("CDC lists what they had. Isolation. Quarantine. Good hygiene. Disinfectants. And limits on public gatherings. They were applied unevenly.",
  [I("seattle_rc", kb="in")], dict(tag=("RED CROSS WORKROOM, WITH INFLUENZA MASKS ON FACES", "SEATTLE, WASH. · DEC. 1918 · NATIONAL ARCHIVES 165-WW-269B"), kind="calm")),
 ("In Seattle, police officers wore masks made by the local Red Cross chapter.",
  [I("seattle_police", kb="pan")], dict(tag=("POLICE IN MASKS MADE BY THE SEATTLE RED CROSS", "SEATTLE, WASH. · DEC. 1918 · NATIONAL ARCHIVES 165-WW-269B"), kind="calm")),
 ("Timing mattered. Two NIH-funded studies, published in two thousand seven, compared American cities. St. Louis brought in a broad set of measures within two days of its first reported cases. Philadelphia waited more than two weeks, and let a city-wide parade go ahead first.",
  [G("map", map=dict(useUS=True, rings=[dict(ll=STL, r=30, n=2, d=0.4), dict(ll=PHL, r=30, n=2, d=0.8, color="#F2B33D")],
     cities=[dict(ll=STL, name="ST. LOUIS", sub="MEASURES WITHIN 2 DAYS", d=0.3, color="#6CF29A"), dict(ll=PHL, name="PHILADELPHIA", sub="WAITED 2+ WEEKS", d=0.7, color="#F2B33D")]),
     kicker="FALL 1918", title="TWO CITIES", footer="SOURCE: NIH-FUNDED STUDIES, PNAS 2007 · VIA INFECTION CONTROL TODAY")], dict(kind="calm")),
 ("Peak death rates in St. Louis were one-eighth of Philadelphia's. Across the cities studied, cities that acted within a few days had peak weekly death rates up to half lower than cities that waited weeks.",
  [G("phases", kicker="PEAK DEATH RATES · 1918", title="ACTING EARLY", left=dict(label="ST. LOUIS · ACTED IN 2 DAYS", num="1/8", desc="OF PHILADELPHIA'S PEAK"),
     right=dict(label="EARLY CITIES VS. LATE CITIES", num="UP TO ½", desc="LOWER PEAK WEEKLY DEATHS"), active=0, footer="SOURCE: NIH-FUNDED STUDIES, PNAS 2007")], dict(kind="calm")),
 ("And then came a third wave, in the winter and spring of nineteen nineteen, adding to the death toll. CDC says the pandemic had subsided by that summer.",
  [I("seattle_police", kb="in")], dict(tag=("POLICE IN MASKS MADE BY THE SEATTLE RED CROSS", "SEATTLE, WASH. · DEC. 1918 · NATIONAL ARCHIVES 165-WW-269B"), kind="calm")),
 ("Across the United States, about six hundred seventy-five thousand people died.",
  [G("stat", a="675,000", b="DEATHS IN THE UNITED STATES · ABOUT", c="SOURCE: CDC")], dict(kind="slow", gap=0.9)),

 ("A review in the journal Missouri Medicine notes that the American toll was greater than the combat deaths of the U.S. military in both World Wars, Korea, and Vietnam, combined.",
  [G("stat", a="&gt; 4 WARS", b="U.S. FLU DEATHS EXCEEDED COMBAT DEATHS IN WWI, WWII, KOREA AND VIETNAM COMBINED", c="SOURCE: MISSOURI MEDICINE, 2018")], dict(kind="slow", gap=0.9)),
 # ---------------- VII. WHAT CHANGED ----------------
 ("The Army did not forget.",
  [G("chapter", case="1918", n="VII", t="WHAT CHANGED")], dict(gap=1.1, kind="calm")),
 ("In nineteen forty-one, it set up a board to investigate and control influenza and other epidemic diseases. Its Commission on Influenza was led by Thomas Francis Junior, at the University of Michigan. A young researcher, Jonas Salk, ran much of the day-to-day work.",
  [G("callcard", kicker="U.S. ARMY · 1941", title="THE COMMISSION ON INFLUENZA",
     rows=[["1941", "ARMY BOARD TO INVESTIGATE AND CONTROL INFLUENZA"], ["LED BY", "DR. THOMAS FRANCIS JR. · UNIVERSITY OF MICHIGAN"], ["DAY TO DAY", "JONAS SALK"]],
     footer="SOURCES: MIDRP, HEALTH.MIL · UNIVERSITY OF MICHIGAN HERITAGE PROJECT")], dict(kind="calm")),
 ("They built an inactivated flu vaccine. It was studied in military recruits and college students, including twelve thousand five hundred Army trainees, in the flu season of nineteen forty-three to forty-four.",
  [G("stat", a="12,500", b="ARMY SPECIALIZED TRAINING PROGRAM PARTICIPANTS IN THE TRIAL", c="1943–44 FLU SEASON · DOUBLE-BLIND · SOURCE: UNIVERSITY OF MICHIGAN")], dict(kind="calm")),
 ("The Army ordered every soldier vaccinated in the fall of nineteen forty-five. That November, the vaccine was licensed.",
  [G("timeline", kicker="FROM 1918 TO A VACCINE", title="WHAT THE ARMY BUILT",
     events=[dict(y="1918", t="No vaccine, no antibiotics"), dict(y="1941", t="Army influenza board"), dict(y="1943", t="Trial in 12,500 trainees"), dict(y="NOV. 1945", t="Vaccine licensed")],
     footer="SOURCES: CDC · MIDRP, HEALTH.MIL · UNIVERSITY OF MICHIGAN")], dict(kind="drive")),
 ("And the military kept watching the virus. Between nineteen sixty-one and nineteen ninety-three, the Armed Forces Epidemiological Board made fifty-three separate recommendations on what should go into flu vaccines.",
  [G("callcard", kicker="1961–1993", title="ARMED FORCES EPIDEMIOLOGICAL BOARD", rows=[["THE JOB", "ADVISE ON INFLUENZA VACCINES"], ["1961–1993", "53 SEPARATE RECOMMENDATIONS ON VACCINE COMPOSITION"]], footer="SOURCE: MIDRP, HEALTH.MIL")], dict(kind="calm")),
 ("Today, flu shots are an annual requirement for military members.",
  [C(1027481, 9.0), C(1027481, 20.0)], dict(tag=("FLU DRIVE · CAMP CARROLL, REPUBLIC OF KOREA", "OCT. 26, 2026 · AFN DAEGU VIA DVIDS"), kind="calm")),
 ("And military labs, like this Air Force epidemiology lab, test samples sent in from military treatment facilities around the world.",
  [C(767473, 96.5), C(767473, 108.5)], dict(tag=("EPIDEMIOLOGY LABORATORY · USAF SCHOOL OF AEROSPACE MEDICINE", "WRIGHT-PATTERSON AFB, OHIO · AUG. 2020 · U.S. AIR FORCE"), kind="calm")),
 ("This fall, flu activity rose early. In late October, CDC said the weekly flu hospitalization rate was the highest for that week since the twenty ten to eleven season. Activity was still low overall.",
  [C(1027887, 1.0), C(1027887, 22.0)], dict(tag=("SHOTEX FLU VACCINATION EVENT", "MCAS IWAKUNI, JAPAN · OCT. 6, 2026 · AFN IWAKUNI VIA DVIDS"), kind="calm")),
 ("CDC recommends annual flu vaccination. Flu vaccines are available for people six months and older.",
  [G("stat", a="ANNUAL", b="CDC RECOMMENDS SEASONAL FLU VACCINATION", c="VACCINES AVAILABLE FOR AGES 6 MONTHS AND OLDER · SOURCE: CDC FLUVIEW, WEEK 42, 2026")], dict(kind="slow", gap=0.8)),
 ("In nineteen eighteen, flu and pneumonia killed almost as many American soldiers as combat did. There was no vaccine, and no antibiotics for the pneumonia that followed. Twenty-seven years later, the first of those answers arrived. A licensed flu vaccine, built with the Army's help.",
  [C("wwi_rows", 6.0), C("wwi_march", 11.0)], dict(tag=ARCH, kind="slow", gap=0.9)),
 ("Next time on Kept Alive. The tourniquet. From feared, to lifesaver.",
  [G("stat", a="NEXT", b="THE TOURNIQUET: FROM FEARED TO LIFESAVER", c="KEPT ALIVE · HOW IT WORKS · 007")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · OUTBREAK 006", stamp="1918")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("nineteen eighteen", "1918"), ("Nineteen eighteen", "1918"), ("nineteen nineteen", "1919"), ("nineteen forty-one", "1941"), ("nineteen forty-three to forty-four", "1943-44"), ("nineteen forty-three", "1943"),
 ("nineteen forty-five", "1945"), ("twenty ten to eleven", "2010-11"), ("two thousand seven", "2007"), ("forty-five thousand", "45,000"),
 ("fifty-three thousand, four hundred two", "53,402"), ("five hundred million", "500 million"), ("fifty million", "50 million"),
 ("four million", "4 million"), ("fifty thousand", "50,000"), ("fifty-six thousand two hundred twenty-two", "56,222"), ("fifty-six thousand", "56,000"),
 ("one hundred cases", "100 cases"), ("eleven hundred", "1,100"), ("twenty-four of the Army's thirty-six", "24 of the Army's 36"), ("about thirty", "about 30"),
 ("fourteen thousand", "14,000"), ("Seven hundred fifty-seven", "757"), ("October twenty-second", "October 22"), ("six thousand one hundred thirty-one", "6,131"),
 ("Four hundred four", "404"), ("ten to fourteen days", "10 to 14 days"), ("fifteen burials", "15 burials"), ("three hundred forty thousand", "340,000"),
 ("Two hundred twenty-seven thousand", "227,000"), ("one thousand four hundred fifty-one", "1,451"), ("twenty-one thousand", "21,000"),
 ("two hundred American nurses", "200 American nurses"), ("under five", "under 5"), ("twenty to forty", "20 to 40"), ("sixty-five", "65"),
 ("fifty-eight soldiers", "58 soldiers"), ("eight thousand", "8,000"), ("six hundred seventy-five thousand", "675,000"), ("twelve thousand five hundred", "12,500"),
 ("six months", "6 months"), ("Twenty-seven years", "27 years"), ("Ninety years", "90 years"), ("October seventeenth", "October 17"), ("Thirty-eight", "38"), ("eighty-four thousand", "84,000"), ("Fifteenth Cavalry", "15th Cavalry"), ("thirty-six", "36"), ("six deaths", "6 deaths"), ("two thousand two hundred eighty-nine", "2,289"), ("Two hundred eight", "208"), ("nine hundred", "900"), ("nineteen sixty-one", "1961"), ("nineteen ninety-three", "1993"), ("fifty-three separate", "53 separate"), ("three ambulances", "3 ambulances"), ("King Alfonso the Thirteenth", "King Alfonso XIII"), ("Kept Alive", "KEPT ALIVE"),
 ("Thomas Francis Junior", "Thomas Francis Jr."),
]

META = dict(
    case=CASE, label="KEPT ALIVE · OUTBREAK",
    title="The Flu That Went to War",
    voice="am_fenrir",
    imgs={"funston": "/home/claude/imgs/funston.c.jpg", "masks_boston": "/home/claude/imgs/masks_boston.c.jpg",
          "seattle_police": "/home/claude/imgs/seattle_police.c.jpg", "seattle_rc": "/home/claude/imgs/seattle_rc.c.jpg"},
    mute_nat=["1027481", "1027887", "942620", "767473", "wwi_train", "wwi_march", "wwi_barracks", "wwi_drill", "wwi_rows", "ship_deck", "ship_rail", "ship_lifeboats", "rc_nurses", "rc_front", "rc_canteen"],
    training=[],
    credit=("Footage: U.S. Army, U.S. Marine Corps / AFN, U.S. Air Force via DVIDS (public domain). Archival: U.S. Army Signal Corps films (1918–1919), National Archives / Internet Archive."
            r"\NPhotos: National Archives (165-WW-269B) and National Museum of Health and Medicine (NCP 1603), public domain."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, NIH or CDC."
            r"\NFor education only. This is not medical advice."),
)
