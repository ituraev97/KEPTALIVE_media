# KEPT ALIVE · HOW IT WORKS 011 — How the Army Builds a Hospital in 72 Hours, From MASH to Today
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  mash_a..d = excerpts of U.S. Army Signal Corps film "8209 Mobile Army Surgical Hospital (MASH)", Korea, July 1951 (NARA 111-ADC-9535, catalog 23300, public domain)
#             — only ambulances, the MASH sign, the RECEIVING tent and a surgeon scrubbing are used; no patient shots.
#  745637 = 531st Hospital Center sets up workstations, Javits New York Medical Station, April 2020 (time-lapse, DVIDS, Chief Petty Officer Barry Riley, DoD Support to FEMA)
#  745000 = 47th CSH / 627th Hospital Center begin setup, CenturyLink Field Event Center, Seattle, March 30, 2020 (DVIDS, Pfc. Matthew Marsilia)
#  557722 / 557756 / 557923 = 14th Combat Support Hospital arrives and sets up in Humacao, Puerto Rico, Oct. 9–11, 2017 (DVIDS, Pfc. William Dickinson)
#  152551 = 325th CSH sets up tents for MEDEX 2012 near Camp Zama, Japan (exercise, DVIDS, Jay Mann) — TRAINING
#  810388 = 348th / 378th Field Hospitals and 410th Hospital Center field hospital setup training, 2021 (DVIDS, Nicholas Nystedt) — TRAINING
#  996410 = 512th Field Hospital field training exercise, Rhine Ordnance Barracks, Germany, Feb. 2026 (DVIDS, Sgt. Elijah Campbell) — TRAINING, manikins only
#  1000528 = 11th Field Hospital collective training, Fort McCoy, Wis., March 2026 (DVIDS, Greg Mason) — TRAINING, exterior + manikin ward only
#  No patient is named. No wounds, blood or patients' faces on screen. Training footage carries the TRAINING EXERCISE badge.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "HOW IT WORKS · 011"
S = "<span style=\"color:#2BB3A3\">{}</span>"
MASH = ("8209TH MOBILE ARMY SURGICAL HOSPITAL", "KOREA · 1951 · U.S. ARMY SIGNAL CORPS FILM · NATIONAL ARCHIVES")
JAV = ("SOLDIERS SET UP LAB, X-RAY AND PHARMACY STATIONS", "JAVITS CENTER · NEW YORK · APRIL 2020 · TIME-LAPSE")
SEA = ("AN ARMY HOSPITAL ARRIVES BY TRUCK AND CONTAINER", "CENTURYLINK FIELD EVENT CENTER · SEATTLE · MARCH 30, 2020")
PR1 = ("14TH COMBAT SUPPORT HOSPITAL ARRIVES AFTER HURRICANE MARIA", "PUERTO RICO · OCTOBER 10, 2017")
PR2 = ("SOLDIERS UNLOAD SUPPLIES FOR THE FIELD HOSPITAL", "HUMACAO, PUERTO RICO · OCTOBER 2017")
PR3 = ("A FIELD HOSPITAL GOES UP INSIDE THE HUMACAO ARENA", "HUMACAO, PUERTO RICO · OCTOBER 11, 2017")
JPN = ("A COMBAT SUPPORT HOSPITAL PUTS UP ITS TENTS", "NEAR CAMP ZAMA, JAPAN · 2012 · MEDEX EXERCISE")
RES = ("ARMY RESERVE FIELD HOSPITALS PRACTICE BUILDING FROM SCRATCH", "U.S. ARMY RESERVE · 2021")
G512 = ("512TH FIELD HOSPITAL FIELD TRAINING EXERCISE", "KAISERSLAUTERN, GERMANY · FEBRUARY 2026")
PR4 = ("14TH CSH BEGINS SETTING UP ITS FIELD HOSPITAL", "HUMACAO, PUERTO RICO · OCTOBER 9, 2017")
F11 = ("11TH FIELD HOSPITAL COLLECTIVE TRAINING", "FORT MCCOY, WISCONSIN · MARCH 2026")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("How does the Army build a hospital in seventy-two hours? It brings the whole hospital with it.",
  [C(745637, 11.0), C(745637, 30.0)], dict(tag=JAV, kind="punch")),
 ("In November twenty seventeen, in an Army test, hospital units deployed from Fort Carson, Colorado, to Fort Polk, Louisiana. Within seventy-two hours, they had hospital care with surgery and intensive care up and running.",
  [G("stat", a="72", b="HOURS TO ESTABLISH ROLE 3 HOSPITAL CARE", c="ARMY TEST · FORT POLK, LOUISIANA · NOV. 2017 · SOURCE: ARMY SUSTAINMENT")], dict(kind="drive")),
 ("Tents, beds, operating rooms, intensive care, a lab, x-ray, a pharmacy. All of it packed to travel by truck and container.",
  [C(745000, 25.0), C(745000, 44.0)], dict(tag=SEA, kind="calm")),
 ("The idea is older than most people think. Its most famous version had a nickname you probably know from television.",
  [C("mash_c", 6.0)], dict(tag=MASH, kind="question", gap=0.4)),
 ("This is how a field hospital works. From the MASH to today.",
  [G("title", kicker=CASE, title="FIELD HOSPITAL", sub="FROM MASH TO " + S.format("72 HOURS"), size=200)], dict(kind="slow", gap=2.4)),

 # ---------------- I. THE MASH ----------------
 ("Start with the Second World War, then Korea.",
  [G("chapter", case="1945 · KOREA 1950–1953", n="I", t="THE MASH")], dict(gap=1.0, kind="calm")),
 ("In World War Two, the Army ran evacuation hospitals in the theater of operations. A nineteen forty-five War Department film shows how one worked.",
  [G("doc", header="WAR DEPARTMENT FILM BULLETIN 173 · 1945", title="THE EVACUATION HOSPITAL", body="Tents and equipment set up, a water supply built, casualties received, transfusions given, X-rays made.",
     source="SOURCE: NATIONAL ARCHIVES DESCRIPTION", stamp="1945")], dict(kind="calm")),
 ("Troops pitched the tents and built a water supply. Casualties came in through a receiving tent. Then patients moved on, by plane and train to general hospitals, and by ship to the United States.",
  [G("steps", kicker="WORLD WAR II · EVACUATION HOSPITAL", title="THE CHAIN OF CARE", items=[["BUILD", "Tents and a water supply"], ["RECEIVE", "The receiving tent"], ["TREAT", "Surgery, X-rays, labs"], ["MOVE ON", "Plane, train, ship"]],
     footer="SOURCE: NATIONAL ARCHIVES · FILM BULLETIN 173 (1945)")], dict(kind="drive")),
 ("That idea, receive, treat, and move patients on, is still the core of a field hospital. In Korea, the Army relied on a smaller surgical hospital built to follow the troops.",
  [C("mash_a", 4.0)], dict(tag=MASH, kind="calm")),
 ("In the Korean War, the U.S. Army used Mobile Army Surgical Hospitals. MASH units. Small surgical hospitals that could follow an army in the field.",
  [C("mash_b", 4.0), C("mash_b", 20.0)], dict(tag=MASH, kind="calm")),
 ("This is real Army film of one of them, the eighty-two oh ninth MASH, shot by the Signal Corps in Korea in nineteen fifty-one.",
  [C("mash_c", 16.0)], dict(tag=MASH, kind="calm")),
 ("A year later, in August nineteen fifty-two, a photo caption placed the same unit about twenty miles from the front lines.",
  [G("stat", a="20", b="MILES FROM THE FRONT LINES — THE 8209TH MASH", c="AUGUST 1952 PHOTO CAPTION · SOURCE: DEFENSE MEDIA NETWORK")], dict(kind="calm")),
 ("In Korea, MASH units were first planned as sixty-bed hospitals. Britannica notes that moving a MASH took fifty large trucks.",
  [G("phases", kicker="MOBILE ARMY SURGICAL HOSPITAL", title="BUILT TO MOVE", left=dict(label="PLANNED SIZE", num="60", desc="BEDS"),
     right=dict(label="TO MOVE IT", num="50", desc="LARGE TRUCKS"), active=1, footer="SOURCES: BRITANNICA · DEFENSE MEDIA NETWORK")], dict(kind="drive")),
 ("But the war sent them so many wounded that some MASH units grew to two hundred beds.",
  [G("stat", a="200", b="BEDS — WHAT SOME MASH UNITS GREW TO", c="ORIGINALLY PLANNED FOR 60 · SOURCE: DEFENSE MEDIA NETWORK")], dict(kind="tense")),
 ("Casualties arrived by ambulance at a tent marked receiving.",
  [C("mash_c", 22.0), C("mash_c", 30.5)], dict(tag=MASH, kind="calm")),
 ("Inside, surgeons scrubbed in under bare bulbs, in canvas tents. Almost all of them were civilian doctors who had been drafted. By nineteen fifty-two, ninety percent of doctors in Korea were draftees.",
  [C("mash_d", 4.0), G("stat", a="90%", b="OF DOCTORS IN KOREA WERE DRAFTEES BY 1952", c="SOURCE: DEFENSE MEDIA NETWORK")], dict(tag=MASH, kind="calm")),
 ("And Korea added something new: the helicopter. Helicopters carried more than twenty thousand casualties during the war.",
  [G("stat", a="20,000+", b="CASUALTIES CARRIED BY HELICOPTER IN KOREA", c="SOURCE: DEFENSE MEDIA NETWORK")], dict(kind="drive")),
 ("In nineteen fifty-one, three helicopter detachments were attached to MASH units. On one day that February, about seven hundred fifty critically wounded soldiers were evacuated. The Eighth Army surgeon estimated that half of them would have died if only ground transport had been used.",
  [G("stat", a="750", b="CRITICALLY WOUNDED EVACUATED ON FEB. 20, 1951", c="EIGHTH ARMY SURGEON'S ESTIMATE: HALF WOULD HAVE DIED BY GROUND ALONE · SOURCE: DEFENSE MEDIA NETWORK")], dict(kind="tense")),
 ("Defense Media Network reports that the death rate among seriously wounded soldiers fell from about four and a half percent in the Second World War to about two and a half percent in Korea. Faster evacuation and medical advances are credited.",
  [G("phases", kicker="SERIOUSLY WOUNDED · FATALITY RATE", title="WORLD WAR II VS. KOREA", left=dict(label="WORLD WAR II", num="4.5%", desc="ABOUT"),
     right=dict(label="KOREA", num="2.5%", desc="ABOUT"), active=1, footer="AS REPORTED · SOURCE: DEFENSE MEDIA NETWORK")], dict(kind="slow")),
 ("One of those drafted surgeons, Richard Hornberger, served in the eighty fifty-fifth MASH. In nineteen sixty-eight, he published a novel based on it. It became the film and the TV comedy M.A.S.H.",
  [G("timeline", kicker="FROM A TENT TO TELEVISION", title="THE 8055TH MASH",
     events=[dict(y="1950s", t="A draftee surgeon in Korea"), dict(y="1968", t="The novel"), dict(y="Later", t="The film and TV comedy")],
     footer="SOURCES: DEFENSE MEDIA NETWORK · ARMY.MIL")], dict(kind="calm", gap=0.5)),

 # ---------------- II. THE CSH ----------------
 ("The MASH lasted far longer than the war that made it famous.",
  [G("chapter", case="1953–2017", n="II", t="BIGGER HOSPITALS")], dict(gap=1.0, kind="calm")),
 ("Britannica notes MASH units were still in service in the Persian Gulf War, in nineteen ninety and ninety-one.",
  [G("doc", header="PERSIAN GULF WAR · 1990–1991", title="THE MASH STILL SERVES", body="Mobile Army Surgical Hospitals were still in service during the Gulf War.",
     source="SOURCE: BRITANNICA")], dict(kind="calm")),
 ("But during the Vietnam War, the Army began replacing its mobile surgical and evacuation hospitals with a new design: the combat support hospital, or C.S.H.",
  [G("doc", header="VIETNAM WAR ERA", title="THE COMBAT SUPPORT HOSPITAL", body="Combat support hospitals replace mobile surgical and evacuation hospitals.",
     source="SOURCE: ARMY SUSTAINMENT, 2018", stamp="CSH")], dict(kind="calm")),
 ("A full combat support hospital had two hundred forty-eight beds, split into two companies. One with a hundred sixty-four beds, one with eighty-four.",
  [G("phases", kicker="COMBAT SUPPORT HOSPITAL", title="248 BEDS IN TWO PIECES", left=dict(label="COMPANY A", num="164", desc="BEDS"),
     right=dict(label="COMPANY B", num="84", desc="BEDS"), footer="SOURCES: ARMY SUSTAINMENT · ARMY.MIL")], dict(kind="drive")),
 ("The last MASH lasted until two thousand six. On October sixteenth that year, in Germany, the two hundred twelfth MASH became a combat support hospital. Its last deployment had been to Pakistan.",
  [G("doc", header="MIESAU, GERMANY · OCT. 16, 2006", title="THE ARMY'S LAST MASH", body="The 212th MASH becomes the 212th Combat Support Hospital. Staff grows from about 130 to more than 250.",
     source="SOURCE: ARMY.MIL", stamp="LAST MASH")], dict(kind="slow")),
 ("At the ceremony, its commander, Colonel Angel Lugo, made a promise to soldiers.",
  [G("quote", q="You can be assured that if you are wounded on the battlefield and you make it to the 212th CSH, you will live.", w="COL. ANGEL LUGO · 212TH CSH · OCTOBER 2006 · VIA ARMY.MIL")], dict(kind="slow")),
 ("Combat support hospitals were big, and the Army even kept whole hospitals in storage. In Japan, it stored and maintained the equipment for a nine hundred ninety-two bed deployable hospital. In twenty twelve, about two hundred soldiers of the three twenty-fifth Combat Support Hospital, from Missouri, set up medical tents there for an exercise.",
  [C(152551, 140.0), C(152551, 160.0)], dict(tag=JPN, kind="calm")),
 ("And then the Army changed the design again.",
  [C(152551, 66.0)], dict(tag=JPN, kind="calm", gap=0.4)),

 # ---------------- III. THE MODULE ----------------
 ("Starting in twenty seventeen, the Army began turning its combat support hospitals into field hospitals.",
  [G("chapter", case="2017–TODAY", n="III", t="THE MODULE")], dict(gap=1.0, kind="calm")),
 ("The new building block is small. A thirty-two bed hospital. In Army terms, a role three hospital: the level of care with surgeons, operating rooms and intensive care.",
  [G("stat", a="32", b="BEDS — THE BUILDING BLOCK OF TODAY'S FIELD HOSPITAL", c="ROLE 3 · SOURCES: ARMY SUSTAINMENT · ARMY.MIL")], dict(kind="drive")),
 ("Blocks stack. Add surgical and intensive care detachments, and the plan in the Army's own journal describes a hospital that can grow to two hundred forty beds.",
  [G("steps", kicker="FIELD HOSPITAL DESIGN · 2018", title="A HOSPITAL THAT SCALES", items=[["32", "Beds: the base hospital"], ["+ SURGERY", "A surgical detachment"], ["+ ICU", "Intensive care detachments"], ["240", "Beds: the full hospital"]],
     footer="AS DESCRIBED IN ARMY SUSTAINMENT, 2018")], dict(kind="drive")),
 ("Why change? The Army's own journal listed problems with the old design: how it was organized, its medical and surgical capabilities, and how hard it was to split it across different locations.",
  [G("cards3", kicker="WHY THE ARMY REDESIGNED ITS HOSPITALS", title="THREE PROBLEMS", cards=[dict(h="DESIGN", t="How the unit was organized"), dict(h="CAPABILITY", t="Medical and surgical gaps"), dict(h="SPLITTING", t="Hard to run in pieces")],
     footer="SOURCE: ARMY SUSTAINMENT, 2018")], dict(kind="calm")),
 ("The point is speed. A small piece can go first, and the rest can follow.",
  [C(810388, 36.0), C(810388, 56.0)], dict(tag=RES, kind="calm")),
 ("In the tenth Field Hospital, that first piece was an early-entry element with just six beds. Four for patients, and two for damage-control surgery.",
  [G("phases", kicker="10TH FIELD HOSPITAL · EARLY-ENTRY ELEMENT", title="6 BEDS THAT GO FIRST", left=dict(label="HOSPITAL BEDS", num="4", desc="FOR PATIENTS"),
     right=dict(label="SURGERY", num="2", desc="DAMAGE-CONTROL SURGERY BEDS"), footer="SOURCE: ARMY SUSTAINMENT, 2018")], dict(kind="drive")),
 ("That twenty seventeen test was the proof. The six twenty-seventh Hospital Center and the tenth Field Hospital set up at Fort Polk and supported a fourteen-day exercise.",
  [G("doc", header="FORT POLK, LOUISIANA · NOVEMBER 2017", title="PROOF OF CONCEPT", body="627th Hospital Center and 10th Field Hospital: role 3 care established within 72 hours for a 14-day exercise.",
     source="SOURCE: ARMY SUSTAINMENT, 2018", stamp="72 HOURS")], dict(kind="calm")),
 ("Over seven days, that training hospital received two hundred forty-two simulated casualties. And in the last three days, the six-bed early-entry element ran on its own, and treated more than fifty simulated casualties in seventy-two hours.",
  [G("phases", kicker="FORT POLK EXERCISE · 2017 · SIMULATED CASUALTIES", title="THE TEST IN NUMBERS", left=dict(label="ROLE 3 HOSPITAL", num="242", desc="CASUALTIES IN 7 DAYS"),
     right=dict(label="6-BED ELEMENT", num="50+", desc="CASUALTIES IN 72 HOURS"), footer="TRAINING EXERCISE · SOURCE: ARMY SUSTAINMENT, 2018")], dict(kind="drive")),

 # ---------------- IV. THE BUILD ----------------
 ("So what actually happens in those first hours?",
  [G("chapter", case="DAY 1 TO DAY 3", n="IV", t="THE BUILD")], dict(gap=1.0, kind="calm")),
 ("First, people and equipment arrive. By aircraft, by truck, by container.",
  [C(557722, 5.0), C(557722, 60.0)], dict(tag=PR1, kind="drive")),
 ("Then the site. Flat ground, or a building with a big empty floor. A field. A sports arena. A convention center.",
  [C(557923, 38.0), C(557923, 48.0)], dict(tag=PR3, kind="calm")),
 ("Then the shelters go up. Soldiers unroll and stake down the tents, section by section.",
  [C(152551, 34.0), C(152551, 82.0)], dict(tag=JPN, kind="drive")),
 ("Hospital equipment comes out of its cases: beds, monitors, lab gear.",
  [C(557923, 22.0), C(557923, 80.0)], dict(tag=PR3, kind="calm")),
 ("Supplies have to come too. In Puerto Rico, soldiers trucked in food and water.",
  [C(557756, 26.0), C(557756, 5.0)], dict(tag=PR2, kind="calm")),
 ("Then it's laid out like any hospital. Patients arrive at an emergency treatment area. Those who need surgery go to the operating rooms. After surgery, intensive care. Then intermediate care wards, until patients can be moved on.",
  [G("steps", kicker="HOW A FIELD HOSPITAL FLOWS", title="FROM ARRIVAL TO EVACUATION", items=[["ARRIVE", "Emergency treatment"], ["OPERATE", "Operating rooms"], ["RECOVER", "Intensive care"], ["MOVE ON", "Intermediate care, then evacuation"]],
     footer="SOURCES: ARMY.MIL · ARMY SUSTAINMENT")], dict(kind="drive")),
 ("Behind that are the parts you rarely see: pharmacy, laboratory, dental, and medical logistics.",
  [C(745637, 58.0)], dict(tag=JAV, kind="calm")),
 ("In that twenty seventeen design, the hospital's own vehicles could move thirty-five percent of its equipment in one trip. The rest needs more transport.",
  [G("stat", a="35%", b="OF A FIELD HOSPITAL'S EQUIPMENT ITS OWN VEHICLES CAN MOVE IN ONE LIFT", c="SOURCE: ARMY SUSTAINMENT, 2018")], dict(kind="calm")),
 ("And all of it has to be packed up again when the mission moves.",
  [C(810388, 96.0)], dict(tag=RES, kind="calm", gap=0.5)),

 # ---------------- V. THE REAL CALLS ----------------
 ("Field hospitals aren't only for war.",
  [G("chapter", case="2017 · 2020", n="V", t="THE REAL CALLS")], dict(gap=1.0, kind="calm")),
 ("In October twenty seventeen, after Hurricane Maria, the fourteenth Combat Support Hospital arrived in Puerto Rico by air.",
  [C(557722, 50.0), C(557722, 132.0)], dict(tag=PR1, kind="calm")),
 ("It set up inside the damaged Humacao Arena. In less than a week, it had a full hospital: emergency services, surgery, two intensive care units, and x-ray.",
  [C(557923, 42.0), C(557923, 48.0)], dict(tag=PR3, kind="drive")),
 ("After three days of operations, it had seen one hundred sixty-four patients and performed six surgeries.",
  [G("phases", kicker="14TH CSH · HUMACAO, PUERTO RICO · 2017", title="THE FIRST THREE DAYS", left=dict(label="PATIENTS", num="164", desc="SEEN"),
     right=dict(label="SURGERIES", num="6", desc="PERFORMED"), active=0, footer="SOURCE: DVIDS · 24TH THEATER PUBLIC AFFAIRS")], dict(kind="calm")),
 ("It was equipped to see about one hundred patients a day, with forty-four beds for patients needing intensive care. Running twenty-four hours a day.",
  [C(557756, 100.0)], dict(tag=PR4, kind="calm")),
 ("Then, in March twenty twenty, during the COVID-19 pandemic, Army hospital units deployed to American cities.",
  [C(745000, 4.0), C(745000, 80.0)], dict(tag=SEA, kind="calm")),
 ("In Seattle, the six twenty-seventh Hospital Center set up two hundred fifty beds inside the CenturyLink Field Event Center. With two emergency rooms, two operating rooms, a pharmacy and an x-ray department.",
  [G("cards3", kicker="SEATTLE · MARCH–APRIL 2020", title="A HOSPITAL IN AN EVENT CENTER",
     cards=[dict(h="250", t="Beds"), dict(h="2 + 2", t="Emergency rooms + operating rooms"), dict(h="RX + X-RAY", t="Pharmacy and x-ray")],
     footer="SOURCE: ARMY.MIL")], dict(kind="drive")),
 ("In New York, soldiers helped turn the Javits Convention Center into a field hospital. At first, it took patients without COVID-19, to take pressure off the city's hospitals.",
  [C(745637, 14.0), C(745637, 38.0)], dict(tag=JAV, kind="calm")),
 ("About three thousand six hundred soldiers, sailors, airmen and marines deployed to New York and Washington state. Of the Seattle hospital, Lieutenant General Laura Richardson, the commander of U.S. Army North, said it's one of the most capable hospitals in the Army.",
  [G("doc", header="SEATTLE · APRIL 2020", title="ONE OF THE MOST CAPABLE HOSPITALS IN THE ARMY", body="Lt. Gen. Laura J. Richardson, commander of U.S. Army North, on the 627th Hospital Center.", source="AS REPORTED BY ARMY NEWS SERVICE")], dict(kind="slow", gap=0.5)),

 # ---------------- VI. THE NEXT WAR ----------------
 ("Today, the Army is training field hospitals for a different kind of war.",
  [G("chapter", case="2026", n="VI", t="THE NEXT WAR")], dict(gap=1.0, kind="calm")),
 ("In February twenty twenty-six, in Germany, the five hundred twelfth Field Hospital set up a thirty-two bed hospital that could expand to forty-eight. With two operating rooms and intensive care.",
  [C(996410, 9.0), C(996410, 74.0)], dict(tag=G512, kind="calm")),
 ("Two hundred eight soldiers took part. And the unit moved one hundred percent of its own equipment, by itself.",
  [G("stat", a="100%", b="OF ITS EQUIPMENT, MOVED BY THE UNIT ITSELF", c="512TH FIELD HOSPITAL · FEB. 2026 · TRAINING · SOURCE: ARMY.MIL")], dict(kind="drive")),
 ("They also rehearsed long-distance casualty movement, by convoy and loading litters onto a train, all with simulated casualties. The commander of the five hundred nineteenth Hospital Center, Colonel Crystal Belew, summed up the mission.",
  [C(996410, 78.0), G("quote", q="We are here, we will care for them, and we will get them home.", w="COL. CRYSTAL L. BELEW · COMMANDER, 519TH HOSPITAL CENTER · VIA ARMY.MIL")], dict(tag=G512, kind="calm")),
 ("A month later, at Fort McCoy, Wisconsin, the eleventh Field Hospital from Fort Hood ran a nine-day collective training exercise, with medical simulation.",
  [C(1000528, 104.0), C(1000528, 85.0), C(1000528, 113.0)], dict(tag=F11, kind="calm")),
 ("One Army article argues the limit isn't clinical skill. It's beds.",
  [C(1000528, 101.0)], dict(tag=F11, kind="tense")),
 ("As one twenty twenty-six Army article puts it:",
  [G("quote", q="When ICU and ICW beds fill faster than they clear, the hospital's fate is sealed.", w="TERRY DILDAY · ARMY.MIL · JANUARY 2026")], dict(kind="slow")),
 ("The article describes three clocks. The emergency department works in minutes. The operating room in hours. Intensive care and ward beds in days. If beds fill faster than patients can be moved on, the article warns, the hospital fails as a system.",
  [G("steps", kicker="THREE CLOCKS OF A FIELD HOSPITAL", title="WHERE IT JAMS", items=[["MINUTES", "Emergency department"], ["HOURS", "Operating room"], ["DAYS", "ICU and ward beds"]],
     footer="SOURCE: ARMY.MIL, JANUARY 2026")], dict(kind="drive")),
 ("And drones change the picture. A field hospital spread across acres of tents is hard to hide.",
  [C(810388, 81.0)], dict(tag=RES, kind="tense")),
 ("In March twenty twenty-six, Army medics trained inside an old nuclear storage tunnel at Fort Hood, Texas. An officer told Stars and Stripes that precise targeting makes traditional field hospitals too vulnerable.",
  [G("doc", header="WEST FORT HOOD, TEXAS · MARCH 30, 2026", title="A HOSPITAL UNDERGROUND", body="Army medics train in a decommissioned nuclear storage tunnel.",
     source="SOURCE: STARS AND STRIPES", stamp="UNDERGROUND")], dict(kind="slow")),
 ("The war between Russia and Ukraine, the article notes, has pushed people and troops into subway systems and parking garages for safety. So the Army is practicing hospitals that can hide.",
  [C(810388, 60.0), C(810388, 84.0)], dict(tag=RES, kind="tense", gap=0.6)),

 # ---------------- WHAT CHANGED ----------------
 ("In nineteen fifty-one, a MASH was canvas tents, a sign by the road, and a line of ambulances.",
  [C("mash_c", 8.0)], dict(tag=MASH, kind="slow")),
 ("Today, it's a thirty-two bed module, designed to grow, in the Army's plan, into a two-hundred-forty bed hospital.",
  [C(1000528, 105.0)], dict(tag=F11, kind="slow")),
 ("The goal hasn't changed. Bring surgery and intensive care close to the people who need it. Fast.",
  [C(152551, 72.0)], dict(tag=JPN, kind="slow")),
 ("Next on KEPT ALIVE: more stories about how medicine keeps people alive. Subscribe so you don't miss them.",
  [G("stat", a="SUBSCRIBE", b="REAL MEDICINE · REAL FOOTAGE", c="KEPT ALIVE")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · HOW IT WORKS 011", stamp="FIELD HOSPITAL")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("seventy-two hours", "72 hours"), ("November twenty seventeen", "November 2017"), ("October twenty seventeen", "October 2017"),
 ("twenty seventeen", "2017"), ("nineteen fifties", "1950s"), ("eighty-two oh ninth", "8209th"), ("nineteen fifty-one", "1951"),
 ("nineteen fifty-two", "1952"), ("nineteen sixty-eight", "1968"), ("eighty fifty-fifth", "8055th"), ("nineteen ninety and ninety-one", "1990 and 1991"),
 ("sixty beds", "60 beds"), ("fifty large trucks", "50 large trucks"), ("fifty trucks", "50 trucks"), ("two hundred beds", "200 beds"), ("ninety percent", "90%"),
 ("twenty thousand", "20,000"), ("four and a half percent", "4.5%"), ("two and a half percent", "2.5%"), ("two hundred forty-eight", "248"),
 ("a hundred sixty-four", "164"), ("one hundred sixty-four", "164"), ("eighty-four", "84"), ("two thousand six", "2006"), ("October sixteenth", "October 16"),
 ("two hundred twelfth", "212th"), ("thirty-two bed", "32-bed"), ("two hundred forty beds", "240 beds"), ("two-hundred-forty bed", "240-bed"), ("role three", "Role 3"),
 ("six twenty-seventh", "627th"), ("tenth Field Hospital", "10th Field Hospital"), ("fourteen-day", "14-day"), ("thirty-five percent", "35%"),
 ("fourteenth Combat Support Hospital", "14th Combat Support Hospital"), ("six surgeries", "6 surgeries"), ("March twenty twenty", "March 2020"),
 ("two hundred fifty beds", "250 beds"), ("February twenty twenty-six", "February 2026"), ("March twenty twenty-six", "March 2026"), ("twenty twenty-six", "2026"),
 ("five hundred twelfth", "512th"), ("forty-eight", "48"), ("Two hundred eight", "208"), ("one hundred percent", "100%"), ("C.S.H.", "CSH"), ("M.A.S.H.", "M*A*S*H"),
 ("nineteen forty-five", "1945"), ("five hundred nineteenth", "519th"), ("sixty-bed", "60-bed"), ("World War Two", "World War II"), ("twenty miles", "20 miles"), ("seven hundred fifty", "750"), ("nine hundred ninety-two", "992"),
 ("twenty twelve", "2012"), ("three twenty-fifth", "325th"), ("two hundred forty-two", "242"), ("more than fifty", "more than 50"), ("one hundred patients", "100 patients"),
 ("forty-four beds", "44 beds"), ("twenty-four hours", "24 hours"), ("three thousand six hundred", "3,600"), ("eleventh Field Hospital", "11th Field Hospital"),
 ("nine-day", "9-day"), ("six-bed", "6-bed"), ("six beds", "6 beds"), ("about two hundred soldiers", "about 200 soldiers"), ("three helicopter detachments", "3 helicopter detachments"),
 ("seven days", "7 days"), ("last three days", "last 3 days"), ("Eighth Army", "Eighth Army"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · HOW IT WORKS",
    title="Field Hospital",
    voice="am_fenrir",
    imgs={},
    mute_nat=["mash_a", "mash_b", "mash_c", "mash_d", "745637", "745000", "557722", "557756", "557923", "152551", "810388", "996410", "1000528"],
    training=["152551", "810388", "996410", "1000528"],
    credit=("Archival film (public domain): U.S. Army Signal Corps, 8209th Mobile Army Surgical Hospital, Korea, 1951 (National Archives 111-ADC-9535)."
            r"\NFootage: U.S. Department of Defense via DVIDS (public domain). Training footage is marked TRAINING."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD or any government agency."
            r"\NFor education only. This is not medical advice."),
)

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))  # longest first
