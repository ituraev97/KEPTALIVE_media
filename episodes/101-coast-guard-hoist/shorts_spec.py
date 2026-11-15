# Shorts for KEPT ALIVE · THE SAVE 101 — the Coast Guard hoist (long video Mon 2026-11-16 13:00 ET). Three Shorts from the story; facts as verified for the long episode.
# Templates: s1 = then -> now ("1944 vs. Now": the first helicopter lifesaving flight carried plasma -> Nov 2026 cruise-ship hoist)
#            s2 = one shocking number ("31 of 34": Marine Electric 1983 -> rescue swimmer program -> Nov 2026 swimmer TRAINING)
#            s3 = real save this month ("No ambulance at sea": 4 sick tanker crew hoisted off Vieques, Nov 8, 2026)
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own branded cards (make_cards.py). heli1947 = Navy film 1947 (NARA), never the 1944 flight.
# No patient is named. No blood, wounds or patient faces. 1028863 is TRAINING (label says so).
SHORTS = [
 dict(id="s1", credit="Film: U.S. Navy 1947 (NARA) · Footage: USCG via DVIDS",
      hook="1944<br>[VS. NOW]", title="1944 vs. Now: The First Helicopter Lifesaving Flight",
      label="GRAPHICS: KEPT ALIVE · SOURCES: NHHC, USCG HISTORIAN\\NARCHIVAL FILM 1947 · NOT THE 1944 FLIGHT · USCG, NOV 2026",
      lines=[
  ("In nineteen forty-four, the first helicopter lifesaving flight carried no patient. It carried blood plasma.", [("card_1944", 0.5, .5)], "punch"),
  ("A Navy destroyer had exploded outside New York Harbor. A storm grounded every plane. The wounded needed plasma.", [("heli1947", 18.0, .5), ("heli1947", 28.0, .5)], "tense"),
  ("Two cases were lashed to a Coast Guard helicopter's floats. Frank Erickson flew them to Sandy Hook in about fourteen minutes.", [("card_14min", 0.5, .5)], "drive"),
  ("Now: this November, a Coast Guard crew hoisted a cruise ship passenger off North Carolina and flew her to a hospital.", [("1028902", 14.0, .5), ("1028902", 24.0, .5)], "slow"),
 ]),
 dict(id="s2", credit="Graphics: KEPT ALIVE · Footage: USCG via DVIDS",
      hook="31 OF 34<br>[DIED]", title="31 of 34 Died. Then the Coast Guard Got Rescue Swimmers",
      label="GRAPHICS: KEPT ALIVE · SOURCES: USCG, SEAPOWER\\NFOOTAGE: USCG TRAINING, PUERTO RICO · NOV 2026",
      lines=[
  ("Thirty-one of thirty-four men died when the cargo ship Marine Electric sank off Virginia in nineteen eighty-three.", [("card_31", 0.5, .5)], "punch"),
  ("The water was thirty-seven degrees. And the Coast Guard did not have a single rescue swimmer.", [("card_37", 0.5, .5)], "tense"),
  ("A Navy rescue swimmer went into the water. Only three men survived.", [("card_31", 6.0, .5)], "slow"),
  ("The Coast Guard Authorization Act of nineteen eighty-four funded a rescue swimmer program. The first swimmers reported for duty in nineteen eighty-five.", [("1028863", 62.0, .3), ("1028863", 70.0, .3)], "drive"),
  ("This month, near Puerto Rico, they trained the same way: down the cable, into the sea.", [("1028863", 84.0, .3), ("1028863", 90.5, .5)], "calm"),
 ]),
 dict(id="s3", credit="Footage: U.S. Coast Guard via DVIDS · Graphics: KEPT ALIVE",
      hook="4 SICK CREW<br>[NO AMBULANCE]", title="No Ambulance at Sea: 4 Sick Crew, 1 Helicopter",
      label="REAL MEDEVAC · U.S. COAST GUARD HOIST CAMERA\\NNEAR VIEQUES, PUERTO RICO · NOV 8, 2026",
      lines=[
  ("Four crew members, sick on an oil tanker off Puerto Rico. No ambulance can drive to a ship.", [("1029245", 37.0, .5)], "punch"),
  ("The suspected cause was food poisoning. The Coast Guard sent a Jayhawk helicopter from Air Station Borinquen.", [("1029245", 66.0, .5)], "drive"),
  ("The co-pilot called the tanker a challenging place to hoist. The crew found a safe spot and lifted all four aboard.", [("1029245", 80.0, .5), ("1029245", 100.0, .5)], "tense"),
  ("They flew them to San Juan, where medical crews took them to a hospital. November eighth, twenty twenty-six.", [("card_4of4", 0.5, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("nineteen forty-four", "1944"), ("about fourteen minutes", "about 14 minutes"),
 ("Thirty-one of thirty-four", "31 of 34"), ("nineteen eighty-three", "1983"), ("thirty-seven degrees", "37 degrees"),
 ("three men", "3 men"), ("nineteen eighty-four", "1984"), ("nineteen eighty-five", "1985"),
 ("Four crew members", "4 crew members"), ("all four", "all 4"), ("November eighth, twenty twenty-six", "November 8, 2026"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_1944", "card_14min", "card_31", "card_37", "card_4of4", "heli1947", "1028902", "1028863", "1029245"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
