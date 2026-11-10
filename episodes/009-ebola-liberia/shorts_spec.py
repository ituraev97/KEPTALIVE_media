# Shorts for KEPT ALIVE · THE SAVE 009 — Stopping Ebola in Liberia. Three Shorts, one fact/moment each; facts as verified for the long episode.
# Templates: s1 = before -> after (a week -> hours) · s2 = one moment on footage (Monrovia Medical Unit) · s3 = countdown (No. 3 -> No. 1).
# shot: (clip_id, start, cx). card_* = 12 s push-ins of our own branded cards (make_cards.py). No patients, no bodies on screen.
SHORTS = [
 dict(id="s1", credit="Footage: U.S. Army via DVIDS · Graphics: KEPT ALIVE",
      hook="A WEEK<br>[TO HOURS]", title="Ebola Tests Took Up to a Week. Then Mobile Labs Arrived",
      label="MOBILE EBOLA LABS · LIBERIA · 2014–2015\\NFOOTAGE: U.S. ARMY 1ST AREA MEDICAL LAB, FEB. 2015",
      lines=[
  ("In Liberia in twenty fourteen, confirming a case of Ebola could take as long as a week.", [("card_week", 0.5, .5)], "punch"),
  ("Then U.S. military mobile labs arrived.", [("391346", 61.7, .5)], "drive"),
  ("The Navy's labs cut the wait for a result from seven days to less than four hours.", [("card_hours", 0.5, .5)], "punch"),
  ("Army labs, like this one, joined them. By March twenty fifteen, the Navy labs alone had tested more than five thousand three hundred samples.", [("391346", 69.95, .5)], "slow"),
 ]),
 dict(id="s2", credit="Footage: 101st Airborne Division via DVIDS",
      hook="BUILT FOR<br>[HEALERS]", title="In 2014, Africa's Only Ebola Unit Just for Health Workers",
      label="MONROVIA MEDICAL UNIT · LIBERIA\\NNOV. 4, 2014 · BEFORE OPENING",
      lines=[
  ("In twenty fourteen, this was the only Ebola treatment unit in Africa dedicated to health care workers.", [("372199", 16.5, .5)], "punch"),
  ("The Monrovia Medical Unit, Liberia, twenty fourteen. Twenty-five beds, built by Navy Seabees, soldiers and airmen.", [("372199", 276.5, .5)], "calm"),
  ("It was run by the U.S. Public Health Service, in four rotations of seventy people.", [("372199", 125.2, .5)], "calm"),
  ("Over the whole epidemic in Liberia, three hundred seventy-eight health workers were infected with Ebola.", [("card_hcw", 0.5, .5)], "slow"),
 ]),
 dict(id="s3", credit="KEPT ALIVE graphics · Sources: CDC, Emerging Infectious Diseases",
      hook="1.4 MILLION<br>[CASES?]", title="CDC Warned of 1.4 Million Ebola Cases. Here's What Changed",
      label="CDC MODEL · SEPTEMBER 2014\\NLIBERIA + SIERRA LEONE · AN ESTIMATE",
      lines=[
  ("In twenty fourteen, a CDC model estimated that, without more action, Liberia and Sierra Leone could reach one point four million Ebola cases by January.", [("card_14m", 0.5, .5)], "punch"),
  ("Things changed in Liberia. One: burial teams. Fewer than ten in August, fifty-four by October.", [("card_burial", 0.5, .5)], "drive"),
  ("Two: contact tracing, mostly on paper and Excel spreadsheets.", [("card_paper", 0.5, .5)], "drive"),
  ("Three: isolation. A CDC model estimates it prevented about nine thousand cases in Liberia, in about five weeks.", [("card_iso", 0.5, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("twenty fourteen", "2014"), ("twenty fifteen", "2015"), ("seven days", "7 days"), ("four hours", "4 hours"), ("five thousand three hundred", "5,300"),
 ("Twenty-five beds", "25 beds"), ("four rotations of seventy people", "4 rotations of 70 people"), ("three hundred seventy-eight", "378"),
 ("one point four million", "1.4 million"), ("Fewer than ten", "Fewer than 10"), ("fifty-four", "54"), ("about nine thousand", "about 9,000"), ("five weeks", "5 weeks"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["391346", "372199", "card_week", "card_hours", "card_hcw", "card_14m", "card_burial", "card_paper", "card_iso"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
