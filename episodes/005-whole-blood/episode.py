# KEPT ALIVE · HOW IT WORKS 005 — Whole Blood and the Walking Blood Bank
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty: TRAINING (badge via META["training"]): 1015261 Keris Strike 26, Malaysia, July 2026; 963638 Combined Resolve 25-2, Germany, May 2025;
# 989862 10th Mountain Div., Fort Drum, Dec. 2025; 917871 1st Medical Bn., Camp Pendleton, March 2024; 997652 JTS Valkyrie course, Camp Lejeune, Feb. 2026;
# 925009 Valkyrie training, Darwin, May 2024; 976787 Saber Junction 25, Germany, Sept. 2025; 970588 368th Field Hospital WBB training, CENTCOM AOR, 2025.
# NOT training: 1026297 WBB screening drive, Diego Garcia, 2026; 857891 ASBB Center Okinawa LTOWB collection, Sept. 2022; 850913 ASBP drive, Norfolk, May 2022;
# 882519 ASBP drive, Kelley Barracks, Germany, May 2023. Archival: cb35 = War Department / Army Pictorial Service "Combat Bulletin No. 35" (1945); tokyo1950 = U.S. Army
# Signal Corps "Blood Bank Story, Tokyo, Japan" (Dec. 1950). No needle close-ups, no wounds; casualties in training are role players.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "HOW IT WORKS · 005"
S = "<span style=\"color:#2BB3A3\">{}</span>"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("On the battlefield, among the wounded who could have been saved, the leading cause of death is hemorrhagic shock. Shock from bleeding. That's how one Army regimental surgeon puts it.",
  [C(963638, 8.0), C(963638, 16.9)], dict(tag=("SIMULATED CASUALTY · COMBINED RESOLVE 25-2", "HOHENFELS, GERMANY · MAY 20, 2025 · U.S. ARMY"), kind="tense")),
 ("The answer is blood. But blood has to be kept cold. It has to be the right type. And far from a hospital, it runs out.",
  [C(963638, 44.0), C(963638, 100.0)], dict(kind="tense")),
 ("So the military went back to an old idea. If you can't carry enough blood, bring the donors.",
  [C(1015261, 0.5), C(1015261, 8.0)], dict(tag=("WALKING BLOOD BANK CLASS · KERIS STRIKE 26", "KOTA BELUD, MALAYSIA · JULY 17, 2026 · U.S. ARMY"), kind="drive")),
 ("On a remote island in the Indian Ocean, volunteers are screened ahead of time. If someone is badly hurt, the blood bank is already on the base, walking around.",
  [C(1026297, 16.2), C(1026297, 24.2)], dict(tag=("WALKING BLOOD BANK SCREENING DRIVE", "NAVY SUPPORT FACILITY DIEGO GARCIA · 2026 · U.S. NAVY"), kind="calm", gap=0.6)),
 ("This is how whole blood, and the walking blood bank, keep people alive.",
  [G("title", kicker=CASE, title="WHOLE " + S.format("BLOOD"), sub="AND THE WALKING BLOOD BANK", size=200)], dict(kind="slow", gap=2.6)),

 # ---------------- I. WHAT'S IN THE BAG ----------------
 ("Start with what blood actually is.",
  [G("chapter", case="WHOLE BLOOD", n="I", t="WHAT'S IN THE BAG")], dict(kind="calm")),
 ("More than half of it is plasma, a liquid of water, salts and protein. Red blood cells carry oxygen. White blood cells fight infection. And platelets help blood clot.",
  [G("cards3", kicker="WHAT BLOOD IS MADE OF", title="FOUR PARTS, ONE LIQUID",
     cards=[dict(h="PLASMA", t="water, salts and protein", s="MORE THAN HALF OF BLOOD", size=84), dict(h="RED CELLS", t="carry oxygen", s="", size=84), dict(h="PLATELETS", t="help blood clot", s="WHITE CELLS FIGHT INFECTION", size=84)],
     footer="SOURCE: MEDLINEPLUS, U.S. NATIONAL LIBRARY OF MEDICINE")], dict(kind="calm")),
 ("Whole blood is all of it, together, in one bag.",
  [C(857891, 1.0), C(857891, 51.5)], dict(tag=("LOW TITER O WHOLE BLOOD · ASBB CENTER OKINAWA", "KADENA AIR BASE, JAPAN · SEPT. 16, 2022 · U.S. NAVY"), kind="calm")),
 ("But most transfusions don't use it that way. Donated blood is more often given as its separate parts. Red cells. Plasma. Platelets.",
  [C(850913, 329.0), C(850913, 56.0)], dict(tag=("ARMED SERVICES BLOOD PROGRAM DRIVE", "NORFOLK, VA. · MAY 2022 · DEFENSE HEALTH AGENCY"), kind="calm")),
 ("And there's a catch. Blood comes in types.",
  [C(857891, 16.5)], dict(kind="punch")),
 ("In nineteen oh one, Karl Landsteiner reported that human blood falls into different groups. Mix the wrong ones, and red cells clump together. That explained why early transfusions so often went wrong. Today we know four main types. A, B, AB, and O. And blood is either Rh-positive or Rh-negative.",
  [G("callcard", kicker="NOBEL PRIZE IN MEDICINE · 1930", title="KARL LANDSTEINER",
     rows=[["1901", "REPORTS DIFFERENT HUMAN BLOOD GROUPS"], ["THE PROBLEM", "WRONG MIX = RED CELLS CLUMP TOGETHER"], ["GROUPS", "A, B AND O · AB FOUND SOON AFTER"]],
     footer="SOURCE: NOBELPRIZE.ORG")], dict(kind="calm")),
 ("The clumping comes from antibodies. An Army blood bank director put it simply.",
  [C(882519, 96.0)], dict(tag=("ARMED SERVICES BLOOD PROGRAM DRIVE", "KELLEY BARRACKS, GERMANY · MAY 2023 · U.S. ARMY"), kind="calm")),
 ("Everyone has antibodies. They are naturally occurring, and can attach themselves to transfused blood cells.",
  [G("quote", q="Everyone has antibodies. They are naturally occurring and can attach themselves to transfused blood cells.", w="LT. COL. MELANIE SLOAN · DIRECTOR, FORT BRAGG BLOOD DONOR CENTER · VIA ARMY.MIL, 2019")], dict(kind="slow")),
 ("Type O red cells are already considered universal. But type O donors can carry antibodies against type A and type B blood. So the military tests type O donors, and keeps the ones whose levels are low.",
  [C(882519, 192.0), C(882519, 224.0)], dict(kind="calm")),
 ("Below one to two hundred fifty-six. That's called low titer O. The Army says it can be given to anyone in need, regardless of their blood type. Research cited by the Army found that at those low levels, the risk of a severe reaction in a patient of another blood type is low, or negligible.",
  [G("stat", a="< 1:256", b="ANTI-A AND ANTI-B ANTIBODY TITER = LOW TITER O", c="TYPE O DONORS · ALSO SCREENED FOR INFECTIOUS DISEASE · SOURCE: ARMY.MIL · ASBP")], dict(kind="punch", gap=0.8)),

 # ---------------- II. THE ICE CHEST ----------------
 ("The idea of a blood bank was born in a war.",
  [G("chapter", case="WHOLE BLOOD", n="II", t="THE ICE CHEST")], dict(kind="calm")),
 ("In nineteen seventeen, an American Army doctor named Oswald Robertson set up the first blood depot, in France. It was an ice chest, stocked with blood.",
  [G("callcard", kicker="FRANCE · 1917", title="THE FIRST BLOOD DEPOT",
     rows=[["WHO", "OSWALD H. ROBERTSON · U.S. ARMY MEDICAL CORPS"], ["WHAT", "AN ICE CHEST STOCKED WITH BLOOD"], ["DONORS", "USUALLY LIGHTLY WOUNDED SOLDIERS · TYPE O"]],
     footer="SOURCES: PROTO MAGAZINE (MASS GENERAL), 2017 · HISTORY.COM, 2024")], dict(kind="calm")),
 ("His donors were usually lightly wounded soldiers, with type O blood. Each gave about two cups. The blood was mixed with sodium citrate, bottled, and packed in ammunition boxes, with sawdust and ice. That way, it kept for a few weeks.",
  [G("steps", kicker="ROBERTSON'S METHOD · 1917", title="HOW THE FIRST BLOOD BANK WORKED",
     items=[["Collect", "About two cups from a type O donor"], ["Treat", "Sodium citrate"], ["Pack", "Bottles in ammunition boxes, sawdust and ice"], ["Keep", "For a few weeks"]], active=2,
     footer="SOURCE: PROTO MAGAZINE (MASS GENERAL), 2017")], dict(kind="calm")),
 ("The system was put to the test at the Battle of Cambrai, on the Western Front. Not every soldier who received the blood survived. But by March nineteen eighteen, American army hospitals in France had officially adopted Robertson's method. His depots became the model for the civilian blood banks that came after.",
  [G("timeline", kicker="WORLD WAR I", title="FROM ONE ICE CHEST TO A METHOD",
     events=[dict(y="1901", t="Landsteiner: blood groups"), dict(y="1917", t="Robertson's blood depot"), dict(y="CAMBRAI", t="Put to the test"), dict(y="MAR. 1918", t="AEF hospitals adopt the method")], active=3,
     footer="SOURCES: NOBELPRIZE.ORG · PROTO MAGAZINE (MASS GENERAL)")], dict(kind="calm")),
 ("According to one recent review, an estimated ten thousand or more whole blood transfusions were performed in nineteen eighteen alone.",
  [G("stat", a="10,000+", b="WHOLE BLOOD TRANSFUSIONS IN 1918 ALONE · ESTIMATED", c="SOURCE: REVIEW, TRAUMA SURGERY & ACUTE CARE OPEN")], dict(kind="slow", gap=0.8)),

 # ---------------- III. AN OCEAN OF BLOOD ----------------
 ("In the Second World War, the scale changed.",
  [G("chapter", case="WHOLE BLOOD", n="III", t="AN OCEAN OF BLOOD")], dict(kind="calm")),
 ("By the end of the war, the military and the American Red Cross had collected more than thirteen million pints of whole blood. In March nineteen forty-five alone, up to sixty-two thousand units were shipped overseas.",
  [G("cards3", kicker="WORLD WAR II", title="BLOOD BY THE MILLION", 
     cards=[dict(h="13M+", t="pints of whole blood collected", s="MILITARY AND AMERICAN RED CROSS"), dict(h="62,000", t="units shipped in March 1945", s="UP TO · EUROPE AND PACIFIC"), dict(h="1945", t="flown across the Pacific", s="AS SHOWN IN \"COMBAT BULLETIN NO. 35\"")],
     footer="SOURCES: REVIEW, TRAUMA SURGERY & ACUTE CARE OPEN · \"COMBAT BULLETIN NO. 35\" (1945)")], dict(kind="drive")),
 ("In nineteen forty-five, an Army film showed whole blood from the home front, reaching soldiers overseas.",
  [C("cb35", 130.5), C("cb35", 152.5)], dict(tag=("ARCHIVAL FILM · 1945 · \"COMBAT BULLETIN NO. 35\"", "U.S. ARMY · \"GI'S GET WHOLE BLOOD FROM HOME FRONT\""), kind="calm")),
 ("Then came Korea, and the lesson had to be learned again. When the war began, the U.S. had no operational military blood program. The first blood shipments didn't arrive until more than two months into combat. Long supply lines and the short shelf life of whole blood led to significant waste, and drove innovation in plastic blood bags, and longer red cell storage.",
  [C("tokyo1950", 25.0), C("tokyo1950", 61.0), C("tokyo1950", 42.5)], dict(tag=("ARCHIVAL FILM · DEC. 1950 · U.S. ARMY SIGNAL CORPS", "\"BLOOD BANK STORY, TOKYO, JAPAN\" · NATIONAL ARCHIVES"), kind="tense")),
 ("This Army film from December nineteen fifty shows the Army's blood bank storage and shipment office in Tokyo, during the Korean War.",
  [C("tokyo1950", 169.0), C("tokyo1950", 192.0)], dict(kind="calm")),
 ("In nineteen fifty-two, President Truman stood up what became the Armed Services Blood Program. After Korea, it took over collecting and shipping blood for the military from the American Red Cross.",
  [G("callcard", kicker="1952", title="THE ARMED SERVICES BLOOD PROGRAM",
     rows=[["STOOD UP", "1952 · BY PRESIDENT TRUMAN"], ["WHO", "ARMY · NAVY · AIR FORCE"], ["AFTER KOREA", "TAKES OVER MILITARY BLOOD FROM THE RED CROSS"]],
     footer="SOURCE: ARMED SERVICES BLOOD PROGRAM TALKING POINTS (ARCHIVED 2016)")], dict(kind="calm")),
 ("In Vietnam, whole blood was still at the center of care. Between nineteen sixty-five and nineteen seventy-one, about one point three million units were shipped there. Roughly six hundred thousand were transfused, to more than three hundred thirty thousand American and allied casualties. And walking blood banks were part of that care too. Donors, close at hand.",
  [G("cards3", kicker="VIETNAM · 1965–1971", title="WHOLE BLOOD AT WAR",
     cards=[dict(h="1.3M", t="units shipped to Vietnam", s="APPROXIMATELY"), dict(h="600,000", t="units transfused", s="ROUGHLY"), dict(h="330,000+", t="U.S. and allied casualties", s="", size=96)],
     footer="SOURCE: REVIEW, TRAUMA SURGERY & ACUTE CARE OPEN")], dict(kind="drive")),
 
 # ---------------- IV. TAKEN APART ----------------
 ("Then, after Vietnam, whole blood mostly disappeared.",
  [G("chapter", case="WHOLE BLOOD", n="IV", t="TAKEN APART")], dict(kind="calm")),
 ("In the nineteen seventies, the Army moved to what's called component therapy. Civilian medicine made the same move in the seventies and eighties.",
  [C(857891, 44.5), C(857891, 47.5)], dict(tag=("BLOOD LAB · ASBB CENTER OKINAWA", "KADENA AIR BASE, JAPAN · SEPT. 2022 · U.S. NAVY"), kind="calm")),
 ("There were good reasons. Split into parts, one donation could help three patients instead of one. And components keep longer than whole blood.",
  [G("stat", a="1 → 3", b="ONE DONATION, SPLIT INTO COMPONENTS, CAN HELP THREE PATIENTS", c="SOURCE: DR. JAMES R. STUBBS, MAYO CLINIC, 2022")], dict(kind="calm")),
 ("But a recent review argues that the switch was driven by economics, logistics, and perceived safety, not by clinical evidence. No prospective studies compared the two at the time.",
  [G("list", kicker="WHY WHOLE BLOOD WAS DROPPED", title="NOT BY THE EVIDENCE",
     items=["Economics", "Logistics", "Perceived safety", "No prospective studies compared them"],
     footer="SOURCE: REVIEW, TRAUMA SURGERY & ACUTE CARE OPEN")], dict(kind="calm")),
 ("And for a medic far from a hospital, components had a problem. Plasma has to be kept frozen, and platelets bring their own logistics. An Army surgeon said components are not a feasible option for an immediate need for blood in the field.",
  [C(989862, 4.5), C(989862, 64.5)], dict(tag=("BLOOD TRANSFUSION TRAINING · 10TH MOUNTAIN DIVISION", "FORT DRUM, N.Y. · DEC. 11, 2025 · U.S. ARMY"), kind="calm")),
 ("Robert Blough, a former Special Forces medical sergeant, remembers a man he treated in two thousand seven. An Iraqi, shot in the lower abdomen, and bleeding internally.",
  [G("callcard", kicker="ARMY.MIL · 2019", title="1ST LT. ROBERT BLOUGH", rows=[["BACKGROUND", "FORMER SPECIAL FORCES MEDICAL SERGEANT"], ["2007", "AN IRAQI MAN, SHOT IN THE LOWER ABDOMEN"], ["IN 2019", "PHYSICIAN ASSISTANT, 82ND AIRBORNE DIVISION ARTILLERY"]], footer="SOURCE: ARMY.MIL, 2019")], dict(kind="slow")),
 ("I did not have the ability to transfuse blood to save his life.",
  [G("quote", q="I did not have the ability to transfuse blood to save his life.", w="1ST LT. ROBERT BLOUGH · FORMER SPECIAL FORCES MEDICAL SERGEANT · RECALLING 2007 · VIA ARMY.MIL, 2019")], dict(kind="slow", gap=0.9)),

 # ---------------- V. THE BANK THAT WALKS ----------------
 ("So military medicine went back to the old idea.",
  [G("chapter", case="WHOLE BLOOD", n="V", t="THE BANK THAT WALKS")], dict(kind="calm")),
 ("According to the review, the U.S. military re-adopted fresh whole blood from walking blood banks in two thousand two.",
  [C(970588, 1.0), C(970588, 5.5)], dict(tag=("WALKING BLOOD BANK TRAINING · 368TH FIELD HOSPITAL", "U.S. CENTRAL COMMAND AREA · 2025 · U.S. ARMY"), kind="calm")),
 ("A walking blood bank is, first of all, a list of names. Volunteers are tested ahead of time, for blood type, for antibody levels, and for diseases that can be passed on by transfusion. They're regularly retested for blood-borne diseases.",
  [C(997652, 0.5), C(997652, 8.5)], dict(tag=("JOINT TRAUMA SYSTEM VALKYRIE TRANSFUSION COURSE", "CAMP LEJEUNE, N.C. · FEB. 25, 2026 · U.S. MARINE CORPS"), kind="calm")),
 ("When there's a casualty, and no stored blood, a donor from the list gives blood on the spot. It goes to the patient fresh, without refrigeration.",
  [G("steps", kicker="THE WALKING BLOOD BANK", title="HOW IT WORKS",
     items=[["Screen", "Type O, low titer, infectious disease tests"], ["List", "A donor roster, regularly retested for disease"], ["Call", "A casualty, and no stored blood"], ["Collect", "A donor gives blood on the spot"], ["Transfuse", "Fresh, warm, no refrigeration"]], active=3,
     footer="SOURCES: ARMY.MIL · MARINES.MIL · DVIDS")], dict(kind="drive")),
 ("A Navy surgeon explained why that matters. Stored blood may need warming. Fresh blood, he said, is already in our bodies, at ninety-eight point six degrees.",
  [C(917871, 56.5), C(917871, 100.5)], dict(tag=("EMERGENCY FRESH WHOLE BLOOD TRAINING", "1ST MEDICAL BATTALION · CAMP PENDLETON · MARCH 27, 2024"), kind="calm")),
 ("In Valkyrie training, the Marine Corps says, blood drawn from a volunteer goes back into that same volunteer.",
  [C(917871, 160.5), C(917871, 64.0)], dict(kind="calm")),
 ("Speed is part of the drill. At one twenty twenty-six Navy training event, the organizer said trained personnel must be able to screen donors and complete blood draws in under twenty-eight minutes.",
  [G("stat", a="< 28 MIN", b="TO SCREEN DONORS AND COMPLETE BLOOD DRAWS", c="TARGET STATED AT NAVY WALKING BLOOD BANK TRAINING · NAVAL HOSPITAL CAMP PENDLETON, 2026 · SOURCE: DVIDS")], dict(kind="punch")),
 ("In twenty fifteen, the Army's 75th Ranger Regiment began a program built on low titer O donors. They called it ROLO. Ranger O Low Titer. Using only low titer O donors cut out testing steps, and the chance of mismatching a donor and a patient.",
  [G("callcard", kicker="75TH RANGER REGIMENT", title="ROLO · RANGER O LOW TITER",
     rows=[["MAY 2015", "FIRST RANGER DONORS PRESCREENED"], ["MONTHS LATER", "RANGERS DEPLOY WITH PRESCREENED DONORS"], ["MARCH 2016", "FIRST LOW TITER O SHIPMENT TO AFGHANISTAN"]],
     footer="SOURCE: ASBP VIA KEESLER AFB · ARMY.MIL, 2017")], dict(kind="calm")),
 ("In May twenty fifteen, the first Ranger donors were prescreened. Months later, Rangers deployed with them. And in March twenty sixteen, the first shipment of stored low titer O whole blood left Joint Base Lewis-McChord, in Washington State, for Afghanistan.",
  [C(850913, 212.0), C(857891, 56.0)], dict(tag=("STORED WHOLE BLOOD · ILLUSTRATIVE", "ASBP DRIVE, NORFOLK, VA. · ASBB CENTER OKINAWA · 2022"), kind="calm")),
 ("From concept to the unit level, it took eighteen months. The regiment's surgeon, Lieutenant Colonel Ethan Miles, called the cleared donors a walking blood bank on target.",
  [G("quote", q="A walking blood bank on target.", w="LT. COL. ETHAN MILES · SURGEON, 75TH RANGER REGIMENT · VIA ARMED SERVICES BLOOD PROGRAM")], dict(kind="slow")),
 ("In twenty seventeen, the program won one of the Army's Greatest Innovation Awards. That same year, a Navy surgeon, Lieutenant Commander Russell Wier, developed a version for corpsmen and Marines, inspired by the Rangers. It's called Valkyrie.",
  [C(925009, 10.0), C(925009, 73.0)], dict(tag=("VALKYRIE FRESH WHOLE BLOOD TRAINING · WITH AUSTRALIAN ARMY", "ROBERTSON BARRACKS, DARWIN · MAY 2024 · U.S. MARINE CORPS"), kind="calm")),
 ("In twenty twenty-six, a Marine Corps unit hosted a Joint Trauma System version of the course, which the Marine Corps says implements a new Defense Department-wide standard for fresh whole blood transfusion. The five-day course runs from managing donor rosters, to performing transfusions.",
  [C(997652, 116.5), C(997652, 40.5)], dict(tag=("JTS VALKYRIE PREHOSPITAL TRANSFUSION COURSE · 2ND MLG", "CAMP LEJEUNE, N.C. · FEB. 2026 · U.S. MARINE CORPS"), kind="calm")),
 ("And stored low titer O whole blood came back too. The Rangers' first shipment went out in twenty sixteen. The review dates the military's reintroduction of it to twenty seventeen. Blood centers collect it from prescreened donors, refrigerate it, and ship it forward. By one Army Blood Program count, more than a thousand units had gone to U.S. Central Command. The Army Blood Program's director noted it can be kept in a standard refrigerator. And for teams close to the front, the program said, a unit of whole blood is often their only source of platelets.",
  [C(857891, 8.5), C(857891, 22.5)], dict(tag=("COLLECTING LOW TITER O WHOLE BLOOD", "ASBB CENTER OKINAWA · KADENA AIR BASE · SEPT. 2022 · U.S. NAVY"), kind="calm")),
 ("Why so much effort? A Navy lab chief put it in one sentence.",
  [C(850913, 244.0)], dict(tag=("BLOOD STORAGE · ASBP BLOOD DRIVE", "NORFOLK, VA. · MAY 2022 · DEFENSE HEALTH AGENCY"), kind="calm")),
 ("One patient can wipe out an entire blood supply.",
  [G("quote", q="One patient can wipe out an entire blood supply.", w="LT. CMDR. JEFF HEBERT · LABORATORY DEPARTMENT HEAD, NAVAL MEDICAL CENTER SAN DIEGO · VIA DVIDS, 2026")], dict(kind="slow", gap=0.9)),

 # ---------------- VI. COMING HOME ----------------
 ("The lesson didn't stay on the battlefield.",
  [G("chapter", case="WHOLE BLOOD", n="VI", t="COMING HOME")], dict(kind="calm")),
 ("At Mayo Clinic, doctors brought whole blood to air ambulances in southern Minnesota in twenty fifteen. In twenty twenty-one, they began using it in children as young as four months. Before a patient reaches the hospital, it travels in validated, temperature-controlled coolers.",
  [G("timeline", kicker="MAYO CLINIC · MINNESOTA", title="WHOLE BLOOD COMES HOME",
     events=[dict(y="1970s–80s", t="Components era"), dict(y="2015", t="Whole blood on air ambulances"), dict(y="SEPT. 2021", t="Children as young as 4 months")], active=2,
     footer="SOURCE: MAYO CLINIC, 2022")], dict(kind="calm")),
 ("The reason is balance. In a massive transfusion, the goal is equal parts plasma, platelets and red cells. Whole blood comes that way. One Mayo specialist called it the perfect balanced resuscitation blood product.",
  [G("quote", q="Whole blood is the perfect balanced resuscitation blood product.", w="DR. JAMES R. STUBBS · TRANSFUSION MEDICINE, MAYO CLINIC · 2022")], dict(kind="calm")),
 ("Mayo Clinic says about fifteen to twenty percent of trauma patients receive transfusions. About three percent receive massive transfusions.",
  [G("cards3", kicker="TRAUMA PATIENTS", title="WHO NEEDS BLOOD",
     cards=[dict(h="15–20%", t="receive transfusions", s="ABOUT"), dict(h="~3%", t="receive massive transfusions", s="ABOUT"), dict(h="1:1:1", t="plasma, platelets, red cells", s="WHOLE BLOOD'S BALANCE")],
     footer="SOURCE: MAYO CLINIC, 2022")], dict(kind="calm")),
 ("Whole blood isn't the answer to everything. The review describes it as a first treatment for life-threatening bleeding, with a possible switch to type-specific components once the bleeding is under control, the patient is stable, or supplies run low.",
  [C(850913, 200.0), C(850913, 236.0)], dict(tag=("BLOOD STORAGE · ASBP BLOOD DRIVE", "NORFOLK, VA. · MAY 2022 · DEFENSE HEALTH AGENCY"), kind="calm")),
 ("And it has a limit no lab has solved. Blood can't be manufactured. Every unit, whole or in parts, starts with a donor.",
  [C(882519, 72.5), C(882519, 200.0)], dict(tag=("ARMED SERVICES BLOOD PROGRAM DRIVE", "KELLEY BARRACKS, GERMANY · MAY 2023 · U.S. ARMY"), kind="slow", gap=0.9)),

 # ---------------- VII. FULL CIRCLE ----------------
 ("So how do you get blood to someone who is bleeding, before it's too late?",
  [G("chapter", case="WHOLE BLOOD", n="VII", t="FULL CIRCLE")], dict(kind="question")),
 ("In nineteen seventeen, an ice chest. In World War Two, millions of pints, collected at home. In Vietnam, more than a million units. Then, the parts. And now, the oldest idea of all.",
  [G("steps", kicker="WHOLE BLOOD", title="A CENTURY OF ANSWERS",
     items=[["1917", "Robertson's ice chest"], ["WWII", "13 million pints collected"], ["1970s", "Blood taken apart"], ["2015–17", "ROLO, Valkyrie, low titer O"]], active=3,
     footer="SOURCES: PROTO · TSACO REVIEW · ARMY.MIL · ASBP")], dict(kind="calm")),
 ("Robertson's ice chest became a list of names. People who agree, ahead of time, to give blood to a stranger on the worst day of that stranger's life.",
  [C(1015261, 4.0), C(1026297, 24.5)], dict(tag=("WALKING BLOOD BANK", "KERIS STRIKE 26, MALAYSIA · DIEGO GARCIA · 2026"), kind="slow")),
 ("Next time on Kept Alive. Nineteen eighteen. The flu that came home from war.",
  [G("stat", a="NEXT", b="1918: THE FLU THAT CAME HOME FROM WAR", c="KEPT ALIVE · OUTBREAK · 006")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · HOW IT WORKS 005", stamp="O < 1:256")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("nineteen oh one", "1901"), ("one to two hundred fifty-six", "1 to 256"), ("nineteen seventeen", "1917"), ("March nineteen eighteen", "March 1918"),
 ("ten thousand", "10,000"), ("nineteen eighteen", "1918"), ("thirteen million", "13 million"), ("March nineteen forty-five", "March 1945"),
 ("sixty-two thousand", "62,000"), ("nineteen forty-five", "1945"), ("December nineteen fifty", "December 1950"), ("nineteen fifty-two", "1952"),
 ("nineteen sixty-five", "1965"), ("nineteen seventy-one", "1971"), ("one point three million", "1.3 million"), ("six hundred thousand", "600,000"),
 ("three hundred thirty thousand", "330,000"), ("nineteen seventies", "1970s"), ("two thousand seven", "2007"), ("two thousand two", "2002"),
 ("ninety-eight point six degrees", "98.6 degrees"), ("twenty twenty-six", "2026"), ("twenty-eight minutes", "28 minutes"),
 ("May twenty fifteen", "May 2015"), ("twenty fifteen", "2015"), ("March twenty sixteen", "March 2016"), ("twenty sixteen", "2016"), ("eighteen months", "18 months"),
 ("twenty seventeen", "2017"), ("twenty twenty-one", "2021"), ("four months", "4 months"), ("fifteen to twenty percent", "15 to 20 percent"),
 ("three percent", "3 percent"), ("Nineteen eighteen", "1918"), ("Kept Alive", "KEPT ALIVE"), ("75th Ranger", "75th Ranger"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · HOW IT WORKS",
    title="Whole Blood and the Walking Blood Bank",
    voice="am_fenrir",
    mute_nat=["1026297", "857891", "850913", "882519", "1015261", "963638", "989862", "917871", "997652", "925009", "970588", "cb35", "tokyo1950"],
    training=["1015261", "963638", "989862", "917871", "997652", "925009", "970588"],
    credit=("Footage: U.S. Army, U.S. Navy, U.S. Marine Corps, Defense Health Agency via DVIDS (public domain); training footage is labelled."
            r"\NArchival: \"Combat Bulletin No. 35\" (1945) and U.S. Army Signal Corps \"Blood Bank Story, Tokyo, Japan\" (1950), public domain via National Archives / Internet Archive."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, NIH, CDC or the Armed Services Blood Program."
            r"\NFor education only. This is not medical advice."),
)
