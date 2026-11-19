# KEPT ALIVE · Shorts-only day, Friday 2026-11-20 (Format v2/v3 Shorts rules). One war-medicine fact each, winner subjects (medic hero, army disease, smallpox).
# Templates: s1 = hero medic + time number (30 hours, D-Day 1944) — DHA archival-image video 1010687 (cropped clear of its burned-in text) + own cards
#            s2 = ratio contrast (disease 2 : 1 battle wounds, Civil War) — 1861-65 photographs via The Photographic History of the Civil War vol. 7 (1911) + own cards
#            s3 = year + decision (1777 smallpox inoculation, Continental Army) — Gilbert Stuart 1796 portrait + own cards + fresh DVIDS USMC flu SHOTEX (Oct 2026)
# shot: (clip_id, start, cx). card_*/st_* = 20 s push-ins rendered by make_stills.py. No patient is named or shown; no blood, wounds or patient faces.
SHORTS = [
 dict(id="s1", credit="Images: Defense Health Agency via DVIDS · Graphics: KEPT ALIVE",
      hook="30 HOURS<br>[WOUNDED MEDIC]", title="A Wounded D-Day Army Medic Treated Men for 30 Hours",
      label="SOURCES: ARMY.MIL · HEALTH.MIL (2024)\\NARCHIVAL IMAGES: DEFENSE HEALTH AGENCY, 2026",
      lines=[
  ("Thirty hours. On D-Day, a wounded Army medic kept treating soldiers on Omaha Beach for thirty hours under fire.", [("1010687", 24.0, .85), ("1010687", 35.1, .0)], "punch"),
  ("Corporal Waverly Woodson was twenty-one. His landing craft hit a mine, lost power, and drifted to shore.", [("1010687", 3.1, .85), ("1010687", 27.4, .85)], "drive"),
  ("Mortar shrapnel tore into his back. He kept working anyway.", [("card_shrapnel", 0.5, .5)], "slow"),
  ("A historical commission that reviewed his record later wrote that he cared for more than two hundred casualties.", [("card_200", 0.5, .5)], "calm"),
  ("He gave artificial respiration to three men who had gone under the water.", [("1010687", 49.1, 1.0), ("1010687", 38.5, .0)], "calm"),
  ("Almost eighty years later, in June twenty twenty-four, the Army posthumously awarded him the Distinguished Service Cross.", [("card_dsc", 0.5, .5)], "slow"),
 ]),
 dict(id="s2", credit="Photos: Photographic History of the Civil War, 1911 · KEPT ALIVE",
      hook="2 TO 1<br>[DISEASE]", title="Civil War: Disease Killed Twice as Many Soldiers as Battle",
      label="SOURCES: NPS · AMERICAN BATTLEFIELD TRUST\\NPHOTOS 1861-65 VIA PHOTOGRAPHIC HISTORY (1911)",
      lines=[
  ("Twice as many. In the Civil War, disease killed twice as many soldiers as battle wounds did.", [("card_2x", 0.5, .5), ("st_fieldhosp", 0.5, .45)], "punch"),
  ("Of an estimated six hundred twenty thousand soldiers who died, about two in three were killed by disease and infection, not injuries.", [("card_620", 0.5, .5), ("st_genhosp", 0.5, .4)], "calm"),
  ("Dysentery, typhoid, measles and smallpox spread through crowded, unsanitary camps.", [("st_nelson", 0.5, .5), ("st_eastwards", 0.5, .3)], "drive"),
  ("One Confederate officer was amazed at how many country boys had never had the measles.", [("card_measles", 0.5, .5)], "calm"),
  ("And doctors had only limited knowledge of germs.", [("st_fairoaks", 0.5, .62)], "slow"),
 ]),
 dict(id="s3", credit="Footage: U.S. Marine Corps via DVIDS · Portrait: G. Stuart, 1796",
      hook="1777<br>[SMALLPOX]", title="Washington Secretly Had His Army Inoculated for Smallpox",
      label="SOURCES: NPS · AMERICAN BATTLEFIELD TRUST\\NPORTRAIT 1796 · FLU SHOTS: IWAKUNI, OCT 2026",
      lines=[
  ("In seventeen seventy-seven, George Washington ordered his troops given smallpox. On purpose.", [("st_gw", 0.5, .5)], "punch"),
  ("Smallpox had already ravaged the American army that invaded Canada.", [("card_canada", 0.5, .5)], "calm"),
  ("In February he wrote that if it spread in the army, they would have more to dread from it than from the sword of the enemy.", [("card_quote", 0.5, .5)], "slow"),
  ("Inoculation put smallpox into a small cut. It was risky, but usually milder, and left immunity.", [("card_inoc", 0.5, .5)], "calm"),
  ("It was done in secret. By late seventeen seventy-seven, smallpox in the army was substantially reduced.", [("st_gw2", 0.5, .5), ("card_late", 0.5, .5)], "drive"),
  ("Troops still line up for shots, like these at a Marine base in Japan this October.", [("1027887", 4.5, .5), ("1027887", 38.5, .42)], "calm"),
 ]),
]

DISPLAY = [
 ("Thirty hours", "30 hours"), ("thirty hours", "30 hours"), ("twenty-one", "21"), ("more than two hundred", "more than 200"),
 ("in June twenty twenty-four", "in June 2024"), ("Almost eighty years", "Almost 80 years"),
 ("six hundred twenty thousand", "620,000"), ("two in three", "2 in 3"),
 ("In seventeen seventy-seven", "In 1777"), ("late seventeen seventy-seven", "late 1777"), ("February sixth", "February 6"), ("in seventeen seventy-five and seventy-six", "in 1775-76"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["1010687", "1027887", "card_shrapnel", "card_200", "card_dsc", "card_2x", "card_620", "card_measles", "card_canada", "card_quote", "card_inoc", "card_late",
        "st_fieldhosp", "st_genhosp", "st_nelson", "st_eastwards", "st_fairoaks", "st_gw", "st_gw2"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
