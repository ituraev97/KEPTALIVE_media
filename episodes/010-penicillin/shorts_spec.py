# Shorts for KEPT ALIVE · FIRST 010 — Penicillin. Three Shorts, one fact/moment each; facts as verified for the long episode.
# Templates: s1 = one moment on footage (the cantaloupe mold) · s2 = before -> after ($20 -> 55 cents) · s3 = countdown "in 3 numbers" (12 -> 2,000 -> 2.3 million).
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own branded cards (make_cards.py). 1944 newsreel footage is labelled as such.
# No patient is named. No wounds, blood or patients on screen.
SHORTS = [
 dict(id="s1", credit="1944 newsreels: United News / National Archives · Graphics: KEPT ALIVE",
      hook="MOLDY<br>[CANTALOUPE]", title="The Moldy Cantaloupe Behind Mass-Produced Penicillin",
      label="GRAPHICS: KEPT ALIVE · SOURCE: USDA ARS\\NFILM: 1944 NEWSREEL · LOCATION NOT IDENTIFIED",
      lines=[
  ("The penicillin that went to war owes a lot to one moldy cantaloupe.", [("pen_lab", 16.4, .5)], "punch"),
  ("At a U.S. government lab in Peoria, Illinois, workers collected molds from produce markets, looking for a better penicillin maker.", [("card_hunt", 0.5, .5)], "calm"),
  ("The winner came from a moldy cantaloupe found at a Peoria market.", [("card_cantaloupe", 0.5, .5)], "drive"),
  ("Its strain became the parent of all the strains used commercially. Who actually found it is still uncertain.", [("card_cantaloupe", 6.0, .5)], "slow"),
 ]),
 dict(id="s2", credit="Graphics: KEPT ALIVE · 1944 newsreels: United News / NARA",
      hook="$20<br>[A DOSE]", title="Penicillin Cost $20 a Dose in 1943. 3 Years Later, 55¢",
      label="GRAPHICS: KEPT ALIVE · SOURCE: USDA ARS\\NFILM: 1944 NEWSREEL · PLANT NOT IDENTIFIED",
      lines=[
  ("In July nineteen forty-three, one dose of penicillin cost twenty dollars.", [("card_20", 0.5, .5)], "punch"),
  ("Back in nineteen forty-one, U.S. scientists in Peoria had learned to grow the mold in deep vats of corn steep liquor, with air pumped in.", [("card_vats", 0.5, .5)], "calm"),
  ("Twenty-one American companies joined in. Ahead of D-Day, they had produced two point three million doses.", [("pen_plant", 20.5, .5)], "drive"),
  ("Three years after that twenty-dollar price, a dose cost fifty-five cents.", [("card_055", 0.5, .5)], "slow"),
 ]),
 dict(id="s3", credit="Graphics: KEPT ALIVE · Film: U.S. Coast Guard, 1944 / NARA",
      hook="IN 3<br>[NUMBERS]", title="Penicillin's Race to D-Day, in 3 Numbers",
      label="GRAPHICS: KEPT ALIVE · WWII MUSEUM · PBS\\NFILM: TROOPS EMBARK · ENGLAND, 1944 · NARA",
      lines=[
  ("Penicillin's race to D-Day, in three numbers.", [("card_12", 0.5, .5)], "punch"),
  ("Twelve. The years Alexander Fleming kept his mold growing, after he found it on a dish in nineteen twenty-eight.", [("card_12", 3.0, .5)], "calm"),
  ("Two thousand. The liters of mold fluid it took to make enough penicillin for one human case, in Oxford.", [("card_2000", 0.5, .5)], "drive"),
  ("Two point three million. The doses American companies had produced ahead of D-Day.", [("emb_harbor", 13.0, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("nineteen forty-three", "1943"), ("nineteen forty-one", "1941"), ("nineteen twenty-eight", "1928"), ("twenty dollars", "$20"), ("twenty-dollar", "$20"), ("fifty-five cents", "55 cents"),
 ("Twenty-one", "21"), ("two point three million", "2.3 million"), ("Two point three million", "2.3 million"), ("Two thousand", "2,000"), ("Twelve", "12"),
 ("three numbers", "3 numbers"), ("Three years", "3 years"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_hunt", "card_vats", "card_cantaloupe", "card_20", "card_055", "card_12", "card_2000", "pen_lab", "pen_plant", "emb_harbor"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
