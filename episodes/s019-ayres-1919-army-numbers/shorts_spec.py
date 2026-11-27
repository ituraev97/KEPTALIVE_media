# KEPT ALIVE · s019 Shorts, Fri 2026-11-27 (s1 10:00, s2 18:00) + Sat 2026-11-28 (s3 10:00, s4 18:00).
# Single primary source for every number: Leonard P. Ayres, "The War with Germany: A Statistical Summary" (U.S. War Dept./GPO, 2nd ed., data to Aug 1, 1919),
# Internet Archive item warwithgermanyst01unit (public domain). All visuals are own graphics + page scans; no footage, no bodies, no wounds.
# Templates: s1 timeline/curve-led (Diagram 56 scan + number cards) · s2 document-led (summary page strip + cards) · s3 number/bar-led (ladder cards + Diagram 54) · s4 pie/page-led (Diagram 53 + typhoid page).
CRED = "Source: Ayres, The War with Germany (1919, U.S. War Dept., PD) via Internet Archive"
SHORTS = [
 dict(id="s1", credit=CRED, hook="5 PER 1,000 A YEAR<br>[THEN 4 IN ONE WEEK, AT HOME]", title="Oct. 1918: 4 per 1,000 U.S. Troops Died in One Week",
      label="U.S. ARMY SUMMARY, 1919 · TROOPS IN THE UNITED STATES\\NDEATHS FROM ALL CAUSES · INFLUENZA EPIDEMIC",
      lines=[
  ("From the start of the war until September fourteenth, nineteen eighteen, the Army's disease death rate was five per thousand men a year.", [("card_rate5", 0.5, .5)], "punch"),
  ("Then the flu. Second week of October: the Army's chart shows four out of every thousand troops in this country died. In one week.", [("pg_d56", 0.5, .5)], "tense"),
  ("In eight weeks, the Army reported, among troops at home, more than three hundred sixteen thousand flu cases, and more than fifty-three thousand pneumonia cases.", [("card_316", 0.5, .5)], "drive"),
  ("The Army's nineteen-nineteen summary: more than forty thousand pneumonia deaths. Probably twenty-five thousand were the flu pandemic.", [("card_40k", 0.5, .5)], "calm"),
 ]),
 dict(id="s2", credit=CRED, hook="85% BACK TO DUTY<br>[HOSPITALIZED FOR INJURIES]", title="1919 Army Summary: 85% of Hospitalized Men Returned to Duty",
      label="ARMY SUMMARY OF THE WAR WITH GERMANY, 1919\\NAMERICAN EXPEDITIONARY FORCES · WWI",
      lines=[
  ("The Army's nineteen-nineteen summary says: about eighty-five percent of the men sent to hospitals for injuries were returned to duty.", [("card_85", 0.5, .5)], "punch"),
  ("Its summary list says five of every six men sent to hospitals on account of wounds were cured and returned to duty.", [("pg_sum67", 0.5, .5)], "tense"),
  ("In the American Expeditionary Forces, men who died of wounds numbered only seven percent of the wounded.", [("card_7pct", 0.5, .5)], "drive"),
  ("When the war began, the Army had two thousand eighty-nine commissioned medical officers, Reserves included. During the war, over thirty-one thousand physicians from civil life were commissioned.", [("card_med", 0.5, .5)], "calm"),
 ]),
 dict(id="s3", credit=CRED, hook="110 TO 19<br>[DISEASE DEATHS PER 1,000 A YEAR]", title="110 Disease Deaths per 1,000 (1846), 19 for WWI Overseas",
      label="ARMY SUMMARY, 1919 · DEATHS PER YEAR FOR EACH 1,000 MEN\\NDISEASE DEATHS · WWI FIGURE = OVERSEAS FORCES ONLY",
      lines=[
  ("In the Mexican War, disease killed soldiers at a rate of one hundred ten per year for every thousand men.", [("card_110", 0.5, .5)], "punch"),
  ("Civil War, the North: sixty-five.", [("card_65", 0.5, .5)], "drive"),
  ("Spanish War: twenty-six.", [("card_26", 0.5, .5)], "drive"),
  ("American forces overseas in World War One: nineteen.", [("card_19", 0.5, .5)], "tense"),
  ("The same chart shows battle deaths overseas at fifty-three per thousand, higher than in any previous American war.", [("pg_d54", 0.5, .5)], "calm"),
  ("For the low disease rate, the Army credited trained doctors, typhoid vaccination, clean camps, and hospitals.", [("pg_d54", 11.0, .5)], "slow"),
 ]),
 dict(id="s4", credit=CRED, hook="115,660 ARMY DEATHS<br>[HALF FROM DISEASE]", title="Army + Attached Marines: 115,660 WWI Deaths, Half Disease",
      label="ARMY SUMMARY, 1919 · ARMY DEATHS INCLUDING MARINES ATTACHED\\NDISEASE · BATTLE · OTHER CAUSES",
      lines=[
  ("One hundred fifteen thousand, six hundred sixty Army men, marines attached included, died from the declaration of war to July first, nineteen nineteen.", [("card_115", 0.5, .5)], "punch"),
  ("About fifty-seven thousand died of disease. About fifty thousand in battle. Nearly eight thousand from other causes.", [("pg_d53", 0.5, .5)], "tense"),
  ("Overseas, it was different: battle losses were twice as large as deaths from disease.", [("card_2x", 0.5, .5)], "drive"),
  ("Typhoid, which once ravaged armies: two thousand three hundred twenty-eight cases reported, two hundred twenty-seven deaths.", [("card_typh", 0.5, .5)], "calm"),
  ("The summary credited compulsory vaccination of every man who entered the Army, and sanitary camps.", [("pg_p125", 0.5, .5)], "slow"),
 ]),
]
DISPLAY = [
 ("One hundred fifteen thousand, six hundred sixty", "115,660"), ("three hundred sixteen thousand", "316,000"), ("fifty-three thousand", "53,000"),
 ("two thousand three hundred twenty-eight", "2,328"), ("two hundred twenty-seven", "227"), ("two thousand eighty-nine", "2,089"),
 ("About fifty-seven thousand", "About 57,000"), ("About fifty thousand", "About 50,000"), ("Nearly eight thousand", "Nearly 8,000"),
 ("more than forty thousand", "more than 40,000"), ("twenty-five thousand", "25,000"), ("over thirty-one thousand", "over 31,000"),
 ("July first, nineteen nineteen", "July 1, 1919"), ("September fourteenth, nineteen eighteen", "Sept. 14, 1918"), ("nineteen-nineteen", "1919"), ("nineteen", "19"),
 ("one hundred ten", "110"), ("sixty-five", "65"), ("twenty-six", "26"), ("fifty-three", "53"),
 ("five per thousand", "5 per 1,000"), ("four out of every thousand", "4 of every 1,000"), ("five of every six", "5 of every 6"), ("eighty-five percent", "85%"), ("seven percent", "7%"),
 ("World War One", "World War I"), ("six were wounded", "6 were wounded"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
MUTE = ["card_85", "card_7pct", "card_rate5", "pg_d56", "card_316", "card_40k", "pg_sum67", "card_med", "card_2of100", "card_110", "card_65", "card_26", "card_19", "pg_d54", "card_115", "pg_d53", "card_2x", "card_typh", "pg_p125"]
DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
