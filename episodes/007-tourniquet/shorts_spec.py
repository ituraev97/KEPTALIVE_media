# Shorts for KEPT ALIVE · HOW IT WORKS 007 — The Tourniquet. Three Shorts, one fact/moment each; facts as verified for the long episode.
# Templates: s1 = one shocking fact (quote) · s2 = then vs. now (1883 vs. today) · s3 = one number (87% vs 0%).
# shot: (clip_id, start, cx) — cx = horizontal centre of the 9:16 crop (0..1). label = persistent HUD line describing ALL footage in that Short.
# All DVIDS footage is TRAINING (said in every label). esmarch_fig_kb = slow push-in on Esmarch 1883, Figs. 10-11 (NLM copy, public domain).
SHORTS = [
 dict(id="s1", credit="Training: USMC, U.S. Army, U.S. Air Force via DVIDS · Film: NARA",
      hook="\"THE EVIL<br>[ONE]\"", title="The Lifesaver a WWI Surgeon Called \"the Evil One\"",
      label="TRAINING · MARINES, AFGHANISTAN 2011 · FT. JACKSON\\NTRAINING · GILA BEND · ARMY FILM NARA 111-M-489",
      lines=[
  ("In nineteen sixteen, a British army surgeon wrote that tourniquets might be an invention of the Evil One.", [(111605, 121.6, .5)], "punch"),
  ("For decades, military doctors blamed them for lost limbs, and taught them only as a last resort.", [("arm_field", 6.2, .5)], "calm"),
  ("Then, in two thousand six, Army researchers in Baghdad counted. Of casualties who needed a tourniquet and got one, eighty-seven percent survived. Of the five who didn't get one, none did.", [(888808, 140.0, .5), (888808, 186.0, .5)], "drive"),
  ("Today, it's standard gear for American troops.", [(886668, 172.0, .5)], "slow"),
 ]),
 dict(id="s2", credit="Esmarch 1883 (NLM copy) · Training footage: USMC, U.S. Army via DVIDS",
      hook="1883 VS<br>[NOW]", title="A Stick and a Handkerchief: The Tourniquet in 1883 vs. Now",
      label="ESMARCH · \"EARLY AID IN INJURIES\" · 1883\\NTRAINING · MARINES, AFGHANISTAN 2011 · FT. JACKSON",
      lines=[
  ("In eighteen eighty-three, a famous first aid book showed this improvised tourniquet.", [("esmarch_fig_kb", 0.5, .62)], "punch"),
  ("A handkerchief around the limb, and a short stick under it. Even a sword in its sheath. The stick was twisted, round and round.", [("esmarch_fig_kb", 5.0, .62)], "calm"),
  ("Today, the stick is built in. It's called the windlass, and it locks in place.", [(111605, 172.0, .5)], "drive"),
  ("In two thousand five, the Army began issuing troops in Iraq and Afghanistan a tourniquet built for one hand.", [(888808, 141.0, .5)], "slow"),
 ]),
 dict(id="s3", credit="Training footage: U.S. Air Force / AFN, U.S. Army via DVIDS",
      hook="87% VS<br>[0%]", title="87% vs. 0%: What a 2006 Army Study Found About Tourniquets",
      label="TRAINING · CHIÈVRES AB, BELGIUM 2026 · GILA BEND\\NTRAINING · FORT JACKSON, S.C. · TYNDALL AFB, FLA.",
      lines=[
  ("Eighty-seven percent, versus zero.", [(1000551, 101.0, .5)], "punch"),
  ("In two thousand six, Army researchers followed casualties with major limb injuries, at a combat hospital in Baghdad.", [(888808, 1.0, .5)], "calm"),
  ("Of those who needed a tourniquet and got one, eighty-seven percent survived. Five needed one and didn't get it. None of them survived.", [(888808, 205.0, .5), (888808, 221.0, .5)], "drive"),
  ("And in that study, no amputations resulted solely from the tourniquet.", [(855753, 41.0, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("nineteen sixteen", "1916"), ("two thousand six", "2006"), ("eighty-seven percent", "87%"), ("Eighty-seven percent", "87%"),
 ("eighteen eighty-three", "1883"), ("two thousand five", "2005"), 
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["111605", "888808", "886668", "1000551", "855753", "arm_officers", "arm_field", "esmarch_fig_kb"]
