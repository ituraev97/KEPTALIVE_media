# KEPT ALIVE · Shorts-only day, Saturday 2026-11-21 (Format v2/v3 Shorts rules). One war-medicine fact each, winner subjects (blood, tourniquet, wounded + medevac).
# Templates: s1 = year + object (1917 blood on ice in ammo boxes, WWI) — own cards + fresh-ish DVIDS 95th Med. Det. Blood Support frozen-blood stress test (Camp Humphreys, Aug 25 2026, TRAINING)
#            s2 = percentage hook -> lesson (7.4% Vietnam limb-bleeding deaths -> TCCC 1996 -> tourniquets 2005) — own cards + fresh DVIDS Navy TCCC course (Sigonella, Nov 12 2026, TRAINING)
#            s3 = image contrast then vs now (Korea 1951 H-13 litter pods outside the helicopter) — U.S. Army 1951 photo (via MHS/DVIDS 1029263) + own cards + fresh DVIDS hoist training (Fort McCoy, Nov 2026, TRAINING)
# shot: (clip_id, start, cx). card_*/st_* = 20 s push-ins rendered by make_stills.py. No patient is named or shown; no blood, wounds or patient faces (1030324 moulage shots avoided).
SHORTS = [
 dict(id="s1", credit="Footage: U.S. Army via DVIDS (TRAINING) · Graphics: KEPT ALIVE",
      hook="1917<br>[BLOOD ON ICE]", title="A WWI Army Doctor Shipped Blood in Ammo Boxes on Ice",
      label="SOURCES: KUMC · NATIONAL ARCHIVES (UK) · PROTO\\NTRAINING: ARMY FROZEN BLOOD, KOREA, AUG 2026",
      lines=[
  ("Blood on ice. In nineteen seventeen, a U.S. Army doctor in France found a way to store blood for wounded soldiers.", [("card_ice", 0.5, .5)], "punch"),
  ("Oswald Robertson used only type O donors, safe to give most soldiers.", [("card_typeo", 0.5, .5)], "calm"),
  ("In glass bottles, citrate kept it from clotting.", [("card_bottles", 0.5, .5)], "calm"),
  ("The bottles rode in ammunition boxes, packed with sawdust and ice.", [("card_ammo", 0.5, .5)], "drive"),
  ("It could keep up to twenty-six days.", [("card_26", 0.5, .5)], "slow"),
  ("It was tested at the Battle of Cambrai. Many consider it the world's first blood bank.", [("card_cambrai", 0.5, .5)], "calm"),
  ("Today, Army blood teams in Korea keep frozen blood ready for troops, like this unit in August.", [("1022067", 29.6, .5), ("1022067", 36.3, .4)], "calm"),
 ]),
 dict(id="s2", credit="Footage: U.S. Navy via DVIDS (TRAINING) · Graphics: KEPT ALIVE",
      hook="7.4%<br>[LIMB BLEEDING]", title="Vietnam's Lesson: Why Deploying Troops Carry Tourniquets",
      label="SOURCES: J TRAUMA 2012 · JSOM 2015\\NTRAINING FOOTAGE: NAVY TCCC, SICILY, NOV 2026",
      lines=[
  ("Seven point four percent of U.S. soldiers killed in action in one Vietnam study died of bleeding from an arm or leg alone.", [("card_74", 0.5, .5)], "punch"),
  ("Yet the standard trauma course discouraged tourniquets.", [("card_atls", 0.5, .5)], "slow"),
  ("In nineteen ninety-six, Frank Butler, an ex-SEAL turned doctor, co-wrote the first Tactical Combat Casualty Care guidelines.", [("card_1996", 0.5, .5)], "calm"),
  ("They called tourniquets appropriate on the battlefield.", [("1030324", 21.9, .5)], "drive"),
  ("In two thousand five, the Army ordered them for all soldiers deploying to Iraq and Afghanistan.", [("card_2005", 0.5, .5)], "calm"),
  ("A two thousand nine estimate: one to two thousand American lives saved.", [("card_lives", 0.5, .5)], "slow"),
  ("Navy teams still train for it, like here in Sicily.", [("1030324", 36.6, .65), ("1030324", 42.2, .5)], "calm"),
 ]),
 dict(id="s3", credit="Photo: U.S. Army 1951 via MHS/DVIDS · Footage: U.S. Army (TRAINING)",
      hook="KOREA<br>[OUTSIDE THE CHOPPER]", title="Korea: Wounded Soldiers Rode Outside the Helicopter",
      label="SOURCES: ARMY.MIL · CENTENNIALOFFLIGHT.NET\\NPHOTO: U.S. ARMY 1951 · TRAINING: FT. MCCOY 2026",
      lines=[
  ("Korea, nineteen fifty-one. Wounded soldiers flew outside the helicopter, in pods on the skids of a small Bell H-thirteen.", [("st_h13", 0.5, .5)], "punch"),
  ("Two at a time. The first Army helicopter medevac missions flew that January.", [("card_1951", 0.5, .5)], "calm"),
  ("A cold, windy ride, but it rushed them to trained doctors.", [("st_h13b", 0.5, .5)], "slow"),
  ("H-thirteen crews carried eighteen thousand of twenty-three thousand casualties to MASH units.", [("card_18000", 0.5, .5)], "drive"),
  ("The death rate of evacuated patients before reaching care fell from four point five percent in World War Two to two point five in Korea.", [("card_rate", 0.5, .5)], "calm"),
  ("Today, Black Hawk crews train to hoist litters inside, like here in Wisconsin.", [("1030413", 19.2, .7), ("1030413", 112.95, .3)], "calm"),
 ]),
]

DISPLAY = [
 ("In nineteen seventeen", "In 1917"), ("twenty-six days", "26 days"),
 ("Seven point four percent", "7.4%"), ("ex-SEAL", "ex-SEAL"), ("In nineteen ninety-six", "In 1996"), ("In two thousand five", "In 2005"),
 ("A two thousand nine estimate", "A 2009 estimate"), ("one to two thousand", "1,000 to 2,000"),
 ("Korea, nineteen fifty-one", "Korea, 1951"), ("January third, nineteen fifty-one", "January 3, 1951"), ("H-thirteen", "H-13"),
 ("eighteen thousand of twenty-three thousand", "18,000 of 23,000"), ("four point five percent", "4.5%"), ("two point five", "2.5%"),
 ("World War Two", "World War II"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["1022067", "1030324", "1030413", "card_ice", "card_typeo", "card_bottles", "card_ammo", "card_26", "card_cambrai",
        "card_74", "card_atls", "card_1996", "card_2005", "card_lives", "card_1951", "card_18000", "card_rate", "st_h13", "st_h13b"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
