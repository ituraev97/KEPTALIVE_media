# Shorts for KEPT ALIVE · THE SAVE 102 — the submarine appendectomy, USS Seadragon, Sept. 11, 1942 (long video Wed 2026-11-18 13:00 ET).
# Templates: s1 = one object + number ("5 Spoons, No Doctor": the improvised kit and the clock)
#            s2 = then -> now contrast ("1942 TO 2005": the operation, then the medal 60+ years later; today's IDC on fresh DVIDS)
#            s3 = surprising consequence ("This … Won a Pulitzer": Weller's Chicago Daily News story, 1943 Pulitzer for Reporting)
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own branded cards (make_cards.py).
# Archival = U.S. Navy films 1945 (NPC-3844, MN-9141, NPC-15523), never Seadragon — label says so. The patient is never named.
SHORTS = [
 dict(id="s1", credit="Film: U.S. Navy 1945 (NARA) · Graphics: KEPT ALIVE",
      hook="5 SPOONS<br>[NO DOCTOR]", title="5 Spoons, No Doctor: WWII Surgery 120 Feet Underwater",
      label="ARCHIVAL FILM 1945 · U.S. NAVY · NOT SEADRAGON\\NSOURCES: NAVAL HISTORY AND HERITAGE COMMAND",
      lines=[
  ("Five tablespoons, bent back. They held the incision open in an emergency appendectomy on a U.S. submarine in World War Two.", [("card_5spoons", 0.5, .5)], "punch"),
  ("September nineteen forty-two. U.S.S. Seadragon dived to a hundred and twenty feet in enemy waters. There was no doctor aboard.", [("ss_dive", 8.0, .5), ("ss_dive", 30.0, .5)], "tense"),
  ("Pharmacist's mate Wheeler Lipes, age twenty-three, operated on the wardroom table. The ether mask was a tea strainer covered in gauze.", [("sk_ward", 60.0, .5), ("ss_crew", 48.0, .5)], "drive"),
  ("Two hours and thirty-six minutes later, the last stitch was in. Within days, the nineteen-year-old sailor was back on duty.", [("card_236", 0.5, .5)], "slow"),
 ]),
 dict(id="s2", credit="Film: U.S. Navy 1945 (NARA) · Footage: U.S. Navy via DVIDS",
      hook="1942 TO 2005<br>[THE MEDAL]", title="He Did Surgery at Sea in WWII. His Medal: 60+ Years Later",
      label="ARCHIVAL FILM 1945 · NOT SEADRAGON · SOURCES: NHHC, NPR\\NTODAY: USS COLORADO, PEARL HARBOR · SEPT 2026",
      lines=[
  ("In nineteen forty-two, he removed a shipmate's appendix a hundred and twenty feet under enemy waters. His medal for it came in two thousand five.", [("card_medal", 0.5, .5)], "punch"),
  ("Wheeler Lipes was the pharmacist's mate on the submarine Seadragon. There was no doctor aboard.", [("ss_crew", 4.0, .5), ("ss_crew", 70.0, .5)], "tense"),
  ("The squadron's medical officer wrote that surgery by anyone but qualified surgeons was by no means desirable to encourage.", [("sv_shears", 4.0, .5)], "calm"),
  ("More than sixty years later, at eighty-four, Lipes received the Navy Commendation Medal for saving a crewman's life.", [("card_medal", 9.0, .5)], "slow"),
  ("Today the Navy has a name for that job: the independent duty corpsman.", [("1024936", 134.0, .45), ("1024936", 146.0, .5)], "calm"),
 ]),
 dict(id="s3", credit="Film: U.S. Navy 1945 (NARA) · Graphics: KEPT ALIVE",
      hook="PULITZER<br>[1943]", title="The WWII Submarine Surgery Story That Won a Pulitzer",
      label="ARCHIVAL FILM 1945 · U.S. NAVY · NOT SEADRAGON\\NSOURCES: PULITZER.ORG, WELLER ARCHIVE, NHHC",
      lines=[
  ("This story won the nineteen forty-three Pulitzer Prize for Reporting: an appendix removed on a U.S. submarine, under enemy waters.", [("card_pulitzer", 0.5, .5)], "punch"),
  ("George Weller of the Chicago Daily News called it the first appendix ever known to have been removed below enemy waters.", [("sv_bow", 20.0, .5), ("sv_bow", 34.0, .5)], "drive"),
  ("The man who operated was a twenty-three-year-old pharmacist's mate. His retractors were five bent tablespoons.", [("ss_crew", 92.0, .5)], "tense"),
  ("Hollywood put the story into the nineteen forty-three film Destination Tokyo. And before the year was out, two more submarine pharmacist's mates did the same operation at sea.", [("sk_deck", 6.0, .5), ("ss_uw", 30.0, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("Five tablespoons", "5 tablespoons"), ("five bent tablespoons", "5 bent tablespoons"), ("September nineteen forty-two", "September 1942"),
 ("U.S.S. Seadragon", "USS Seadragon"), ("a hundred and twenty feet", "120 feet"), ("twenty-three-year-old", "23-year-old"), ("age twenty-three", "age 23"),
 ("Two hours and thirty-six minutes", "2 hours and 36 minutes"), ("nineteen-year-old", "19-year-old"), ("nineteen forty-three", "1943"),
 ("nineteen forty-two", "1942"), ("two thousand five", "2005"), ("More than sixty years", "More than 60 years"), ("eighty-four", "84"),
 ("World War Two", "World War II"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_5spoons", "card_236", "card_medal", "card_pulitzer", "ss_dive", "ss_crew", "ss_uw", "sk_ward", "sk_deck", "sv_shears", "sv_bow", "1024936"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
