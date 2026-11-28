# KEPT ALIVE · s020 Shorts, Sun 2026-11-29 (s1 10:00, s2 18:00). Two different WWI subjects, two templates:
# s1 number-card-led: case fatality of Army battle wounds by body region (Table 115, p.1024)  -- Internet Archive item WW1ArmyMedDeptHistV15-2 (vol. XV pt 2, Medical and Casualty Statistics, 1925)
# s2 document/page-led: the Army's estimate that 80-85% of battlefield deaths were primary hemorrhage (p.51) -- Internet Archive item WW1ArmyMedDeptHistV11-1 (vol. XI Surgery pt 1, 1927)
# Own graphics + page scans only (public domain U.S. Army history); no footage, no bodies, no wounds on screen. No clip ids -> used_clips.json not touched.
CRED1 = "Source: Army Medical Dept. in the World War, vol. XV pt 2 (1925, PD)"
CRED2 = "Source: Army Medical Dept. in the World War, vol. XI (1927, PD)"
SHORTS = [
 dict(id="s1", credit=CRED1, hook="43 IN 100 ADMITTED DIED<br>[ARMY · ABDOMEN WOUNDS · WWI]", title="WWI Army Data: 43 in 100 Admitted With Abdomen Wounds Died",
      label="U.S. ARMY MEDICAL REPORTS, 1917–18 · BATTLE WOUNDS\\NDEATHS AMONG MEN ADMITTED, BY BODY REGION · WWI",
      lines=[
  ("Forty-three out of every hundred. In the Army's World War One tables, that is how many men admitted with battle wounds to the abdomen and pelvis died.", [("card_43", 0.5, .5)], "punch"),
  ("The Army counted three thousand five hundred forty-six admissions. One thousand five hundred thirty-six deaths.", [("pg_t115", 0.5, .5)], "tense"),
  ("Wounds to the head: about fourteen percent. The chest: twenty-four. The spine: fifty-six.", [("card_regions", 0.5, .5)], "drive"),
  ("Arms: about four percent. Legs: about seven.", [("card_limbs", 0.5, .5)], "drive"),
  ("All battle wounds together, poison gas excepted: about eight percent.", [("card_all", 0.5, .5)], "calm"),
  ("And by missile, for the abdomen and pelvis: a rifle ball, the table's term, thirty-three percent. A shell, about forty-five.", [("card_weapon", 0.5, .5)], "tense"),
 ]),
 dict(id="s2", credit=CRED2, hook="80–85%<br>[ESTIMATE: BATTLEFIELD BLEEDING]", title="WWI Army Surgeons Estimated 80-85% of Battlefield Deaths Were Bleeding",
      label="ARMY SURGERY HISTORY OF WWI · BATTLEFIELD DEATHS\\NPRIMARY HEMORRHAGE · AN ESTIMATE, NOT A COUNT",
      lines=[
  ("Eighty to eighty-five percent of battlefield deaths. The Army's own World War One surgery history estimates: bleeding.", [("card_80", 0.5, .5)], "punch"),
  ("Read the sentence. No accurate figures are available; quote, we are probably safe in estimating.", [("pg_hem", 0.5, .5)], "tense"),
  ("It adds: relatively few wounded men with central chest injuries ever reached first-aid stations.", [("pg_hem", 7.0, .5)], "drive"),
  ("Why so little data? The page says its conclusions about the battle dead rest on inferences, for, quote, lack of observation and lack of records.", [("pg_lack", 0.5, .5)], "calm"),
  ("An estimate: eighty to eighty-five percent of battlefield deaths, from bleeding.", [("card_80b", 0.5, .5)], "slow"),
 ]),
]
DISPLAY = [
 ("three thousand five hundred forty-six", "3,546"), ("One thousand five hundred thirty-six", "1,536"), ("Eighty to eighty-five percent", "80–85%"), ("eighty to eighty-five percent", "80–85%"),
 ("Forty-three out of every hundred", "43 out of every 100"), ("World War One", "World War I"), ("thirty-three percent", "33%"), ("about forty-five", "about 45"),
 ("about fourteen percent", "about 14%"), ("twenty-four", "24"), ("fifty-six", "56"), ("about four percent", "about 4%"), ("about seven", "about 7"), ("about eight percent", "about 8%"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_43", "pg_t115", "card_regions", "card_limbs", "card_all", "card_weapon", "card_80", "pg_hem", "pg_lack", "card_80b"]
DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
