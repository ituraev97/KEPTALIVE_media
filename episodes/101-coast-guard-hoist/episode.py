# KEPT ALIVE · THE SAVE 101 — No Ambulance at Sea: the Coast Guard hoist (published title A: "4 People, a Burning Boat, 50 Miles From Shore")
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty (all U.S. Coast Guard / DoD via DVIDS unless noted; real events unless marked TRAINING):
#  1026608 = "Shrimp boat fire and MEDEVAC", Air Station New Orleans + ATC Mobile, ~50 mi off Dauphin Island AL, Oct. 13, 2026 (DVIDS pub. 2026-10-16, PO3 Tasha Smith; footage from aircrews and survivors)
#  1029245 = 4 crew with suspected food poisoning hoisted from tanker Daibelli near Vieques PR, Nov. 8, 2026 (pub. 2026-11-09, Ricardo Castrodad)
#  1028902 = Air Station Elizabeth City hoist, cruise ship Norwegian Bliss off Oregon Inlet NC, Nov. 2, 2026 (pub. 2026-11-06, PO2 Matthew Thieme) — litter shots from above only, no faces; cabin patient shots avoided
#  1023702 = Air Station Borinquen long-range medevac ~100 nm E of St. Maarten, Sept. 19, 2026 (pub. 2026-09-20, Ricardo Castrodad) — FLIR deck shots 0-20 s only
#  1024523 = Air Station Borinquen night medevac, cruise ship Allure of the Seas off Puerto Rico, Sept. 24, 2026 (pub. 2026-09-25)
#  1028385 = Air Station San Francisco MH-65 medevac, container ship 34 mi NW of San Francisco, Oct. 31, 2026 (pub. 2026-11-02)
#  1025010 = Air Station Sitka hoist of boater after vessel sank, life raft taking on water, Murder Cove AK, Sept. 28, 2026 (pub. 2026-09-30, PO3 Nathan Bishop)
#  1029116 = Air Station Traverse City hoist from grounded sailboat, Lake Michigan, Nov. 7, 2026 (pub. 2026-11-08, PO3 Dillon Grimsley)
#  1028766 = Air Station Savannah hoists six from grounded boat, Jasper County SC, Nov. 4, 2026 (pub. 2026-11-05)
#  1028863 = Air Station Borinquen rescue swimmer hoist TRAINING near Mona Island PR, Nov. 5, 2026 (pub. 2026-11-06, PO3 Jessica Walker) — TRAINING
#  heli1947 = excerpt of Naval Photographic Center film #3017 (NARA 76656, via Internet Archive NPC-3017a, public domain): a Navy Sikorsky HO3S-1 on floats, Nov. 1947.
#             Always tagged ARCHIVAL FILM · 1947 · NOT THE 1944 FLIGHT. No film of the 1944 plasma flight is used.
#  No patient is named. No injuries, blood or patients' faces on screen.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "THE SAVE · 101"
S = "<span style=\"color:#2BB3A3\">{}</span>"
FIRE = ("A 90-FOOT FISHING BOAT ON FIRE, ABOUT 50 MILES OFFSHORE", "OFF DAUPHIN ISLAND, ALABAMA · OCT. 13, 2026 · U.S. COAST GUARD VIDEO")
FLIR = ("COAST GUARD INFRARED VIDEO OF THE BURNING BOAT", "OFF DAUPHIN ISLAND, ALABAMA · NIGHT OF OCT. 13–14, 2026")
TANK = ("4 SICK MARINERS HOISTED FROM AN OIL TANKER", "NEAR VIEQUES, PUERTO RICO · NOV. 8, 2026 · HOIST CAMERA")
BLISS = ("A COAST GUARD CREW MEMBER RIDES THE HOIST TO A CRUISE SHIP", "OFF OREGON INLET, NORTH CAROLINA · NOV. 2, 2026")
BLISS2 = ("THE HOIST BRINGS A RESCUE LITTER UP INTO THE HELICOPTER", "NORWEGIAN BLISS · OFF NORTH CAROLINA · NOV. 2, 2026")
STM = ("LONG-RANGE MEDEVAC FROM A COMMERCIAL SHIP", "ABOUT 100 NAUTICAL MILES EAST OF ST. MAARTEN · SEPT. 19, 2026 · INFRARED")
ALL = ("NIGHT MEDEVAC FROM A CRUISE SHIP'S HELICOPTER PAD", "ALLURE OF THE SEAS · OFF PUERTO RICO · SEPT. 24, 2026")
SFO = ("MH-65 DOLPHIN MEDEVAC FROM A CONTAINER SHIP", "34 MILES NORTHWEST OF SAN FRANCISCO · OCT. 31, 2026")
AK = ("A BOATER HOISTED AFTER HIS FISHING VESSEL SANK", "NEAR MURDER COVE, ALASKA · SEPT. 28, 2026")
LM = ("A MAN HOISTED FROM A GROUNDED SAILBOAT", "LAKE MICHIGAN · NIGHT OF NOV. 7, 2026 · INFRARED")
SC = ("SIX PEOPLE HOISTED FROM A GROUNDED BOAT AT NIGHT", "JASPER COUNTY, SOUTH CAROLINA · NOV. 4, 2026")
TRN = ("A RESCUE SWIMMER DEPLOYS FROM AN MH-60T JAYHAWK", "NEAR MONA ISLAND, PUERTO RICO · NOV. 5, 2026 · TRAINING")
H47 = ("A NAVY SIKORSKY HELICOPTER ON FLOATS", "ARCHIVAL FILM · 1947 · U.S. NAVY · NOT THE 1944 FLIGHT")
NY = [-74.02, 40.56]
FBF, BAT, SH, AMB = [-73.890, 40.591], [-74.017, 40.703], [-74.003, 40.466], [-73.831, 40.459]
AGU, SJU, SXM, STX = [-67.13, 18.50], [-66.07, 18.45], [-63.05, 18.04], [-61.30, 18.04]

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Fifty miles off the coast of Alabama, a ninety-foot fishing boat is on fire. Four people are aboard.",
  [C(1026608, 99.5)], dict(tag=FLIR, kind="punch")),
 ("Out here, there is no fire truck. There is no ambulance. There is no road.",
  [C(1026608, 28.0)], dict(tag=FLIR, kind="tense")),
 ("What comes is a Coast Guard airplane, and then a Coast Guard helicopter.",
  [C(1026608, 76.0)], dict(tag=FLIR, kind="tense")),
 ("That same autumn, Coast Guard helicopter crews lifted people off an oil tanker, two cruise ships, a container ship, and a rocky shore in Alaska, where a boater was stranded after his boat sank.",
  [C(1029245, 25.0), C(1028902, 40.0)], dict(tag=("REAL COAST GUARD HOISTS, AUTUMN 2026", "TANKER, PUERTO RICO, NOV. 8 · CRUISE SHIP, N.C., NOV. 2"), kind="drive")),
 ("No ambulance can drive to a ship a hundred miles out at sea. So the Coast Guard lowers help down a cable from the sky.",
  [C(1028863, 72.0)], dict(tag=TRN, kind="calm")),
 ("This is how they do it, why it took a war and a shipwreck to get here, and what happened to the four people on that burning boat.",
  [C(1024523, 34.0)], dict(tag=ALL, kind="question", gap=0.4)),
 ("No ambulance at sea.",
  [G("title", kicker=CASE, title="THE HOIST", sub="NO AMBULANCE AT " + S.format("SEA"), size=250)], dict(kind="slow", gap=2.4)),

 # ---------------- I. FOUR SICK MARINERS ----------------
 ("Start with a weekend in November, off Puerto Rico, and a call to the Coast Guard.",
  [G("chapter", case="NOV. 7–8, 2026", n="I", t="FOUR SICK MARINERS")], dict(gap=1.0, kind="calm")),
 ("The Daibelli is a small oil tanker, three hundred twenty-eight feet long, flagged in Cyprus. That weekend she was at anchor off Vieques, an island just east of Puerto Rico. She was built in twenty twenty-two, and her inspection record is clean.",
  [G("map", map=dict(bounds=[[-67.4, 17.8], [-64.6, 18.7]], cities=[dict(ll=[-65.45, 18.08], name="VIEQUES", sub="TANKER DAIBELLI AT ANCHOR", d=0.5), dict(ll=SJU, name="SAN JUAN", sub="AIRPORT · HOSPITAL", anchor="end", d=0.9), dict(ll=AGU, name="AIR STATION BORINQUEN", d=1.2, size=30)],
       rings=[dict(ll=[-65.45, 18.08], r=34, n=3, d=0.5)], arcs=[dict(**{"from": AGU, "to": [-65.45, 18.08]}, d=1.4, color="#6CF29A")]),
     kicker="PUERTO RICO · NOVEMBER 2026", title="A TANKER AT ANCHOR", footer="SOURCES: U.S. COAST GUARD VIA DVIDS · MARINE INSIGHT · MARITIME EXECUTIVE")], dict(kind="calm")),
 ("On Saturday night, the ship's master called the Coast Guard's rescue center in San Juan. Four of his crew were sick. The suspected cause was food poisoning.",
  [G("callcard", kicker="RESCUE SUB-CENTER SAN JUAN · SATURDAY NIGHT", title="THE CALL",
     rows=[["VESSEL", "Oil tanker Daibelli · Cyprus flag · 328 ft"], ["POSITION", "At anchor off Vieques"], ["PATIENTS", "4 crew members"], ["SUSPECTED", "Food poisoning"]],
     footer="SOURCES: U.S. COAST GUARD VIA DVIDS · MARINE INSIGHT, NOV. 10, 2026")], dict(kind="tense")),
 ("A ship at anchor has no emergency room. The hospital they needed was on the main island, across the water. The Coast Guard decided that a helicopter was the best way to get the four of them there.",
  [C(1029245, 3.0)], dict(tag=TANK, kind="calm")),
 ("On Sunday morning, an MH-60T Jayhawk from Coast Guard Air Station Borinquen reached the tanker.",
  [C(1028863, 28.0)], dict(tag=TRN, kind="drive")),
 ("A Jayhawk usually flies with a crew of four. Two pilots. A flight mechanic. And a rescue swimmer.",
  [G("cards3", kicker="MH-60T JAYHAWK · STANDARD CREW", title="FOUR PEOPLE ABOARD",
     cards=[dict(h="2", t="Pilots", s="Pilot and co-pilot"), dict(h="1", t="Flight mechanic", s=""), dict(h="1", t="Rescue swimmer", s="")],
     footer="SOURCE: U.S. COAST GUARD COMMUNITY BRIEF, NAVAL AIR TRAINING COMMAND")], dict(kind="calm")),
 ("Then came the first problem. The crew had trouble finding a safe spot on the tanker's deck to lower the hoist.",
  [C(1029245, 15.5)], dict(tag=TANK, kind="tense")),
 ("Lieutenant Stan Raymond, the co-pilot, said the ship presented a challenging hoisting environment. The crew worked out what he called the safest and most effective location.",
  [G("quote", q="…a challenging hoisting environment… the safest and most effective location.", w="LT. STAN RAYMOND · CO-PILOT, AIR STATION BORINQUEN · VIA MARITIME EXECUTIVE")], dict(kind="calm")),
 ("Then the hoist went to work. The camera on the helicopter shows the rescue basket going down to the deck, and coming back up, again and again.",
  [C(1029245, 51.0), C(1029245, 80.0)], dict(tag=TANK, kind="drive")),
 ("All four mariners were hoisted into the helicopter. The crew flew them to San Juan's main airport, Luis Muñoz Marín. Medical crews met them there and took them to a hospital.",
  [C(1029245, 94.1)], dict(tag=TANK, kind="calm")),
 ("I'm grateful, Raymond said, that our crew was able to safely evacuate all four mariners and get them to a higher level of medical care.",
  [G("quote", q="I'm grateful our crew was able to safely evacuate all four mariners and get them to a higher level of medical care.", w="LT. STAN RAYMOND · U.S. COAST GUARD · VIA MARITIME EXECUTIVE, NOV. 9, 2026")], dict(kind="slow")),
 ("Notice one detail in the reports. At the airport, Coast Guard Sector San Juan had arranged two things for the helicopter: medical services for the patients, and fuel for the aircraft. The patients needed a hospital. The helicopter needed fuel.",
  [G("callcard", kicker="LUIS MUÑOZ MARÍN INTERNATIONAL AIRPORT · NOV. 8, 2026", title="WAITING ON THE GROUND",
     rows=[["FOR THE PATIENTS", "Emergency medical staff, then a regional hospital"], ["FOR THE HELICOPTER", "Fuel"], ["ARRANGED BY", "Coast Guard Sector San Juan"]],
     footer="SOURCE: MARINE INSIGHT, NOV. 10, 2026, CITING LT. STAN RAYMOND")], dict(kind="calm")),
 ("By Monday, the Daibelli was under way again, headed for the U.S. Virgin Islands, back on her usual run around the Caribbean.",
  [C(1029245, 56.0)], dict(tag=TANK, kind="calm")),
 ("Customs and Border Protection, the U.S. Public Health Service and Puerto Rico's emergency medical services all had a part. The Coast Guard does not say how the four are doing. Their privacy stays theirs. What it does show is the hoist.",
  [C(1029245, 31.0)], dict(tag=TANK, kind="calm", gap=0.6)),

 # ---------------- II. PLASMA IN A STORM ----------------
 ("For most of history, none of this was possible.",
  [G("chapter", case="JAN. 3, 1944", n="II", t="PLASMA IN A STORM")], dict(gap=1.0, kind="calm")),
 ("A sick sailor far from shore waited for port, or for another ship. Then, in the middle of a world war, came a disaster at the door of New York Harbor.",
  [C("heli1947", 3.0)], dict(tag=H47, kind="calm")),
 ("On the morning of January third, nineteen forty-four, the Navy destroyer U.S.S. Turner was anchored near Ambrose Light, outside the harbor.",
  [G("map", map=dict(bounds=[[-74.12, 40.40], [-73.74, 40.74]], cities=[dict(ll=AMB, name="AMBROSE LIGHT", sub="USS TURNER", d=0.4), dict(ll=FBF, name="FLOYD BENNETT FIELD", d=0.7, size=32), dict(ll=BAT, name="BATTERY PARK", anchor="end", d=1.0, size=32), dict(ll=SH, name="SANDY HOOK", sub="HOSPITAL · COAST GUARD STATION", anchor="end", d=1.3, size=32)],
       rings=[dict(ll=AMB, r=30, n=3, d=0.4, color="#E5383B")], topPad=140),
     kicker="NEW YORK HARBOR · JANUARY 3, 1944", title="A DESTROYER EXPLODES", footer="SOURCES: NAVAL HISTORY AND HERITAGE COMMAND · U.S. COAST GUARD HISTORIAN")], dict(kind="tense")),
 ("Explosions tore her apart, and fires set off her ammunition. According to the Coast Guard's historian, a second explosion, forty-seven minutes after the first, sank her.",
  [G("doc", header="U.S. NAVY · DESTROYER DD-648 · JANUARY 3, 1944", title="USS TURNER", body="Explosions rip the ship apart while she is at anchor. Fires set off her ammunition. A second explosion, 47 minutes later, sinks her.",
     source="SOURCES: NHHC · U.S. COAST GUARD HISTORIAN'S OFFICE", stamp="SUNK")], dict(kind="tense")),
 ("Survivors were taken to a hospital at Sandy Hook, New Jersey. The wounded urgently needed blood plasma.",
  [G("stat", a="PLASMA", b="WHAT THE WOUNDED AT SANDY HOOK URGENTLY NEEDED", c="JANUARY 3, 1944 · SOURCE: NAVAL HISTORY AND HERITAGE COMMAND")], dict(kind="punch")),
 ("But a nor'easter was raging. High winds, snow squalls, sleet. Airfields were closed. Every aircraft was grounded.",
  [G("list", kicker="NEW YORK · MORNING OF JANUARY 3, 1944", title="THE WEATHER", items=["A nor'easter: high winds, snow squalls, sleet", "Airfields closed", "All aircraft grounded", "Plasma needed at Sandy Hook"],
     footer="SOURCES: NAVAL HISTORY AND HERITAGE COMMAND · U.S. COAST GUARD HISTORIAN")], dict(kind="tense")),
 ("Except one kind of aircraft. At Floyd Bennett Field in Brooklyn, a Coast Guard pilot named Frank Erickson, an early champion of the helicopter, had a Sikorsky H-N-S-1.",
  [C("heli1947", 12.5)], dict(tag=H47, kind="drive")),
 ("Erickson was not a typical aviator. Born near Portland, Oregon, he enlisted in the Navy, became a midshipman, resigned, and then enlisted in the Coast Guard. He graduated from the Coast Guard Academy and was commissioned in nineteen thirty-one.",
  [G("doc", header="U.S. COAST GUARD · AVIATOR", title="FRANK A. ERICKSON", body="Born near Portland, Oregon. Navy enlisted, then midshipman. Coast Guard Academy, commissioned 1931. Served on cutters. In Honolulu, witnessed the Pearl Harbor attack, Dec. 7, 1941.",
     source="SOURCE: NAVAL HISTORY AND HERITAGE COMMAND")], dict(kind="calm")),
 ("He served on cutters, and he was in Honolulu when Japan attacked Pearl Harbor. After that, he pushed for a new idea. He saw the helicopter as a search and rescue machine, and also as protection for convoys against submarines.",
  [G("list", kicker="FRANK ERICKSON · U.S. COAST GUARD", title="HIS IDEA FOR THE HELICOPTER", items=["Search and rescue", "Protecting convoys against submarines"], footer="SOURCE: U.S. COAST GUARD HISTORIAN'S OFFICE")], dict(kind="calm")),
 ("Around ten in the morning, an admiral asked whether a helicopter could fly plasma to Sandy Hook. Erickson said yes at once. He had never flown in conditions like these. Floyd Bennett Field itself was closed by the weather, so permission had to come from the commander of the New York Air Patrol.",
  [G("doc", header="U.S. COAST GUARD · NEW YORK · ABOUT 10:00 A.M.", title="THE REQUEST", body="Can a helicopter fly plasma from Manhattan to Sandy Hook? Erickson agrees at once, though he has never flown in such conditions.",
     source="SOURCE: U.S. COAST GUARD HISTORIAN'S OFFICE, THE LONG BLUE LINE", stamp="APPROVED")], dict(kind="calm")),
 ("At ten twenty, with Ensign Walter Bolton beside him, Erickson lifted off into swirling snow and gusting wind. Visibility was so low that, he said later, they had to feel their way around the ships in the bay.",
  [C("heli1947", 24.0)], dict(tag=H47, kind="tense")),
 ("At Battery Park, on the tip of Manhattan, Bolton stayed behind while two cases of plasma were lashed to the helicopter's floats.",
  [G("callcard", kicker="BATTERY PARK, MANHATTAN · JANUARY 3, 1944", title="THE CARGO",
     rows=[["10:20 A.M.", "Lift-off from Floyd Bennett Field"], ["LOADED", "2 cases of blood plasma"], ["STOWED", "Lashed to the floats"], ["CREW", "Erickson alone"]],
     footer="SOURCES: NHHC · U.S. COAST GUARD HISTORIAN'S OFFICE")], dict(kind="drive")),
 ("Trees blocked the way ahead, so he backed the helicopter out, and at about ten fifty-five, it rose straight up into the storm.",
  [G("steps", kicker="JANUARY 3, 1944 · THE FLIGHT", title="FROM BROOKLYN TO SANDY HOOK", items=[["10:20", "Lift-off, Floyd Bennett Field"], ["Battery Park", "Plasma lashed to floats"], ["Trees", "Backs out"], ["~10:55", "Rises straight up"], ["11:09", "Lands at Sandy Hook"]], footer="SOURCE: U.S. COAST GUARD HISTORIAN'S OFFICE")], dict(kind="tense")),
 ("At eleven oh nine, Erickson landed at the Coast Guard station at Sandy Hook. About fourteen minutes. The plasma was there.",
  [G("stat", a="14 MIN", b="BATTERY PARK TO SANDY HOOK, THROUGH A NOR'EASTER", c="ABOUT 10:55 TO 11:09 A.M. · JAN. 3, 1944 · SOURCE: U.S. COAST GUARD HISTORIAN'S OFFICE")], dict(kind="punch")),
 ("Erickson said the weather was such that this flight could not have been made in any other type of aircraft.",
  [G("quote", q="Weather conditions were such that this flight could not have been made in any other type of aircraft.", w="FRANK A. ERICKSON, U.S. COAST GUARD PILOT · VIA NAVAL HISTORY AND HERITAGE COMMAND")], dict(kind="slow")),
 ("The Navy's historians call it the first helicopter lifesaving operation. It carried no patient. It carried plasma. Erickson went on to pioneer some of the techniques the Navy and Coast Guard adapted. And it proved that a helicopter could go where nothing else could fly.",
  [G("doc", header="NAVAL HISTORY AND HERITAGE COMMAND", title="THE FIRST HELICOPTER LIFESAVING OPERATION", tsize=80, body="January 3, 1944. Cargo: two cases of blood plasma, lashed to the floats. Pilot: Frank A. Erickson, U.S. Coast Guard.", source="SOURCE: NHHC · U.S. COAST GUARD HISTORIAN'S OFFICE", stamp="FIRST")], dict(kind="calm")),
 ("The next step was the cable. Late in November nineteen forty-five, a storm drove a Texaco oil barge onto Penfield Reef, off Fairfield, Connecticut. Waves broke over it. It was coming apart. Two men were trapped aboard, and rescue boats could not reach them.",
  [G("doc", header="PENFIELD REEF · FAIRFIELD, CONNECTICUT · NOVEMBER 1945", title="A BARGE ON THE REEF", body="Storm, rain and snow. An oil barge breaking up on the reef. Two men trapped. Rescue boats cannot reach them.",
     source="SOURCES: LOCKHEED MARTIN / SIKORSKY HISTORY, 2026 · VERTICAL FLIGHT SOCIETY", stamp="TRAPPED")], dict(kind="tense")),
 ("Sikorsky's chief test pilot, Jimmy Viner, and an Army Air Forces pilot, Jackson Beighle, flew out in an R-5 helicopter fitted with a hoist and a lifting harness. Viner had only tested that harness a few feet above the ground. The winds were close to sixty miles an hour.",
  [G("callcard", kicker="SIKORSKY R-5 · NOVEMBER 1945", title="WIDELY REGARDED AS THE FIRST HOIST RESCUE OVER WATER",
     rows=[["PILOTS", "Jimmy Viner · Jackson Beighle"], ["EQUIPMENT", "Hoist + lifting harness"], ["TESTED", "Only a few feet above the ground"], ["WIND", "Close to 60 mph"]],
     footer="SOURCE: LOCKHEED MARTIN, \"THE RESCUE THAT CHANGED SEARCH AND RESCUE FOREVER\", 2026")], dict(kind="drive")),
 ("They lifted the men off one at a time. The Vertical Flight Society has made the spot a heritage site, for what is widely regarded as the world's first successful helicopter hoist rescue over water. It showed that a helicopter could pull people off a wreck on a cable.",
  [G("stat", a="&#8203;1945", b="WIDELY REGARDED AS THE FIRST HELICOPTER HOIST RESCUE OVER WATER", c="PENFIELD REEF, CONNECTICUT · VERTICAL FLIGHT SOCIETY HERITAGE SITE · SOURCE: LOCKHEED MARTIN")], dict(kind="calm", gap=0.6)),

 # ---------------- III. THE CLOCK ----------------
 ("Eighty-two years later, every rescue flight still runs on a clock: distance, fuel and weather.",
  [G("chapter", case="2026", n="III", t="THE CLOCK")], dict(gap=1.0, kind="calm")),
 ("The helicopter that flew to the tanker, the MH-60T Jayhawk, is what the Coast Guard calls a medium range recovery helicopter. Its hoist raises and lowers rescue swimmers, survivors and equipment.",
  [C(1028863, 37.3)], dict(tag=TRN, kind="calm")),
 ("The Coast Guard's own fact sheet gives three numbers. A range of about seven hundred nautical miles. A top speed of one hundred seventy knots. And six and a half hours in the air.",
  [G("cards3", kicker="MH-60T JAYHAWK · U.S. COAST GUARD FACT SHEET", title="THE NUMBERS THAT SET THE CLOCK",
     cards=[dict(h="700", t="Nautical miles", s="Range"), dict(h="170", t="Knots", s="Top speed"), dict(h="6.5", t="Hours", s="Endurance")],
     footer="SOURCE: U.S. COAST GUARD ACQUISITION DIRECTORATE, MH-60T FACT SHEET")], dict(kind="drive")),
 ("Those numbers are the clock. Every mile out is a mile back. Every minute spent hovering over a ship is fuel the crew will need to get home.",
  [C(1028863, 0.5)], dict(tag=TRN, kind="tense")),
 ("In September, a Jayhawk crew from Borinquen flew to a commercial ship about one hundred nautical miles east of St. Maarten. The Coast Guard called it a complex, long-range medical evacuation.",
  [G("map", map=dict(bounds=[[-68.0, 16.9], [-60.6, 19.4]], cities=[dict(ll=AGU, name="BORINQUEN", d=0.4, anchor="end", size=32), dict(ll=SJU, name="SAN JUAN", sub="CENTRO MÉDICO", d=1.6, dy=40, size=32), dict(ll=SXM, name="ST. MAARTEN", d=0.7, size=32, dy=50), dict(ll=STX, name="SHIP", sub="~100 NM EAST OF ST. MAARTEN", d=1.0, anchor="end", dy=70)],
       rings=[dict(ll=STX, r=30, n=3, d=1.0)], arcs=[dict(**{"from": STX, "to": SJU}, d=1.5, color="#6CF29A")], topPad=120),
     kicker="CARIBBEAN · SEPTEMBER 19, 2026", title="A LONG-RANGE MEDEVAC", footer="SOURCE: U.S. COAST GUARD VIA DVIDS · POSITIONS APPROXIMATE")], dict(kind="calm")),
 ("Infrared video shows the ship's deck. The crew hoisted a forty-six-year-old mariner and flew him to the Centro Médico trauma center in San Juan for emergency specialized care.",
  [C(1023702, 1.0)], dict(tag=STM, kind="calm")),
 ("On Halloween, off San Francisco, the job went to another Coast Guard helicopter, an MH-65 Dolphin. The patient was a fifty-three-year-old man on a container ship, thirty-four miles out.",
  [C(1028385, 8.2)], dict(tag=SFO, kind="drive")),
 ("Overhead, a C-27 Spartan airplane from Air Station Sacramento provided coordination and overwatch while the Dolphin made the hoist.",
  [C(1028385, 30.0)], dict(tag=SFO, kind="calm")),
 ("Often, that is the pattern. One aircraft to search, guide and watch. One to hoist. And on the end of the cable, a human being from the crew.",
  [C(1028863, 80.0)], dict(tag=TRN, kind="calm", gap=0.6)),

 # ---------------- IV. 37 DEGREES ----------------
 ("For decades, that person on the cable was missing.",
  [G("chapter", case="FEB. 12, 1983", n="IV", t="37 DEGREES")], dict(gap=1.0, kind="calm")),
 ("The S.S. Marine Electric was a six hundred five foot cargo ship with a crew of thirty-four. On February twelfth, nineteen eighty-three, about thirty miles off Chincoteague, Virginia, she capsized and sank.",
  [G("doc", header="ATLANTIC OCEAN · FEBRUARY 12, 1983", title="SS MARINE ELECTRIC", body="605-foot cargo ship · 34 crew · capsizes about 30 miles off Chincoteague, Virginia. First distress call: 2:51 a.m.",
     source="SOURCES: U.S. COAST GUARD · SEAPOWER MAGAZINE", stamp="CAPSIZED")], dict(kind="tense")),
 ("Her first distress call went out at two fifty-one in the morning. The water was thirty-seven degrees.",
  [G("stat", a="37°F", b="THE WATER TEMPERATURE THE CREW FACED", c="FEBRUARY 12, 1983 · SOURCE: U.S. COAST GUARD")], dict(kind="punch")),
 ("Coast Guard helicopters came. One crew lifted a survivor from a life raft in a rescue basket, and pulled another man from a life ring. A Norwegian merchant ship spotted a third man in a lifeboat, and a helicopter lifted him out.",
  [G("callcard", kicker="MARINE ELECTRIC · FEBRUARY 12, 1983", title="THE THREE WHO LIVED",
     rows=[["LIFE RAFT", "Hoisted into a Coast Guard helicopter in a basket"], ["LIFE RING", "Retrieved by the same helicopter crew"], ["LIFEBOAT", "Spotted by the Norwegian ship Berganger, lifted in a basket"]],
     footer="SOURCE: U.S. COAST GUARD, \"THE SHIPWRECK THAT CHANGED THE COAST GUARD FOREVER\", 2025")], dict(kind="tense")),
 ("But in nineteen eighty-three, the Coast Guard did not have any rescue swimmers. No one on its helicopters was trained to go down into that water and bring a survivor to the basket.",
  [G("doc", header="U.S. COAST GUARD · 1983", title="RESCUE SWIMMERS", body="At that time the Coast Guard did not have any rescue swimmers.", source="SOURCE: SEAPOWER MAGAZINE (NAVY LEAGUE)", stamp="NONE")], dict(kind="tense")),
 ("The Navy did. Petty Officer Second Class James McCann, a Navy rescue swimmer from Naval Air Station Oceana, went into the water.",
  [G("doc", header="U.S. NAVY · NAVAL AIR STATION OCEANA · 1983", title="PO2 JAMES McCANN", body="Navy rescue swimmer. The Navy had rescue swimmers in 1983. The Coast Guard did not.",
     source="SOURCES: U.S. COAST GUARD · SEAPOWER MAGAZINE", stamp="NAVY SWIMMER")], dict(kind="drive")),
 ("The Coast Guard's own account says one rescue swimmer recovered five unresponsive sailors before hypothermia left him unable to go on.",
  [G("stat", a="5", b="UNRESPONSIVE SAILORS RECOVERED BY ONE RESCUE SWIMMER BEFORE HYPOTHERMIA STOPPED HIM", c="FEBRUARY 12, 1983 · SOURCE: U.S. COAST GUARD, 2025")], dict(kind="tense")),
 ("Of thirty-four men, three survived. Thirty-one died. Rescuers recovered twenty-four bodies. Seven men were never found.",
  [G("stat", a="3 OF 34", b="SURVIVED THE SINKING OF THE MARINE ELECTRIC", c="31 DIED · 7 NEVER FOUND · SOURCE: U.S. COAST GUARD, 2025")], dict(kind="slow")),
 ("A board of inquiry later found that inspectors had missed problems on the ship, despite recent inspections. It concluded the sinking most likely came from poor cargo hatches and deck plating, which let waves flood the forward spaces.",
  [G("doc", header="MARINE BOARD OF INQUIRY · MARINE ELECTRIC", title="THE FINDINGS", body="Inspectors missed several discrepancies despite recent inspections. Most likely cause: inadequate cargo hatches and deck plating let waves flood the forward spaces.",
     source="SOURCE: U.S. COAST GUARD, 2025", stamp="MISSED")], dict(kind="calm")),
 ("The investigation that followed changed ship safety. It led to new rules for cold water survival suits, enclosed lifeboats and tighter inspections of old ships. Seventy vessels from the Second World War era were scrapped.",
  [G("list", kicker="AFTER THE MARINE ELECTRIC", title="WHAT CHANGED ON SHIPS", items=["Cold water survival suits", "Enclosed lifeboats and launching systems", "Flooding alarms in unmanned spaces", "Tighter inspections of ships 20+ years old"],
     footer="70 WWII-ERA VESSELS SCRAPPED · SOURCE: U.S. COAST GUARD")], dict(kind="calm")),
 ("And it changed the helicopters. With funding from the Coast Guard Authorization Act of nineteen eighty-four, the Coast Guard started its own rescue swimmer program.",
  [G("doc", header="U.S. CONGRESS · 1984", title="COAST GUARD AUTHORIZATION ACT OF 1984", tsize=78, body="Funding for a Coast Guard rescue swimmer program.", source="SOURCE: SEAPOWER MAGAZINE (NAVY LEAGUE)", stamp="FUNDED")], dict(kind="drive")),
 ("This is what that program looks like today. On November fifth, in training near Mona Island, Puerto Rico, a rescue swimmer from Air Station Borinquen rode the hoist from a Jayhawk all the way down to the sea, then back up to the door.",
  [C(1028863, 14.0), C(1028863, 61.7)], dict(tag=TRN, kind="drive")),
 ("In March nineteen eighty-five, the first rescue swimmers reported to Air Station Elizabeth City, North Carolina. Two months later, the program saved its first life. By nineteen ninety-one, rescue swimmers were at twenty-three Coast Guard bases.",
  [G("timeline", kicker="FROM ONE FLIGHT TO A SYSTEM", title="HOW THE HOIST GOT A SWIMMER",
     events=[dict(y="1944", t="Erickson flies plasma in a storm"), dict(y="1945", t="First hoist rescue over water"), dict(y="1983", t="Marine Electric: 31 of 34 die"), dict(y="1984", t="Rescue swimmer program funded"), dict(y="1985", t="First swimmers: Elizabeth City"), dict(y="1991", t="Swimmers at 23 bases")],
     footer="SOURCES: U.S. COAST GUARD · NHHC · SEAPOWER MAGAZINE")], dict(kind="calm", gap=0.6)),

 # ---------------- V. DOWN THE WIRE ----------------
 ("Forty-one years later, a crew from that same air station got a call from a cruise ship.",
  [G("chapter", case="NOV. 2, 2026", n="V", t="DOWN THE WIRE")], dict(gap=1.0, kind="calm")),
 ("Norwegian Bliss carries about four thousand guests. On November second, she was about thirty-two miles off Oregon Inlet, North Carolina, on a cruise from New York to the Bahamas. The ship reported that a passenger needed medical attention.",
  [C(1028902, 171.0)], dict(tag=BLISS, kind="calm")),
 ("The ship had left New York the day before, on an eight-night round trip. November second was a sea day. No hospital, no port, only open water off the Outer Banks.",
  [C(1028902, 1.0)], dict(tag=BLISS, kind="calm")),
 ("An aircrew from Air Station Elizabeth City flew out. This is the view from a camera inside the helicopter's door.",
  [C(1028902, 13.0)], dict(tag=BLISS, kind="drive")),
 ("Inside, the crew wear helmets marked U-S-C-G. The door is open. Below them is the top deck of a cruise ship, and the sea beyond it.",
  [C(1028902, 20.0)], dict(tag=BLISS, kind="calm")),
 ("A crew member rides the hoist down to the ship's deck. The yellow circle below is the spot marked for the winch.",
  [C(1028902, 29.0), C(1028902, 36.0)], dict(tag=BLISS, kind="tense")),
 ("Then the patient comes up, strapped into a rescue litter, turning slowly on the cable, until the crew can pull it in through the door.",
  [C(1028902, 56.0), C(1028902, 66.0)], dict(tag=BLISS2, kind="slow")),
 ("The Coast Guard hoisted an onboard nurse as well. The aircrew flew both of them to Sentara Norfolk General Hospital in Norfolk, Virginia.",
  [C(1028902, 140.0)], dict(tag=BLISS, kind="calm")),
 ("Officials said the passenger was transferred in stable condition. No change to the cruise was reported.",
  [C(1028902, 161.0)], dict(tag=BLISS, kind="calm")),
 ("In September, a Borinquen crew did the same job in the dark, over the helicopter pad of the cruise ship Allure of the Seas, off Puerto Rico. The patient, a crew member, was taken to a hospital in Aguadilla.",
  [C(1024523, 2.0), C(1024523, 47.0)], dict(tag=ALL, kind="calm", gap=0.6)),

 # ---------------- VI. FIFTY MILES OUT ----------------
 ("Now, back to the burning boat.",
  [G("chapter", case="OCT. 13, 2026", n="VI", t="FIFTY MILES OUT")], dict(gap=1.0, kind="calm")),
 ("On October thirteenth, a ninety-foot fishing vessel caught fire about fifty miles off Dauphin Island, Alabama. Four people were aboard. This video, released by the Coast Guard, shows the fire up close.",
  [C(1026608, 32.8), C(1026608, 59.0)], dict(tag=FIRE, kind="tense")),
 ("The first Coast Guard aircraft to find it was not a helicopter. It was an HC-144 Ocean Sentry airplane from the Coast Guard's Aviation Training Center in Mobile.",
  [G("map", map=dict(bounds=[[-89.6, 29.0], [-87.2, 30.9]], cities=[dict(ll=[-88.11, 30.25], name="DAUPHIN ISLAND", d=0.4, size=32), dict(ll=[-88.07, 30.69], name="MOBILE", sub="AVIATION TRAINING CENTER", d=0.7, size=32), dict(ll=[-90.03, 29.83], name="NEW ORLEANS", d=0.9, size=32), dict(ll=[-88.11, 29.53], name="FISHING VESSEL", sub="ABOUT 50 MILES OFFSHORE", d=1.1, anchor="end", dy=40)],
       rings=[dict(ll=[-88.11, 29.53], r=30, n=3, d=1.1, color="#E5383B")], arcs=[dict(**{"from": [-89.95, 29.85], "to": [-88.11, 29.53]}, d=1.5, color="#6CF29A")]),
     kicker="GULF COAST · OCTOBER 13, 2026", title="A BOAT ON FIRE", footer="SOURCE: U.S. COAST GUARD VIA DVIDS · POSITIONS APPROXIMATE")], dict(kind="drive")),
 ("The Ocean Sentry is built for exactly this kind of search. The Coast Guard's fact sheet lists more than ten hours of endurance, a range of two thousand one hundred nautical miles, and search radar with infrared sensors. It can stay up long after a helicopter has to turn home.",
  [G("cards3", kicker="HC-144 OCEAN SENTRY · U.S. COAST GUARD FACT SHEET", title="THE AIRCRAFT THAT FINDS",
     cards=[dict(h="10+", t="Hours", s="Endurance"), dict(h="2,100", t="Nautical miles", s="Range", size=96), dict(h="IR", t="Sensors", s="Radar + electro-optical/infrared")],
     footer="SOURCE: U.S. COAST GUARD ACQUISITION DIRECTORATE, HC-144 FACT SHEET, 2025")], dict(kind="calm")),
 ("On infrared, the fire shows up as a blaze of white heat on a black sea. The plane found the boat, then guided a Jayhawk from Air Station New Orleans to it.",
  [C(1026608, 54.0), C(1026608, 84.0)], dict(tag=FLIR, kind="tense")),
 ("The boat kept burning while the helicopter worked.",
  [C(1026608, 96.0)], dict(tag=FLIR, kind="tense")),
 ("The Jayhawk crew rescued all four people and flew them to the Aviation Training Center. Officials said no one was injured. The cause of the fire was not known.",
  [G("stat", a="4 OF 4", b="RESCUED FROM THE BURNING BOAT · NO ONE INJURED", c="OCT. 13, 2026 · SOURCES: U.S. COAST GUARD VIA DVIDS · WKRG")], dict(kind="punch")),
 ("Four people. Fifty miles from shore. A boat on fire. And a crew that came down out of the night.",
  [C(1026608, 40.0)], dict(tag=FLIR, kind="slow", gap=0.6)),

 # ---------------- VII. ORDINARY WEEKS ----------------
 ("These were not the only calls.",
  [G("chapter", case="SEPT.–NOV. 2026", n="VII", t="ORDINARY WEEKS")], dict(gap=1.0, kind="calm")),
 ("Off Alaska in September, near Murder Cove on Admiralty Island, a Jayhawk crew from Air Station Sitka found a boater whose fishing vessel had sunk. His life raft had begun taking on water. The crew lowered the hoist to the rocks and brought him up.",
  [C(1025010, 10.0), C(1025010, 205.0)], dict(tag=AK, kind="tense")),
 ("On Lake Michigan in November, near Green Island, Wisconsin, a crew from Air Station Traverse City hoisted a man from a sailboat that had lost power and run aground. A Coast Guard response boat from Station Sturgeon Bay also came, but shallow water kept it back.",
  [C(1029116, 1.0), C(1029116, 20.0)], dict(tag=LM, kind="drive")),
 ("In South Carolina, a crew from Air Station Savannah hoisted six people from a grounded eighteen-foot boat near Turtle Island, at night, and flew them to Hunter Army Airfield. No one was hurt. Off Hawaii, a Dolphin crew from Barbers Point medevaced a man with a medical condition from a cargo ship eighty-six miles out, and flew him to Hilo for higher medical care.",
  [C(1028766, 63.0), C(1028766, 84.1)], dict(tag=SC, kind="calm")),
 ("Put the cases from this story together and you get the Coast Guard's ordinary autumn.",
  [G("callcard", kicker="U.S. COAST GUARD RELEASES VIA DVIDS · SEPTEMBER–NOVEMBER 2026", title="ONE AUTUMN OF HOISTS",
     rows=[["SEPT. 19", "Mariner · ~100 NM east of St. Maarten"], ["SEPT. 28", "Boater · raft taking on water · Alaska"], ["OCT. 13", "4 people · burning boat · Alabama"], ["NOV. 2", "Passenger + nurse · cruise ship · N.C."], ["NOV. 8", "4 mariners · oil tanker · Puerto Rico"]])], dict(kind="drive")),
 ("In nineteen forty-four, one helicopter carried two cases of plasma for fourteen minutes, and it was history.",
  [C("heli1947", 37.5)], dict(tag=H47, kind="calm")),
 ("In nineteen eighty-three, Coast Guard helicopters reached the men in the water, and the Coast Guard had no one of its own to send in after them.",
  [G("stat", a="31", b="MEN LOST WITH THE MARINE ELECTRIC, 1983", c="THE COAST GUARD HAD NO RESCUE SWIMMERS · SOURCES: U.S. COAST GUARD · SEAPOWER")], dict(kind="slow")),
 ("And in big disasters, the system Erickson started scales up. The Coast Guard's historian counts twelve thousand five hundred thirty-five air rescues in two weeks during Hurricane Katrina, and eleven thousand three hundred sixty-three lives saved in the twenty seventeen hurricane season.",
  [G("stat", a="12,535", b="COAST GUARD AIR RESCUES IN TWO WEEKS · HURRICANE KATRINA", c="2017 HURRICANE SEASON: 11,363 LIVES SAVED · SOURCE: U.S. COAST GUARD HISTORIAN'S OFFICE")], dict(kind="punch")),
 ("Today, a crew of four flies out a hundred miles, lowers one of its own onto a ship's deck, and brings people back to a hospital.",
  [C(1025010, 214.0)], dict(tag=AK, kind="calm")),
 ("No ambulance can reach them out there. So the Coast Guard sends one down a cable.",
  [C(1028902, 149.5)], dict(tag=BLISS, kind="slow", gap=0.6)),
 ("Next time on KEPT ALIVE: another real save, and the history behind it.",
  [G("end", label="KEPT ALIVE · THE SAVE · NEXT", stamp="NEXT SAVE")], dict(kind="calm")),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="FOR EDUCATION ONLY · NOT MEDICAL ADVICE", stamp="KEPT ALIVE")], dict(kind="calm", gap=2.0)),
]

DISPLAY = [
 ("ninety-foot", "90-foot"), ("Fifty miles", "50 miles"), ("fifty miles", "50 miles"), ("a hundred miles", "100 miles"),
 ("three hundred twenty-eight feet", "328 feet"), ("MH-60T", "MH-60T"), ("U.S.S. Turner", "USS Turner"),
 ("January third, nineteen forty-four", "January 3, 1944"), ("nineteen forty-four", "1944"), ("forty-seven minutes", "47 minutes"),
 ("ten twenty", "10:20"), ("ten fifty-five", "10:55"), ("eleven oh nine", "11:09"), ("fourteen minutes", "14 minutes"),
 ("Eighty-two years", "82 years"), ("seven hundred nautical miles", "700 nautical miles"), ("one hundred seventy knots", "170 knots"),
 ("six and a half hours", "6.5 hours"), ("one hundred nautical miles", "100 nautical miles"), ("forty-six-year-old", "46-year-old"),
 ("fifty-three-year-old", "53-year-old"), ("thirty-four miles", "34 miles"), ("six hundred five foot", "605-foot"),
 ("a crew of thirty-four", "a crew of 34"), ("February twelfth, nineteen eighty-three", "February 12, 1983"), ("nineteen eighty-three", "1983"),
 ("thirty miles", "30 miles"), ("two fifty-one", "2:51"), ("thirty-seven degrees", "37 degrees"),
 ("Of thirty-four men, three survived. Thirty-one died. Rescuers recovered twenty-four bodies. Seven", "Of 34 men, 3 survived. 31 died. Rescuers recovered 24 bodies. 7"),
 ("Seventy vessels", "70 vessels"), ("nineteen eighty-four", "1984"), ("March nineteen eighty-five", "March 1985"),
 ("nineteen ninety-one", "1991"), ("twenty-three", "23"), ("Forty-one years", "41 years"), ("four thousand", "4,000"),
 ("November second", "November 2"), ("thirty-two miles", "32 miles"), ("October thirteenth", "October 13"),
 ("eighty-six miles", "86 miles"), ("eighteen-foot", "18-foot"), ("twenty twenty-two", "2022"), ("November fifth", "November 5"), ("U-S-C-G", "USCG"), ("H-N-S-1", "HNS-1"), ("twelve thousand five hundred thirty-five", "12,535"), ("eleven thousand three hundred sixty-three", "11,363"), ("twenty seventeen", "2017"), ("November nineteen forty-five", "November 1945"), ("sixty miles an hour", "60 miles an hour"), ("ten hours", "10 hours"), ("two thousand one hundred nautical miles", "2,100 nautical miles"), ("nineteen thirty-one", "1931"), ("Second Class", "2nd Class"), ("C-27", "C-27"), ("HC-144", "HC-144"), ("MH-65", "MH-65"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · THE SAVE",
    title="The Hoist",
    voice="am_fenrir",
    imgs={},
    mute_nat=["1026608", "1029245", "1028902", "1023702", "1024523", "1028385", "1025010", "1029116", "1028766", "1028863", "heli1947"],
    training=["1028863"],
    credit=("Footage: U.S. Coast Guard via DVIDS (public domain). Training footage is marked TRAINING."
            r"\NArchival film (public domain): U.S. Navy, Naval Photographic Center film 3017, 1947 (National Archives) — not the 1944 flight."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the U.S. Coast Guard, DoD or any government agency."
            r"\NFor education only. This is not medical advice."),
)

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))  # longest first
