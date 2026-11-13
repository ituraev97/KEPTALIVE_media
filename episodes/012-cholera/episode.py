# KEPT ALIVE · OUTBREAK 012 — How One Doctor Traced a Deadly Cholera Outbreak to a Single Pump
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  map_* / snow_title / table9 = 20 s push-ins of John Snow, "On the Mode of Communication of Cholera", 2nd ed., London 1855
#             (Wellcome Collection scan b28985266 via Internet Archive, Public Domain Mark): Map 1 (Broad Street deaths), Map 2 (south London water companies), title page, Table IX (p. 86).
#  purif_* = excerpts of U.S. War Department training film "Purification of Water" (T.F. 8-1174, Signal Corps, 1943; NLM HF 1862, via Internet Archive, public domain).
#             Always tagged as a 1943 Army film; never presented as 1854 London or as Vibrio cholerae.
#  1020953 = 2ID Sustainment Brigade Tactical Water Purification System field training, Imjin River, South Korea, Aug. 2026 (DVIDS, Spc. Mark Bowman) — TRAINING
#  1000130 = U.S./ROK water and fuel purification demonstration, Freedom Shield, South Korea, March 2026 (DVIDS, Jaeyoon Lee) — TRAINING (exercise)
#  702231 = Task Force Medical preventive medicine soldiers test water for potability, Kosovo, Aug. 2019 (DVIDS, Sgt. Patrick Kirby)
#  653659 / 654823 = JTF-Bravo preventive medicine specialists test community water sources, Colon, Honduras, Dec. 2018 (DVIDS, Maria Pinel) — medical readiness training exercise -> TRAINING
#  1021069 = Puerto Rico National Guard water purification and distribution during drought, Canovanas, Aug. 2026 (DVIDS, Sgt. 1st Class Josue Rivera)
#  671211 = CJTF-HOA Cyclone Idai relief / DoD effort against the spread of cholera, Mozambique, April 2019 (DVIDS, Tech. Sgt. Tommy Grimes) — logistics shots only
#  1002024 = Army Public Health / Preventive Medicine "Clinic Notes" B-roll, SHAPE, Belgium, March 2026 (DVIDS, Senior Airman Christina Carter) — epidemic-curve screens and water-sample meter only
#  No patient is named (the 1854 index case and the Hampstead widow stay anonymous). No patients, bodies or illness on screen.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "OUTBREAK · 012"
S = "<span style=\"color:#2BB3A3\">{}</span>"
MAP1 = ("JOHN SNOW'S MAP OF CHOLERA DEATHS AROUND BROAD STREET", "LONDON 1854 · PUBLISHED 1855 · WELLCOME COLLECTION")
MAP2 = ("SNOW'S MAP OF SOUTH LONDON'S TWO WATER COMPANIES", "BLUE: SOUTHWARK & VAUXHALL · RED: LAMBETH · PURPLE: BOTH · 1855")
BOOK = ("ON THE MODE OF COMMUNICATION OF CHOLERA", "JOHN SNOW · SECOND EDITION · LONDON, 1855")
TAB9 = ("SNOW'S TABLE IX: CHOLERA DEATHS BY WATER COMPANY", "ON THE MODE OF COMMUNICATION OF CHOLERA · 1855")
FILM = ("U.S. ARMY TRAINING FILM \"PURIFICATION OF WATER\"", "ARCHIVAL FILM · 1943 · WAR DEPARTMENT · NATIONAL LIBRARY OF MEDICINE")
KOR = ("SOLDIERS PURIFY WATER FROM THE IMJIN RIVER", "SOUTH KOREA · AUGUST 2026 · 2ND INFANTRY DIVISION · TRAINING")
FSH = ("U.S. AND SOUTH KOREAN SOLDIERS DEMONSTRATE WATER PURIFICATION", "FREEDOM SHIELD EXERCISE · SOUTH KOREA · MARCH 2026")
KOS = ("ARMY PREVENTIVE MEDICINE SOLDIERS TEST DRINKING WATER", "KOSOVO · AUGUST 2019")
HON = ("ARMY PREVENTIVE MEDICINE SPECIALISTS TEST COMMUNITY WATER", "COLON, HONDURAS · DECEMBER 2018 · READINESS EXERCISE")
PRG = ("NATIONAL GUARD SOLDIERS PURIFY WATER DURING A DROUGHT", "CANOVANAS, PUERTO RICO · AUGUST 2026")
MOZ = ("U.S. MILITARY RELIEF FLIGHTS AFTER CYCLONE IDAI", "MOZAMBIQUE · APRIL 2019")
BEL = ("AN ARMY PUBLIC HEALTH TEAM CHARTS EPIDEMIC CURVES", "SHAPE, BELGIUM · MARCH 2026")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("In ten days in eighteen fifty-four, more than five hundred people died of cholera in a few streets of London.",
  [C("map_wide", 1.0)], dict(tag=MAP1, kind="punch")),
 ("Almost all of them lived within about two hundred fifty yards of one thing. A water pump.",
  [G("stat", a="500+", b="CHOLERA DEATHS IN 10 DAYS, WITHIN ABOUT 250 YARDS OF ONE PUMP", c="SOHO, LONDON · 1854 · SOURCE: JOHN SNOW, 1855")], dict(kind="tense")),
 ("Most doctors of the day blamed bad air. One doctor blamed the water. And he went house by house to prove it.",
  [C("map_pump", 1.0)], dict(tag=MAP1, kind="drive")),
 ("The famous version of this story says a map stopped the outbreak. The real story is better.",
  [C("map_soho", 2.0)], dict(tag=MAP1, kind="question", gap=0.4)),
 ("This is how John Snow traced a deadly cholera outbreak to a single pump.",
  [G("title", kicker=CASE, title="CHOLERA", sub="ONE DOCTOR · ONE " + S.format("PUMP"), size=230)], dict(kind="slow", gap=2.4)),

 # ---------------- I. A NEW KILLER ----------------
 ("Start with the disease.",
  [G("chapter", case="1817–1849", n="I", t="A NEW KILLER")], dict(gap=1.0, kind="calm")),
 ("Cholera is caused by a bacterium, Vibbree-oh kollerie. The World Health Organization says it spreads through food or water contaminated with it.",
  [G("doc", header="WORLD HEALTH ORGANIZATION · CHOLERA FACT SHEET · 2026", title="VIBRIO CHOLERAE", body="Infection comes from food or water contaminated with the bacterium. Most people infected do not develop symptoms.",
     source="SOURCE: WHO")], dict(kind="calm")),
 ("For most of history, nobody knew that. A cholera epidemic began in India in eighteen seventeen. It reached Britain in eighteen thirty-one, and that first epidemic killed around thirty thousand people.",
  [G("timeline", kicker="CHOLERA SPREADS", title="FROM INDIA TO LONDON",
     events=[dict(y="1817", t="Epidemic begins in India"), dict(y="1831", t="Reaches Britain"), dict(y="1832", t="About 30,000 dead in Britain"), dict(y="1832", t="Reaches New York")],
     footer="SOURCES: LONDON MUSEUM · HISTORY NEWS NETWORK")], dict(kind="drive")),
 ("In eighteen thirty-two, it reached New York. A city of more than two hundred thousand people. About half of them fled. Three thousand five hundred thirteen died.",
  [G("stat", a="3,513", b="CHOLERA DEATHS IN NEW YORK CITY, SUMMER 1832", c="ABOUT HALF THE CITY FLED · SOURCE: DANIEL S. LEVY, HISTORY NEWS NETWORK")], dict(kind="tense")),
 ("What caused it? The leading theory was miasma. Disease, doctors believed, came from breathing foul air: the stink of filth and rot.",
  [G("doc", header="MEDICAL CONSENSUS · 1850s", title="MIASMA", body="The belief that disease spread by breathing dirty, foul-smelling air.", source="SOURCE: LONDON MUSEUM", stamp="WRONG")], dict(kind="calm")),
 ("A London doctor named John Snow did not believe it. Snow was a pioneer of anesthesia. In the eighteen fifties, he gave chloroform to Queen Victoria during the births of two of her children.",
  [C("snow_title", 1.0)], dict(tag=BOOK, kind="calm")),
 ("In eighteen forty-nine, during another London epidemic, Snow published his theory that cholera spread through water. It was mostly ignored.",
  [G("doc", header="LONDON · 1849", title="ON THE MODE OF COMMUNICATION OF CHOLERA", tsize=72, body="John Snow argues that cholera is spread through water. Few doctors accept it.",
     source="SOURCE: LONDON MUSEUM", stamp="IGNORED")], dict(kind="calm", gap=0.5)),

 # ---------------- II. BROAD STREET ----------------
 ("Five years later, he got a test he never wanted.",
  [G("chapter", case="AUG. 31 – SEPT. 8, 1854", n="II", t="BROAD STREET")], dict(gap=1.0, kind="calm")),
 ("On the night of August thirty-first, eighteen fifty-four, cholera exploded in Soho, a crowded neighborhood in central London.",
  [C("map_wide", 6.0)], dict(tag=MAP1, kind="tense")),
 ("Snow later called it, probably, the most terrible outbreak of cholera ever to occur in the kingdom.",
  [G("quote", q="The most terrible outbreak of cholera which ever occurred in this kingdom, is probably that which took place in Broad Street, Golden Square…", w="JOHN SNOW · ON THE MODE OF COMMUNICATION OF CHOLERA · 1855")], dict(kind="slow")),
 ("On September first alone, one hundred forty-three people were struck. Within six days, the worst-hit streets had lost more than three quarters of their residents.",
  [G("stat", a="143", b="NEW CHOLERA CASES ON SEPTEMBER 1, 1854 — THE WORST DAY", c="SOURCES: JOHN SNOW, 1855 · UCLA JOHN SNOW ARCHIVE")], dict(kind="tense")),
 ("Snow suspected the water right away, and the pump on Broad Street. When he first looked at its water, it seemed almost clear. Over the next two days, he saw small white particles in it.",
  [C("map_pump", 3.0)], dict(tag=MAP1, kind="calm")),
 ("Clear-looking water can still carry germs. A nineteen forty-three Army training film made the same point under a microscope: water that looks clean can be, quote, alive with all sorts of living matter.",
  [C("purif_micro", 1.0)], dict(tag=FILM, kind="calm")),
 ("So Snow got the list of cholera deaths from the General Register Office. Eighty-three deaths in the last three days of that week. Then he went house by house.",
  [G("steps", kicker="JOHN SNOW'S INVESTIGATION · SEPTEMBER 1854", title="FOLLOW THE WATER", items=[["THE LIST", "83 deaths, Aug. 31 – Sept. 2"], ["THE STREETS", "Where each person lived"], ["THE QUESTION", "Where did they get water?"], ["THE ANSWER", "Nearly all near one pump"]],
     footer="SOURCE: JOHN SNOW, 1855")], dict(kind="drive")),
 ("Nearly all the deaths had happened a short distance from the pump. Only ten were in houses clearly nearer another pump. In five of those, the families told him they always sent for water from Broad Street. They preferred it. Three more were children who went to school near the pump.",
  [C("map_pump", 8.0), G("cards3", kicker="THE 10 DEATHS CLOSER TO OTHER PUMPS", title="THE EXCEPTIONS FIT TOO", cards=[dict(h="5", t="Families sent to Broad Street for water"), dict(h="3", t="Children at school near the pump"), dict(h="2", t="Deaths already occurring before the outbreak")],
     footer="SOURCE: JOHN SNOW, 1855")], dict(tag=MAP1, kind="calm")),
 ("Then he looked at the people who did not get sick.",
  [C("map_soho", 6.0)], dict(tag=MAP1, kind="question")),
 ("The workhouse on Poland Street held five hundred thirty-five people. It was almost surrounded by houses where people died of cholera. Only five of its inmates died. The workhouse had its own well.",
  [C("map_work", 1.0), G("phases", kicker="POLAND STREET WORKHOUSE · 1854", title="ITS OWN WELL", left=dict(label="INMATES", num="535", desc="PEOPLE"),
     right=dict(label="CHOLERA DEATHS", num="5", desc="INMATES"), active=1, footer="SOURCE: JOHN SNOW, 1855")], dict(tag=MAP1, kind="calm")),
 ("A brewery on Broad Street, near the pump, had more than seventy workmen. None of them had cholera, at least in a severe form. The owner told Snow his men drank malt liquor, not water. And the brewery had a deep well of its own.",
  [C("map_brew", 1.0), G("stat", a="0", b="SEVERE CHOLERA CASES AMONG 70+ BREWERY WORKERS", c="THEY DRANK MALT LIQUOR · THE BREWERY HAD ITS OWN WELL · SOURCE: JOHN SNOW, 1855")], dict(tag=MAP1, kind="drive")),
 ("And a case far away fit too. In Hampstead, a widow who had not been near Broad Street for months had a large bottle of its water brought to her every day, because she preferred it. She died of cholera. So did a niece who visited her and drank the water. At the time, there was no cholera in either of their neighborhoods.",
  [G("doc", header="WEEKLY RETURN OF BIRTHS AND DEATHS · SEPT. 9, 1854", title="THE HAMPSTEAD CASE", body="A widow who had not been near Broad Street for months drank its water, brought out by cart. She and a visiting niece died of cholera.",
     source="SOURCE: JOHN SNOW, 1855", stamp="BROAD ST. WATER")], dict(kind="slow")),
 ("On the evening of Thursday, September seventh, Snow presented his evidence to the parish Board of Guardians.",
  [C("map_pump", 12.0)], dict(tag=MAP1, kind="calm")),
 ("Snow wrote what happened next.",
  [G("quote", q="In consequence of what I said, the handle of the pump was removed on the following day.", w="JOHN SNOW · ON THE MODE OF COMMUNICATION OF CHOLERA · 1855")], dict(kind="slow", gap=0.6)),

 # ---------------- III. THE REAL STORY ----------------
 ("That's where the famous version ends. Snow drew a map, the handle came off, and the outbreak stopped. Almost every part of that is more complicated.",
  [G("chapter", case="1854–1855", n="III", t="THE REAL STORY")], dict(gap=1.0, kind="calm")),
 ("First, the map came later. Snow first showed a map of the deaths in December eighteen fifty-four. It appeared in his book in eighteen fifty-five. His suspicion of the pump came first.",
  [C("map_wide", 11.0)], dict(tag=MAP1, kind="calm")),
 ("On the map, each black bar is a death at that address. You can see them stacked around the pump on Broad Street.",
  [C("map_pump", 5.0)], dict(tag=MAP1, kind="slow")),
 ("Second, the outbreak was already fading. Snow said so himself. New cases had fallen from one hundred forty-three on September first to twelve on the eighth, the day the handle was removed.",
  [G("phases", kicker="NEW CHOLERA CASES PER DAY · 1854", title="ALREADY FALLING", left=dict(label="SEPTEMBER 1", num="143", desc="NEW CASES"),
     right=dict(label="SEPTEMBER 8 · HANDLE REMOVED", num="12", desc="NEW CASES"), active=1, footer="SOURCE: JOHN SNOW, 1855")], dict(kind="drive")),
 ("Many people had fled. Snow wrote that cases had dropped so far before the water was stopped that it was impossible to decide whether the well still carried the disease.",
  [C("map_soho", 10.0)], dict(tag=MAP1, kind="calm")),
 ("And most experts were not convinced. A government Board of Health report dismissed his theory.",
  [G("doc", header="GENERAL BOARD OF HEALTH · 1855", title="THEORY REJECTED", body="An official report dismisses Snow's idea that the Broad Street water caused the outbreak.",
     source="SOURCE: UCLA JOHN SNOW ARCHIVE", stamp="DISMISSED")], dict(kind="calm")),
 ("The strongest support came from a man who expected to prove Snow wrong. The Reverend Henry Whitehead, a local clergyman.",
  [G("doc", header="ST. LUKE'S, BERWICK STREET · 1855", title="REV. HENRY WHITEHEAD", body="A local clergyman who expected a careful investigation to disprove Snow. He interviewed residents, some households four or five times.",
     source="SOURCE: UCLA JOHN SNOW ARCHIVE")], dict(kind="calm")),
 ("In the spring of eighteen fifty-five, Whitehead found what was likely the first case: a five-month-old baby at forty Broad Street, right beside the pump, who died on September second.",
  [C("map_pump", 15.0)], dict(tag=MAP1, kind="slow")),
 ("The baby's mother had soaked the soiled diapers in water and emptied it into the cesspool in front of the house.",
  [G("steps", kicker="40 BROAD STREET · 1854", title="HOW THE WELL WAS POISONED", items=[["THE HOUSE", "Next to the pump"], ["THE CESSPOOL", "Waste emptied out front"], ["THE BRICKS", "Decayed, leaking"], ["THE WELL", "Under 3 feet away"]],
     footer="SOURCE: UCLA JOHN SNOW ARCHIVE · 1855 SURVEYOR'S REPORT")], dict(kind="calm")),
 ("When the surveyor dug it out, the cesspool was two feet eight inches from the well. Its decayed brickwork let waste seep into the drinking water.",
  [G("stat", a="2 FT 8 IN", b="FROM THE CESSPOOL TO THE WELL", c="SURVEYOR'S REPORT, MAY 1, 1855 · SOURCE: UCLA JOHN SNOW ARCHIVE")], dict(kind="tense")),
 ("Whitehead admitted he had come, slowly and, as he put it, reluctantly, to link the pump water to the outbreak.",
  [G("quote", q="Slowly and I may add reluctantly…", w="REV. HENRY WHITEHEAD · REPORT, JUNE 1855 · VIA UCLA JOHN SNOW ARCHIVE")], dict(kind="slow")),
 ("In August eighteen fifty-five, the parish committee concluded the outbreak was, in some manner, attributable to the use of the impure water of the well on Broad Street. The vote was split evenly. The chairman cast the deciding vote.",
  [G("doc", header="ST. JAMES'S PARISH · AUGUST 9, 1855", title="\"ATTRIBUTABLE TO THE USE OF THE IMPURE WATER\"", tsize=78, body="The committee's vote is split evenly. The chairman casts the deciding vote.",
     source="SOURCE: UCLA JOHN SNOW ARCHIVE", stamp="1 VOTE")], dict(kind="calm", gap=0.5)),

 # ---------------- IV. THE EXPERIMENT ----------------
 ("Snow had a second piece of evidence. And it covered three hundred thousand people.",
  [G("chapter", case="SOUTH LONDON · 1854", n="IV", t="THE EXPERIMENT")], dict(gap=1.0, kind="calm")),
 ("In south London, two water companies ran their pipes down the same streets. In eighteen fifty-two, the Lambeth Company moved its intake up the Thames, to Thames Ditton, getting water free of London's sewage. The Suthuck and Vauxhall Company still drew from the Thames at Battersea.",
  [C("map_south", 1.0)], dict(tag=MAP2, kind="calm")),
 ("Each company supplied rich and poor, large houses and small. Snow saw no difference between the two groups except the water.",
  [C("map_south", 8.0)], dict(tag=MAP2, kind="calm")),
 ("He called it an experiment on the grandest scale.",
  [G("quote", q="No fewer than three hundred thousand people … were divided into two groups without their choice, and, in most cases, without their knowledge.", w="JOHN SNOW · 1855")], dict(kind="slow")),
 ("Then he counted. In the first seven weeks of the eighteen fifty-four epidemic, houses supplied by Suthuck and Vauxhall had three hundred fifteen cholera deaths per ten thousand houses. Houses supplied by Lambeth had thirty-seven.",
  [G("phases", kicker="CHOLERA DEATHS PER 10,000 HOUSES · FIRST 7 WEEKS, 1854", title="SAME CITY, DIFFERENT WATER", left=dict(label="SOUTHWARK & VAUXHALL", num="315", desc="SEWAGE-TAINTED THAMES WATER"),
     right=dict(label="LAMBETH", num="37", desc="WATER FROM UPRIVER"), active=0, footer="SOURCE: JOHN SNOW, 1855, TABLE IX")], dict(kind="drive")),
 ("Snow concluded that the death rate was between eight and nine times higher with the dirtier water.",
  [C("table9", 1.0)], dict(tag=TAB9, kind="slow", gap=0.5)),

 # ---------------- V. THE GERM ----------------
 ("But Snow never saw the germ itself.",
  [G("chapter", case="1854–1884", n="V", t="THE GERM")], dict(gap=1.0, kind="calm")),
 ("Someone else already had. In eighteen fifty-four, the Italian anatomist Filippo Pa-cheeny saw and described the cholera pathogen under a microscope.",
  [G("doc", header="1854", title="FILIPPO PACINI", body="Sees and describes the cholera pathogen under a microscope.", source="SOURCE: ROBERT KOCH INSTITUTE", stamp="1854")], dict(kind="calm")),
 ("Then, at the end of eighteen eighty-three, the German scientist Robert Kohk traveled to Calcutta, India, during an outbreak. At the beginning of eighteen eighty-four, he identified the bacterium.",
  [G("timeline", kicker="FINDING THE GERM", title="30 YEARS LATER",
     events=[dict(y="1854", t="Pacini sees it"), dict(y="1855", t="Snow's book"), dict(y="1883", t="Koch in Calcutta"), dict(y="1884", t="Koch identifies it")],
     footer="SOURCES: ROBERT KOCH INSTITUTE · JOHN SNOW, 1855")], dict(kind="drive")),
 ("John Snow did not live to see it. He died in June eighteen fifty-eight, at forty-five.",
  [C("snow_title", 9.0)], dict(tag=BOOK, kind="slow")),
 ("That summer, London had what became known as the Great Stink: hot weather and sewage exposed in the Thames. It pushed the city to build a modern sewer system, overseen by the engineer Joseph Bazzle-jet.",
  [G("doc", header="LONDON · SUMMER 1858", title="THE GREAT STINK", body="Hot weather exposes sewage in the River Thames. London begins a modern sewer system under engineer Joseph Bazalgette.",
     source="SOURCE: LONDON MUSEUM", stamp="1858")], dict(kind="calm")),
 ("London's final cholera outbreak came in eighteen sixty-six. It hit parts of east London that drew water from the Old Ford Reservoir, and were not connected to the new sewers.",
  [G("doc", header="EAST LONDON · 1866", title="THE LAST LONDON OUTBREAK", body="Areas supplied from the Old Ford Reservoir, not yet connected to Bazalgette's new sewers.", source="SOURCE: LONDON MUSEUM", stamp="1866")], dict(kind="calm", gap=0.5)),

 # ---------------- VI. WATER FIRST ----------------
 ("In America, the lesson became chlorine.",
  [G("chapter", case="1908–TODAY", n="VI", t="WATER FIRST")], dict(gap=1.0, kind="calm")),
 ("In nineteen oh eight, Jersey City, New Jersey, became the first U.S. city to begin routine disinfection of its drinking water. Thousands of cities and towns followed over the next decade.",
  [G("stat", a="&#8203;1908", b="JERSEY CITY BEGINS ROUTINE DISINFECTION OF DRINKING WATER", c="THE FIRST U.S. CITY · SOURCE: CDC")], dict(kind="drive")),
 ("The CDC says diseases like cholera and typhoid dropped dramatically. Typhoid fever went from about one hundred cases per hundred thousand people in nineteen hundred, to zero point one in two thousand six.",
  [G("phases", kicker="TYPHOID FEVER IN THE UNITED STATES · CASES PER 100,000", title="WHAT CLEAN WATER DID", left=dict(label="1900", num="~100", desc="CASES PER 100,000"),
     right=dict(label="2006", num="0.1", desc="CASES PER 100,000"), active=1, footer="CREDITED TO WATER TREATMENT, CLEANER SOURCES AND SANITATION · SOURCE: CDC")], dict(kind="calm")),
 ("Cities cleaned their water by aerating, settling, filtering and chlorinating it. That's how the Army explained it to soldiers in nineteen forty-three.",
  [C("purif_plant", 0.5), C("purif_plant", 6.6)], dict(tag=FILM, kind="calm")),
 ("Because in the field, there was no city water plant. So soldiers hung a canvas bag from a tripod. It held thirty-six gallons.",
  [C("purif_bag", 3.0), C("purif_bag", 23.0)], dict(tag=FILM, kind="calm")),
 ("They treated the water with chlorine, then tested a sample to check there was enough. The film says it took thirty minutes for the chemicals to kill germs.",
  [C("purif_test", 2.0), C("purif_bag2", 2.0)], dict(tag=FILM, kind="drive")),
 ("Today, Army units still train to make their own drinking water. In August twenty twenty-six, during field training in South Korea, soldiers pumped water from the Imjin River, tested it and purified it with a Tactical Water Purification System.",
  [C(1020953, 8.5), C(1020953, 41.0)], dict(tag=KOR, kind="calm")),
 ("Preventive medicine soldiers test the water troops drink. In Kosovo, they tested water at liaison team houses to make sure it was safe to drink.",
  [C(702231, 17.0), C(702231, 45.0)], dict(tag=KOS, kind="calm")),
 ("And sometimes the water goes to civilians. During a drought in Puerto Rico in twenty twenty-six, National Guard soldiers purified and delivered drinking water. More than a million gallons distributed so far.",
  [C(1021069, 37.0), C(1021069, 66.0)], dict(tag=PRG, kind="drive", gap=0.5)),

 # ---------------- WHAT CHANGED ----------------
 ("Today, the CDC says cholera is rare in the United States. With modern water and sewer treatment systems, there are typically fewer than twenty U.S. cases a year, mostly linked to travel.",
  [G("stat", a="&lt;20", b="U.S. CHOLERA CASES IN A TYPICAL YEAR", c="MOSTLY LINKED TO TRAVEL · SOURCE: CDC")], dict(kind="calm")),
 ("But the disease is not history. Researchers cited by the World Health Organization estimate one point three to four million cases a year worldwide, and twenty-one thousand to one hundred forty-three thousand deaths.",
  [G("phases", kicker="CHOLERA WORLDWIDE · ESTIMATED PER YEAR · CITED BY WHO", title="STILL HERE", left=dict(label="CASES", num="1.3–4M", desc="ESTIMATED"),
     right=dict(label="DEATHS", num="21–143K", desc="ESTIMATED"), footer="SOURCE: WHO FACT SHEET, 2026")], dict(kind="tense")),
 ("In twenty twenty-five, forty-seven countries reported cases to the WHO, and the reported death toll was the highest since nineteen ninety-nine.",
  [G("stat", a="47", b="COUNTRIES REPORTED CHOLERA IN 2025", c="REPORTED DEATHS: HIGHEST SINCE 1999 · SOURCE: WHO")], dict(kind="tense")),
 ("In twenty nineteen, after Cyclone Ee-dye hit Mozambique, the Defense Department took part in the effort to stop cholera from spreading, moving relief for the U.S. Agency for International Development.",
  [C(671211, 37.0), C(671211, 57.0)], dict(tag=MOZ, kind="calm")),
 ("The WHO says safe water, basic sanitation and hygiene are essential to prevent cholera. John Snow pointed to the water first.",
  [C(1021069, 188.0)], dict(tag=PRG, kind="slow")),
 ("In eighteen fifty-four, a doctor counted deaths, asked where each family got its water, and followed the evidence to a pump.",
  [C("map_pump", 2.0)], dict(tag=MAP1, kind="slow")),
 ("Public health teams still count cases and chart them over time, to see when an outbreak started and whether it is growing or fading.",
  [C(1002024, 218.0), C(1002024, 225.75)], dict(tag=BEL, kind="slow")),
 ("Next on KEPT ALIVE: more stories about how medicine keeps people alive. Subscribe so you don't miss them.",
  [G("stat", a="SUBSCRIBE", b="REAL MEDICINE · REAL FOOTAGE", c="KEPT ALIVE")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · OUTBREAK 012", stamp="CHOLERA")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("eighteen fifty-four", "1854"), ("eighteen fifty-five", "1855"), ("eighteen fifty-eight", "1858"), ("eighteen fifty-two", "1852"),
 ("eighteen fifties", "1850s"), ("eighteen forty-nine", "1849"), ("eighteen seventeen", "1817"), ("eighteen thirty-one", "1831"), ("eighteen thirty-two", "1832"),
 ("eighteen sixty-six", "1866"), ("eighteen eighty-three", "1883"), ("eighteen eighty-four", "1884"), ("nineteen oh eight", "1908"), ("nineteen hundred", "1900"),
 ("nineteen forty-three", "1943"), ("nineteen ninety-nine", "1999"), ("two thousand six", "2006"), ("twenty twenty-six", "2026"), ("twenty twenty-five", "2025"),
 ("twenty nineteen", "2019"), ("five hundred", "500"), ("two hundred fifty yards", "250 yards"), ("thirty thousand", "30,000"), ("two hundred thousand", "200,000"),
 ("Three thousand five hundred thirteen", "3,513"), ("one hundred forty-three thousand", "143,000"), ("one hundred forty-three", "143"), ("three quarters", "three-quarters"),
 ("Eighty-three", "83"), ("five hundred thirty-five", "535"), ("seventy", "70"), ("August thirty-first", "August 31"), ("September first", "September 1"),
 ("September seventh", "September 7"), ("September second", "September 2"), ("forty Broad Street", "40 Broad Street"), ("two feet eight inches", "2 feet 8 inches"),
 ("three hundred thousand", "300,000"), ("three hundred fifteen", "315"), ("ten thousand", "10,000"), ("thirty-seven", "37"), ("one hundred cases per hundred thousand", "100 cases per 100,000"),
 ("zero point one", "0.1"), ("thirty-six gallons", "36 gallons"), ("thirty minutes", "30 minutes"), ("fewer than twenty", "fewer than 20"),
 ("one point three to four million", "1.3 to 4 million"), ("twenty-one thousand", "21,000"), ("forty-seven", "47"), ("five-month-old", "5-month-old"),
 ("Vibbree-oh kollerie", "Vibrio cholerae"), ("Suthuck", "Southwark"), ("Pa-cheeny", "Pacini"), ("Kohk", "Koch"), ("Bazzle-jet", "Bazalgette"), ("Ee-dye", "Idai"),
 ("at forty-five", "at 45"), ("on the eighth", "on the 8th"), ("to twelve", "to 12"), ("Only ten", "Only 10"), ("In five of those", "In 5 of those"), ("Three more", "3 more"),
 ("Only five", "Only 5"), ("a million gallons", "a million gallons"), ("first seven weeks", "first 7 weeks"), ("ten days", "10 days"), ("two days", "2 days"),
 ("three days", "3 days"), ("Five years", "Five years"), ("eight and nine times", "8 and 9 times"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · OUTBREAK",
    title="Cholera",
    voice="am_fenrir",
    imgs={},
    mute_nat=["map_wide", "map_soho", "map_pump", "map_brew", "map_work", "map_south", "snow_title", "table9",
              "purif_micro", "purif_plant", "purif_bag", "purif_test", "purif_bag2", "purif_title",
              "1020953", "1000130", "702231", "653659", "654823", "1021069", "671211", "1002024"],
    training=["1020953", "1000130", "653659", "654823"],
    credit=("Illustrations: John Snow, On the Mode of Communication of Cholera, 2nd ed., London 1855 (Wellcome Collection, public domain)."
            r"\NArchival film (public domain): U.S. War Department training film \"Purification of Water\", 1943 (National Library of Medicine)."
            r"\NFootage: U.S. Department of Defense via DVIDS (public domain). Training footage is marked TRAINING."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, CDC, WHO or any government agency."
            r"\NFor education only. This is not medical advice."),
)

DISPLAY = sorted(DISPLAY, key=lambda x: -len(x[0]))  # longest first
