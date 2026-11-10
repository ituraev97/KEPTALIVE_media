# KEPT ALIVE · THE SAVE 009 — How the Worst Ebola Outbreak in History Was Stopped in Liberia (2014–2015)
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty (all DVIDS, U.S. government, public domain):
#  374379 = Tubmanburg Ebola Treatment Unit walkthrough, official opening Nov. 11, 2014 (built by the Armed Forces of Liberia with DoD support) — empty, no patients
#  372199 = Monrovia Medical Unit walkthrough, Nov. 4, 2014 (before it opened) — U.S. Public Health Service staff, empty wards, a PPE run-through
#  375113 = Army engineers build an Ebola treatment unit, Liberia, Nov. 2014 (101st Airborne Division public affairs, B-roll)
#  383474 = 104th Engineer Company and Armed Forces of Liberia build an ETU at Gbediah, Liberia, Dec. 2014
#  382681 = Armed Forces of Liberia and 62nd Engineer Battalion build an ETU outside Sinje, Liberia, 2014 (DVIDS title says "ETU Training B-Roll", but the burned-in slate at 0–4 s reads: "Engineers from the Armed Forces of Liberia and Soldiers from the 62nd Engineer Battalion, Fort Hood, TX work together to build an Ebola Treatment Unit… outside of Senje, Liberia")
#  376214 = Mobile training team teaches Liberian health workers to wear PPE, Liberia, Nov. 2014 -> TRAINING
#  381629 = Ebola treatment unit training, day 4: mock ETU with simulated patients, Liberia, Nov. 2014 -> TRAINING
#  382659 = Five-day ETU training for NGO health workers from nine nations, run by U.S. Army and Air Force, Liberia, Nov.–Dec. 2014 -> TRAINING
#  391346 = 1st Area Medical Laboratory packs up its mobile lab before redeploying, Liberia, Feb. 2015
#  384510 = 2-501st Aviation Regiment "Fat Cow" refueling, first use in Operation United Assistance, Liberia, Dec. 2014
#  381205 = 2-501st Aviation Regiment CH-47 supply mission to an ETU in Ganta, Liberia, Dec. 2014
#  370135 = Dyess AFB airmen deploy for Operation United Assistance, Texas, Oct. 29, 2014
#  366907 = 36th Engineer Brigade cases its colors before deploying to Liberia, Fort Hood, Texas, Oct. 2014
#  389638 = JFC-UA service members' final medical screening before flying home, Liberia, Feb. 2, 2015
#  No patients, no bodies, no blood on screen. Burials, contact tracing and case numbers are told with our own graphics.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "THE SAVE · 009"
S = "<span style=\"color:#2BB3A3\">{}</span>"
TUB = ("TUBMANBURG EBOLA TREATMENT UNIT · LIBERIA", "OFFICIAL OPENING · NOV. 11, 2014 · NO PATIENTS YET")
MMU = ("MONROVIA MEDICAL UNIT · LIBERIA", "NOV. 4, 2014 · BEFORE OPENING · U.S. PUBLIC HEALTH SERVICE")
ENG = ("U.S. ARMY ENGINEERS BUILD AN EBOLA TREATMENT UNIT", "LIBERIA · NOV. 2014 · OPERATION UNITED ASSISTANCE")
GBE = ("ARMED FORCES OF LIBERIA + U.S. 104TH ENGINEER COMPANY", "EBOLA TREATMENT UNIT, GBEDIAH, LIBERIA · DEC. 2014")
SIN = ("ARMED FORCES OF LIBERIA + U.S. 62ND ENGINEER BATTALION", "EBOLA TREATMENT UNIT NEAR SINJE, LIBERIA · 2014")
PPE = ("LIBERIAN HEALTH WORKERS LEARN TO WEAR PROTECTIVE GEAR", "MOBILE TRAINING TEAM · LIBERIA · NOV. 2014")
SIM = ("EBOLA TREATMENT UNIT COURSE · MOCK WARD", "LIBERIA · NOV. 2014 · U.S. ARMY AND AIR FORCE TRAINERS")
LAB = ("U.S. ARMY 1ST AREA MEDICAL LABORATORY", "MOBILE EBOLA LAB · LIBERIA · FEB. 2015")
FAT = ("\"FAT COW\" HELICOPTER REFUELING", "2-501ST AVIATION REGIMENT · LIBERIA · DEC. 2014")
CH47 = ("CH-47 SUPPLY RUN TO AN EBOLA TREATMENT UNIT", "GANTA, LIBERIA · DEC. 2014 · 2-501ST AVIATION REGIMENT")
DYE = ("AIRMEN DEPLOY FOR OPERATION UNITED ASSISTANCE", "DYESS AIR FORCE BASE, TEXAS · OCT. 29, 2014")
RUG = ("36TH ENGINEER BRIGADE CASES ITS COLORS FOR LIBERIA", "FORT HOOD, TEXAS · OCT. 2014")
HOME = ("FINAL MEDICAL SCREENING BEFORE THE FLIGHT HOME", "LIBERIA · FEB. 2, 2015 · JOINT FORCES COMMAND–UNITED ASSISTANCE")

WA = [[-15.5, 4.0], [-6.5, 12.8]]            # Guinea / Sierra Leone / Liberia
MONROVIA = [-10.80, 6.30]; LOFA = [-9.75, 8.15]; GUEC = [-10.13, 8.55]
AF = [[12.0, -6.0], [35.0, 5.5]]              # DRC / Uganda
BUNIA = [30.25, 1.56]

LINES = [
 # ---------------- COLD OPEN ----------------
 ("In early September twenty fourteen, in Monrovia, the capital of Liberia, taxis filled with entire families circled the city, searching for a treatment bed.",
  [G("doc", header="MONROVIA, LIBERIA · SEPTEMBER 2014", title="NO BEDS", body="Taxis filled with entire families searched the city for a treatment bed for Ebola.",
     source="SOURCE: WORLD HEALTH ORGANIZATION, 2015", stamp="EBOLA")], dict(kind="tense")),
 ("Liberia was reporting three hundred to four hundred new Ebola cases every week. At one point, the World Health Organization says, there were virtually no treatment beds available anywhere in the country.",
  [G("stat", a="300–400", b="NEW EBOLA CASES EVERY WEEK · LIBERIA", c="AUG.–SEPT. 2014 · SOURCE: WORLD HEALTH ORGANIZATION")], dict(kind="tense")),
 ("That September, a CDC model warned that, without more action, Liberia and Sierra Leone could reach an estimated one point four million cases by January.",
  [G("stat", a="1.4 MILLION", b="CASES BY JAN. 2015 · IF NOTHING CHANGED", c="CDC MODEL, SEPT. 2014 · NO NEW INTERVENTIONS · CORRECTED FOR UNDERREPORTING · AN ESTIMATE, NOT A COUNT")], dict(kind="punch")),
 ("Eight months later, on May ninth, twenty fifteen, the World Health Organization declared Liberia free of Ebola transmission.",
  [C(381205, 51.75)], dict(tag=CH47, kind="slow", gap=0.4)),
 ("So how was the largest Ebola epidemic in history stopped in Liberia? The answer is not the one most people expect.",
  [C(374379, 124.3)], dict(tag=TUB, kind="question", gap=0.4)),
 ("Stopping Ebola. Liberia, twenty fourteen.",
  [G("title", kicker=CASE, title="STOPPING " + S.format("EBOLA"), sub="LIBERIA · 2014–2015", size=200)], dict(kind="slow", gap=2.4)),

 # ---------------- I. CONTACT ----------------
 ("To understand how it was stopped, start with how it spreads.",
  [G("chapter", case="1976–2014", n="I", t="CONTACT")], dict(gap=1.0, kind="calm")),
 ("Ebola viruses were discovered in nineteen seventy-six, in what is now the Democratic Republic of the Congo. The epidemic in West Africa was caused by one species, Zaire ebolavirus.",
  [G("stat", a="&#8203;1976", b="EBOLA VIRUSES DISCOVERED", c="DEMOCRATIC REPUBLIC OF THE CONGO · SOURCE: CDC")], dict(kind="calm")),
 ("According to the CDC, people get Ebola through contact with the body fluids of a person who is sick with it, or who has died from it. It does not spread through the air, the way flu does.",
  [G("cards3", kicker="HOW EBOLA SPREADS · CDC", title="CONTACT, NOT AIR",
     cards=[dict(h="FLUIDS", t="Of a person who is sick"), dict(h="AFTER DEATH", t="A body can still spread it", size=96), dict(h="NOT AIRBORNE", t="Not like flu or COVID", size=96)],
     footer="SOURCE: CDC, EBOLA DISEASE BASICS")], dict(kind="calm")),
 ("Symptoms can appear two to twenty-one days after contact. On average, eight to ten days.",
  [G("stat", a="2–21", b="DAYS FROM CONTACT TO SYMPTOMS", c="ON AVERAGE 8–10 DAYS · SOURCE: CDC")], dict(kind="calm", gap=0.4)),
 ("That put two kinds of work at the front line. Caring for the sick. And burying the dead.",
  [C(376214, 102.2), C(376214, 115.8)], dict(tag=PPE, kind="slow", gap=0.5)),
 ("According to the CDC, the first case was reported in Guinea, in December twenty thirteen. On March thirtieth, twenty fourteen, Ebola was reported in Liberia, in Lofa County.",
  [G("map", map=dict(bounds=WA, highlight={430: "#0E3A35", 324: "#13242A", 694: "#13242A"},
     cities=[dict(ll=GUEC, name="GUINEA", sub="FIRST CASE · DEC. 2013", d=0.3, color="#EEF2EF"),
             dict(ll=LOFA, name="LOFA COUNTY", sub="LIBERIA · MARCH 30, 2014", d=0.8, color="#6CF29A", dy=70),
             dict(ll=MONROVIA, name="MONROVIA", sub="CAPITAL", d=1.3, color="#EEF2EF", anchor="end")]),
     kicker="WEST AFRICA · 2013–2014", title="THE SPREAD", footer="SOURCES: CDC · EMERGING INFECTIOUS DISEASES, 2016")], dict(kind="drive")),
 ("Then it reached the capital. Monrovia.",
  [G("map", map=dict(bounds=WA, highlight={430: "#0E3A35"}, rings=[dict(ll=MONROVIA, r=40, n=3, d=0.5)],
     cities=[dict(ll=MONROVIA, name="MONROVIA", sub="CAPITAL OF LIBERIA", d=0.3, color="#6CF29A", anchor="end")]),
     kicker="LIBERIA · 2014", title="THE CAPITAL", footer="SOURCE: WORLD HEALTH ORGANIZATION, 2015")], dict(kind="slow", gap=0.6)),

 # ---------------- II. NO BEDS ----------------
 ("And the capital had almost nowhere to put the sick.",
  [G("chapter", case="JULY–SEPTEMBER 2014", n="II", t="NO BEDS")], dict(gap=1.0, kind="calm")),
 ("By mid-July twenty fourteen, Liberia had only two Ebola treatment units running. Twenty beds each.",
  [G("stat", a="2", b="EBOLA TREATMENT UNITS RUNNING IN LIBERIA", c="MID-JULY 2014 · 20 BEDS EACH · SOURCE: EMERGING INFECTIOUS DISEASES, 2016")], dict(kind="calm")),
 ("In mid-August, a WHO team estimated that a thousand beds were needed, just for the patients already infected. Only two hundred forty were available.",
  [G("phases", kicker="WHO ASSESSMENT · MID-AUGUST 2014", title="THE BED GAP", left=dict(label="NEEDED (ESTIMATED)", num="1,000", desc="BEDS"),
     right=dict(label="AVAILABLE", num="240", desc="BEDS"), active=1, footer="SOURCE: WORLD HEALTH ORGANIZATION, 2015")], dict(kind="tense")),
 ("On August seventeenth, Doctors Without Borders opened a new hundred-and-twenty-bed Ebola center in Monrovia, called ELWA three. In its first week, it was already full.",
  [G("doc", header="MONROVIA · AUGUST 17, 2014", title="ELWA 3", body="A new 120-bed Ebola center run by Doctors Without Borders (MSF). In its first week: \"already at capacity with 120 patients.\"",
     source="SOURCE: MSF, AUG. 27, 2014", stamp="FULL")], dict(kind="calm")),
 ("Patients were turned away. Many died on hospital grounds, in city streets, or in their homes.",
  [G("quote", q="…Ebola patients were turned away, often dying on hospital grounds, in city streets, or in their homes.", w="NYENSWAH ET AL. · EMERGING INFECTIOUS DISEASES (CDC) · 2016")], dict(kind="slow", gap=0.6)),
 ("Health workers were hit hard. In Liberia, three hundred seventy-eight were infected, and one hundred ninety-two died. The country lost eight percent of its doctors, nurses and midwives.",
  [G("phases", kicker="LIBERIA · 2014–2015", title="HEALTH WORKERS", left=dict(label="INFECTED", num="378", desc="CONFIRMED"),
     right=dict(label="DIED", num="192", desc="8% OF DOCTORS, NURSES AND MIDWIVES LOST"), active=1, footer="SOURCES: EMERGING INFECTIOUS DISEASES, 2016 · CDC")], dict(kind="slow", gap=0.6)),

 # ---------------- III. THE CALL ----------------
 ("Then, the United States made a decision.",
  [G("chapter", case="SEPTEMBER 16, 2014", n="III", t="THE CALL")], dict(gap=1.0, kind="calm")),
 ("On September sixteenth, twenty fourteen, President Barack Obama spoke at the CDC in Atlanta. He described the epidemic bluntly. It's spiraling out of control, he said. It is getting worse.",
  [G("quote", q="It's spiraling out of control. It is getting worse.", w="PRESIDENT BARACK OBAMA · CDC, ATLANTA · SEPT. 16, 2014")], dict(kind="tense")),
 ("He announced a military command center in Liberia, to support civilian efforts across the region, and an air bridge to get health workers and supplies into West Africa faster. The White House said an estimated three thousand U.S. forces would go.",
  [G("callcard", kicker="WHITE HOUSE FACT SHEET · SEPT. 16, 2014", title="THE U.S. RESPONSE",
     rows=[["COMMAND", "Joint Force Command, Monrovia"], ["FORCES", "An estimated 3,000"], ["TRAINING", "Up to 500 health care providers a week"]],
     footer="SOURCE: THE WHITE HOUSE (ARCHIVED)")], dict(kind="drive")),
 ("But the Pentagon was clear about one thing. The U.S. military would not provide direct care to Ebola patients.",
  [G("quote", q="The U.S. military will not provide direct care to Ebola patients.", w="REAR ADM. JOHN KIRBY · PENTAGON PRESS SECRETARY · 2014")], dict(kind="punch", gap=0.4)),
 ("Its job was the kind of work militaries do well. Moving things. Testing. Building. Training.",
  [G("steps", kicker="THE MILITARY'S ROLE", title="NO PATIENT CARE. FOUR JOBS.",
     items=[["LIFT", "Airlift and helicopters"], ["TEST", "Mobile labs"], ["BUILD", "Treatment units"], ["TRAIN", "Health workers"]],
     footer="SOURCES: THE WHITE HOUSE · U.S. DEPARTMENT OF DEFENSE")], dict(kind="drive")),
 ("The mission was called Operation United Assistance. It was the Defense Department's part of a wider effort, led by the U.S. Agency for International Development.",
  [C(370135, 4.2), C(370135, 13.75)], dict(tag=DYE, kind="calm")),
 ("Engineers went too. At Fort Hood, Texas, the thirty-sixth Engineer Brigade cased its colors and prepared to deploy to Liberia.",
  [C(366907, 40.0), C(366907, 92.0)], dict(tag=RUG, kind="calm")),
 ("In late October, the headquarters of the hundred-and-first Airborne Division took over the command in Liberia, under Major General Gary Volesky. At the peak, about two thousand eight hundred Defense Department personnel were deployed to West Africa.",
  [G("stat", a="2,800", b="DEFENSE DEPARTMENT PERSONNEL IN WEST AFRICA", c="AT THE PEAK · SOURCES: DOD NEWS · AIR & SPACE FORCES MAGAZINE, 2015")], dict(kind="calm", gap=0.6)),

 # ---------------- IV. FOUR JOBS ----------------
 ("And they went to work.",
  [G("chapter", case="SEPTEMBER 2014–FEBRUARY 2015", n="IV", t="TEST. BUILD. TRAIN.")], dict(gap=1.0, kind="calm")),
 ("First, testing. Early in the epidemic, confirming a case of Ebola could take as long as a week.",
  [C(391346, 53.8)], dict(tag=LAB, kind="calm")),
 ("On September twenty-ninth, mobile labs from the Navy's Naval Medical Research Center landed in Liberia. By October second, they were receiving samples in Monrovia.",
  [G("timeline", kicker="NAVAL MEDICAL RESEARCH CENTER", title="MOBILE LABS",
     events=[dict(y="SEPT. 29", t="Labs land in Liberia"), dict(y="OCT. 2", t="Receiving samples, Monrovia"), dict(y="OCT. 3", t="Bong County"), dict(y="MARCH 2015", t="5,300+ samples")],
     footer="SOURCE: NAVY MEDICINE, 2024")], dict(kind="drive")),
 ("They cut the wait for a result from seven days to less than four hours.",
  [G("phases", kicker="EBOLA TEST RESULTS · LIBERIA", title="FROM DAYS TO HOURS", left=dict(label="BEFORE", num="7", desc="DAYS"),
     right=dict(label="WITH THE NAVY LABS", num="<4", desc="HOURS"), active=1, footer="SOURCE: NAVY MEDICINE, 2024")], dict(kind="punch")),
 ("Army labs joined them. The command set up four Army mobile testing labs across Liberia. Here, soldiers of the first Area Medical Laboratory pack up their lab before heading home.",
  [C(391346, 61.7), C(391346, 69.95)], dict(tag=LAB, kind="calm", gap=0.4)),
 ("Second, building. U.S. Army engineers built Ebola treatment units, often working alongside the Armed Forces of Liberia.",
  [C(375113, 9.1), C(375113, 26.95)], dict(tag=ENG, kind="drive")),
 ("Near Sinje, Liberian army engineers worked with soldiers of the sixty-second Engineer Battalion.",
  [C(382681, 44.8), C(382681, 52.3)], dict(tag=SIN, kind="calm")),
 ("At Gbediah, in December, the hundred-and-fourth Engineer Company built a treatment unit with Liberian troops.",
  [C(383474, 8.6), C(383474, 48.6)], dict(tag=GBE, kind="calm")),
 ("Some sites were so far out that Army helicopter crews used a refueling method called Fat Cow, a helicopter carrying fuel to the field, just to fly far enough to reach them.",
  [C(384510, 43.9), C(384510, 49.8)], dict(tag=FAT, kind="drive")),
 ("Chinooks flew supplies to treatment units like the one in Ganta, near the border with Guinea.",
  [C(381205, 11.7), C(381205, 41.7)], dict(tag=CH47, kind="calm")),
 ("On November eleventh, the treatment unit at Tubmanburg officially opened. It was built by the Armed Forces of Liberia, with support and oversight from the U.S. Department of Defense.",
  [C(374379, 134.3), C(374379, 160.5)], dict(tag=TUB, kind="calm", gap=0.4)),
 ("Third, a hospital for the healers. Navy Seabees, soldiers and airmen built the Monrovia Medical Unit. Twenty-five beds, for health workers who caught Ebola.",
  [C(372199, 16.5), C(372199, 276.5)], dict(tag=MMU, kind="calm")),
 ("It was run not by the military, but by the U.S. Public Health Service Commissioned Corps, in four rotations of seventy people. It was the only Ebola treatment unit in Africa dedicated to health care workers.",
  [G("doc", header="MONROVIA · NOVEMBER 2014", title="MONROVIA MEDICAL UNIT", body="25 beds for health care workers. Built by Navy Seabees, soldiers and airmen. Run by the U.S. Public Health Service Commissioned Corps.",
     source="SOURCES: DVIDS · FEDERAL PRACTITIONER, 2017", stamp="25 BEDS")], dict(kind="calm")),
 ("Fourth, training. U.S. trainers taught health workers how to put on and take off protective equipment, step by step.",
  [C(376214, 6.2), C(376214, 102.2)], dict(tag=PPE, kind="calm")),
 ("And they walked them through mock treatment wards, before the real thing.",
  [C(381629, 35.3)], dict(tag=SIM, kind="calm")),
 ("By the end of the mission, the division said it had trained more than fifteen hundred health care workers in Liberia.",
  [G("stat", a="1,500+", b="HEALTH CARE WORKERS TRAINED", c="BY U.S. FORCES IN LIBERIA · SOURCE: ARMY.MIL, 2015")], dict(kind="calm")),
 ("In all, the hundred-and-first said its joint force built and supported seventeen treatment units in Liberia. Other official counts are lower, depending on who built which unit.",
  [G("stat", a="17", b="TREATMENT UNITS BUILT AND SUPPORTED", c="101ST AIRBORNE DIVISION'S COUNT · OTHER COUNTS ARE LOWER · SOURCE: ARMY.MIL, 2015")], dict(kind="calm", gap=0.6)),

 # ---------------- V. THE TURN ----------------
 ("And here is the part of the story that often gets left out.",
  [G("chapter", case="WHAT REALLY HAPPENED", n="V", t="THE TURN")], dict(gap=1.0, kind="calm")),
 ("Liberia's epidemic had started to slow before most of those units opened. A CDC report published in November twenty fourteen noted a decrease in cases since mid-September.",
  [G("doc", header="CDC · MMWR · NOVEMBER 2014", title="ALREADY FALLING", body="\"There has been a decrease in cases since mid-September.\"",
     source="SOURCE: CDC MMWR, 2014")], dict(kind="calm")),
 ("By late September, treatment-bed capacity in Liberia had overtaken the number of new cases. And as the epidemic waned, many treatment units were underused, and three never opened.",
  [G("quote", q="…of which 3 never opened and many remained underutilized as the epidemic waned.", w="NYENSWAH ET AL. · EMERGING INFECTIOUS DISEASES (CDC) · 2016")], dict(kind="calm")),
 ("In twenty fifteen, The New York Times reported that the eleven treatment units the U.S. built in Liberia had treated only twenty-eight Ebola patients.",
  [G("stat", a="28", b="EBOLA PATIENTS IN 11 U.S.-BUILT UNITS", c="AS REPORTED BY THE NEW YORK TIMES, VIA STARS AND STRIPES, 2015")], dict(kind="punch", gap=0.6)),
 ("So what actually turned the tide? Researchers and health agencies point to Liberians themselves.",
  [C(383474, 21.5), C(383474, 8.6)], dict(tag=GBE, kind="question")),
 ("A study in the CDC's journal, Emerging Infectious Diseases, puts it simply. Community engagement resulted in remarkable behavior change.",
  [G("quote", q="Community engagement resulted in remarkable behavior change.", w="NYENSWAH ET AL. · EMERGING INFECTIOUS DISEASES (CDC) · 2016")], dict(kind="slow")),
 ("Burials changed. Because a body can still spread Ebola, safe burials mattered. Liberia went from fewer than ten burial teams in August, to fifty-four trained and equipped teams by October fifth.",
  [G("phases", kicker="LIBERIA · 2014", title="SAFE BURIAL TEAMS", left=dict(label="AUGUST", num="<10", desc="TEAMS"),
     right=dict(label="BY OCTOBER 5", num="54", desc="TRAINED AND EQUIPPED"), active=1, footer="SOURCE: CDC MMWR, NOVEMBER 2014")], dict(kind="drive")),
 ("Teams tried to trace everyone who had been in contact with a patient. The same study notes that contact tracing generally depended on paper and Excel spreadsheets.",
  [G("doc", header="LIBERIA · 2014–2015", title="CONTACT TRACING", body="\"Contact tracing generally depended on paper and Excel … spreadsheets maintained at the county level.\"",
     source="SOURCE: EMERGING INFECTIOUS DISEASES, 2016", stamp="PAPER")], dict(kind="calm")),
 ("And isolation worked, even outside the big treatment units. The CDC estimated that, from September twenty-third to October thirty-first, isolating patients in treatment units, community care centers, and similar settings prevented about nine thousand cases in Liberia.",
  [G("stat", a="9,097", b="CASES PREVENTED IN LIBERIA (ESTIMATED)", c="SEPT. 23–OCT. 31, 2014 · ISOLATION IN ETUs, COMMUNITY CARE CENTERS AND SIMILAR SETTINGS · SOURCE: CDC MMWR")], dict(kind="calm")),
 ("So what did the U.S. military add? The Emerging Infectious Diseases study gives its verdict. The deployment of the U.S. military provided a logistic and psychological boost.",
  [G("quote", q="The deployment of the US military provided a logistic and psychological boost.", w="NYENSWAH ET AL. · EMERGING INFECTIOUS DISEASES (CDC) · 2016")], dict(kind="slow", gap=0.6)),

 # ---------------- VI. ZERO ----------------
 ("Week by week, the numbers fell.",
  [G("chapter", case="2015–2016", n="VI", t="ZERO")], dict(gap=1.0, kind="calm")),
 ("By March twenty fifteen, Liberia was down to fewer than two new cases a week.",
  [G("phases", kicker="NEW EBOLA CASES IN LIBERIA", title="FROM HUNDREDS TO ALMOST NONE", left=dict(label="SEPTEMBER 2014", num="100s", desc="A WEEK"),
     right=dict(label="MARCH 2015", num="<2", desc="A WEEK"), active=1, footer="SOURCE: DEFENSE HEALTH AGENCY, 2026")], dict(kind="drive")),
 ("The last confirmed patient was buried on March twenty-eighth. Forty-two days later, twice the longest incubation period, on May ninth, twenty fifteen, the WHO declared Liberia free of Ebola transmission.",
  [G("timeline", kicker="LIBERIA", title="COUNTING TO ZERO",
     events=[dict(y="MAR. 28", t="Last confirmed case buried"), dict(y="+42 DAYS", t="Twice the maximum incubation"), dict(y="MAY 9", t="WHO: free of transmission"), dict(y="2016", t="Final end: June 9")],
     footer="SOURCES: WHO, 2015 AND 2016 · CDC")], dict(kind="slow")),
 ("It wasn't quite over. The virus flared up again, more than once. The WHO declared the end of Liberia's last outbreak on June ninth, twenty sixteen.",
  [G("stat", a="JUNE 9", b="LIBERIA'S LAST EBOLA OUTBREAK DECLARED OVER", c="2016 · SOURCE: WORLD HEALTH ORGANIZATION")], dict(kind="calm", gap=0.4)),
 ("By then, the U.S. troops had long gone home. Before boarding, they went through final medical screening. Back in the United States, each spent twenty-one days in controlled monitoring.",
  [C(389638, 10.0), C(389638, 30.0)], dict(tag=HOME, kind="calm")),
 ("In February twenty fifteen, the hundred-and-first cased its colors in Monrovia. General Volesky said: the fight to get to zero Ebola cases will continue.",
  [G("quote", q="…the fight to get to zero Ebola cases will continue.", w="MAJ. GEN. GARY VOLESKY · MONROVIA · FEBRUARY 2015 · VIA ARMY.MIL")], dict(kind="slow", gap=0.5)),
 ("Across Guinea, Liberia and Sierra Leone, the epidemic caused about twenty-eight thousand six hundred cases, and more than eleven thousand three hundred deaths. In Liberia alone, according to the CDC, ten thousand six hundred seventy-eight cases, and four thousand eight hundred ten deaths.",
  [G("phases", kicker="WEST AFRICA · 2014–2016", title="THE TOLL", left=dict(label="CASES", num="28,616", desc="GUINEA, LIBERIA, SIERRA LEONE"),
     right=dict(label="DEATHS", num="11,310", desc="LIBERIA: 10,678 CASES · 4,810 DEATHS"), active=1, footer="SOURCE: CDC")], dict(kind="slow", gap=0.8)),

 # ---------------- WHAT CHANGED ----------------
 ("What changed after Liberia?",
  [G("chapter", case="2015–TODAY", n="VII", t="AFTER")], dict(gap=1.0, kind="question")),
 ("In twenty fifteen, a vaccine trial in Guinea tested ring vaccination, vaccinating people around each new case. Its first results suggested high protection.",
  [G("doc", header="GUINEA · 2015", title="RING VACCINATION TRIAL", body="Over 7,500 participants. Interim results published in The Lancet suggested high protection.",
     source="SOURCE: LONDON SCHOOL OF HYGIENE & TROPICAL MEDICINE")], dict(kind="calm")),
 ("In December twenty nineteen, the FDA approved Ervebo, the first FDA-approved vaccine for Ebola. In twenty twenty, it approved two treatments, Inmazeb and Ebanga.",
  [G("cards3", kicker="U.S. FOOD AND DRUG ADMINISTRATION", title="APPROVED SINCE 2019",
     cards=[dict(h="ERVEBO", t="Vaccine · Dec. 2019"), dict(h="INMAZEB", t="Treatment · Oct. 2020"), dict(h="EBANGA", t="Treatment · Dec. 2020")],
     footer="ALL FOR ZAIRE EBOLAVIRUS · SOURCE: FDA")], dict(kind="calm")),
 ("But all three are for one species, Zaire ebolavirus. And today, a different one is spreading.",
  [G("stat", a="ZAIRE", b="THE SPECIES THESE PRODUCTS TARGET", c="SOURCE: FDA")], dict(kind="tense", gap=0.4)),
 ("In May twenty twenty-six, the Democratic Republic of the Congo and Uganda declared outbreaks of Bundibugyo virus disease. As of November sixth, the CDC counts ten thousand nine hundred ten confirmed cases, and five thousand three hundred six deaths, almost all of them in Congo.",
  [G("map", map=dict(bounds=AF, highlight={180: "#0E3A35", 800: "#13242A"},
     cities=[dict(ll=BUNIA, name="DR CONGO + UGANDA", sub="BUNDIBUGYO VIRUS · DECLARED MAY 15, 2026", d=0.3, color="#6CF29A", anchor="end")]),
     kicker="AS OF NOV. 6, 2026 · CDC", title="10,910 CASES · 5,306 DEATHS (CONFIRMED)", footer="SOURCES: CDC · CDC MMWR, 2026")], dict(kind="calm")),
 ("In June, the CDC reported that no medications or vaccines against it had been approved. The CDC also says the risk to the American public remains low.",
  [G("callcard", kicker="CDC · 2026", title="BUNDIBUGYO VIRUS DISEASE",
     rows=[["VACCINES", "None approved"], ["MEDICATIONS", "None approved · supportive care"], ["RISK TO U.S. PUBLIC", "Low, according to the CDC"]],
     footer="SOURCES: CDC MMWR, JUNE 2026 · CDC CURRENT SITUATION, NOV. 2026")], dict(kind="calm", gap=0.5)),
 ("The tools that worked in Liberia still matter. Fast labs. Beds. Safe burials. Contact tracing. And the trust of communities.",
  [C(372199, 202.0), C(372199, 207.0)], dict(tag=MMU, kind="slow")),
 ("In twenty fourteen, the help that came from outside was real. But when Liberia reached zero, the WHO put it plainly. It is a tribute to the government and people of Liberia.",
  [G("quote", q="It is a tribute to the government and people of Liberia.", w="WORLD HEALTH ORGANIZATION · MAY 9, 2015")], dict(kind="slow", gap=0.9)),
 ("If this story surprised you, subscribe. Next time on Kept Alive: penicillin. The mold that went to war.",
  [G("stat", a="NEXT", b="PENICILLIN: THE MOLD THAT WENT TO WAR", c="KEPT ALIVE · FIRST")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · THE SAVE 009", stamp="STOPPING EBOLA")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("twenty fourteen", "2014"), ("twenty fifteen", "2015"), ("twenty sixteen", "2016"), ("twenty thirteen", "2013"), ("twenty nineteen", "2019"), ("twenty twenty-six", "2026"), ("twenty twenty", "2020"),
 ("nineteen seventy-six", "1976"), ("three hundred to four hundred", "300 to 400"), ("one point four million", "1.4 million"), ("May ninth", "May 9"), ("March thirtieth", "March 30"),
 ("two to twenty-one days", "2 to 21 days"), ("eight to ten days", "8 to 10 days"), ("twenty-one days", "21 days"), ("Twenty beds each", "20 beds each"),
 ("a thousand beds", "1,000 beds"), ("two hundred forty", "240"), ("August seventeenth", "August 17"), ("hundred-and-twenty-bed", "120-bed"), ("ELWA three", "ELWA 3"),
 ("three hundred seventy-eight", "378"), ("one hundred ninety-two", "192"), ("eight percent", "8%"), ("September sixteenth", "September 16"),
 ("three thousand", "3,000"), ("thirty-sixth", "36th"), ("hundred-and-first", "101st"), ("two thousand eight hundred", "2,800"),
 ("September twenty-ninth", "September 29"), ("October second", "October 2"), ("seven days", "7 days"), ("four hours", "4 hours"), ("first Area Medical Laboratory", "1st Area Medical Laboratory"),
 ("four Army mobile testing labs", "4 Army mobile testing labs"), ("sixty-second", "62nd"), ("hundred-and-fourth", "104th"), ("November eleventh", "November 11"), ("Twenty-five beds", "25 beds"), ("four rotations of seventy people", "4 rotations of 70 people"),
 ("fifteen hundred", "1,500"), ("seventeen", "17"), ("eleven treatment units", "11 treatment units"), ("twenty-eight", "28"), ("fewer than ten", "fewer than 10"), ("fifty-four", "54"),
 ("October fifth", "October 5"), ("September twenty-third", "September 23"), ("October thirty-first", "October 31"), ("about nine thousand", "about 9,000"),
 ("fewer than two", "fewer than 2"), ("March twenty-eighth", "March 28"), ("Forty-two days", "42 days"), ("June ninth", "June 9"),
 ("twenty-eight thousand six hundred", "28,600"), ("eleven thousand three hundred", "11,300"), ("ten thousand six hundred seventy-eight", "10,678"), ("four thousand eight hundred ten", "4,810"),
 ("November sixth", "November 6"), ("ten thousand nine hundred ten", "10,910"), ("five thousand three hundred six", "5,306"), ("Kept Alive", "KEPT ALIVE"), ("Eight months", "8 months"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · THE SAVE",
    title="Stopping Ebola",
    voice="am_fenrir",
    imgs={},
    mute_nat=["374379", "372199", "375113", "383474", "382681", "376214", "381629", "391346", "384510", "381205", "370135", "366907", "389638"],
    training=["376214", "381629"],
    credit=("Footage: U.S. Army, U.S. Air Force via DVIDS (public domain); training footage marked TRAINING."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, NIH, CDC or WHO."
            r"\NFor education only. This is not medical advice."),
)

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))  # longest first
