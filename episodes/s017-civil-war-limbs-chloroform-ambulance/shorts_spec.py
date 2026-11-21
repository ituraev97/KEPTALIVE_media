# KEPT ALIVE · Shorts-only day, Sunday 2026-11-22 — Civil War week (teasers for WAR MEDICINE · EP 2, Mon 2026-11-23).
# Templates: s1 = percentage hook -> consequence (71% of wounds hit limbs -> 29,980 amputations -> mortality by site)
#            s2 = myth-bust with a number ("bite the bullet" vs 80,000 anaesthetic cases, 254 without)
#            s3 = "lay unattended" -> invention (Second Bull Run 1862 -> Letterman's ambulance corps -> Antietam -> 1864 Act)
# shot: (clip_id, start, cx). card_*/st_* = 20 s push-ins rendered by make_stills.py (stills: Miller, Photographic History of the
# Civil War 1911, vols. 2 and 7, public domain via Internet Archive). No blood, wounds, stumps, bodies or patient faces.
# Fresh DVIDS (TRAINING): 1030224 USARPAC Best Medic, South Korea, Nov 17 2026 · 1030574 Madigan simulation center, Nov 20 2026 ·
#                         1030600 WBAMC / El Paso airport full-scale exercise, Oct 29 2026 (published Nov 20 2026).
SHORTS = [
 dict(id="s1", credit="Photos: Miller 1911 (PD) · Footage: U.S. Army via DVIDS (TRAINING)",
      hook="71%<br>[HIT ARMS OR LEGS]", title="Why Civil War Surgeons Amputated: 71% of Wounds Hit Limbs",
      label="SOURCES: MEDICAL & SURGICAL HISTORY OF THE WAR (1883)\\NTRAINING: ARMY BEST MEDIC, SOUTH KOREA, NOV 2026",
      lines=[
  ("Seventy-one percent of treated Union gunshot wounds in the Civil War hit an arm or a leg.", [("card_71", 0.5, .5)], "punch"),
  ("The usual bullet was the soft lead Minié ball, point five eight caliber.", [("card_minie", 0.5, .5)], "calm"),
  ("It splintered bone and drove dirt and cloth into the wound.", [("st_surgeons", 0.5, .45)], "tense"),
  ("With no antibiotics, amputation often gave the best chance of survival.", [("card_why", 0.5, .5)], "slow"),
  ("The Union army recorded twenty-nine thousand nine hundred eighty amputations. About one in four died.", [("card_29980", 0.5, .5)], "drive"),
  ("The closer to the body, the deadlier: hand and fingers, three percent. The hip, eighty-three.", [("card_site", 0.5, .5)], "calm"),
  ("Today, Army medics train for hours of care far from a hospital, like here in South Korea.", [("1030224", 18.6, .5), ("1030224", 22.6, .5)], "calm"),
 ]),
 dict(id="s2", credit="Photos: Miller 1911 (PD) · Footage: U.S. Army via DVIDS (TRAINING)",
      hook="80,000<br>[NOT BITING A BULLET]", title="Civil War Soldiers Didn't 'Bite the Bullet' for Surgery",
      label="SOURCES: MEDICAL & SURGICAL HISTORY (1883) · MIL MED 2014\\NTRAINING: MADIGAN SIMULATION CENTER, NOV 2026",
      lines=[
  ("Eighty thousand. The Army's own low-end estimate of Union cases with anesthesia in the Civil War.", [("card_80000", 0.5, .5)], "punch"),
  ("Only two hundred fifty-four records say none was given.", [("card_254", 0.5, .5)], "calm"),
  ("Where the drug was recorded, about three in four got chloroform.", [("card_chloro", 0.5, .5)], "calm"),
  ("A wartime manual: a folded cloth cone.", [("card_cone", 0.5, .5)], "slow"),
  ("Field surgeons liked it: fast, and a little was enough.", [("st_irwine", 0.5, .5)], "drive"),
  ("A twenty fourteen Military Medicine article says this should put to rest the stories of soldiers biting on bullets.", [("card_myth", 0.5, .5)], "calm"),
  ("Today, Army teams rehearse with manikins and role-players, like here in Washington State.", [("1030574", 193.0, .5), ("1030574", 232.5, .55)], "calm"),
 ]),
 dict(id="s3", credit="Photos: Miller 1911 (PD) · Footage: U.S. Army via DVIDS (TRAINING)",
      hook="24+ HOURS<br>[LEFT ON THE GROUND]", title="Left 24+ Hours on the Field: Why Ambulance Corps Mattered",
      label="SOURCES: LETTERMAN 1866 · GILLETT (U.S. ARMY CMH) · 13 STAT. 20\\NTRAINING: EL PASO EXERCISE, OCT 2026",
      lines=[
  ("Twenty-four hours and more. After Second Bull Run in eighteen sixty-two, wounded Union soldiers lay unattended.", [("card_24h", 0.5, .5)], "punch"),
  ("Official records concede a few hired drivers ran away. A few got drunk.", [("card_drivers", 0.5, .5)], "tense"),
  ("Weeks earlier, Jonathan Letterman had designed a trained ambulance corps for the Army of the Potomac.", [("st_letterman", 0.5, .38)], "calm"),
  ("Then came Antietam, America's bloodiest day, with the system only partly ready.", [("st_bridge", 0.5, .5)], "drive"),
  ("Letterman wrote his wounded on the right were in by the next afternoon.", [("st_smith", 0.5, .5)], "calm"),
  ("In eighteen sixty-four, it became law for every Union army.", [("card_1864", 0.5, .5)], "slow"),
  ("Today, Army hospitals still drill it, like here in El Paso.", [("1030600", 27.6, .55), ("1030600", 32.9, .5)], "calm"),
 ]),
]

DISPLAY = [
 ("Seventy-one percent", "71%"), ("point five eight caliber", ".58 caliber"), ("Minié ball", "Minié ball"),
 ("twenty-nine thousand nine hundred eighty", "29,980"), ("three percent", "3%"), ("eighty-three", "83%"),
 ("Eighty thousand", "80,000"), ("two hundred fifty-four", "254"), ("A twenty fourteen Military Medicine article", "A 2014 Military Medicine article"), ("on August second", "on August 2"),
 ("Twenty-four hours", "24 hours"), ("in eighteen sixty-two", "in 1862"), ("In eighteen sixty-four", "In 1864"),
 ("eight thousand three hundred fifty", "8,350"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["1030224", "1030574", "1030600", "card_71", "card_minie", "st_surgeons", "card_why", "card_29980", "card_site",
        "card_80000", "card_254", "card_chloro", "card_cone", "st_irwine", "card_myth",
        "card_24h", "card_drivers", "st_letterman", "st_bridge", "st_smith", "card_1864"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
