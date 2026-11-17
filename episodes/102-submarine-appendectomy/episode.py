# KEPT ALIVE · THE SAVE 102 — No doctor aboard: the submarine appendectomy, USS Seadragon, Sept. 11, 1942
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  ARCHIVAL (public domain, U.S. Navy, Naval Photographic Center, 1945, via Internet Archive / National Archives) — NEVER Seadragon, never 1942:
#   ss_uw / ss_dive / ss_crew = excerpts of NPC-3844 "Supplements to 1945 U.S. Navy Submarine Film 'Silent Service'" (underwater periscope, bow going under, crew compartment)
#   sv_surf / sv_bow / sv_shears / sv_bow2 / sv_hz = excerpts of MN-9141 "Silent Service" (1945), burned-in timecode cropped off
#   sk_ward / sk_crew / sk_deck = excerpts of NPC-15523 "Submarine Film From USS Skate (SS-305) 1945" (officers in the wardroom, crew at a table, deck awash)
#  FRESH (U.S. Navy / USMC via DVIDS, published Sept. 29 – Nov. 13, 2026) — always tagged with ship, place and date; medical clips are TRAINING:
#   1024936 USS Colorado (SSN 788) arrives Pearl Harbor, Sept. 23, 2026 (pub. 2026-09-29, MC2 Nicholas Russell)
#   1029701 USS Columbia (SSN 771) arrives Portsmouth Naval Shipyard, Oct. 29, 2026 (pub. 2026-11-13, Jordon Johnson)
#   1028519 USS Washington (SSN 787) undocking, Portsmouth Naval Shipyard, Oct. 27, 2026 (pub. 2026-11-03, Joel Messer & Jordon Johnson)
#   1029320 U.S. Naval Hospital Okinawa mass-casualty TRAINING, Keen Sword 27, Camp Foster, Oct. 26, 2026 (pub. 2026-11-09, LCpl Nathan Saucier) — instrument tray + masked corpsman over a manikin only; moulage shots avoided
#   1030005 USS Spruance (DDG 111) returns to Naval Base San Diego, Nov. 13, 2026 (pub. 2026-11-16, PO3 Reef Rogers) — crew manning the rails only
#   1027493 Navy Medicine Readiness and Training Unit Iwakuni TRAINING, Keen Sword 27, Oct. 23, 2026 (pub. 2026-10-26, LCpl Tyler Bassett) — clipboard close-up only
#  The patient is never named. No surgery, tissue, blood or wounds on screen — the operation is told with graphics and archival exteriors.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "THE SAVE · 102"
S = "<span style=\"color:#2BB3A3\">{}</span>"
A45 = "ARCHIVAL FILM · 1945 · U.S. NAVY · NOT SEADRAGON"
UW = ("A U.S. FLEET SUBMARINE RUNS SUBMERGED", A45)
DIVE = ("A U.S. FLEET SUBMARINE GOES UNDER", A45)
CREW = ("INSIDE A U.S. FLEET SUBMARINE", A45)
SURF = ("A U.S. FLEET SUBMARINE ON THE SURFACE", A45)
SHEARS = ("PERISCOPE SHEARS OF A U.S. FLEET SUBMARINE", A45)
ARCH = ("A U.S. FLEET SUBMARINE AT SEA", A45)
HZ = ("A LONE SUBMARINE ON AN EMPTY SEA", A45)
WARD = ("OFFICERS IN A SUBMARINE WARDROOM · USS SKATE", A45)
SKCREW = ("SUBMARINE CREW AT WORK · USS SKATE", A45)
DECK = ("A SUBMARINE'S DECK AWASH · USS SKATE", A45)
COLO = ("TODAY: FAST-ATTACK SUBMARINE USS COLORADO", "PEARL HARBOR, HAWAII · SEPT. 23, 2026 · U.S. NAVY")
COLU = ("TODAY: USS COLUMBIA ARRIVES FOR OVERHAUL", "PORTSMOUTH NAVAL SHIPYARD, MAINE · OCT. 29, 2026")
WASH = ("TODAY: USS WASHINGTON LEAVES DRY DOCK", "PORTSMOUTH NAVAL SHIPYARD, MAINE · OCT. 27, 2026")
TRAY = ("TODAY: SURGICAL INSTRUMENTS · NAVY HOSPITAL DRILL", "U.S. NAVAL HOSPITAL OKINAWA · OCT. 26, 2026 · TRAINING")
CLIP = ("TODAY: A NAVY MEDICAL TEAM KEEPS NOTES", "IWAKUNI, JAPAN · OCT. 23, 2026 · TRAINING")
MASK = ("TODAY: NAVY CORPSMEN IN A HOSPITAL DRILL", "U.S. NAVAL HOSPITAL OKINAWA · OCT. 26, 2026 · TRAINING")
NH = ("TODAY: A NAVY HOSPITAL TRAINING DRILL", "U.S. NAVAL HOSPITAL OKINAWA · OCT. 26, 2026 · TRAINING")
SPRU = ("TODAY: USS SPRUANCE'S CREW MANS THE RAILS", "SAN DIEGO · NOV. 13, 2026 · U.S. NAVY")
CAVITE, MANILA = [120.89, 14.48], [120.98, 14.60]
FREM, MACC = [115.75, -32.05], [114.3, 15.9]
NHHC = "NAVAL HISTORY AND HERITAGE COMMAND"
CLOCK = [dict(y="10:46", t="Ether starts"), dict(y="11:07", t="First incision"), dict(y="12:30", t="Appendix removed"), dict(y="13:22", t="Last stitch")]
CLOCK_FOOT = "SOURCE: SUBMARINE SQUADRON TWO REPORT TO THE BUREAU OF MEDICINE AND SURGERY, OCT. 22, 1942 (NHHC)"

LINES = [
 # ---------------- COLD OPEN ----------------
 ("September eleventh, nineteen forty-two. An American submarine is a hundred and twenty feet under the surface, in enemy waters.",
  [C("ss_uw", 8.0)], dict(tag=UW, kind="punch")),
 ("In the officers' wardroom, the dining table has become an operating table.",
  [C("sk_ward", 60.5)], dict(tag=WARD, kind="tense")),
 ("The man about to operate is twenty-three years old. He is a pharmacist's mate, not a doctor. There is no doctor aboard.",
  [G("stat", a="23", b="THE AGE OF THE MAN WHO HAD TO OPERATE", c="PHARMACIST'S MATE · NOT A DOCTOR · SOURCE: " + NHHC)], dict(kind="tense")),
 ("His instruments include five tablespoons, bent back to hold the incision open, and an ether mask made from a tea strainer.",
  [G("cards3", kicker="USS SEADRAGON · SEPTEMBER 11, 1942", title="THE OPERATING KIT",
     cards=[dict(h="5", t="Tablespoons", s="Handles bent back · retractors"), dict(h="1", t="Tea strainer", s="Covered in gauze · ether mask"), dict(h="12", t="Hemostats", s="One became the scalpel handle")],
     footer="SOURCES: " + NHHC + " · SUBMARINE SQUADRON TWO REPORT, 1942")], dict(kind="drive")),
 ("The patient is a nineteen-year-old seaman. His appendix is inflamed, and part of it is already turning black.",
  [C("ss_dive", 0.5)], dict(tag=DIVE, kind="punch")),
 ("If they wait, it can burst. If they operate, the man holding the knife has helped at a few appendectomies, as an assistant.",
  [C("ss_crew", 36.0)], dict(tag=CREW, kind="tense")),
 ("This is the true story of that operation, the two that followed it, and the Navy job it helped create.",
  [C("sv_bow", 20.0)], dict(tag=DIVE, kind="question", gap=0.4)),
 ("No doctor aboard.",
  [G("title", kicker=CASE, title="NO DOCTOR", sub="120 FEET UNDER ENEMY " + S.format("WATERS"), size=250)], dict(kind="slow", gap=2.4)),

 # ---------------- I. THE BOAT THAT SURVIVED ----------------
 ("The submarine was U.S.S. Seadragon.",
  [G("chapter", case="DEC. 10, 1941", n="I", t="THE BOAT THAT SURVIVED")], dict(gap=1.0, kind="calm")),
 ("She was commissioned in nineteen thirty-nine. When the Pacific war began, she was in the Philippines, at the Navy Yard in Cavite, near Manila.",
  [G("map", map=dict(bounds=[[116.5, 10.5], [125.5, 18.5]], cities=[dict(ll=MANILA, name="MANILA", d=0.5, size=34), dict(ll=CAVITE, name="CAVITE NAVY YARD", sub="SEADRAGON MOORED HERE", d=0.9, anchor="end", dy=40)],
       rings=[dict(ll=CAVITE, r=30, n=3, d=0.9, color="#E5383B")]),
     kicker="THE PHILIPPINES · DECEMBER 1941", title="THE FIRST DAYS OF WAR", footer="SOURCE: " + NHHC + " · DANFS: SEADRAGON")], dict(kind="calm")),
 ("On December tenth, nineteen forty-one, Japanese bombers struck the yard. Seadragon was moored beside another submarine, Sealion.",
  [C("sv_surf", 12.0)], dict(tag=SURF, kind="tense")),
 ("Sealion took a direct hit and was wrecked. The blast ripped off part of Seadragon's bridge. Shrapnel pierced her conning tower, killing one man and wounding five.",
  [G("doc", header="DICTIONARY OF AMERICAN NAVAL FIGHTING SHIPS", title="CAVITE · DEC. 10, 1941", body="Sealion took a direct hit. The explosion ripped off part of Seadragon's bridge; shrapnel pierced her conning tower, killing one man and wounding five.",
     source="SOURCE: " + NHHC, stamp="1 KILLED · 5 WOUNDED")], dict(kind="tense")),
 ("One of the men at Cavite that day was a young pharmacist's mate named Wheeler Lipes.",
  [G("callcard", kicker="U.S. NAVY HOSPITAL CORPS · 1942", title="WHEELER B. LIPES",
     rows=[["RATING", "Pharmacist's Mate First Class"], ["AGE", "23"], ["JOINED", "U.S. Navy, 1936"], ["TRAINED", "Navy hospital course, San Diego"], ["SUBMARINES", "Since 1941"]],
     footer="SOURCES: " + NHHC + " · NAVY DEPARTMENT LIBRARY ORAL HISTORY")], dict(kind="calm")),
 ("Lipes was born in nineteen twenty, in New Castle, Virginia. When the bombers came, he was aboard Sealion. He ended up in the water and was picked up that night. Seadragon's own pharmacist's mate had been wounded, and Lipes took his place.",
  [C("sv_hz", 18.5)], dict(tag=HZ, kind="calm")),
 ("He had joined the Navy in nineteen thirty-six, trained in its hospital course in San Diego, and worked in naval hospitals in Philadelphia and near Manila. In nineteen forty-one, he went to submarines.",
  [C(1029320, 15.8), C(1029320, 19.0), C(1029320, 22.7)], dict(tag=NH, kind="calm")),
 ("His specialty was the electrocardiograph, the machine that records the heart. He had assisted at several appendectomies. He was not a surgeon.",
  [G("doc", header="NAVAL HISTORY AND HERITAGE COMMAND", title="HIS TRAINING", body="Classified as an electro-cardiographer. He had assisted in several appendectomies.",
     source="SOURCE: " + NHHC, stamp="PHM1/C · AGE 23")], dict(kind="calm")),
 ("When the newspapers later described him, they called him a lab technician who had worked three years in a Philadelphia hospital.",
  [C("sk_crew", 46.0)], dict(tag=SKCREW, kind="calm")),
 ("Seadragon got out of the Philippines. By the late summer of nineteen forty-two, she was sailing from Fremantle, in Western Australia.",
  [C("sv_hz", 9.0)], dict(tag=HZ, kind="drive")),

 # ---------------- II. HEY DOC ----------------
 ("And then, one of her crew got sick.",
  [G("chapter", case="SEPT. 8, 1942", n="II", t="\"HEY DOC\"")], dict(gap=1.0, kind="calm")),
 ("On August twenty-sixth, Seadragon left Australia on her fourth war patrol, bound for the shipping lanes off the coast of Indochina. Fifty-five men were aboard.",
  [G("map", map=dict(bounds=[[95, -36], [135, 22]], cities=[dict(ll=FREM, name="FREMANTLE", sub="SEADRAGON'S BASE", d=0.5, size=32), dict(ll=MACC, name="PATROL AREA", sub="OFF INDOCHINA", d=1.2, anchor="end", size=32), dict(ll=MANILA, name="MANILA", d=0.9, size=28)],
       arcs=[dict(**{"from": FREM, "to": MACC}, d=1.4, color="#6CF29A")], rings=[dict(ll=MACC, r=34, n=3, d=1.2, color="#E5383B")]),
     kicker="FOURTH WAR PATROL · AUG. 26, 1942", title="55 MEN, ONE PHARMACIST'S MATE", footer="SOURCES: " + NHHC + " · DANFS: SEADRAGON · POSITIONS APPROXIMATE")], dict(kind="drive")),
 ("Seadragon carried no doctor. For medical care, those fifty-five men had Lipes.",
  [C("ss_crew", 4.0)], dict(tag=CREW, kind="calm")),
 ("A pharmacist's mate was one of the Navy's enlisted medical men, a corpsman. On a submarine, he was the whole medical department.",
  [C("ss_crew", 44.5)], dict(tag=CREW, kind="calm")),
 ("On September eighth, a nineteen-year-old seaman reported feeling sick. Lipes later remembered finding him in the after battery compartment, the crew's quarters.",
  [C("ss_crew", 70.0)], dict(tag=CREW, kind="tense")),
 ("His words were simple. \"Hey Doc, I don't feel very good.\"",
  [G("quote", q="Hey Doc, I don't feel very good.", w="AS RECALLED BY WHEELER LIPES · NAVY DEPARTMENT LIBRARY ORAL HISTORY")], dict(kind="slow", gap=0.6)),
 ("By September eleventh, three days later, the diagnosis was appendicitis.",
  [G("stat", a="3 DAYS", b="FROM FIRST SYMPTOMS TO THE OPERATION", c="SEPT. 8 → SEPT. 11, 1942 · SOURCE: " + NHHC)], dict(kind="punch")),
 ("The appendix is a small, finger-shaped pouch attached to the large intestine. The National Institutes of Health says about five to nine of every hundred people develop appendicitis at some point.",
  [G("cards3", kicker="NATIONAL INSTITUTES OF HEALTH · NIDDK", title="WHAT IS APPENDICITIS?",
     cards=[dict(h="5–9", t="in 100 people", s="Develop it at some point"), dict(h="#1", t="Cause of sudden belly pain", s="Needing surgery in the U.S."), dict(h="BURST", t="If untreated", s="Can lead to peritonitis")],
     footer="SOURCE: NIDDK, APPENDICITIS: DEFINITION & FACTS · EDUCATION ONLY, NOT MEDICAL ADVICE")], dict(kind="calm")),
 ("And the N.I.H. is blunt about the danger. Untreated, an inflamed appendix can burst. One result is peritonitis, a serious infection that can spread through the abdomen.",
  [C("sv_hz", 37.0), C("sk_deck", 7.0)], dict(tag=ARCH, kind="tense")),
 ("Seadragon was several days and thousands of miles out from her base at Fremantle, Australia.",
  [C("sv_hz", 30.0)], dict(tag=HZ, kind="slow")),

 ("What happened next would end up in a Pulitzer Prize-winning newspaper story, in a Hollywood movie, and, more than sixty years later, in a medal.",
  [C("sv_bow", 40.0)], dict(tag=DIVE, kind="question", gap=0.4)),
 # ---------------- III. THE ORDER ----------------
 ("So the captain had to decide.",
  [G("chapter", case="SEPT. 11, 1942", n="III", t="THE ORDER")], dict(gap=1.0, kind="calm")),
 ("Seadragon's commanding officer was Lieutenant Commander William Ferrall. He asked Lipes whether he could do the operation himself.",
  [C("sk_ward", 5.0)], dict(tag=WARD, kind="tense")),
 ("Lipes said he could. And then he told the captain the truth.",
  [G("quote", q="Yes sir, I can do it… everything is against us.", w="PHM1/C WHEELER B. LIPES · AS RECORDED BY THE " + NHHC)], dict(kind="slow", gap=0.6)),
 ("In the Navy's account, he went further. Our chances, he said, are slim.",
  [C("sk_ward", 17.0)], dict(tag=WARD, kind="slow", gap=0.4)),
 ("Decades later, Lipes recalled what the captain said next. \"I fire torpedoes every day, and some of them miss.\" Lipes answered that this was one torpedo he could not fire and miss.",
  [G("quote", q="I fire torpedoes every day and some of them miss.", w="LT. CMDR. WILLIAM FERRALL · AS RECALLED BY LIPES · NAVY DEPARTMENT LIBRARY")], dict(kind="calm")),
 ("The patient had a say too. His answer, as the Navy's historians record it, was: \"Whatever the doc feels has to be done is okay with me.\"",
  [C("sk_crew", 10.0)], dict(tag=SKCREW, kind="calm")),
 ("Ferrall gave the order. Lipes would operate.",
  [C("sv_shears", 4.0)], dict(tag=SHEARS, kind="punch")),
 ("First, the captain took Seadragon into relatively safe water. Then he dived, and leveled off at a hundred and twenty feet.",
  [C("sv_bow", 30.0), C("ss_dive", 23.0)], dict(tag=DIVE, kind="drive")),
 ("A hundred and twenty feet of sea above them. Fifty-five men inside. And a twenty-three-year-old pharmacist's mate at the table.",
  [G("stat", a="120 FT", b="SEADRAGON'S DEPTH DURING THE OPERATION", c="SEPT. 11, 1942 · SOURCE: SUBMARINE SQUADRON TWO REPORT, 1942")], dict(kind="slow")),

 # ---------------- IV. THE KIT ----------------
 ("Now he had to build an operating room inside a submarine.",
  [G("chapter", case="SEPT. 11, 1942", n="IV", t="THE KIT")], dict(gap=1.0, kind="calm")),
 ("The operating table was the wardroom mess table, where the officers ate.",
  [C("sk_ward", 66.0)], dict(tag=WARD, kind="calm")),
 ("His medical kit held a pocket case with twelve hemostats, scalpel blades, catgut for stitches, sulfa tablets, and a limited supply of ether.",
  [G("list", kicker="SEADRAGON'S MEDICAL KIT · SEPTEMBER 1942", title="WHAT WAS ABOARD",
     items=["A pocket case with 12 hemostats", "Scalpel blades, but no handle", "Catgut for stitches", "Sulfa tablets", "A limited supply of ether"],
     footer="SOURCES: " + NHHC + " · SUBMARINE SQUADRON TWO REPORT, 1942")], dict(kind="calm")),
 ("There was no handle for the scalpel blades. So one of the hemostats became the handle.",
  [C(1029320, 26.3), C(1029320, 1.0)], dict(tag=NH, kind="calm")),
 ("There were no surgical retractors, the tools that hold a wound open. So they took five tablespoons and bent the handles back.",
  [G("steps", kicker="IMPROVISED ON SEADRAGON · SEPT. 11, 1942", title="WHAT THEY USED INSTEAD",
     items=[["Operating table", "Wardroom mess table"], ["Scalpel handle", "A hemostat"], ["Retractors", "5 tablespoons, handles bent"], ["Ether mask", "Tea strainer + gauze"], ["Sponges", "\"Handi-pads\""]],
     footer="SOURCES: " + NHHC + " · SUBMARINE SQUADRON TWO REPORT, 1942")], dict(kind="drive")),
 ("For sponges, they used commercially sterilized Handi-pads, in their tissue envelopes.",
  [C("sk_crew", 55.0)], dict(tag=SKCREW, kind="calm")),
 ("There was no anesthesia mask. So they covered a tea strainer with gauze and gave the ether through that.",
  [C("ss_crew", 92.0)], dict(tag=CREW, kind="calm")),
 ("Instruments were boiled. Gloves and pajamas were sterilized in alcohol. Torpedo alcohol.",
  [C("sk_crew", 40.0)], dict(tag=SKCREW, kind="calm")),
 ("The report even records the air inside the boat: two inches of mercury above normal pressure. The stitches would be number zero, twenty-day chromic catgut.",
  [C("ss_crew", 10.0)], dict(tag=CREW, kind="calm")),
 ("Lipes ground sulfa tablets into powder, and baked the powder in the boat's oven to kill anything that might be living in it.",
  [C("ss_crew", 20.0)], dict(tag=CREW, kind="calm")),
 ("The anesthetist was not a doctor either. He was Lieutenant Franz Hoskins, the boat's communications officer.",
  [C("sk_ward", 30.0)], dict(tag=WARD, kind="calm")),
 ("And the captain stood by, writing down what he saw every few minutes, for the record.",
  [C(1027493, 70.0), C(1027493, 75.8)], dict(tag=CLIP, kind="calm")),

 ("Those notes went into a report to the Navy's Bureau of Medicine and Surgery, dated October twenty-second, nineteen forty-two. It is the reason we know the times to the minute.",
  [G("doc", header="SUBMARINE SQUADRON TWO → BUREAU OF MEDICINE AND SURGERY", title="THE REPORT", body="Appendectomy performed on war patrol. Depth: 120 feet. Operator: Lipes, Wheeler B., PhM1c. Anesthesia: Lt. F. P. Hoskins. Observations recorded by the commanding officer.",
     source="SOURCE: NAVY DEPARTMENT LIBRARY · " + NHHC, stamp="OCT. 22, 1942")], dict(kind="calm")),
 # ---------------- V. THE CLOCK ----------------
 ("Then the clock started.",
  [G("chapter", case="10:46 A.M.", n="V", t="THE CLOCK")], dict(gap=1.0, kind="calm")),
 ("Here is where things stood. A sick nineteen-year-old on a mess table. A pharmacist's mate with a tea strainer, five spoons and a pocket case. A communications officer giving the ether. A captain with a notebook. And a submarine holding her depth in enemy waters.",
  [C("ss_dive", 8.0)], dict(tag=DIVE, kind="tense")),
 ("At ten forty-six in the morning, the ether began.",
  [G("timeline", kicker="SEPTEMBER 11, 1942 · 120 FEET DOWN", title="THE OPERATION", events=CLOCK, active=0, footer=CLOCK_FOOT)], dict(kind="punch")),
 ("Twenty-one minutes later, at eleven oh seven, Lipes made the first cut, about three inches long.",
  [G("timeline", kicker="SEPTEMBER 11, 1942 · 120 FEET DOWN", title="THE OPERATION", events=CLOCK, active=1, footer=CLOCK_FOOT)], dict(kind="tense")),
 ("All around them, the rest of the crew kept the boat steady. In the after torpedo room, men waited for news.",
  [C("ss_crew", 81.0)], dict(tag=CREW, kind="calm")),
 ("George Weller, the reporter who later told the story, wrote that the order on the boat was simple. Keep her steady.",
  [C("sv_bow", 44.0)], dict(tag=DIVE, kind="tense")),
 ("Finding the appendix took time. When Lipes found it, the end of it had turned black. Gangrene had set in.",
  [C("ss_uw", 30.0)], dict(tag=UW, kind="tense")),
 ("Years later he put it this way: it wasn't one of those snappy-valve appendixes.",
  [G("quote", q="It wasn't one of those \"snappy valve\" appendixes.", w="WHEELER LIPES · NPR, 2005")], dict(kind="slow", gap=0.4)),
 ("At twelve thirty, the appendix came out. Lipes cauterized the stump with carbolic acid, and kept the appendix in a jar of torpedo alcohol.",
  [G("timeline", kicker="SEPTEMBER 11, 1942 · 120 FEET DOWN", title="THE OPERATION", events=CLOCK, active=2, footer=CLOCK_FOOT)], dict(kind="drive")),
 ("Then he closed the wound layer by layer, dusting each layer with the baked sulfa powder.",
  [C("ss_uw", 55.0)], dict(tag=UW, kind="calm")),
 ("At one twenty-two in the afternoon, the last stitch was in.",
  [G("timeline", kicker="SEPTEMBER 11, 1942 · 120 FEET DOWN", title="THE OPERATION", events=CLOCK, active=3, footer=CLOCK_FOOT)], dict(kind="punch")),
 ("Two hours and thirty-six minutes, from the first breath of ether to the last stitch. A hundred and twenty feet down.",
  [G("stat", a="2 H 36 MIN", b="ETHER TO LAST STITCH · 120 FEET DOWN", c="10:46 → 13:22 · SEPT. 11, 1942 · SOURCE: SUBMARINE SQUADRON TWO REPORT")], dict(kind="slow")),

 # ---------------- VI. STILL IN THERE PITCHING ----------------
 ("Now they waited for him to wake up.",
  [G("chapter", case="SEPT. 1942", n="VI", t="STILL PITCHING")], dict(gap=1.0, kind="calm")),
 ("He did. The newspaper story that later made this operation famous reported his first words.",
  [C("sk_crew", 66.0)], dict(tag=SKCREW, kind="calm")),
 ("\"I'm still in there pitching.\"",
  [G("quote", q="I'm still in there pitching.", w="THE PATIENT, ON WAKING · AS REPORTED BY GEORGE WELLER, CHICAGO DAILY NEWS, 1942")], dict(kind="slow", gap=0.8)),
 ("His temperature climbed the next day, to a hundred and three point six, and then came down. Within a few days he was back on duty.",
  [G("stat", a="103.6°F", b="HIGHEST TEMPERATURE · 18 HOURS AFTER SURGERY", c="THEN RECOVERY · BACK ON DUTY WITHIN DAYS · SOURCES: SQUADRON TWO REPORT · NHHC")], dict(kind="calm")),
 ("When he had trouble after the operation, a period the report calls post-operative depression, they gave him oxygen, and he improved markedly. Six hours after he came round, he was drinking water.",
  [C("sk_crew", 20.0)], dict(tag=SKCREW, kind="calm")),
 ("The cook had a theory about the recovery. \"Doc,\" he told Lipes, \"you must have sewed him up with rubber bands, the way he eats.\"",
  [G("quote", q="Doc, you must have sewed him up with rubber bands, the way he eats.", w="SEADRAGON'S COOK · AS RECALLED BY LIPES · NAVY DEPARTMENT LIBRARY")], dict(kind="calm")),
 ("Seadragon went on with her war patrol. On October tenth, she sank the Japanese cargo ship Shigitre Maru, forty-seven seconds after the first torpedo hit.",
  [C("sv_shears", 14.0)], dict(tag=SHEARS, kind="drive")),
 ("She kept fighting. On September twenty-second she attacked a cruiser, and missed. On September thirtieth, a surface attack damaged a ship in a convoy.",
  [C("sv_surf", 24.0), C("sv_shears", 9.0)], dict(tag=SURF, kind="drive")),
 ("She came back to port about six weeks after the operation. The squadron medical officer examined the patient and found a firm, healed scar. His conclusion, as the Navy's historians tell it: Lipes and his shipmates had saved the young man's life.",
  [C("sv_surf", 34.0)], dict(tag=SURF, kind="calm")),
 ("The Navy's official history of Seadragon gives the whole drama a single line. Her progress, it says, was delayed by an emergency appendectomy, performed successfully by the pharmacist's mate.",
  [G("doc", header="DICTIONARY OF AMERICAN NAVAL FIGHTING SHIPS · SEADRAGON", title="ONE LINE IN THE RECORD", body="\"…her progress was delayed by an emergency appendectomy performed successfully by the pharmacist's mate.\"",
     source="SOURCE: " + NHHC, stamp="SEPT. 11, 1942")], dict(kind="calm")),
 ("But the official report also carried a warning. Major surgery by anyone other than qualified surgeons, it said, was by no means desirable to encourage.",
  [G("doc", header="SUBMARINE SQUADRON TWO · OCT. 22, 1942", title="THE NAVY'S VERDICT", body="The result was \"entirely satisfactory.\" But major surgery by anyone other than qualified surgeons was \"by no means desirable to encourage.\"",
     source="SOURCE: " + NHHC + " · NAVY DEPARTMENT LIBRARY", stamp="\"BY NO MEANS DESIRABLE\"")], dict(kind="calm")),

 # ---------------- VII. THE STORY ----------------
 ("The Navy may not have wanted to encourage it. America wanted to hear about it.",
  [G("chapter", case="DEC. 14, 1942", n="VII", t="THE STORY")], dict(gap=1.0, kind="calm")),
 ("After the patrol, a war correspondent named George Weller met Lipes aboard the submarine tender Holland. Weller wrote for the Chicago Daily News.",
  [C("sv_bow2", 6.0)], dict(tag=DIVE, kind="calm")),
 ("Lipes himself was back in the United States by January nineteen forty-three. By then, his name was in newspapers across the country.",
  [C("sv_hz", 2.0)], dict(tag=HZ, kind="calm")),
 ("His story ran on December fourteenth, nineteen forty-two. He called it the first appendix ever known to have been removed below enemy waters.",
  [G("doc", header="CHICAGO DAILY NEWS · DECEMBER 14, 1942", title="BELOW ENEMY WATERS", body="George Weller's report on the operation called it \"the first appendix ever known to have been removed below enemy waters.\"",
     source="SOURCES: PULITZER PRIZE BOARD · WELLER ARCHIVE", stamp="PULITZER 1943")], dict(kind="calm")),
 ("The story won Weller the Pulitzer Prize for Reporting in nineteen forty-three. The Pulitzer citation describes a man who performed an operation for appendicitis, saving a sailor's life.",
  [G("stat", a="PULITZER", b="1943 PRIZE FOR REPORTING · GEORGE WELLER", c="\"…PERFORMED AN OPERATION FOR APPENDICITIS SAVING A SAILOR'S LIFE\" · SOURCE: PULITZER.ORG")], dict(kind="punch")),
 ("Hollywood noticed too. The submarine film Destination Tokyo, released in nineteen forty-three with Cary Grant, borrowed the operation for its plot.",
  [C("sv_bow2", 30.0)], dict(tag=DIVE, kind="calm")),

 ("Radio told it next. In May nineteen forty-three, the program Cavalcade of America aired an episode called Pharmacist's Mate, First Class, and Lipes himself spoke at the end of the broadcast.",
  [G("doc", header="CAVALCADE OF AMERICA · MAY 24, 1943", title="ON THE RADIO", body="Episode: \"Pharmacist's Mate, First Class.\" An actor played the sailor based on Lipes. Lipes himself appeared at the end of the show.",
     source="SOURCE: WIKIPEDIA, \"WHEELER BRYSON LIPES\"", stamp="MAY 1943")], dict(kind="calm")),
 ("Fifteen years later, the television series The Silent Service told it again, in an episode called Operation Seadragon. By then, the operation was a legend of the submarine force.",
  [C("sv_bow2", 18.0)], dict(tag=DIVE, kind="calm")),
 # ---------------- VIII. TWICE MORE ----------------
 ("And before that year was over, it happened again. Twice.",
  [G("chapter", case="DEC. 1942", n="VIII", t="TWICE MORE")], dict(gap=1.0, kind="calm")),
 ("In December nineteen forty-two, the submarine Grayback was only a week out of Australia when one of her torpedomen needed the same operation.",
  [G("map", map=dict(bounds=[[110, -36], [160, 5]], cities=[dict(ll=FREM, name="FREMANTLE", d=0.4, size=30), dict(ll=[150.5, -3.5], name="BISMARCK ARCHIPELAGO", sub="GRAYBACK · DEC. 1942", d=0.9, anchor="end", size=30), dict(ll=[153.0, -27.5], name="BRISBANE", d=0.6, size=28)],
       rings=[dict(ll=[150.5, -3.5], r=32, n=3, d=0.9, color="#E5383B")]),
     kicker="USS GRAYBACK · FIFTH WAR PATROL", title="100 FEET BENEATH THE SURFACE", footer="SOURCE: " + NHHC + " · DANFS: GRAYBACK · POSITIONS APPROXIMATE")], dict(kind="calm")),
 ("Grayback had sailed from Australia on December seventh, nineteen forty-two, exactly one year after Pearl Harbor.",
  [C("sv_surf", 2.0)], dict(tag=SURF, kind="calm")),
 ("Her pharmacist's mate, Harry Roby, operated a hundred feet beneath the surface, in the Bismarck Archipelago. His patient was back on watch by the end of the patrol.",
  [C("ss_uw", 37.0)], dict(tag=UW, kind="drive")),
 ("Then, on Christmas Eve, aboard the submarine Silversides, the pharmacist's mate performed another emergency appendectomy. It was over at four in the morning, on Christmas Day.",
  [C("sk_crew", 72.0), C("sv_bow2", 49.0)], dict(tag=ARCH, kind="tense")),
 ("Silversides already knew what the war could cost. In May of that year, an enemy machine-gun bullet had killed one of her deck gunners.",
  [C("ss_dive", 28.0)], dict(tag=DIVE, kind="slow")),
 ("Three submarines. Three pharmacist's mates. Three emergency appendectomies in about three and a half months. All three were reported as successful.",
  [G("timeline", kicker="U.S. SUBMARINES · 1942", title="THREE OPERATIONS AT SEA",
     events=[dict(y="SEPT. 11", t="Seadragon · 120 ft"), dict(y="DEC.", t="Grayback · 100 ft"), dict(y="DEC. 24–25", t="Silversides")], active=2,
     footer="SOURCES: " + NHHC + " · DANFS: SEADRAGON, GRAYBACK, SILVERSIDES")], dict(kind="punch")),

 ("None of the three men holding the knife was a doctor. Each one had a crew at sea, far from any hospital, and a shipmate who needed an emergency operation.",
  [C("sv_surf", 47.0)], dict(tag=SURF, kind="slow")),
 # ---------------- IX. A DEPARTMENT OF ONE ----------------
 ("What the Navy learned from those months is still sailing today.",
  [G("chapter", case="1944 → TODAY", n="IX", t="A DEPARTMENT OF ONE")], dict(gap=1.0, kind="calm")),
 ("In nineteen forty-four, the Navy identified a need for medical personnel who could work where no medical officer was available. They became Independent Duty Corpsmen.",
  [C(1024936, 134.0), C(1024936, 146.0)], dict(tag=COLO, kind="calm")),
 ("Their first course, an intermediate course at the Hospital Corps School in Portsmouth, Virginia, was two hundred forty-five hours in the classroom and two hundred thirty-five hours of practical exercises. Submarine corpsmen trained in a separate course, in Groton, Connecticut.",
  [G("cards3", kicker="NAVY BUREAU OF MEDICINE AND SURGERY", title="INDEPENDENT DUTY CORPSMEN, 1944",
     cards=[dict(h="245", t="Hours", s="Classroom"), dict(h="235", t="Hours", s="Practical exercises"), dict(h="GROTON", t="Connecticut", s="Submarine course", size=84)],
     footer="SOURCE: BUMED, A BRIEF HISTORY OF THE U.S. NAVY INDEPENDENT DUTY CORPSMAN (2014), VIA DVIDS")], dict(kind="calm")),
 ("In nineteen forty-nine, that course gave way to a twenty-week advanced course in San Diego. A year later, it grew to twenty-six weeks. As of twenty fourteen, independent duty corpsman courses ran in North Carolina, Connecticut and California, and submarine service also required Basic Enlisted Submarine School.",
  [C(1024936, 34.0)], dict(tag=COLO, kind="calm")),
 ("Corpsmen have served aboard American submarines since nineteen twenty-four.",
  [C(1028519, 7.0)], dict(tag=WASH, kind="calm")),
 ("From nineteen fifty-nine into the nineteen seventies, the big missile submarines did carry physicians. Each of their two crews, Blue and Gold, had a doctor and an independent duty corpsman. Even then, according to a Navy medicine historian, the corpsmen handled most of the daily medical care.",
  [C(1024936, 67.0)], dict(tag=COLO, kind="calm")),
 ("One of those submarine doctors later told a Navy historian about setting a broken leg at sea and putting it in a plaster cast. The submarine stayed on patrol, with about two or three weeks still to go.",
  [C(1024936, 106.0)], dict(tag=COLO, kind="calm")),
 ("That did not last. A study sponsored by the Navy's Bureau of Medicine later found that independent duty corpsmen could handle most submarine medical services.",
  [C(1024936, 163.0)], dict(tag=COLO, kind="calm")),
 ("Navy medicine calls the job a department of one. As one independent duty corpsman, the only medical provider on his ship, told Navy reporters:",
  [C(1030005, 24.3)], dict(tag=SPRU, kind="calm")),
 ("His work, as Navy medicine described it: sick call, medical training for the crew, daily water testing, and pest surveys every two weeks. He reported directly to the commanding officer and the executive officer, and he looked after a crew of more than a hundred.",
  [C(1024936, 90.5)], dict(tag=COLO, kind="calm")),
 ("\"The work is stressful because all of the responsibility and accountability lies completely with me.\"",
  [G("quote", q="…all of the responsibility and accountability lies completely with me.", w="HM1 SEO SONG · INDEPENDENT DUTY CORPSMAN, USS MOBILE · NAVY MEDICINE, 2023")], dict(kind="slow", gap=0.6)),
 ("That is the job Wheeler Lipes did at twenty-three, a hundred and twenty feet down, before it even had a name.",
  [C(1024936, 154.0)], dict(tag=COLO, kind="slow")),

 # ---------------- X. AFTERWARDS ----------------
 ("And the people in this story?",
  [G("chapter", case="1944 · 2005", n="X", t="AFTERWARDS")], dict(gap=1.0, kind="calm")),
 ("Seadragon served through the whole war. She made twelve war patrols and earned eleven battle stars. Among the ships she is credited with sinking was the Japanese submarine I-4.",
  [C("sv_bow", 6.0)], dict(tag=DIVE, kind="calm")),
 ("Grayback did not come home. She was listed as overdue and presumed lost in March nineteen forty-four.",
  [C("ss_uw", 16.0)], dict(tag=UW, kind="slow")),
 ("The young seaman Lipes saved did not survive the war either. In October nineteen forty-four, he was serving aboard the submarine Tang when she was lost. Only nine of her crew survived.",
  [C("sv_hz", 44.5), C("sv_bow2", 47.0)], dict(tag=HZ, kind="slow")),
 ("Lipes stayed in the Navy. He was commissioned in the Medical Service Corps in nineteen fifty-one, served until nineteen sixty-two, and retired as a lieutenant commander. Then he ran hospitals. When he retired for good in nineteen ninety-one, he was president of Memorial Medical Center in Corpus Christi, Texas.",
  [G("callcard", kicker="AFTER THE WAR", title="LT. CMDR. WHEELER B. LIPES",
     rows=[["1951", "Commissioned, Medical Service Corps"], ["1962", "Left the Navy · lieutenant commander"], ["1991", "Retired as hospital president, Corpus Christi, Texas"], ["2005", "Navy Commendation Medal"]],
     footer="SOURCE: WIKIPEDIA, \"WHEELER BRYSON LIPES\" (CITING WASHINGTON POST, 2005) · NPR, 2005")], dict(kind="calm")),
 ("Wheeler Lipes lived to be eighty-four. In February two thousand five, more than sixty years after the operation, the Navy presented him with the Navy Commendation Medal for saving a crewman's life.",
  [G("stat", a="60+ YEARS", b="BEFORE THE NAVY GAVE LIPES A MEDAL FOR THE OPERATION", c="NAVY COMMENDATION MEDAL · FEBRUARY 2005 · SOURCE: NPR")], dict(kind="calm")),
 ("The ceremony was at Camp Lejeune, North Carolina. Years earlier, Lipes recalled, his grandson had found the story in a schoolbook, and his teacher told him not to tell stories.",
  [C("sk_ward", 40.5)], dict(tag=WARD, kind="calm")),
 ("He died that April.",
  [C("sv_bow2", 44.0)], dict(tag=DIVE, kind="slow", gap=0.6)),
 ("Twenty-three years old. A hundred and twenty feet down. Five bent spoons, a tea strainer, and no doctor aboard. And a sailor who woke up still in there pitching.",
  [C("ss_dive", 39.0)], dict(tag=DIVE, kind="slow", gap=0.6)),
 ("Next time on KEPT ALIVE: another life on a clock, and the people who kept it going.",
  [G("end", label="KEPT ALIVE · THE SAVE · NEXT", stamp="NEXT SAVE")], dict(kind="calm")),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="FOR EDUCATION ONLY · NOT MEDICAL ADVICE", stamp="KEPT ALIVE")], dict(kind="calm", gap=2.0)),
]

DISPLAY = [
 ("September eleventh, nineteen forty-two", "September 11, 1942"), ("nineteen forty-two", "1942"), ("a hundred and twenty feet", "120 feet"),
 ("twenty-three years old", "23 years old"), ("twenty-three", "23"), ("nineteen-year-old", "19-year-old"), ("five tablespoons", "5 tablespoons"),
 ("nineteen thirty-nine", "1939"), ("December tenth, nineteen forty-one", "December 10, 1941"), ("nineteen thirty-six", "1936"),
 ("nineteen forty-one", "1941"), ("August twenty-sixth", "August 26"), ("Fifty-five men", "55 men"), ("fifty-five men", "55 men"),
 ("September eighth", "September 8"), ("By September eleventh", "By September 11"), ("five to nine of every hundred", "5 to 9 of every 100"),
 ("twelve hemostats", "12 hemostats"), ("ten forty-six", "10:46"), ("Twenty-one minutes", "21 minutes"), ("eleven oh seven", "11:07"),
 ("three inches", "3 inches"), ("twelve thirty", "12:30"), ("one twenty-two", "1:22"), ("Two hours and thirty-six minutes", "2 hours and 36 minutes"),
 ("a hundred and three point six", "103.6"), ("October tenth", "October 10"), ("forty-seven seconds", "47 seconds"),
 ("December fourteenth, nineteen forty-two", "December 14, 1942"), ("nineteen forty-three", "1943"), ("December nineteen forty-two", "December 1942"),
 ("a hundred feet", "100 feet"), ("four in the morning", "4 in the morning"), ("three and a half months", "3.5 months"),
 ("nineteen forty-four", "1944"), ("twenty fourteen", "2014"), ("October twenty-second, nineteen forty-two", "October 22, 1942"), ("January nineteen forty-three", "January 1943"), ("nineteen fifty-one", "1951"), ("nineteen sixty-two", "1962"), ("nineteen ninety-one", "1991"), ("December seventh, nineteen forty-two", "December 7, 1942"), ("nineteen fifty-nine", "1959"), ("nineteen seventies", "1970s"), ("two inches", "2 inches"), ("number zero, twenty-day", "No. 0, 20-day"), ("three years", "3 years"), ("nineteen twenty", "1920"), ("more than sixty years", "more than 60 years"), ("May nineteen forty-three", "May 1943"), ("Fifteen years later", "15 years later"), ("September twenty-second", "September 22"), ("September thirtieth", "September 30"), ("nineteen forty-nine", "1949"), ("twenty-week", "20-week"), ("twenty-six weeks", "26 weeks"), ("two or three weeks", "2 or 3 weeks"), ("Six hours", "6 hours"), ("two hundred forty-five hours", "245 hours"), ("two hundred thirty-five hours", "235 hours"),
 ("nineteen twenty-four", "1924"), ("twelve war patrols", "12 war patrols"), ("eleven battle stars", "11 battle stars"),
 ("March nineteen forty-four", "March 1944"), ("October nineteen forty-four", "October 1944"), ("Only nine", "Only 9"),
 ("eighty-four", "84"), ("February two thousand five", "February 2005"), ("more than sixty years", "more than 60 years"),
 ("U.S.S. Seadragon", "USS Seadragon"), ("N.I.H.", "NIH"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · THE SAVE",
    title="No Doctor Aboard",
    voice="am_fenrir",
    imgs={},
    mute_nat=["ss_uw", "ss_dive", "ss_crew", "sv_surf", "sv_bow", "sv_shears", "sv_bow2", "sv_hz", "sk_ward", "sk_crew", "sk_deck",
              "1024936", "1029701", "1028519", "1029320", "1027493", "1030005"],
    training=["1029320", "1027493"],
    credit=("Archival film (public domain): U.S. Navy, Naval Photographic Center, 1945 — \"Silent Service\" (MN-9141) and supplements (NPC-3844), USS Skate film (NPC-15523), via National Archives / Internet Archive. Not USS Seadragon."
            r"\NFootage: U.S. Navy and U.S. Marine Corps via DVIDS (public domain), Sept.–Nov. 2026. Training footage is marked TRAINING."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the U.S. Navy, DoD or any government agency."
            r"\NFor education only. This is not medical advice."),
)

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))  # longest first
