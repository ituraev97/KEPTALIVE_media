# Shorts for KEPT ALIVE · HOW IT WORKS 011 — Field hospitals. Three Shorts, one fact/moment each; facts as verified for the long episode.
# Templates: s1 = one moment on footage (a hospital inside a sports arena, Puerto Rico 2017)
#            s2 = countdown "in 3 numbers" (72 hours -> 32 beds -> 250 beds)
#            s3 = then -> now (MASH 1951 -> last MASH 2006 -> 32-bed field hospital module today)
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own branded cards (make_cards.py). Training footage labelled.
# No patient is named. No wounds, blood or patients on screen.
SHORTS = [
 dict(id="s1", credit="Footage: U.S. Army via DVIDS · Humacao, Puerto Rico, 2017",
      hook="HOSPITAL<br>[IN AN ARENA]", title="The Army Hospital Built Inside a Sports Arena",
      label="14TH COMBAT SUPPORT HOSPITAL · HUMACAO ARENA\\NPUERTO RICO · OCTOBER 2017 · SOURCE: DVIDS",
      lines=[
  ("This Army hospital was built inside a sports arena.", [("557923", 40.0, .5)], "punch"),
  ("After Hurricane Maria in twenty seventeen, the fourteenth Combat Support Hospital set up in the damaged Humacao Arena, in Puerto Rico.", [("557722", 5.0, .5)], "calm"),
  ("In less than a week, it had emergency care, surgery, two intensive care units and x-ray.", [("557923", 22.0, .5)], "drive"),
  ("In its first three days, it saw one hundred sixty-four patients.", [("557923", 44.0, .5)], "slow"),
 ]),
 dict(id="s2", credit="Graphics: KEPT ALIVE · Footage: U.S. Army via DVIDS",
      hook="IN 3<br>[NUMBERS]", title="An Army Hospital in 72 Hours, in 3 Numbers",
      label="GRAPHICS: KEPT ALIVE · ARMY SUSTAINMENT · ARMY.MIL\\NFILM: SEATTLE, MARCH 2020 · DVIDS",
      lines=[
  ("An Army field hospital, in three numbers.", [("card_72", 0.5, .5)], "punch"),
  ("Seventy-two. The hours it took, in a twenty seventeen Army test, to set up hospital care with surgery and intensive care at Fort Polk, Louisiana.", [("card_72", 3.0, .5)], "calm"),
  ("Thirty-two. The beds in the basic building block of today's Army field hospital.", [("card_32", 0.5, .5)], "drive"),
  ("Two hundred fifty. The beds an Army hospital center set up inside a Seattle event center in twenty twenty.", [("745000", 25.0, .5)], "slow"),
 ]),
 dict(id="s3", credit="Film: U.S. Army Signal Corps, Korea, 1951 / NARA · Graphics: KEPT ALIVE",
      hook="THE LAST<br>[MASH]", title="The Army's Last MASH Ended in 2006. Here's What Replaced It",
      label="GRAPHICS: KEPT ALIVE · BRITANNICA · ARMY.MIL\\NFILM: 8209TH MASH, KOREA, 1951 · NARA",
      lines=[
  ("The Army's last MASH unit ended in two thousand six. Here's what replaced it.", [("mash_c", 4.6, .5), ("mash_c", 16.0, .5)], "punch"),
  ("A MASH had sixty beds and, Britannica says, took fifty large trucks to move.", [("card_then", 0.5, .5)], "calm"),
  ("In two thousand six, the last one, the two hundred twelfth, became a combat support hospital with two hundred forty-eight beds.", [("card_csh", 0.5, .5)], "drive"),
  ("Today, Army field hospitals are built from thirty-two bed blocks, which the Army's plan says can grow to two hundred forty beds.", [("card_now", 0.5, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("twenty seventeen", "2017"), ("fourteenth Combat Support Hospital", "14th Combat Support Hospital"), ("one hundred sixty-four", "164"), ("first three days", "first 3 days"),
 ("three numbers", "3 numbers"), ("Seventy-two", "72"), ("Thirty-two", "32"), ("Two hundred fifty", "250"), ("twenty twenty", "2020"),
 ("two thousand six", "2006"), ("sixty beds", "60 beds"), ("fifty large trucks", "50 large trucks"), ("two hundred twelfth", "212th"),
 ("two hundred forty-eight", "248"), ("thirty-two bed", "32-bed"), ("two hundred forty", "240"), ("two intensive care units", "2 intensive care units"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_72", "card_32", "card_then", "card_csh", "card_now", "557923", "557722", "557756", "745000", "mash_c"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
