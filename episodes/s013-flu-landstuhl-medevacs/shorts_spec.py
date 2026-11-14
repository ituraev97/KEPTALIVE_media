# KEPT ALIVE · Shorts-only day, Sunday 2026-11-15 (Format v2). Three Shorts, one fact each, fresh DVIDS footage (published Oct 2 – Nov 9, 2026).
# Templates: s1 = then -> now (1918 wrong germ -> 1945 first licensed flu vaccine -> Navy clinic, Oct 2026)
#            s2 = one shocking number (97,000+ troops, 56 countries, one hospital) + fresh LRMC drill (TRAINING)
#            s3 = count / "N in M days" (4 real Coast Guard cruise-ship medevacs in 11 days, Oct 26 – Nov 5, 2026)
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own branded cards (make_cards.py).
# No patient is named. No blood, wounds or patient faces. LRMC footage is a simulated exercise -> TRAINING label.
SHORTS = [
 dict(id="s1", credit="Graphics: KEPT ALIVE · Footage: U.S. Marine Corps via DVIDS",
      hook="1918<br>[WRONG GERM]", title="The Flu Vaccine First Tested on U.S. Troops",
      label="GRAPHICS: KEPT ALIVE · SOURCES: CDC, WHO\\NFOOTAGE: NAVY MEDICAL UNIT, IWAKUNI, JAPAN · OCT 2026",
      lines=[
  ("In nineteen eighteen, early flu vaccines were aimed at the wrong germ. Researchers thought bacteria caused the flu.", [("card_flu1918", 0.5, .5)], "punch"),
  ("In the nineteen thirties, scientists proved that influenza is caused by a virus.", [("card_flu1930", 0.5, .5)], "calm"),
  ("The U.S. Army had lost troops to flu in World War One. So it backed Thomas Francis and Jonas Salk at the University of Michigan.", [("1027903", 21.5, .5), ("1027903", 8.4, .5), ("1027903", 0.3, .55)], "drive"),
  ("Their inactivated flu vaccine was tested on the U.S. military. In nineteen forty-five, it was licensed for civilians.", [("card_flu1945", 0.5, .5)], "calm"),
  ("This October, Navy medical staff in Japan lined up for their flu shots.", [("1027903", 39.2, .5), ("1027903", 17.4, .5), ("1027903", 42.9, .5)], "slow"),
 ]),
 dict(id="s2", credit="Graphics: KEPT ALIVE · Footage: U.S. Air Force via DVIDS",
      hook="97,000+<br>[TROOPS]", title="One Hospital Treated 97,000+ Troops From 56 Countries",
      label="GRAPHICS: KEPT ALIVE · SOURCE: U.S. ARMY\\NFOOTAGE: LANDSTUHL, GERMANY · OCT 2026 · TRAINING",
      lines=[
  ("More than ninety-seven thousand wounded, injured and ill troops. One hospital in Germany treated them.", [("card_97k", 0.5, .5)], "punch"),
  ("Landstuhl Regional Medical Center. The Army calls it the largest American medical facility outside the United States.", [("1028444", 9.6, .5), ("1028444", 13.3, .45), ("1028444", 35.3, .5)], "calm"),
  ("U.S. and coalition troops from fifty-six countries, evacuated from Europe, Africa and the Middle East.", [("card_56", 0.5, .5)], "drive"),
  ("The Army reports a ninety-nine percent survival rate.", [("card_99", 0.5, .5)], "slow"),
  ("Its staff still drill for the worst day. This October: a simulated mass casualty decontamination.", [("1028444", 26.3, .5), ("1028444", 31.1, .5)], "calm"),
 ]),
 dict(id="s3", credit="Footage: U.S. Coast Guard via DVIDS · Graphics: KEPT ALIVE",
      hook="4 CRUISE SHIPS<br>[11 DAYS]", title="4 Cruise Ships, 11 Days: Real Coast Guard Medevacs",
      label="REAL MEDEVACS · U.S. COAST GUARD VIDEO\\NOCT 26 – NOV 5, 2026 · GRAPHICS: KEPT ALIVE",
      lines=[
  ("Four cruise ships in eleven days. Four times, a Coast Guard helicopter crew was sent to lift a patient off at sea.", [("1027649", 0.08, .15)], "punch"),
  ("October twenty-sixth: a passenger from the Star Pride, about one hundred fifty nautical miles north of Puerto Rico.", [("1027649", 9.0, .2), ("1027649", 36.0, .45)], "drive"),
  ("November second, off North Carolina: a passenger and an onboard nurse, hoisted from the Norwegian Bliss.", [("card_4ships", 0.5, .5)], "calm"),
  ("November fourth: a man with a head injury, about seventy-six miles off Charleston.", [("1029322", 3.2, .5)], "drive"),
  ("November fifth: a woman, hoisted from a cruise ship nearly twelve hundred feet long.", [("1028920", 30.5, .5), ("1028920", 52.4, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("nineteen eighteen", "1918"), ("nineteen thirties", "1930s"), ("World War One", "World War I"), ("nineteen forty-five", "1945"),
 ("ninety-seven thousand", "97,000"), ("fifty-six", "56"), ("ninety-nine percent", "99%"),
 ("Four cruise ships", "4 cruise ships"), ("eleven days", "11 days"), ("Four times", "4 times"),
 ("October twenty-sixth", "October 26"), ("one hundred fifty", "150"), ("November second", "November 2"),
 ("November fourth", "November 4"), ("seventy-six", "76"), ("November fifth", "November 5"), ("twelve hundred", "1,200"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_56", "card_flu1930", "card_flu1918", "card_flu1945", "card_97k", "card_99", "card_4ships", "1027903"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
