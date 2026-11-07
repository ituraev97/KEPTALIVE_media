# Shorts for KEPT ALIVE · OUTBREAK 006 — The Flu That Went to War (1918). Three Shorts, one fact each; facts as verified for the long episode.
# Templates: s1 = one shocking fact · s2 = then vs. now · s3 = countdown (3 numbers).
# shot: (clip_id, start, cx) — cx = horizontal centre of the 9:16 crop (0..1). label = persistent HUD line describing ALL footage in that Short.
# *_kb = slow push-in clips rendered from the public-domain photos (NMHM NCP 1603; NARA 165-WW-269B).
SHORTS = [
 dict(id="s1", credit="Photo: NMHM · Film: U.S. Army Signal Corps, NARA · public domain",
      hook="45,000<br>[SOLDIERS]", title="The Flu That Killed Almost as Many U.S. Soldiers as Combat",
      label="EMERGENCY HOSPITAL · CAMP FUNSTON, KANS. · 1918\\NARMY FILM \"INFANTRY TRAINING\" · 1918–19",
      lines=[
  ("In nineteen eighteen, flu and the pneumonia that followed killed about forty-five thousand American soldiers.", [("funston_kb", 0.5, .5)], "punch"),
  ("This is an emergency hospital at Camp Funston, Kansas, during that epidemic.", [("funston_kb", 5.0, .62)], "calm"),
  ("American combat deaths in the entire war were about fifty-three thousand.", [("wwi_march", 1.0, .5)], "drive"),
  ("Flu and pneumonia killed almost as many soldiers as combat did.", [("wwi_rows", 2.0, .5)], "slow"),
 ]),
 dict(id="s2", credit="Footage: U.S. Army Signal Corps, NARA · AFN via DVIDS · public domain",
      hook="1918 VS<br>[TODAY]", title="What Really Killed Most Victims of the 1918 Flu",
      label="ARMY FILM · RED CROSS · 1918–19 · CAMP FUNSTON 1918\\NFLU DRIVE · CAMP CARROLL, KOREA · OCT. 2026",
      lines=[
  ("Most victims of the nineteen eighteen flu didn't die from the virus alone.", [("rc_nurses", 1.0, .5)], "punch"),
  ("NIH scientists studied lung tissue from fifty-eight soldiers who died back then. Most victims died of bacterial pneumonia that followed the flu.", [("funston_kb", 1.0, .5), ("rc_canteen", 4.0, .5)], "calm"),
  ("In nineteen eighteen, there were no antibiotics, and no flu vaccine.", [("rc_front", 1.0, .5)], "drive"),
  ("Today, the military gives flu shots every year.", [(1027481, 9.0, .5), (1027481, 15.5, .5)], "slow"),
 ]),
 dict(id="s3", credit="Photos: NARA 165-WW-269B · NMHM · public domain",
      hook="1918 IN<br>[3 NUMBERS]", title="The Deadliest Flu in Modern History, in 3 Numbers",
      label="SEATTLE & BOSTON · 1918 · NARA 165-WW-269B\\NCAMP FUNSTON, KANS. · 1918 · NMHM",
      lines=[
  ("The nineteen eighteen flu pandemic, in three numbers.", [("seattle_police_kb", 0.5, .5)], "punch"),
  ("Number one. Five hundred million. That's about a third of the world's people, infected, by CDC's estimate.", [("masks_boston_kb", 0.5, .45)], "calm"),
  ("Number two. Fifty million. At least that many died worldwide.", [("seattle_rc_kb", 0.5, .5)], "calm"),
  ("Number three. Six hundred seventy-five thousand. That's about how many died in the United States. CDC calls it the most severe pandemic in recent history.", [("seattle_police_kb", 3.0, .45), ("funston_kb", 0.5, .6)], "slow"),
 ]),
]

DISPLAY = [
 ("nineteen eighteen", "1918"), ("Nineteen eighteen", "1918"), ("forty-five thousand", "45,000"), ("fifty-three thousand", "53,000"),
 ("fifty-eight", "58"), ("Five hundred million", "500 million"), ("Fifty million", "50 million"), ("Six hundred seventy-five thousand", "675,000"),
 ("three numbers", "3 numbers"), ("Number one", "#1"), ("Number two", "#2"), ("Number three", "#3"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["rc_canteen", "funston_kb", "seattle_police_kb", "masks_boston_kb", "seattle_rc_kb", "wwi_march", "wwi_rows", "rc_nurses", "rc_front"]
