# KEPT ALIVE · Shorts-only day Tuesday 2026-11-24 (owner rule 2026-11-23: 3 candidates, only the best 1–2 on YouTube, 10:00 + 18:00 ET).
# Visual templates (yesterday s1–s3 of 104 were all number-card-led):
#   s1 = archival-photo + location footage led (Desmond Doss portrait 1945 + Hacksaw Ridge today) — famous name + number hook
#   s2 = fresh footage led (Coast Guard hoist-cam, Nov 20 2026, real event) + one distance card
#   s3 = paradox hook (WWII Pacific corpsmen took off the red cross) — archival-film led (NPC-8963 Iwo Jima 1945) + 2 quote cards + fresh Keen Sword 27 TRAINING footage
# shot: (clip_id, start, cx). st_*/card_* = 20 s push-ins from make_cards.py. No blood, wounds, bodies or patient faces.
SHORTS = [
 dict(id="s1", credit="Photo: AMEDD Historian (PD) · Footage: U.S. Army via DVIDS",
      hook="DESMOND DOSS<br>[NO RIFLE. ~75 MEN.]", title="Desmond Doss Refused a Rifle. He Saved About 75 Men",
      label="SOURCES: MOH CITATION · ARMY.MIL · AMEDD HISTORIAN\\NRIDGE: HACKSAW RIDGE, OKINAWA · 2020 VIDEO",
      lines=[
  ("Desmond Doss refused to carry a rifle. The Army credits him with rescuing about seventy-five men.", [("st_doss", 0.5, .5)], "punch"),
  ("He was an Army medic who would not take a life.", [("st_doss_face", 0.5, .5)], "calm"),
  ("Okinawa, nineteen forty-five: fire drove his battalion back from the top of a cliff about four hundred feet high.", [("766514", 167.0, .5), ("766514", 202.0, .45)], "tense"),
  ("Doss stayed. One by one, he lowered the wounded down on a rope-supported litter.", [("766514", 42.5, .5), ("766514", 62.0, .5)], "drive"),
  ("His prayer, as the Army tells it: Dear God, let me get just one more man.", [("766514", 205.0, .4)], "slow"),
  ("President Truman gave him the Medal of Honor. The only known conscientious objector to receive it in World War Two.", [("st_doss", 0.5, .5)], "calm"),
 ]),
 dict(id="s2", credit="Footage: PO3 Richard Uranga, U.S. Coast Guard via DVIDS",
      hook="~80 MILES OUT<br>[POSSIBLE HEART ATTACK]", title="About 80 Miles Out: Coast Guard Hoists a Cruise Passenger",
      label="REAL MEDEVAC · NOV. 20, 2026 · OFF SAN DIEGO\\NU.S. COAST GUARD VIDEO",
      lines=[
  ("About eighty miles off San Diego, a seventy-four-year-old cruise passenger had symptoms of a possible heart attack.", [("1030654", 3.0, .35), ("1030654", 9.0, .35)], "punch"),
  ("Coast Guard Sector San Diego coordinated the launch of an MH-60 Jayhawk crew from Air Station Ventura.", [("card_80mi", 0.5, .5)], "drive"),
  ("This is Coast Guard video of the hoist from the cruise ship Koningsdam.", [("1030654", 14.0, .45), ("1030654", 19.0, .5)], "calm"),
  ("The hoist. The litter. The deck. The open sea.", [("1030654", 23.5, .4), ("1030654", 46.0, .3)], "tense"),
  ("The man was taken to Scripps Memorial Hospital in La Jolla.", [("1030654", 51.0, .3)], "slow"),
 ]),
 dict(id="s3", credit="Film: Iwo Jima 1945 (NARA, PD) · Footage: USMC via DVIDS",
      hook="WHY HIDE<br>[THE RED CROSS?]", title="Why WWII Medics in the Pacific Took Off Their Red Crosses",
      label="FILM: MARINES ON IWO JIMA, MARCH 1945 (NARA)\\NTODAY: KEEN SWORD 27, IWAKUNI, OCT 2026 · TRAINING",
      lines=[
  ("In the Pacific in World War Two, Navy corpsmen began taking off their red crosses, because the enemy aimed at them.", [("npc_walk", 2.0, .5), ("npc_walk", 7.0, .4)], "punch"),
  ("The National Museum of the Pacific War: Japanese forces made an intentional effort to target American corpsmen.", [("card_target", 0.5, .5)], "tense"),
  ("An Army historian's account: medics even dyed their bandages jungle green.", [("npc_sit", 0.5, .5)], "drive"),
  ("Corpsmen started carrying pistols.", [("npc_walk", 13.5, .55)], "calm"),
  ("In nineteen forty-five, Navy Secretary James Forrestal told them: sniper's bullets were aimed at the brassards on your arms.", [("card_forrestal", 0.5, .5)], "slow"),
  ("Today, Navy medical sailors still train beside Marines, like this exercise in Japan last month.", [("1027486", 31.0, .45), ("1027486", 77.0, .5)], "calm"),
 ]),
]

DISPLAY = [
 ("about seventy-five", "about 75"), ("seventy-five", "75"), ("Okinawa, nineteen forty-five", "Okinawa, 1945"),
 ("about four hundred feet", "about 400 feet"), ("World War Two", "World War II"), ("nineteen forty-five", "1945"),
 ("About eighty miles", "About 80 miles"), ("seventy-four-year-old", "74-year-old"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["766514", "st_doss", "st_doss_face", "card_80mi", "card_target", "card_forrestal", "npc_walk", "npc_sit", "1027486"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
