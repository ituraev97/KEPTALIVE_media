# KEPT ALIVE · long day Monday 2026-11-23 — 3 Shorts from WAR MEDICINE · EP 2 (104, "What Being Wounded in the Civil War Actually Felt Like").
# Templates: s1 = fraction hook (71 of 2,818 pyemia cases recovered) -> no germ theory -> Lister 1867 -> today
#            s2 = contrast hook (922 blade wounds vs 245,790 gunshot) -> Minié ball -> today's medevac
#            s3 = head-to-head numbers (44,558 dysentery deaths vs 44,238 killed in battle) -> camp diseases
# shot: (clip_id, start, cx). card_*/st_* = 20 s push-ins rendered by make_cards.py (stills: Miller, Photographic History of the
# Civil War 1911, public domain via Internet Archive). No blood, wounds, bodies or patient faces.
# Fresh DVIDS: 1028647 USS Nimitz TCCC Tier II training, Atlantic, Nov 4 2026 (pub. Nov 20) · 1030252 Oregon Guard HH-60M medevac
#              flyover, Eugene, Nov 14 2026 (pub. Nov 18; real event, not training).
SHORTS = [
 dict(id="s1", credit="Photos: Miller 1911 (PD) · Footage: U.S. Navy via DVIDS (TRAINING)",
      hook="71 OF 2,818<br>[RECOVERED]", title="Blood Poisoning After Civil War Wounds: 71 of 2,818 Lived",
      label="SOURCES: MEDICAL & SURGICAL HISTORY (1883) · KEEN\\NTRAINING: USS NIMITZ, NOV 2026",
      lines=[
  ("Seventy-one. Of two thousand eight hundred eighteen soldiers in Union Army records with pyemia after gunshot wounds, only seventy-one recovered.", [("card_71of", 0.5, .5)], "punch"),
  ("Pyemia was what doctors then called blood poisoning.", [("st_ward", 0.5, .5)], "calm"),
  ("Surgeons knew nothing of germs. One recalled operating in old blood-stained coats.", [("card_coats", 0.5, .5)], "tense"),
  ("Sponges were reused, washed only in tap water.", [("card_sponges", 0.5, .5)], "drive"),
  ("The Army's history: in established cases, all remedies were found ineffective.", [("card_remedies", 0.5, .5)], "slow"),
  ("Joseph Lister's antiseptic method came in eighteen sixty-seven.", [("card_1867", 0.5, .5)], "calm"),
  ("Today, sailors train in casualty care, like here aboard USS Nimitz.", [("1028647", 15.6, .62), ("1028647", 19.0, .5)], "calm"),
 ]),
 dict(id="s2", credit="Photos: Miller 1911 (PD) · Footage: Oregon Army National Guard via DVIDS",
      hook="922 VS. 245,790<br>[BLADES VS. GUNSHOT]", title="Sabres and Bayonets: 922 Recorded Wounds. Gunshot: 245,790",
      label="SOURCES: MEDICAL & SURGICAL HISTORY (1883) · CIVIL WAR MONITOR\\NMEDEVAC FLYOVER: EUGENE, ORE., NOV 2026",
      lines=[
  ("Nine hundred twenty-two. That is how many sabre and bayonet wounds Union surgeons recorded in the Civil War.", [("card_922", 0.5, .5)], "punch"),
  ("Gunshot wounds: two hundred forty-five thousand seven hundred ninety.", [("card_245790", 0.5, .5)], "drive"),
  ("The standard infantry bullet was the Minié ball: soft lead, just over an ounce, with a hollow base that gripped the rifling.", [("card_hollow", 0.5, .5)], "calm"),
  ("One modern estimate credits it with about three in four battlefield injuries.", [("card_76", 0.5, .5)], "tense"),
  ("Swords and bayonets were the weapons of old paintings. The rifle did the damage.", [("st_knaps", 0.5, .5)], "slow"),
  ("Today, units like this Oregon Guard medevac company fly the wounded by helicopter.", [("1030252", 24.8, .5), ("1030252", 38.0, .5)], "calm"),
 ]),
 dict(id="s3", credit="Photos: Photographic History of the Civil War, 1911 · KEPT ALIVE",
      hook="44,558<br>[DIARRHEA & DYSENTERY]", title="44,558 Union Soldiers Died of Diarrhea and Dysentery",
      label="SOURCES: MEDICAL & SURGICAL HISTORY OF THE WAR (1870, 1879)\\NPHOTOS 1861-64 VIA PHOTOGRAPHIC HISTORY (1911)",
      lines=[
  ("Forty-four thousand five hundred fifty-eight. Union soldiers the Army recorded as dead of diarrhea and dysentery.", [("card_44558", 0.5, .5)], "punch"),
  ("Killed in battle, in the Army's own records: at least forty-four thousand two hundred thirty-eight. Another forty-nine thousand died of wounds and injuries.", [("card_44238", 0.5, .5)], "tense"),
  ("Recorded cases ran well over a million.", [("card_million", 0.5, .5)], "calm"),
  ("The camp fevers, typhoid and others grouped with it, killed more than forty thousand more.", [("card_fevers", 0.5, .5)], "drive"),
  ("Men lived packed together in big army camps like this one in Kentucky.", [("st_recruits", 0.5, .5)], "calm"),
  ("The surgeons fought the wounds. The camps fought germs nobody yet understood.", [("st_eastwards", 0.5, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("Seventy-one", "71"), ("two thousand eight hundred eighteen", "2,818"), ("seventy-one", "71"),
 ("in eighteen sixty-seven", "in 1867"), ("Nine hundred twenty-two", "922"),
 ("two hundred forty-five thousand seven hundred ninety", "245,790"), ("Minié ball", "Minié ball"),
 ("Forty-four thousand five hundred fifty-eight", "44,558"), ("forty-four thousand two hundred thirty-eight", "44,238"),
 ("more than forty thousand", "more than 40,000"), ("forty-nine thousand", "49,000"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["1028647", "1030252", "card_71of", "card_coats", "card_sponges", "card_remedies", "card_1867", "st_ward",
        "card_922", "card_245790", "card_hollow", "card_76", "st_knaps",
        "card_44558", "card_44238", "card_million", "card_fevers", "st_recruits", "st_eastwards"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
