# Shorts for KEPT ALIVE · WAR MEDICINE EP 1 — What Being Wounded in WWI Actually Felt Like (long video Thu 2026-11-19 13:00 ET).
# Templates: s1 = big contrast numbers on a winning subject (flu that hit soldiers): "340,000 vs 227,000"
#            s2 = one object + number (blood on ice: "22 units", the first blood bank, 1917) → fresh DVIDS blood drive today
#            s3 = before -> after (thigh fracture "4 in 5" died → 15.6% with the Thomas splint)
# shot: (clip_id, start, cx). card_* = 20 s push-ins of our own cards; stl_* = push-ins of 1917/1925 Army book images.
# Archival = U.S. Army Signal Corps films 1918 (National Archives). No patient is named. No wounds on screen.
SHORTS = [
 dict(id="s1", credit="Film: U.S. Army Signal Corps 1918 (NARA) · Graphics: KEPT ALIVE",
      hook="340,000 VS 227,000<br>[FLU VS. WOUNDS]", title="WWI: Flu Hospitalized More U.S. Soldiers Than Battle",
      label="ARCHIVAL FILM 1918 · U.S. ARMY SIGNAL CORPS\\NSOURCES: NATIONAL GUARD · PUBLIC HEALTH REPORTS",
      lines=[
  ("Three hundred and forty thousand versus two hundred and twenty-seven thousand. In France in nineteen eighteen, the flu put more American soldiers in the hospital than battle wounds did.", [("card_flu", 0.5, .5)], "punch"),
  ("Its deadliest wave hit in the autumn, during the Meuse-Argonne offensive.", [("ma_jam", 22.0, .5), ("arg_tents", 10.0, .5)], "tense"),
  ("In October, fourteen hundred and fifty-one Americans died of flu there, and the sick clogged the roads and trains the wounded needed.", [("sav_train", 30.0, .5)], "drive"),
  ("By the end of nineteen eighteen, about forty-five thousand American soldiers had died of flu and pneumonia.", [("card_45k", 0.5, .5)], "slow"),
 ]),
 dict(id="s2", credit="Graphics: KEPT ALIVE · Footage: U.S. Army 1918 (NARA), U.S. Navy via DVIDS",
      hook="22 UNITS<br>[BLOOD ON ICE]", title="22 Units of Blood on Ice: The WWI Army Blood Bank",
      label="1918 ARMY FILM (NARA) · TODAY: RED CROSS DRIVE, SASEBO, OCT 2026\\NSOURCES: STANFORD BLOOD CENTER · NLM · U.K. NAT. ARCHIVES",
      lines=[
  ("Twenty-two units of blood, stored on ice. In nineteen seventeen, a U.S. Army doctor in France built what is often called the first blood bank.", [("card_blood", 0.5, .5)], "punch"),
  ("Oswald Robertson took blood from group O donors, mixed it with citrate and sugar, and kept it in glass bottles for up to twenty-six days.", [("sav_ward", 8.0, .5), ("sav_ward", 30.0, .5)], "drive"),
  ("He gave it to twenty wounded soldiers who were too badly hurt to withstand surgery.", [("fis_tents", 16.0, .5)], "tense"),
  ("Today, military medicine still runs on that idea, and on donors.", [("1029529", 6.5, .5), ("1029529", 52.5, .5)], "slow"),
 ]),
 dict(id="s3", credit="Drawings: U.S. Army manual 1917 · Film: Signal Corps 1918",
      hook="~4 IN 5 DIED (EST.)<br>[THEN: A SPLINT]", title="An Estimated 4 in 5 Died of This WWI Wound. Then: a Splint",
      label="1917 U.S. ARMY SPLINT MANUAL · 1918 SIGNAL CORPS FILM\\NSOURCES: GRAY 1919 · J SPEC OPS MED 2014",
      lines=[
  ("Four in five. Early in World War One, that was roughly how many soldiers died of an open fracture of the thigh bone, by one British surgeon's estimate.", [("card_80", 0.5, .5)], "punch"),
  ("The fix was an iron frame from the eighteen seventies, the Thomas splint. It held the broken leg straight under tension.", [("stl_thomas_bed", 1.0, .5), ("stl_thomas_str", 1.0, .5)], "drive"),
  ("At Arras in nineteen seventeen, Henry Gray followed one thousand and nine of these fractures. About one in six died. Faster evacuation helped too.", [("card_156", 0.5, .5)], "tense"),
  ("In nineteen eighteen, American aid stations carried it as standard kit.", [("bac_aid", 2.0, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("Three hundred and forty thousand", "340,000"), ("two hundred and twenty-seven thousand", "227,000"), ("nineteen eighteen", "1918"),
 ("fourteen hundred and fifty-one", "1,451"), ("forty-five thousand", "45,000"), ("Twenty-two units", "22 units"), ("nineteen seventeen", "1917"),
 ("twenty-six days", "26 days"), ("twenty wounded", "20 wounded"), ("Four in five", "4 in 5"), ("World War One", "World War I"),
 ("eighteen seventies", "1870s"), ("one thousand and nine", "1,009"), ("one in six", "1 in 6"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_flu", "card_45k", "card_blood", "card_80", "card_156", "stl_thomas_bed", "stl_thomas_str", "stl_cantigny",
        "ma_jam", "arg_tents", "sav_train", "sav_ward", "fis_tents", "bac_aid", "1029529"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
