# KEPT ALIVE · FIRST 010 — Penicillin: How It Was Discovered, and How It Was Rushed to D-Day
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  No footage exists here of Fleming, Oxford or Peoria: those parts are told with our own graphics.
#  pen_plant = United News newsreel "Penicillin Drug Saves Allied Lives" (1944, NARA 208-UN-113, public domain) — penicillin manufacture, plant not named
#  pen_lab   = United News newsreel "Penicillin and Plasma Save Lives" (1944, NARA 208-UN-1008, public domain) — penicillin culture/production shots only
#             (plasma and casualty shots of the same reel are NOT used). Both always tagged "1944 NEWSREEL"; never presented as Fleming's, Oxford's or Pfizer's lab.
#  emb_* = "Embarkation: Normandy Invasion of Europe, 1944" (U.S. Coast Guard/Navy color film, NARA via Naval Photographic Center #10769) — England, 1944
#  land_* = "Landing Craft at Anchor Before Invasion; Troops Land in France, 06/05–06/06/1944" (NPC #4360) — cropped to remove a burned-in timecode
#  norm_hosp = U.S. Army film "2d Hospital Set Up, Normandy, France, 07/28/1944" (NARA 15776 via Internet Archive) — tents and supplies, no patients
#  876964 = WRAIR Multidrug-Resistant Organism Repository and Surveillance Network (MRSN), 2023 (real lab, DVIDS)
#  876974 = WRAIR Experimental Therapeutics, 2023 (real lab, DVIDS) · 811325 = NMCSD Microbiology Laboratory b-roll, San Diego, Aug. 2021 (DVIDS)
#  No patient is named. No wounds, blood or patients on screen.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "FIRST · 010"
S = "<span style=\"color:#2BB3A3\">{}</span>"
NR1 = ("PENICILLIN PRODUCTION · 1944 NEWSREEL", "PLANT NOT IDENTIFIED · UNITED NEWS · NATIONAL ARCHIVES 208-UN-113")
NR2 = ("PENICILLIN MOLD CULTURES · 1944 NEWSREEL", "LOCATION NOT IDENTIFIED · UNITED NEWS · NARA 208-UN-1008")
EMB = ("U.S. TROOPS EMBARK FOR THE NORMANDY INVASION", "ENGLAND · 1944 · U.S. COAST GUARD FILM · NATIONAL ARCHIVES")
LAND = ("LANDING CRAFT HEAD FOR THE FRENCH COAST", "JUNE 1944 · U.S. NAVY FILM · NATIONAL ARCHIVES")
HOSP = ("A U.S. ARMY HOSPITAL IS SET UP IN NORMANDY", "FRANCE · JULY 1944 · U.S. ARMY FILM · NATIONAL ARCHIVES")
MRSN = ("TRACKING ANTIBIOTIC-RESISTANT BACTERIA", "WALTER REED ARMY INSTITUTE OF RESEARCH · 2023")
WRL = ("BACTERIA CULTURES IN A LAB TODAY", "WALTER REED ARMY INSTITUTE OF RESEARCH · 2023")
NMC = ("MICROBIOLOGY LABORATORY", "NAVAL MEDICAL CENTER SAN DIEGO · 2021")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("How was penicillin discovered? By accident.",
  [G("stat", a="&#8203;1928", b="PENICILLIN IS DISCOVERED — BY ACCIDENT", c="ST. MARY'S HOSPITAL, LONDON · SOURCES: AAI · PBS NEWSHOUR")], dict(kind="punch")),
 ("In September nineteen twenty-eight, a London bacteriologist named Alexander Fleming came back from a summer vacation and found that a mold had contaminated one of his dishes of bacteria. Around the mold, the bacteria did not grow.",
  [G("doc", header="ST. MARY'S HOSPITAL · LONDON · SEPTEMBER 1928", title="THE CONTAMINATED DISH", body="A mold had landed on a culture of staphylococcus bacteria. Around it: a ring where the bacteria did not grow.",
     source="SOURCES: AAI · PBS NEWSHOUR", stamp="CONTAMINATED")], dict(kind="tense")),
 ("Sixteen years later, American companies had produced two point three million doses of the drug first found in that mold. In time for D-Day.",
  [C("emb_harbor", 13.0), C("emb_march", 15.9)], dict(tag=EMB, kind="drive")),
 ("Between the dish and the beaches were a team in Oxford, a moldy cantaloupe in Illinois, and an old ice plant in Brooklyn.",
  [G("timeline", kicker="FROM DISH TO D-DAY", title="1928–1944",
     events=[dict(y="1928", t="A dish in London"), dict(y="1940", t="A team in Oxford"), dict(y="1943", t="A cantaloupe in Illinois"), dict(y="1944", t="An ice plant in Brooklyn")],
     footer="SOURCES: AAI · SCIENCE HISTORY INSTITUTE · USDA ARS · AMERICAN CHEMICAL SOCIETY")], dict(kind="calm")),
 ("This is the story of the first antibiotic to be mass-produced. And of the warning its discoverer gave the world.",
  [C("pen_lab", 16.4)], dict(tag=NR2, kind="question", gap=0.4)),
 ("Penicillin. The mold that went to war.",
  [G("title", kicker=CASE, title="PENICILLIN", sub="THE MOLD THAT " + S.format("WENT TO WAR"), size=210)], dict(kind="slow", gap=2.4)),

 # ---------------- I. THE WOUNDS ----------------
 ("To see why it mattered, start with the First World War.",
  [G("chapter", case="1914–1918", n="I", t="THE WOUNDS")], dict(gap=1.0, kind="calm")),
 ("Fleming served as a captain in the British Royal Army Medical Corps. He worked in a field laboratory in France, studying infected wounds.",
  [G("doc", header="FRANCE · WORLD WAR I", title="CAPTAIN ALEXANDER FLEMING", body="Royal Army Medical Corps. A field laboratory, studying wound infections.",
     source="SOURCE: AMERICAN ASSOCIATION OF IMMUNOLOGISTS")], dict(kind="calm")),
 ("What he and his mentor, Almroth Wright, found was troubling. The antiseptics surgeons used in the field were more harmful than helpful. They were often better at killing the body's own infection-fighting white blood cells than the bacteria.",
  [G("stat", a="HARMFUL", b="FIELD ANTISEPTICS IN WORLD WAR I", c="OFTEN KILLED WHITE BLOOD CELLS MORE THAN BACTERIA · SOURCE: AAI")], dict(kind="tense")),
 ("Doctors had no drug that could clear a wound infection from inside the body. And in the Great War, disease caused about one in three military deaths.",
  [G("stat", a="1 IN 3", b="MILITARY DEATHS IN WORLD WAR I CAUSED BY DISEASE", c="APPROXIMATELY · SOURCE: NATIONAL WWII MUSEUM")], dict(kind="slow", gap=0.6)),
 ("After the war, Fleming went back to his laboratory at St. Mary's Hospital in London. Ten years later, a mistake would eventually make him famous.",
  [G("cards3", kicker="ALEXANDER FLEMING · BEFORE PENICILLIN", title="THE PATH TO 1928",
     cards=[dict(h="WWI", t="Wound infections, France"), dict(h="1921", t="Discovers lysozyme"), dict(h="1928", t="The contaminated dish")],
     footer="SOURCES: AAI · SCIENCE HISTORY INSTITUTE")], dict(kind="calm", gap=0.5)),

 # ---------------- II. THE DISH ----------------
 ("It began with a dirty bench.",
  [G("chapter", case="LONDON · 1928", n="II", t="THE DISH")], dict(gap=1.0, kind="calm")),
 ("In the summer of nineteen twenty-eight, Fleming went on vacation to Scotland. He left some of his bacterial cultures out on the bench.",
  [G("doc", header="LONDON · SUMMER 1928", title="A MESSY LAB BENCH", body="Fleming returns from vacation in Scotland. Cultures of staphylococcus had been left out.",
     source="SOURCES: PBS NEWSHOUR · AAI")], dict(kind="calm")),
 ("A culture is a dish of jelly where bacteria are grown on purpose. This is what they look like in a lab today, at the Walter Reed Army Institute of Research.",
  [C(876964, 214.4), C(876964, 270.5)], dict(tag=WRL, kind="calm")),
 ("Fleming's dishes held staphylococcus, a common bacterium. On one of them, a mold had landed. And around the mold was a ring where the bacteria did not grow.",
  [G("steps", kicker="SEPTEMBER 1928", title="WHAT FLEMING SAW", items=[["DISH", "Staphylococcus bacteria"], ["MOLD", "A contaminant lands"], ["RING", "No bacteria around it"], ["QUESTION", "What is the mold making?"]],
     footer="SOURCES: AAI · PBS NEWSHOUR")], dict(kind="drive")),
 ("The mold was a Penicillium. The bacteria-killing substance it made became known as penicillin.",
  [G("stat", a="PENICILLIUM", b="THE MOLD", c="PENICILLIUM NOTATUM · SOURCES: NATIONAL WWII MUSEUM · PBS NEWSHOUR")], dict(kind="calm")),
 ("In nineteen twenty-nine, Fleming published his findings in the British Journal of Experimental Pathology. The paper was largely ignored.",
  [G("doc", header="LONDON · 1929", title="BRITISH JOURNAL OF EXPERIMENTAL PATHOLOGY", body="Fleming publishes his findings on the mold. The paper is \"largely ignored.\"",
     source="SOURCE: AAI", stamp="IGNORED")], dict(kind="calm")),
 ("Fleming did little more work on it. But he kept his mold growing. For twelve years.",
  [G("stat", a="12", b="YEARS FLEMING KEPT THE MOLD GROWING", c="SOURCE: NATIONAL WWII MUSEUM")], dict(kind="slow")),
 ("A line often attributed to him puts it this way:",
  [G("quote", q="I certainly didn't plan to revolutionize all medicine by discovering the world's first antibiotic…", w="ATTRIBUTED TO ALEXANDER FLEMING · AS QUOTED BY PBS NEWSHOUR")], dict(kind="slow", gap=0.2)),
 ("I certainly didn't plan to revolutionize all medicine by discovering the world's first antibiotic.",
  [G("quote", q="I certainly didn't plan to revolutionize all medicine by discovering the world's first antibiotic…", w="ATTRIBUTED TO ALEXANDER FLEMING · AS QUOTED BY PBS NEWSHOUR")], dict(kind="calm", gap=0.8)),

 # ---------------- III. THE TEAM ----------------
 ("The mold waited. Then, in Oxford, someone read the paper.",
  [G("chapter", case="OXFORD · 1938–1941", n="III", t="THE TEAM")], dict(gap=1.0, kind="calm")),
 ("In nineteen thirty-eight, the pathologist Howard Florey and the biochemist Ernst Chain decided to study substances that kill bacteria. Penicillin was one of them.",
  [G("cards3", kicker="SIR WILLIAM DUNN SCHOOL OF PATHOLOGY · OXFORD", title="THE OXFORD TEAM",
     cards=[dict(h="FLOREY", t="Pathologist · led the work"), dict(h="CHAIN", t="Biochemist"), dict(h="HEATLEY", t="Biochemist · grew the mold, purified the drug")],
     footer="SOURCES: SCIENCE HISTORY INSTITUTE · PBS NEWSHOUR")], dict(kind="calm")),
 ("A third biochemist, Norman Heatley, found ways to grow and purify it. The lab grew the mold practically everywhere, from bedpans to bathtubs. Six women technicians, nicknamed the penicillin girls, tended it.",
  [G("doc", header="OXFORD · EARLY 1940s", title="THE \"PENICILLIN GIRLS\"", body="Six technicians tended the mold. It was grown \"practically everywhere, from bedpans to bathtubs.\"",
     source="SOURCE: SMITHSONIAN MAGAZINE")], dict(kind="calm")),
 ("On May twenty-fifth, nineteen forty, Florey's team tested penicillin on infected mice. The mice it was given to survived.",
  [G("stat", a="MAY 25, 1940", b="PENICILLIN CURES INFECTED MICE", c="FLOREY'S TEAM, OXFORD · SOURCES: NATIONAL WWII MUSEUM · PBS NEWSHOUR")], dict(kind="punch")),
 ("That August, Florey and Chain reported their findings in the Lancet. Research groups around the world were electrified.",
  [G("doc", header="THE LANCET · AUGUST 24, 1940", title="PENICILLIN AS A CHEMOTHERAPEUTIC AGENT", body="Florey and Chain report the Oxford results. Research groups around the world take notice.",
     source="SOURCE: SCIENCE HISTORY INSTITUTE")], dict(kind="calm")),
 ("Next came a human patient. In February nineteen forty-one, a policeman became the first patient with an infection to be treated with the Oxford team's purified penicillin.",
  [G("doc", header="OXFORD · FEBRUARY 1941", title="THE FIRST PATIENT", body="A policeman with an infection becomes the first patient treated with the Oxford team's purified penicillin.",
     source="SOURCE: SCIENCE HISTORY INSTITUTE")], dict(kind="tense")),
 ("At first, he improved. There was so little penicillin that the team even recovered it from his urine to use again. It wasn't enough. He relapsed, and died.",
  [G("steps", kicker="OXFORD · 1941", title="THE FIRST TREATMENT", items=[["IMPROVED", "At first"], ["RECOVERED", "Drug reclaimed from urine"], ["RAN LOW", "Supply almost gone"], ["RELAPSED", "He did not survive"]],
     footer="SOURCE: SCIENCE HISTORY INSTITUTE")], dict(kind="slow")),
 ("Making enough penicillin for one human case took about two thousand liters of mold culture fluid.",
  [G("stat", a="2,000", b="LITERS OF MOLD FLUID FOR ONE HUMAN CASE", c="OXFORD, EARLY 1940s · SOURCE: PBS NEWSHOUR")], dict(kind="punch", gap=0.4)),
 ("Early purification was just as hard. Many gallons of mold broth gave an amount of penicillin just large enough to cover a fingernail.",
  [G("stat", a="A FINGERNAIL", b="OF PENICILLIN FROM MANY GALLONS OF MOLD BROTH", c="EARLY PURIFICATION, OXFORD · SOURCE: SCIENCE HISTORY INSTITUTE")], dict(kind="slow", gap=0.4)),
 ("Britain was at war. So at the beginning of July nineteen forty-one, Florey and Heatley flew across the Atlantic, to ask America for help.",
  [G("timeline", kicker="FROM DISH TO DRUG", title="THE OXFORD YEARS",
     events=[dict(y="1938", t="Florey and Chain begin"), dict(y="1940", t="Mice cured · Lancet paper"), dict(y="FEB 1941", t="First patient"), dict(y="JUL 1941", t="Florey and Heatley fly to the U.S.")],
     footer="SOURCES: SCIENCE HISTORY INSTITUTE · NATIONAL WWII MUSEUM")], dict(kind="calm", gap=0.6)),

 # ---------------- IV. THE CANTALOUPE ----------------
 ("America answered. In the middle of the corn belt.",
  [G("chapter", case="PEORIA, ILLINOIS · 1941–1944", n="IV", t="THE CANTALOUPE")], dict(gap=1.0, kind="calm")),
 ("They were sent to the Northern Regional Research Laboratory of the U.S. Department of Agriculture, in Peoria, Illinois. They arrived on July fourteenth, nineteen forty-one. Work began the very next day.",
  [G("callcard", kicker="U.S. DEPARTMENT OF AGRICULTURE", title="PEORIA, ILLINOIS",
     rows=[["LAB", "Northern Regional Research Laboratory"], ["ARRIVED", "July 14, 1941"], ["WORK BEGAN", "The very next day"]],
     footer="SOURCE: USDA AGRICULTURAL RESEARCH SERVICE")], dict(kind="calm")),
 ("Until then, the mold had been grown on the surface of liquid, in flasks and bottles, like these in a nineteen forty-four newsreel.",
  [C("pen_lab", 1.0), C("pen_lab", 10.0)], dict(tag=NR2, kind="calm")),
 ("Peoria's scientists grew it submerged instead, in deep vats of corn steep liquor, a byproduct of corn milling, with air pumped in. It grew faster, and made more penicillin.",
  [G("steps", kicker="USDA · PEORIA", title="DEEP-VAT FERMENTATION", items=[["CORN", "Corn steep liquor"], ["AIR", "Pumped into the vat"], ["DEEP", "Mold grows submerged"], ["MORE", "Faster growth, more penicillin"]],
     footer="SOURCE: USDA AGRICULTURAL RESEARCH SERVICE")], dict(kind="drive")),
 ("They also needed a better mold. Lab workers collected samples from produce markets and other local sources.",
  [G("list", kicker="USDA · PEORIA · 1943", title="THE MOLD HUNT", items=["Produce markets", "Other local sources", "Hundreds of samples tested", "Looking for a better penicillin maker"],
     footer="SOURCE: USDA ARS")], dict(kind="calm")),
 ("The winner came from a moldy cantaloupe found at a Peoria market. Its strain became the parent of all the strains used commercially.",
  [G("stat", a="CANTALOUPE", b="THE PARENT OF ALL COMMERCIAL STRAINS", c="FROM A PEORIA MARKET · STRAIN NRRL 1951 · SOURCE: USDA ARS")], dict(kind="punch")),
 ("Who found it? A lab technician named Mary Hunt is often credited, and the nickname Moldy Mary stuck. But the U.S.D.A. itself says the finder is uncertain.",
  [G("doc", header="PEORIA · 1943", title="\"MOLDY MARY\"?", body="Technician Mary Hunt helped collect mold samples. Who actually found the cantaloupe is uncertain.",
     source="SOURCE: USDA ARS", stamp="UNCERTAIN")], dict(kind="calm")),
 ("Scientists then pushed the mold to change. At the University of Wisconsin, ultraviolet light helped produce a strain called Q one seventy-six. It became the most productive strain of the wartime program.",
  [G("stat", a="Q-176", b="THE MOST PRODUCTIVE WARTIME STRAIN", c="UNIVERSITY OF WISCONSIN–MADISON · SOURCE: UW–MADISON CALS")], dict(kind="calm")),
 ("Norman Heatley stayed on in America. He later worked at the drug company Merck, on the problems of making penicillin at scale.",
  [C("pen_plant", 8.6), C("pen_plant", 28.6)], dict(tag=NR1, kind="calm")),
 ("Meanwhile, drug companies joined in. At first, four of them: Merck, Squibb, Pfizer and Lederle. After the attack on Pearl Harbor, twenty-one American companies combined their efforts.",
  [C("pen_plant", 1.0), C("pen_plant", 20.5)], dict(tag=NR1, kind="drive")),
 ("In March nineteen forty-two, a woman near death in a hospital in New Haven, Connecticut, became the first patient in the United States successfully treated with penicillin.",
  [G("doc", header="NEW HAVEN, CONNECTICUT · MARCH 1942", title="A FIRST FOR THE U.S.", body="A patient near death becomes the first in the U.S. successfully treated with penicillin.",
     source="SOURCE: PBS NEWSHOUR")], dict(kind="tense")),
 ("In Brooklyn, the company Pfizer converted an old ice plant into a penicillin factory, with fourteen tanks of seventy-five hundred gallons each. It opened on March first, nineteen forty-four.",
  [G("callcard", kicker="BROOKLYN, NEW YORK", title="THE ICE PLANT",
     rows=[["BEFORE", "An old ice plant"], ["TANKS", "Fourteen, 7,500 gallons each"], ["OPENED", "March 1, 1944"]],
     footer="SOURCE: AMERICAN CHEMICAL SOCIETY")], dict(kind="calm")),
 ("Soon, it was making more penicillin in one month than the company had made in all of nineteen forty-three.",
  [G("phases", kicker="PFIZER · BROOKLYN", title="ONE MONTH VS. ONE YEAR", left=dict(label="ALL OF 1943", num="1 YEAR", desc="OF PRODUCTION"),
     right=dict(label="1944", num="1 MONTH", desc="MORE THAN ALL OF 1943"), active=1, footer="SOURCE: AMERICAN CHEMICAL SOCIETY")], dict(kind="punch", gap=0.6)),

 # ---------------- V. D-DAY ----------------
 ("By the spring of nineteen forty-four, the Allies were getting ready to invade Normandy.",
  [G("chapter", case="NORMANDY · 1944", n="V", t="D-DAY")], dict(gap=1.0, kind="calm")),
 ("In English ports, American troops boarded landing ships.",
  [C("emb_quay", 1.0), C("emb_harbor", 1.0)], dict(tag=EMB, kind="calm")),
 ("Ahead of D-Day, twenty-one American companies had produced two point three million doses of penicillin.",
  [G("stat", a="2,300,000", b="DOSES OF PENICILLIN READY BEFORE D-DAY", c="21 U.S. COMPANIES · SOURCE: NATIONAL WWII MUSEUM")], dict(kind="punch")),
 ("According to the American Chemical Society, most of the penicillin that went ashore with Allied forces on D-Day came from that converted ice plant in Brooklyn.",
  [C("emb_march", 0.5), C("emb_march", 9.4)], dict(tag=EMB, kind="calm")),
 ("On June sixth, nineteen forty-four, Allied troops landed in Normandy.",
  [C("land_lcvp", 1.0), C("land_beach", 2.0)], dict(tag=LAND, kind="tense")),
 ("Behind them came the field hospitals. This U.S. Army hospital was set up in Normandy in July nineteen forty-four.",
  [C("norm_hosp", 0.6), C("norm_hosp", 22.9)], dict(tag=HOSP, kind="calm")),
 ("The drug was getting cheaper fast. In July nineteen forty-three, a dose of penicillin cost twenty dollars. Three years later, it cost fifty-five cents.",
  [G("phases", kicker="THE PRICE OF A DOSE", title="1943 VS. 1946", left=dict(label="JULY 1943", num="$20", desc="PER DOSE"),
     right=dict(label="THREE YEARS LATER", num="$0.55", desc="PER DOSE"), active=1, footer="SOURCE: USDA AGRICULTURAL RESEARCH SERVICE")], dict(kind="drive")),
 ("From January to May of nineteen forty-two, four hundred million units of pure penicillin were made. By the end of the war, American companies were producing six hundred fifty billion units a month.",
  [G("phases", kicker="U.S. PENICILLIN PRODUCTION", title="FROM SCARCE TO MASS-PRODUCED", left=dict(label="JAN.–MAY 1942", num="400 MILLION", desc="UNITS IN TOTAL"),
     right=dict(label="END OF WWII", num="650 BILLION", desc="UNITS A MONTH"), active=1, footer="SOURCE: PBS NEWSHOUR")], dict(kind="punch")),
 ("One more number. In World War One, the death rate from bacterial pneumonia was eighteen percent. In World War Two, with sulfa drugs and then penicillin, it was less than one percent.",
  [G("phases", kicker="BACTERIAL PNEUMONIA", title="DEATH RATE", left=dict(label="WORLD WAR I", num="18%", desc="DEATH RATE"),
     right=dict(label="WORLD WAR II", num="<1%", desc="DEATH RATE"), active=1, footer="SULFA DRUGS AND PENICILLIN · SOURCE: PBS NEWSHOUR")], dict(kind="slow")),
 ("The early publicity went mostly to Fleming. The Oxford group's part was largely ignored, even though they were the ones who turned penicillin into a medicine.",
  [G("stat", a="OVERLOOKED", b="THE OXFORD TEAM", c="FLOREY, CHAIN AND HEATLEY MADE IT USABLE · SOURCE: PBS NEWSHOUR")], dict(kind="calm")),
 ("In nineteen forty-five, Fleming, Florey and Chain shared the Nobel Prize in Physiology or Medicine. Norman Heatley was left out. In nineteen ninety, Oxford gave him an honorary doctorate of medicine.",
  [G("cards3", kicker="NOBEL PRIZE IN PHYSIOLOGY OR MEDICINE · 1945", title="THE PRIZE",
     cards=[dict(h="FLEMING", t="Discovered it · 1928"), dict(h="FLOREY", t="Proved it works"), dict(h="CHAIN", t="Biochemist")],
     footer="HEATLEY: HONORARY DOCTORATE, OXFORD, 1990 · SOURCES: AAI · PBS NEWSHOUR")], dict(kind="calm", gap=0.6)),

 # ---------------- VI. THE WARNING ----------------
 ("But the story doesn't end with a prize.",
  [G("chapter", case="1945–TODAY", n="VI", t="THE WARNING")], dict(gap=1.0, kind="calm")),
 ("On December eleventh, nineteen forty-five, Fleming gave his Nobel lecture. He ended it with a warning.",
  [G("quote", q="The time may come when penicillin can be bought by anyone in the shops.", w="ALEXANDER FLEMING · NOBEL LECTURE · DECEMBER 11, 1945")], dict(kind="slow")),
 ("The time may come, he said, when penicillin can be bought by anyone in the shops. He feared that people who took too little of it would breed microbes that resist it.",
  [G("quote", q="The time may come when penicillin can be bought by anyone in the shops.", w="ALEXANDER FLEMING · NOBEL LECTURE, 1945 · VIA LIVE SCIENCE")], dict(kind="tense")),
 ("He even described an imagined case. A man takes too little penicillin. His microbes become resistant. He passes them to his wife. She develops pneumonia, and penicillin fails to save her.",
  [G("steps", kicker="FLEMING'S IMAGINED CASE · 1945", title="HOW RESISTANCE SPREADS", items=[["TOO LITTLE", "A man underdoses himself"], ["RESISTANT", "His microbes survive"], ["SPREAD", "They pass to his wife"], ["FAILS", "Penicillin can't save her"]],
     footer="A HYPOTHETICAL FROM FLEMING'S NOBEL LECTURE · SOURCE: LIVE SCIENCE")], dict(kind="slow")),
 ("He had reason to worry. In nineteen forty, Edward Abraham and Ernst Chain had already described an enzyme from bacteria able to destroy penicillin.",
  [G("doc", header="OXFORD · 1940", title="AN ENZYME THAT DESTROYS PENICILLIN", body="Abraham and Chain report a bacterial enzyme able to destroy penicillin.",
     source="SOURCE: NATURE 146:837 (1940)", stamp="RESISTANT")], dict(kind="calm")),
 ("So how does penicillin work? Many bacteria are wrapped in a cell wall. Penicillin binds to the enzymes that build it, called penicillin-binding proteins. The wall weakens. Water pushes in. And the cell bursts.",
  [G("steps", kicker="HOW PENICILLIN WORKS", title="BREAKING THE WALL", items=[["BIND", "Penicillin-binding proteins"], ["BLOCK", "The wall can't be built"], ["WEAKEN", "The wall breaks down"], ["BURST", "Water pushes in"]],
     footer="SOURCE: STATPEARLS")], dict(kind="drive")),
 ("Some bacteria fight back. They make an enzyme, beta-lactamase, that breaks down part of the drug before it can work.",
  [C(876974, 406.5), C(876974, 445.0)], dict(tag=("DRUG RESEARCH LABORATORY", "WALTER REED ARMY INSTITUTE OF RESEARCH · 2023"), kind="calm")),
 ("The C.D.C. estimates that more than two point eight million antimicrobial-resistant infections occur in the U.S. each year, and that more than thirty-five thousand people die as a result.",
  [G("phases", kicker="CDC · 2019 AR THREATS REPORT", title="ANTIMICROBIAL RESISTANCE IN THE U.S.", left=dict(label="INFECTIONS", num="2.8M+", desc="EACH YEAR (ESTIMATED)"),
     right=dict(label="DEATHS", num="35,000+", desc="EACH YEAR (ESTIMATED)"), active=1, footer="SOURCE: CDC")], dict(kind="slow")),
 ("And in twenty twenty-five, the World Health Organization reported that one in six laboratory-confirmed bacterial infections worldwide is resistant to standard antibiotics.",
  [G("stat", a="1 IN 6", b="LAB-CONFIRMED BACTERIAL INFECTIONS RESISTANT TO STANDARD ANTIBIOTICS", c="WORLDWIDE · WHO REPORT, OCTOBER 2025 · VIA UN NEWS")], dict(kind="tense")),
 ("The military tracks the problem too. At the Walter Reed Army Institute of Research, one network watches for antibiotic-resistant bacteria across the Army, Navy and Air Force.",
  [C(876964, 30.5), C(876964, 121.0)], dict(tag=MRSN, kind="calm")),
 ("And military hospitals run their own microbiology labs, like this one at Naval Medical Center San Diego.",
  [C(811325, 22.0), C(811325, 108.5)], dict(tag=NMC, kind="calm")),
 ("World A.M.R. Awareness Week runs from November eighteenth to twenty-fourth. The World Health Organization's message this year is blunt. A.M.R. is no longer a future challenge. It is a global threat.",
  [G("quote", q="AMR is no longer a future challenge; it is a global threat.", w="WORLD HEALTH ORGANIZATION · WORLD AMR AWARENESS WEEK · NOV. 18–24, 2026")], dict(kind="slow", gap=0.6)),

 # ---------------- WHAT CHANGED ----------------
 ("In nineteen twenty-eight, a mold landed on a dish in London, and the paper about it was largely ignored.",
  [G("doc", header="ST. MARY'S HOSPITAL · LONDON · 1928", title="THE CONTAMINATED DISH", body="A mold, a ring, and a paper that was largely ignored.",
     source="SOURCES: AAI · PBS NEWSHOUR", stamp="1928")], dict(kind="slow")),
 ("It took a team in Oxford, a lab in Peoria, a cantaloupe, and twenty-one companies to turn it into a medicine. In time for D-Day.",
  [C("emb_harbor", 22.0), C("emb_march", 15.9)], dict(tag=EMB, kind="slow")),
 ("Today, penicillin and the antibiotics that followed are so ordinary that it's easy to forget the world before them.",
  [C(876964, 1091.0)], dict(tag=WRL, kind="slow")),
 ("And the man who noticed it first used his Nobel lecture to warn that it could stop working.",
  [C("pen_plant", 32.2)], dict(tag=NR1, kind="slow", gap=0.6)),
 ("If this story surprised you, subscribe. There are more stories on this channel about how medicine keeps people alive.",
  [G("stat", a="SUBSCRIBE", b="REAL MEDICINE · REAL FOOTAGE", c="KEPT ALIVE")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · FIRST 010", stamp="PENICILLIN")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("nineteen twenty-eight", "1928"), ("nineteen twenty-nine", "1929"), ("nineteen thirty-eight", "1938"), ("May twenty-fifth, nineteen forty", "May 25, 1940"),
 ("nineteen forty-one", "1941"), ("nineteen forty-two", "1942"), ("nineteen forty-three", "1943"), ("nineteen forty-four", "1944"), ("nineteen forty-five", "1945"),
 ("nineteen ninety", "1990"), ("nineteen forty", "1940"), ("twenty twenty-five", "2025"), ("July fourteenth", "July 14"), ("March first", "March 1"),
 ("June sixth", "June 6"), ("December eleventh", "December 11"), ("November eighteenth to twenty-fourth", "November 18 to 24"),
 ("two point three million", "2.3 million"), ("two point eight million", "2.8 million"), ("thirty-five thousand", "35,000"), ("two thousand liters", "2,000 liters"),
 ("seventy-five hundred gallons", "7,500 gallons"), ("four hundred million", "400 million"), ("six hundred fifty billion", "650 billion"),
 ("eighteen percent", "18%"), ("less than one percent", "less than 1%"), ("twenty-one", "21"), ("twenty dollars", "$20"), ("fifty-five cents", "55 cents"),
 ("Q one seventy-six", "Q-176"), ("Sixteen years", "16 years"), ("twelve years", "12 years"), ("Ten years", "10 years"), ("one in three", "1 in 3"), ("one in six", "1 in 6"),
 ("U.S.D.A.", "USDA"), ("C.D.C.", "CDC"), ("A.M.R.", "AMR"), ("fourteen tanks", "14 tanks"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · FIRST",
    title="Penicillin",
    voice="am_fenrir",
    imgs={},
    mute_nat=["pen_plant", "pen_lab", "emb_quay", "emb_harbor", "emb_march", "land_lcvp", "land_beach", "norm_hosp", "876964", "876974", "811325"],
    training=[],
    credit=("Archival film (public domain, National Archives via Internet Archive): United News newsreels, 1944; U.S. Coast Guard, U.S. Navy and U.S. Army films, 1944."
            r"\NFootage: Walter Reed Army Institute of Research; Naval Medical Center San Diego via DVIDS (public domain)."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, NIH, CDC or WHO."
            r"\NFor education only. This is not medical advice."),
)

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))  # longest first
