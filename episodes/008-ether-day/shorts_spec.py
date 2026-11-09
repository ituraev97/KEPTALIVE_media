# Shorts for KEPT ALIVE · FIRST 008 — Ether Day. Three Shorts, one fact/moment each; facts as verified for the long episode.
# Templates: s1 = before -> after ("Before X, doctors did Y") · s2 = countdown (3 claimants, 1842 -> 1844 -> 1846) · s3 = one shocking fact / myth vs. record.
# shot: (clip_id, start, cx). *_kb = 12 s push-in renders of public-domain stills (see episode.py) or of our own branded cards (card_*).
# No modern footage is used for historical claims. No patient is named.
SHORTS = [
 dict(id="s1", credit="Illustrations: \"Semi-Centennial of Anaesthesia\" (MGH, 1897)",
      hook="BEFORE<br>[1846]", title="Before 1846, a Surgeon's Best Painkiller Was Speed",
      label="ILLUSTRATIONS · \"THE SEMI-CENTENNIAL OF ANAESTHESIA\"\\NMASSACHUSETTS GENERAL HOSPITAL · PUBLISHED 1897",
      lines=[
  ("Before eighteen forty-six, surgery was done on patients who were wide awake.", [("card_speed", 0.5, .5)], "punch"),
  ("Alcohol and opium dulled the senses, but not reliably. So surgeons worked as fast as they could.", [("card_speed", 5.0, .5)], "calm"),
  ("Then, on October sixteenth, eighteen forty-six, in Boston, a patient breathed ether, fell asleep, and had a growth removed from his neck.", [("keller_kb", 0.5, .5), ("mgh_kb", 1.0, .5)], "drive"),
  ("He said it felt like a scraping. But it didn't hurt. The surgeon reportedly said: Gentlemen, this is no humbug.", [("keller_kb", 6.0, .5), ("warren_kb", 1.0, .5)], "slow"),
 ]),
 dict(id="s2", credit="Wells 1847 (NLM copy) · Morton 1853 (LoC copy) · Internet Archive",
      hook="WHO WAS<br>[FIRST?]", title="Before Morton, 2 Men Tried Anesthesia First",
      label="TITLE PAGES · HORACE WELLS, HARTFORD, 1847\\NW. T. G. MORTON'S CLAIM TO THE U.S. SENATE, 1853",
      lines=[
  ("Four men claimed credit for anesthesia. Here are three of them.", [("morton_kb", 0.5, .5)], "punch"),
  ("Number three. Crawford Long, in Georgia, eighteen forty-two. He used ether, but didn't publish until eighteen forty-nine.", [("card_long1842", 0.5, .5)], "calm"),
  ("Number two. Horace Wells, a Hartford dentist, eighteen forty-four. Laughing gas. His Boston demonstration was judged a humbug.", [("wells_kb", 0.5, .5)], "drive"),
  ("Number one. William Morton. Ether, in public, in Boston, eighteen forty-six. Congress never passed a reward. The fight was never clearly settled.", [("keller_kb", 1.0, .5), ("morton_kb", 5.0, .5)], "slow"),
 ]),
 dict(id="s3", credit="KEPT ALIVE graphics · Source: National Museum of Civil War Medicine",
      hook="BITE THE<br>[BULLET?]", title="How Brutal Was Civil War Surgery, Really?",
      label="GRAPHICS · UNION ARMY RECORDS, 1861–1865\\NILLUSTRATION · BOSTON 1846 · PUBLISHED 1897",
      lines=[
  ("Did Civil War soldiers really bite a bullet during surgery?", [("card_bullet", 0.5, .5)], "punch"),
  ("The Union army's own medical records say no.", [("card_bullet", 4.5, .5)], "calm"),
  ("At least eighty thousand operations were done with anesthesia. Only two hundred fifty-four were recorded without it.", [("card_civil80k", 0.5, .5)], "drive"),
  ("Mostly chloroform. Sometimes ether. Just fifteen years after the first public demonstration in Boston.", [("keller_kb", 2.0, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("eighteen forty-six", "1846"), ("October sixteenth", "October 16"), ("eighteen forty-two", "1842"), ("eighteen forty-nine", "1849"),
 ("eighteen forty-four", "1844"), ("eighty thousand", "80,000"), ("two hundred fifty-four", "254"), ("fifteen years", "15 years"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_speed", "card_long1842", "card_bullet", "card_civil80k", "keller_kb", "mgh_kb", "warren_kb", "morton_kb", "wells_kb"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
