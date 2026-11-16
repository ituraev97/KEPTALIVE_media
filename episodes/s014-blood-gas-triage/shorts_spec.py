# KEPT ALIVE · Shorts-only day, Tuesday 2026-11-17 (Format v2). Three Shorts, one war-medicine fact each, fresh DVIDS footage (published Nov 5 – Nov 12, 2026).
# Templates: s1 = one shocking number (9 in 10 survivable combat deaths: bleeding) -> fresh blood-by-drone drill (TRAINING)
#            s2 = number contrast (70,522 WWI gas cases vs 1,221 deaths) -> decontamination then / gas-mask drill now (TRAINING)
#            s3 = money number ($1.5M grand prize) -> DARPA Triage Challenge finals, robots and drones finding simulated casualties
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own branded cards (make_cards.py).
# No patient is named. No blood, wounds or patient faces. 1028630 is the native 1080x1920 vertical DVIDS file (cx irrelevant).
SHORTS = [
 dict(id="s1", credit="Graphics: KEPT ALIVE · Footage: U.S. Army via DVIDS",
      hook="9 IN 10<br>[BLEEDING]", title="Bleeding Linked to 9 in 10 Potentially Survivable War Deaths",
      label="SOURCE: EASTRIDGE ET AL., J TRAUMA 2012\\NFOOTAGE: FORT HOOD, TEXAS · OCT 2026 · TRAINING",
      lines=[
  ("Nine in ten. Of potentially survivable U.S. deaths in Iraq and Afghanistan before reaching a medical facility, about nine in ten were linked to bleeding.", [("card_9in10", 0.5, .5)], "punch"),
  ("A study of four thousand five hundred ninety-six U.S. battlefield deaths found that most died before ever reaching a surgeon.", [("card_87", 0.5, .5)], "calm"),
  ("Today, the Army trains to bring blood closer. In October at Fort Hood, Texas, cavalry troopers practiced a blood resupply drop.", [("1028630", 1.0, .5), ("1028630", 23.3, .5), ("1028630", 11.9, .5), ("1028630", 13.8, .5)], "drive"),
  ("The blood rides in a small refrigerator aboard a drone, and comes down under a parachute.", [("1028630", 17.0, .5), ("1028630", 20.3, .5)], "calm"),
  ("Troopers on the ground stand by to receive it.", [("1028630", 29.2, .5)], "slow"),
 ]),
 dict(id="s2", credit="Graphics: KEPT ALIVE · Footage: U.S. Army via DVIDS",
      hook="70,522<br>[GASSED]", title="70,522 U.S. Gas Cases in WWI. 1,221 Deaths",
      label="SOURCES: U.S. ARMY HERITAGE CENTER, ANCA\\NFOOTAGE: LANDSTUHL, GERMANY · NOV 2026 · TRAINING",
      lines=[
  ("Seventy thousand five hundred twenty-two. That is how many gas cases American forces reported in World War One.", [("card_70k", 0.5, .5)], "punch"),
  ("Nearly a third of all casualties in the American Expeditionary Forces.", [("card_31", 0.5, .5)], "drive"),
  ("Of those gas cases, one thousand two hundred twenty-one died. Most of them from mustard gas.", [("card_1221", 0.5, .5)], "calm"),
  ("Care started before the hospital. For mustard gas, decontamination: the uniform came off, the soldier was bathed and given new clothes.", [("card_decon", 0.5, .5)], "calm"),
  ("This November, soldiers of an Army hospital center in Germany still trained in gas masks for chemical threats.", [("1029569", 36.4, .45), ("1029569", 50.2, .5), ("1029569", 28.6, .5)], "slow"),
 ]),
 dict(id="s3", credit="Footage: DARPA via DVIDS · Graphics: KEPT ALIVE",
      hook="$1.5M<br>[FIND CASUALTIES]", title="$1.5 Million for Robots That Find Casualties",
      label="DARPA TRIAGE CHALLENGE FINALS · TEXAS\\NNOV 2026 · SIMULATED CASUALTIES · GRAPHICS: KEPT ALIVE",
      lines=[
  ("One and a half million dollars. That was DARPA's top prize for robots and drones that find casualties.", [("1029282", 0.3, .5), ("1029282", 42.0, .5)], "punch"),
  ("This month in Texas, teams sent drones and robot dogs through smoke and rubble to find simulated casualties.", [("1029282", 76.0, .5), ("1029281", 112.2, .5)], "drive"),
  ("Their job: find each casualty, spot life-threatening injuries, and read vital signs from a distance.", [("1029281", 330.0, .5), ("1029281", 344.5, .5)], "calm"),
  ("The goal: help medics triage faster at mass casualty events, on and off the battlefield.", [("1029281", 56.2, .5), ("1029281", 176.5, .5)], "drive"),
  ("The one and a half million went to RoboScout, a University of Maryland team.", [("card_prize", 0.5, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("Nine in ten", "9 in 10"), ("nine in ten", "9 in 10"), ("four thousand five hundred ninety-six", "4,596"),
 ("Seventy thousand five hundred twenty-two", "70,522"), ("one thousand two hundred twenty-one", "1,221"),
 ("World War One", "World War I"), ("One and a half million dollars", "$1.5 million"), ("one and a half million", "$1.5 million"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_9in10", "card_87", "card_70k", "card_31", "card_1221", "card_decon", "card_prize", "1028630", "1029569", "1029282", "1029281"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
