# KEPT ALIVE · EP 3 (302) "Why Disease Often Killed More U.S. Soldiers Than Combat, Explained" · 4 Short candidates (shorts.py reads this file).
# Facts: /home/claude/work/facts302.md + wording corrections in factcheck.md. Sources per fact: shorts_sources.md. Clips: make_cards.py (st_* / card_*) + episode excerpts + clips.json.
# Visual templates (all different):
#   s1 TRAILER   = number-card-led (Spanish-American War, CRS 385 vs 2,061) + 1898 photos / 1904 Board plan, ends "Full story on the channel."
#   s2           = archival-photo-led (Walter Reed's question, Camp Lazear 1900 photos; ONE 1945 PHS mosquito film shot, labelled with its year, "not Cuba")
#   s3           = film-led (WWII: Navy 1943-44 + Army 1944 malaria films, labelled; 2 number cards)
#   s4           = map/illustration-led (Mexican War: 1847 War Dept map, 1846/1847 engravings = illustrations; bar + number cards)
# Honesty: no blood / wounds / bodies / sick faces; each Short's HUD label is true over the WHOLE Short and names the years of every image/film.
# shot: (clip_id, start, cx). st_*/card_* = 20 s push-ins from make_cards.py (fitted into the 9:16 column, so cx stays .5 for them).
SHORTS = [
 dict(id="s1", credit="Images: Harper's (1899), Typhoid Board report (1904) · public domain",
      hook="{\\fs92}385 BATTLE DEATHS<br>[2,061 OTHER DEATHS]", title="Spanish-American War: 385 Battle Deaths, 2,061 Other",
      label="SOURCES: CRS RL32492 · NMHM · PBS · TYPHOID BOARD\\N1898 CAMP PHOTOS (SAN FRANCISCO, DAIQUIRI) · 1904 PLAN",
      lines=[
  ("Three hundred eighty-five battle deaths. Two thousand sixty-one other deaths. The Spanish-American War.", [("card_sa_nums", 0.5, .5)], "punch"),
  ("Congressional Research Service data cover May to August of eighteen ninety-eight. Records are incomplete.", [("card_sa_note", 0.5, .5)], "calm"),
  ("The best-known camp killer was typhoid, spread through contaminated food or water.", [("st_sa_camp", 0.5, .5), ("st_sa_daiquiri", 0.5, .5)], "tense"),
  ("An Army board studied ninety-two regiments. Typhoid moved by contact, flies and water.", [("st_sa_plan", 0.5, .5)], "drive"),
  ("By another count, twenty thousand seven hundred of one hundred seventy-one thousand camp personnel caught typhoid. Over fifteen hundred died.", [("card_sa_typhoid", 0.5, .5)], "slow"),
  ("More than five other deaths for every battle death. Full story on the channel.", [("card_sa_ratio", 0.5, .5)], "punch"),
 ]),
 dict(id="s2", credit="Photos: Kelly (1906) · Film: U.S. PHS 1945 (NLM) · PD",
      hook="DID THE<br>[MOSQUITO] DO IT?", title="Did the Mosquito Do It? Walter Reed's 1900 Army Test",
      label="PHOTOS 1900-01 · SOURCES: UVA · JAMES LIND LIB.\\N1945 U.S. PHS MOSQUITO FILM · NOT CUBA, 1900",
      lines=[
  ("Did the mosquito do it? Havana averaged four hundred sixty-two yellow fever deaths a year.", [("aedes_macro", 48.3, .65), ("card_havana462", 0.5, .5)], "question"),
  ("Walter Reed wrote those words in September, nineteen hundred.", [("st_reed", 0.5, .5), ("card_reed_q", 0.5, .5)], "calm"),
  ("At Camp Lazear, the first mosquito bites on four volunteers changed nothing.", [("st_lazear_camp", 0.5, .5)], "tense"),
  ("In December, one volunteer fell ill with yellow fever. Three more followed.", [("st_lazear_camp", 6.0, .5)], "drive"),
  ("Infected clothing, tested on seven men: none fell ill.", [("st_lazear_clothes", 0.5, .5)], "calm"),
  ("Yes: the Commission showed it, Virginia's library exhibit says. Havana's last yellow fever death under American occupation: September twenty-eighth, nineteen oh one.", [("st_reed", 8.0, .5), ("card_havana_last", 0.5, .5)], "slow"),
 ]),
 dict(id="s3", credit="Films: U.S. Navy 1943-44, U.S. Army 1944 (NARA via archive.org, PD)",
      hook="{\\fs60}U.S. ARMY · WWII<br>{\\fs86}15 MILLION ADMISSIONS<br>[14,904 DISEASE DEATHS]", title="U.S. Army, WWII: 15 Million Medical Admissions, 14,904 Disease Deaths",
      label="SOURCES: MED. STATISTICS IN WWII (U.S. ARMY ONLY) · CRS\\NFILMS: NAVY 1943-44 · ARMY 1944 · PLACES UNSTATED",
      lines=[
  ("Nearly fifteen million medical admissions for disease. Over seven hundred twenty-three thousand for battle wounds. U.S. Army, World War Two.", [("nm_lab", 31.0, .5), ("card_ww2_adm", 0.5, .5)], "punch"),
  ("In four earlier wars, other deaths outnumbered battle deaths. Would disease win again?", [("card_earlier", 0.5, .5)], "question"),
  ("Malaria alone brought about five hundred thousand Army hospital admissions.", [("nm_larvae", 30.0, .5)], "tense"),
  ("Navy and Army films show the fight: a jar of larvae, a hammock net.", [("nm_lab", 19.0, .5), ("fb147_net", 0.5, .5)], "calm"),
  ("Army battle deaths: two hundred twenty-nine thousand, eight hundred twenty-three. Disease deaths: fourteen thousand, nine hundred four. The old rule broke.", [("card_ww2_battle", 0.5, .5), ("card_ww2_dis", 0.5, .5)], "slow"),
 ]),
 dict(id="s4", credit="Map: War Dept 1847 · Engravings: Frost 1862, Lippard 1850 · PD",
      hook="{\\fs96}ABOUT 7 TO 1<br>{\\fs76}[OTHER VS BATTLE DEATHS]", title="Mexican War: 1,733 Battle Deaths vs 11,550 Other Deaths",
      label="MEXICAN WAR · CRS · 1847 MAP · ENGRAVINGS 1850, 1862\\NENGRAVINGS ARE ILLUSTRATIONS, NOT PHOTOGRAPHS",
      lines=[
  ("About seven to one: eleven thousand five hundred fifty other deaths, one thousand seven hundred thirty-three battle deaths. The Mexican War.", [("card_mex_ratio", 0.5, .5)], "punch"),
  ("Monterrey in eighteen forty-six. Veracruz in March, eighteen forty-seven. Then Mexico City.", [("st_mex_monterrey", 0.5, .5), ("st_mex_vcmap", 0.5, .5), ("st_mex_city", 0.5, .5)], "calm"),
  ("In all, thirteen thousand two hundred eighty-three American deaths.", [("card_mex_split", 0.5, .5)], "drive"),
  ("The CRS notes that data before World War One are based on incomplete records.", [("card_mex_note", 0.5, .5)], "tense"),
  ("About eighty-seven percent were other deaths.", [("card_mex_pay", 0.5, .5)], "slow"),
 ]),
]

DISPLAY = [
 ("Three hundred eighty-five", "385"), ("Two thousand sixty-one", "2,061"), ("eighteen ninety-eight", "1898"), ("ninety-two", "92"),
 ("fifteen hundred", "1,500"), ("one hundred seventy-one thousand", "171,000"), ("twenty thousand seven hundred", "20,700"), ("More than five", "More than 5"), ("four hundred sixty-two", "462"), ("nineteen hundred", "1900"),
 ("four volunteers", "4 volunteers"), ("Three more", "3 more"), ("seven men", "7 men"),
 ("September twenty-eighth, nineteen oh one", "September 28, 1901"),
 ("Nearly fifteen million", "Nearly 15 million"), ("Over seven hundred twenty-three thousand", "Over 723,000"),
 ("World War Two", "World War II"), ("World War One", "World War I"), ("four earlier wars", "4 earlier wars"),
 ("five hundred thousand", "500,000"), ("two hundred twenty-nine thousand, eight hundred twenty-three", "229,823"),
 ("fourteen thousand, nine hundred four", "14,904"), ("About seven to one", "About 7 to 1"),
 ("eleven thousand five hundred fifty", "11,550"), ("one thousand seven hundred thirty-three", "1,733"),
 ("eighteen forty-six", "1846"), ("eighteen forty-seven", "1847"), ("thirteen thousand two hundred eighty-three", "13,283"),
 ("About eighty-seven percent", "About 87 percent"),
]
CTA = "FOLLOW FOR MORE REAL MEDICINE"
# every source here is silent film / stills / cards: no natural sound under the narration
MUTE = ["nm_lab", "nm_larvae", "fb147_net", "aedes_macro",
        "card_sa_nums", "card_sa_note", "card_sa_typhoid", "card_sa_ratio", "st_sa_camp", "st_sa_plan", "st_sa_dock", "st_sa_daiquiri",
        "card_havana462", "card_reed_q", "card_havana_last", "st_reed", "st_lazear_camp", "st_lazear_clothes",
        "card_ww2_adm", "card_earlier", "card_ww2_battle", "card_ww2_dis",
        "card_mex_ratio", "card_mex_split", "card_mex_note", "card_mex_pay", "st_mex_monterrey", "st_mex_vcmap", "st_mex_city"]

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))
