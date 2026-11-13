# Shorts for KEPT ALIVE · OUTBREAK 012 — Cholera and the Broad Street pump. Three Shorts, one fact each; facts as verified for the long episode.
# Templates: s1 = one shocking fact (the brewery workers who escaped, Snow 1855)
#            s2 = countdown "in 3 numbers" (500 deaths -> 61 who drank the pump water -> 2 ft 8 in from cesspool to well)
#            s3 = then -> now (typhoid 1900 vs 2006, CDC; 1943 Army film -> 2026 field purification)
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own branded cards (make_cards.py). map_* = push-ins of Snow's 1855 map (public domain).
# No patient is named. No patients, bodies or illness on screen. Training footage labelled.
SHORTS = [
 dict(id="s1", credit="Map: John Snow, 1855 (Wellcome Collection) · Graphics: KEPT ALIVE",
      hook="70+ WORKERS<br>[NO SEVERE CASES]", title="The Brewery Workers Who Escaped London's 1854 Cholera",
      label="GRAPHICS: KEPT ALIVE · SOURCE: JOHN SNOW, 1855\\NMAP: SOHO, LONDON · SNOW, 1855 · WELLCOME COLLECTION",
      lines=[
  ("In eighteen fifty-four, cholera killed more than five hundred people around one London pump. The brewery near it had no severe cases.", [("card_brew", 0.5, .5)], "punch"),
  ("It had more than seventy workmen. The owner told Doctor John Snow they drank malt liquor, not water.", [("map_brew", 1.0, .64)], "calm"),
  ("The brewery had its own deep well. The owner was certain his men never took water from the pump in the street.", [("map_brew", 9.0, .64)], "drive"),
  ("Snow traced the outbreak to that pump. Its handle came off on September eighth.", [("map_pump", 2.0, .5)], "slow"),
 ]),
 dict(id="s2", credit="Graphics: KEPT ALIVE · Map: John Snow, 1855 (Wellcome Collection)",
      hook="1 PUMP<br>[3 NUMBERS]", title="500 Deaths, 1 Pump: London's 1854 Cholera in 3 Numbers",
      label="GRAPHICS: KEPT ALIVE · JOHN SNOW, 1855 · UCLA\\NMAP: BROAD STREET, LONDON · SNOW, 1855",
      lines=[
  ("London, eighteen fifty-four. One water pump, in three numbers.", [("card_500", 0.5, .5)], "punch"),
  ("More than five hundred. Cholera deaths in ten days, within about two hundred fifty yards of the pump.", [("card_500", 3.0, .5)], "drive"),
  ("Sixty-one. The victims John Snow was told had drunk its water.", [("card_61", 0.5, .5)], "calm"),
  ("Two feet eight inches. The distance from the well to a leaking cesspool beside it.", [("card_2ft8", 0.5, .5), ("map_pump", 6.0, .5)], "slow"),
 ]),
 dict(id="s3", credit="Graphics: KEPT ALIVE · Film: U.S. Army 1943 / NLM · DVIDS",
      hook="TYPHOID<br>[~1,000X DROP]", title="Why Typhoid Fell About 1,000-Fold in America",
      label="GRAPHICS: KEPT ALIVE · SOURCE: CDC\\NFILM: U.S. ARMY 1943 · KOREA 2026 TRAINING",
      lines=[
  ("In nineteen hundred, typhoid fever struck about one hundred in every hundred thousand Americans. By two thousand six, zero point one.", [("card_typh", 0.5, .5)], "punch"),
  ("The CDC credits drinking water treatment, cleaner water sources and better sanitation.", [("purif_plant", 0.5, .5), ("purif_plant", 6.6, .5)], "calm"),
  ("In nineteen oh eight, Jersey City became the first U.S. city to routinely disinfect its drinking water.", [("card_1908", 0.5, .5)], "drive"),
  ("Today, Army units still purify their own water in the field.", [("1020953", 8.5, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("eighteen fifty-four", "1854"), ("five hundred", "500"), ("seventy", "70"), ("September eighth", "September 8"), ("three numbers", "3 numbers"),
 ("More than five hundred", "More than 500"), ("ten days", "10 days"), ("two hundred fifty yards", "250 yards"), ("Sixty-one", "61"), ("Two feet eight inches", "2 feet 8 inches"),
 ("nineteen hundred", "1900"), ("one hundred in every hundred thousand", "100 in every 100,000"), ("two thousand six", "2006"), ("zero point one", "0.1"),
 ("nineteen oh eight", "1908"), ("Doctor John Snow", "Dr. John Snow"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_brew", "card_500", "card_61", "card_2ft8", "card_typh", "card_1908", "map_brew", "map_pump", "purif_plant", "1020953"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
