# KEPT ALIVE · FIRST 004 — The Iron Lung and the End of Polio
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts)
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  ilung1945 = U.S. Army Signal Corps reel "Iron Lung Evacuation, 60th General Hospital, Manila" (1945, NARA 111-ADC-5218, CC0).
#              The film does not state the patient's diagnosis -> never called a polio patient. Close-ups of patients NOT used.
#  unc1956   = "Unconditional Surrender" (1956), National Foundation for Infantile Paralysis film, public domain (Prelinger).
#              Lab scenes are vaccine production/testing in general -> never tied to Cutter Laboratories.
#  bab1961   = "Babies and Breadwinners" (1961), Communicable Disease Center film of the 1961 Columbus, Ga. campaign, public domain.
#  kan1957   = Universal Newsreel 1957 (Salk vaccine being administered), public domain.
#  dimes1944 = Universal Newsreel "Thanks for the Dimes" (Feb. 28, 1944), public domain. Child not named.
#  fdr1930   = FDR Presidential Library film "FDR at Warm Springs" (1928–1939), CC0.
#  999485 / 861320 = modern TRAINING (ventilator training, Tanzania 2026; mannequin bag ventilation, BAMC 2022).
#  997537 = U.S. Naval Hospital Guam ICU virtual tour (empty rooms, 2026). 813274 = Navy immunization site, Operation Allies Welcome, 2021.
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
CASE = "FIRST · 004"
S = "<span style=\"color:#2BB3A3\">{}</span>"
WORLD = [[-120, -15], [120, 62]]
COPEN = [12.57, 55.68]; AFG = [67.7, 33.9]; PAK = [69.3, 30.4]; BOSTON = [-71.06, 42.36]

LINES = [
 # ---------------- COLD OPEN ----------------
 ("Nineteen forty-five. Manila, in the Philippines. A U.S. Army film crew records a patient being moved out of a military hospital.",
  [C("ilung1945", 17.0), C("ilung1945", 64.5)], dict(tag=("ARCHIVAL FILM · 1945 · U.S. ARMY SIGNAL CORPS", "\"IRON LUNG EVACUATION\" · 60TH GENERAL HOSPITAL, MANILA"), kind="calm")),
 ("The patient isn't on a stretcher. The patient is inside a machine. A steel tank, loaded onto a plane.",
  [C("ilung1945", 93.0), C("ilung1945", 106.0)], dict(kind="tense")),
 ("It was called an iron lung. And it did one job. It breathed for people who could not.",
  [C("ilung1945", 121.0)], dict(kind="punch", gap=0.7)),
 ("For decades, the disease that filled these machines came back every summer. It was called infantile paralysis. Polio.",
  [C("unc1956", 49.0), C("unc1956", 101.0)], dict(tag=("ARCHIVAL FILM · 1956", "\"UNCONDITIONAL SURRENDER\" · NATIONAL FOUNDATION FOR INFANTILE PARALYSIS"), kind="slow")),
 ("Then, in about twenty-five years, America stopped wild polio from spreading. This is how.",
  [C("unc1956", 811.0)], dict(kind="question", gap=0.6)),
 ("The iron lung, and the end of polio in America.",
  [G("title", kicker=CASE, title="The Iron " + S.format("Lung"), sub="AND THE END OF POLIO IN AMERICA", size=210)], dict(kind="slow", gap=2.6)),

 # ---------------- I. EVERY SUMMER ----------------
 ("Start with the virus.",
  [G("chapter", case="POLIO", n="I", t="EVERY SUMMER")], dict(kind="calm")),
 ("Polio is caused by a virus. According to the World Health Organization, it spreads mainly from person to person, through what's called the fecal-oral route.",
  [C("unc1956", 31.0), C("unc1956", 41.0)], dict(tag=("ARCHIVAL FILM · 1956", "NATIONAL FOUNDATION FOR INFANTILE PARALYSIS"), kind="calm")),
 ("Most infections cause no symptoms at all. The CDC says about seventy percent of polio infections in children are silent. But the World Health Organization says about one in two hundred infections leads to irreversible paralysis, usually in the legs.",
  [G("cards3", kicker="POLIO · WHAT ONE INFECTION CAN DO", title="MOSTLY SILENT. SOMETIMES DEVASTATING.",
     cards=[dict(h="~70%", t="of infections in children cause no symptoms", s="SOURCE: CDC"), dict(h="1 IN 200", t="infections leads to irreversible paralysis", s="USUALLY IN THE LEGS · WHO", size=96), dict(h="5–10%", t="of those paralysed die", s="WHEN BREATHING MUSCLES ARE IMMOBILIZED · WHO")],
     footer="SOURCES: CDC PINK BOOK, CH. 18 · WHO POLIOMYELITIS FACT SHEET")], dict(kind="calm")),
 ("And when the paralysis reached the muscles used for breathing, five to ten percent of those paralyzed died.",
  [C("unc1956", 102.5)], dict(kind="tense")),
 ("In the first half of the twentieth century, epidemics hit the developed countries of the Northern Hemisphere every summer and fall, and they kept getting worse. In the United States, paralytic polio peaked in nineteen fifty-two, with more than twenty-one thousand cases reported.",
  [G("stat", a="21,000+", b="PARALYTIC POLIO CASES REPORTED IN THE U.S. IN 1952", c="THE PEAK YEAR · SOURCE: CDC PINK BOOK, CH. 18")], dict(kind="tense")),
 ("In the late nineteen forties and early fifties, according to the CDC, polio crippled an average of more than thirty-five thousand people a year in the U.S.",
  [C("unc1956", 31.5), C("unc1956", 45.0)], dict(kind="slow")),
 ("Mass Humanities notes severe American epidemics in nineteen sixteen and in the nineteen thirties. The most devastating came in nineteen fifty-two.",
  [G("timeline", kicker="POLIO IN THE UNITED STATES", title="THE WORST SUMMERS",
     events=[dict(y="1916", t="Severe epidemic"), dict(y="LATE 1940S", t="35,000+ crippled a year, on average"), dict(y="1952", t="Peak: 21,000+ paralytic cases")], active=2,
     footer="SOURCES: MASS HUMANITIES · CDC")], dict(kind="calm", gap=0.8)),

 # ---------------- II. THE MACHINE ----------------
 ("For the patients who could no longer breathe, there was a machine.",
  [G("chapter", case="POLIO", n="II", t="THE MACHINE")], dict(kind="calm")),
 ("It was developed at Harvard by Philip Drinker and Louis Agassiz Shaw. According to Mass Humanities, the first one was little more than a galvanized iron box, a bed, and two household vacuum cleaners.",
  [G("callcard", kicker="HARVARD · 1928", title="THE DRINKER RESPIRATOR",
     rows=[["WHO", "PHILIP DRINKER AND LOUIS AGASSIZ SHAW"], ["BUILT FROM", "AN IRON BOX, A BED, TWO VACUUM CLEANERS"], ["FIRST USE", "OCT. 12, 1928 · CHILDREN'S HOSPITAL, BOSTON"]],
     footer="SOURCES: HARVARD MEDICAL SCHOOL · MASS HUMANITIES · BOSTON CHILDREN'S ARCHIVES")], dict(kind="calm")),
 ("On October twelfth, nineteen twenty-eight, it was used on a young girl, at Children's Hospital in Boston. It was the first successful use of a mechanical respirator there.",
  [G("map", map=dict(bounds=[[-80, 38], [-66, 46]], rings=[dict(ll=BOSTON, r=40, n=3, d=0.5)],
     cities=[dict(ll=BOSTON, name="BOSTON", sub="CHILDREN'S HOSPITAL · OCT. 12, 1928", d=0.3, color="#6CF29A", anchor="end")]),
     kicker="OCTOBER 12, 1928", title="THE FIRST PATIENT", footer="SOURCES: MASS HUMANITIES · BOSTON CHILDREN'S HOSPITAL ARCHIVES")], dict(kind="drive")),
 ("Here's how it worked. The patient lay inside the tank, with only the head outside, sealed off by an airtight collar.",
  [G("steps", kicker="HOW AN IRON LUNG BREATHES FOR YOU", title="NEGATIVE PRESSURE",
     items=[["Seal", "Body inside, head out, airtight collar"], ["Lower", "Pressure in the tank drops"], ["Inhale", "Chest expands, air flows in"], ["Exhale", "Pressure rises, air flows out"]], active=0,
     footer="SOURCES: HARVARD MEDICAL SCHOOL · KANSAS HISTORICAL SOCIETY")], dict(kind="calm")),
 ("When the pressure inside the tank dropped, the chest expanded, and air streamed into the lungs. When the pressure rose again, the air flowed out. Over and over, it did what the patient's own muscles could not.",
  [G("steps", kicker="HOW AN IRON LUNG BREATHES FOR YOU", title="NEGATIVE PRESSURE",
     items=[["Seal", "Body inside, head out, airtight collar"], ["Lower", "Pressure in the tank drops"], ["Inhale", "Chest expands, air flows in"], ["Exhale", "Pressure rises, air flows out"]], active=2,
     footer="SOURCES: HARVARD MEDICAL SCHOOL · KANSAS HISTORICAL SOCIETY")], dict(kind="drive")),
 ("In nineteen thirty-one, an improved version was completed by J. H. Emerson, of Cambridge, Massachusetts. A nineteen thirty-three account put its price at about a thousand dollars, half or less the cost of the other machine.",
  [G("phases", kicker="THE IRON LUNG GETS CHEAPER", title="DRINKER VS. EMERSON",
     left=dict(label="DRINKER RESPIRATOR", num="$2,000+", desc="$2,000 OR $2,300 IN A 1933 ACCOUNT"), right=dict(label="EMERSON RESPIRATOR · 1931", num="$1,000", desc="PRICE CITED IN A 1933 ACCOUNT"), active=1,
     footer="SOURCES: MASS HUMANITIES (MASS MOMENTS) · HARVARD MEDICAL SCHOOL")], dict(kind="calm")),
 ("Harvard Medical School says the Emerson model became the main iron lung used in hospitals across the country. Boston Children's had a room-sized one, in a hospital basement. It could hold five patients at once, and nurses could walk inside to care for them.",
  [G("cards3", kicker="THE IRON LUNG ERA", title="HOSPITALS BUILT AROUND A MACHINE",
     cards=[dict(h="1931", t="Emerson model completed", s="BECAME THE MAIN MODEL IN U.S. HOSPITALS"), dict(h="5", t="patients in one room-sized respirator", s="BOSTON CHILDREN'S · 1930S"), dict(h="1,200", t="people in the U.S. using tank respirators", s="IN 1959")],
     footer="SOURCES: HARVARD MEDICAL SCHOOL · BOSTON CHILDREN'S ARCHIVES · MASS HUMANITIES")], dict(kind="calm")),
 ("Iron lungs were meant to give temporary relief, until a patient recovered. But not everyone did. In nineteen fifty-nine, about twelve hundred people in the United States were still using tank respirators.",
  [C("ilung1945", 109.0)], dict(tag=("ARCHIVAL FILM · 1945 · U.S. ARMY SIGNAL CORPS", "IRON LUNG EVACUATION · MANILA"), kind="slow")),
 ("Caring for someone inside a tank was hard. Later machines, like a nineteen fifty-seven Emerson model described by the Kansas Historical Society, had a plastic dome that could go over the patient's head and take over the breathing, during bathing or other care.",
  [G("callcard", kicker="EMERSON RESPIRATOR · 1957", title="LIVING INSIDE THE MACHINE",
     rows=[["HEAD", "OUTSIDE, THROUGH A PLASTIC COLLAR"], ["FOR CARE", "A PLASTIC DOME TOOK OVER THE BREATHING"], ["PURPOSE", "TEMPORARY RELIEF UNTIL RECOVERY"]],
     footer="SOURCE: KANSAS HISTORICAL SOCIETY (KANSAPEDIA)")], dict(kind="calm", gap=0.8)),

 # ---------------- III. THE DIMES ----------------
 ("Polio's most famous patient was a future president.",
  [G("chapter", case="POLIO", n="III", t="THE DIMES")], dict(kind="calm")),
 ("In August nineteen twenty-one, at thirty-nine, Franklin D. Roosevelt was diagnosed with infantile paralysis. In nineteen twenty-four, he went to Warm Springs, Georgia, hoping its waters would help. Two years later, he bought the resort.",
  [C("fdr1930", 37.0), C("fdr1930", 190.0)], dict(tag=("ARCHIVAL FILM · WARM SPRINGS, GA. · 1928–1939", "FDR PRESIDENTIAL LIBRARY"), kind="calm")),
 ("Fundraising for Warm Springs grew into something bigger. In nineteen thirty-eight, Roosevelt founded the National Foundation for Infantile Paralysis.",
  [G("timeline", kicker="FROM ONE PATIENT TO A NATIONAL CAUSE", title="ROOSEVELT AND POLIO",
     events=[dict(y="1921", t="FDR diagnosed, age 39"), dict(y="1924", t="First visit to Warm Springs, Ga."), dict(y="1926", t="Buys the resort"), dict(y="1934", t="First Birthday Ball fundraiser"), dict(y="1938", t="National Foundation founded")], active=4,
     footer="SOURCE: FDR PRESIDENTIAL LIBRARY & MUSEUM")], dict(kind="calm")),
 ("The radio comedian Eddie Cantor urged Americans to send their dimes directly to the president, at the White House. And he suggested a name. The March of Dimes.",
  [G("quote", q="…send their dimes directly to the President at the White House … and we could call it the March of Dimes.", w="EDDIE CANTOR · AS QUOTED BY DR. HOWARD MARKEL, PBS NEWSHOUR")], dict(kind="slow")),
 ("Movie audiences gave. In this nineteen forty-four newsreel, a young girl on crutches thanks moviegoers for their dimes.",
  [C("dimes1944", 8.3), C("dimes1944", 11.2)], dict(tag=("UNIVERSAL NEWSREEL · FEB. 28, 1944", "\"THANKS FOR THE DIMES\""), kind="calm")),
 ("And the National Foundation would pick the man to run what PBS NewsHour calls the largest vaccine trial of its kind ever.",
  [C("unc1956", 312.0)], dict(kind="drive", gap=0.8)),

 # ---------------- IV. THE TRIAL ----------------
 ("The vaccine came from Jonas Salk.",
  [G("chapter", case="POLIO", n="IV", t="THE TRIAL")], dict(kind="calm")),
 ("In the early nineteen fifties, Salk developed an inactivated polio vaccine. It used killed virus. In this nineteen fifty-six film, made by the National Foundation, the vaccine is produced and checked, batch by batch.",
  [C("unc1956", 186.0), C("unc1956", 262.0), C("unc1956", 376.0)], dict(tag=("ARCHIVAL FILM · 1956", "POLIO VACCINE PRODUCTION · NATIONAL FOUNDATION FILM"), kind="calm")),
 ("To find out if it worked, the National Foundation turned to Salk's former teacher, Thomas Francis Junior, at the University of Michigan.",
  [C("unc1956", 160.5)], dict(tag=("ARCHIVAL FILM · 1956", "VACCINE LAB · NATIONAL FOUNDATION FILM"), kind="calm")),
 ("The trial formally began on April twenty-sixth, nineteen fifty-four. More than one point eight million children took part. It relied on about one hundred fifty thousand volunteers, some fifteen thousand schools, and forty-four state health departments.",
  [G("cards3", kicker="THE 1954 FIELD TRIAL", title="THE BIGGEST TEST OF ITS KIND",
     cards=[dict(h="1.8M+", t="children took part", s="1,829,916 IN THE FINAL REPORT"), dict(h="~150,000", t="volunteers", s="", size=96), dict(h="44", t="state health departments", s="AND ABOUT 15,000 SCHOOLS")],
     footer="SOURCES: UNIVERSITY OF MICHIGAN SCHOOL OF PUBLIC HEALTH · PBS NEWSHOUR")], dict(kind="drive")),
 ("In part of the trial, some children got the vaccine, and a group at least as large got a placebo. That part was double-blind. Neither the children nor the doctors giving the shots knew which was which.",
  [C("unc1956", 75.0), C("unc1956", 121.0)], dict(tag=("ARCHIVAL FILM · 1956", "NATIONAL FOUNDATION FOR INFANTILE PARALYSIS"), kind="calm")),
 ("On April twelfth, nineteen fifty-five, Francis stepped up in Rackham Auditorium, in Ann Arbor, to announce the results.",
  [G("stat", a="APRIL 12, 1955", b="RESULTS ANNOUNCED · RACKHAM AUDITORIUM, ANN ARBOR", c="UNIVERSITY OF MICHIGAN · SOURCES: UMICH SPH · PBS NEWSHOUR")], dict(kind="tense")),
 ("The vaccine works. It is safe, effective, and potent.",
  [G("quote", q="The vaccine works. It is safe, effective, and potent.", w="DR. THOMAS FRANCIS JR. · APRIL 12, 1955 · ANN ARBOR")], dict(kind="slow", gap=0.8)),
 ("According to the University of Michigan, it was up to eighty to ninety percent effective in preventing paralytic polio. Newspapers ran the news.",
  [G("stat", a="80–90%", b="EFFECTIVE IN PREVENTING PARALYTIC POLIO · \"UP TO\"", c="SOURCE: UNIVERSITY OF MICHIGAN SCHOOL OF PUBLIC HEALTH")], dict(kind="drive")),
 ("That same year, nineteen fifty-five, the vaccine was licensed for use in the United States.",
  [C("unc1956", 811.5), C("unc1956", 816.0)], dict(tag=("ARCHIVAL FILM · 1956", "POLIOMYELITIS VACCINE VIALS"), kind="calm", gap=0.8)),

 # ---------------- V. THE SETBACK ----------------
 ("Then came a setback.",
  [G("chapter", case="POLIO", n="V", t="THE SETBACK")], dict(kind="tense")),
 ("In nineteen fifty-five, some batches of polio vaccine given to the public contained live polio virus. The CDC says more than two hundred fifty cases of polio were attributed to vaccine made by one company, Cutter Laboratories.",
  [G("callcard", kicker="1955 · THE CUTTER INCIDENT", title="A BAD BATCH",
     rows=[["WHAT WENT WRONG", "SOME BATCHES CONTAINED LIVE POLIO VIRUS"], ["CASES", "250+ ATTRIBUTED TO ONE MAKER'S VACCINE"], ["RESPONSE", "RECALLED AS SOON AS CASES WERE DETECTED"]],
     footer="SOURCE: CDC, HISTORICAL VACCINE SAFETY CONCERNS")], dict(kind="tense")),
 ("The vaccine was recalled as soon as the cases were detected. The government improved the production process and increased oversight. By the fall of nineteen fifty-five, vaccinations had resumed. The CDC says the incident led to a better system for regulating vaccines.",
  [G("steps", kicker="AFTER CUTTER", title="WHAT CHANGED",
     items=[["Recall", "As soon as cases were detected"], ["Fix", "Improved the production process"], ["Oversee", "More government oversight"], ["Resume", "Vaccination restarts, fall 1955"]], active=2,
     footer="SOURCE: CDC, HISTORICAL VACCINE SAFETY CONCERNS")], dict(kind="calm")),
 ("Vaccination went on. In this nineteen fifty-seven newsreel, the Salk vaccine is given to children, including twin girls.",
  [C("kan1957", 3.5), C("kan1957", 24.0)], dict(tag=("UNIVERSAL NEWSREEL · APRIL 1957", "SALK VACCINE BEING GIVEN"), kind="calm", gap=0.8)),

 # ---------------- VI. ONE, TWO, THREE ----------------
 ("Next, America had to reach everyone.",
  [G("chapter", case="POLIO", n="VI", t="ONE, TWO, THREE")], dict(kind="calm")),
 ("In nineteen sixty-one, the Communicable Disease Center, today's CDC, filmed a polio vaccination campaign in Columbus, Georgia, with the state and county health departments.",
  [C("bab1961", 19.0), C("bab1961", 109.0)], dict(tag=("ARCHIVAL FILM · 1961 · COMMUNICABLE DISEASE CENTER", "\"BABIES AND BREADWINNERS\" · COLUMBUS, GA."), kind="calm")),
 ("Free vaccine stations went up. Signs went up on street corners and buses. The message was simple. One shot, good. Two shots, better. Three shots, best.",
  [C("bab1961", 74.0), C("bab1961", 577.0), C("bab1961", 594.5)], dict(kind="drive")),
 ("Health workers went door to door with forms. And the campaign kept score, charting how many young children in each area had three or more shots.",
  [C("bab1961", 205.0), C("bab1961", 223.0), C("bab1961", 266.0)], dict(tag=("ARCHIVAL FILM · 1961 · COMMUNICABLE DISEASE CENTER", "COLUMBUS, GA. CAMPAIGN"), kind="calm")),
 ("Meanwhile, a second vaccine arrived. The CDC credits Albert Sabin with developing the oral polio vaccine, in the early nineteen sixties. Oral vaccines were licensed in the U.S. starting in nineteen sixty-one.",
  [G("phases", kicker="TWO VACCINES", title="SALK AND SABIN",
     left=dict(label="INACTIVATED · JONAS SALK", num="1955", desc="KILLED VIRUS · GIVEN AS A SHOT"), right=dict(label="ORAL · ALBERT SABIN", num="1961", desc="FIRST ORAL VACCINES LICENSED IN THE U.S."),
     footer="SOURCES: CDC PINK BOOK, CH. 18 · CDC")], dict(kind="calm")),
 ("It worked. According to the CDC, the last cases of paralytic polio caused by locally acquired wild virus in the United States were reported in nineteen seventy-nine.",
  [G("stat", a="\u20601979", b="LAST LOCALLY ACQUIRED WILD POLIO CASES REPORTED IN THE U.S.", c="SOURCE: CDC PINK BOOK, CH. 18")], dict(kind="slow")),
 ("Since two thousand, the only polio vaccine used in the U.S. has been the inactivated one, given as a shot. The CDC notes that because it's made from killed virus, it cannot cause polio.",
  [C(813274, 26.0), C(813274, 34.0)], dict(tag=("U.S. NAVY IMMUNIZATION SITE · 2021", "OPERATION ALLIES WELCOME · VACCINES INCLUDED POLIO"), kind="calm", gap=0.8)),

 # ---------------- VII. ONE IRON LUNG ----------------
 ("But what replaced the iron lung? That story starts in Denmark.",
  [G("chapter", case="POLIO", n="VII", t="ONE IRON LUNG")], dict(kind="question")),
 ("In nineteen fifty-two, polio hit Copenhagen hard. Two accounts of the epidemic say the city's infectious disease hospital, and Denmark as a whole, had just one iron lung.",
  [G("map", map=dict(bounds=[[0, 50], [25, 60]], rings=[dict(ll=COPEN, r=40, n=3, d=0.5)],
     cities=[dict(ll=COPEN, name="COPENHAGEN", sub="1952 · ONE IRON LUNG IN THE COUNTRY", d=0.3, color="#6CF29A")]),
     kicker="DENMARK · 1952", title="AN EPIDEMIC, ONE MACHINE", footer="SOURCES: NEW STATESMAN (2020) · ATS CONFERENCE NEWS")], dict(kind="tense")),
 ("A Danish anesthesiologist, Bjørn Ibsen, suggested another approach. Instead of pulling air in from the outside of the body, push air into the lungs, through a tube in the windpipe. Positive pressure.",
  [G("phases", kicker="TWO WAYS TO BREATHE FOR SOMEONE", title="PULL VS. PUSH",
     left=dict(label="IRON LUNG", num="PULL", desc="LOWER PRESSURE AROUND THE CHEST"), right=dict(label="BJØRN IBSEN · 1952", num="PUSH", desc="POSITIVE PRESSURE INTO THE LUNGS"), active=1,
     footer="SOURCES: UNIVERSITY OF FLORIDA COLLEGE OF MEDICINE · KANSAS HISTORICAL SOCIETY")], dict(kind="calm")),
 ("But there weren't machines to do the pushing. So people did it by hand, squeezing a bag, in shifts, around the clock. Some accounts put the number of medical and dental students who took part at more than a thousand.",
  [C(861320, 92.5), C(999485, 84.0)], dict(tag=("MODERN TRAINING FOOTAGE · NOT 1952", "BAMC 2022 · VENTILATOR TRAINING, TANZANIA 2026"), kind="drive")),
 ("Deaths among the patients with breathing paralysis fell sharply. And in December nineteen fifty-three, the first intensive care unit opened in Copenhagen.",
  [G("stat", a="DEC. 1953", b="THE FIRST INTENSIVE CARE UNIT OPENS IN COPENHAGEN", c="SOURCES: UNIVERSITY OF FLORIDA COLLEGE OF MEDICINE · ATS CONFERENCE NEWS")], dict(kind="slow")),
 ("Harvard Medical School says iron lungs eventually became obsolete. Today, intensive care units like these, at U.S. Naval Hospital Guam, use mechanical ventilators.",
  [C(997537, 44.0), C(997537, 79.0)], dict(tag=("ICU VIRTUAL TOUR · EMPTY ROOMS", "U.S. NAVAL HOSPITAL GUAM · 2026"), kind="calm")),
 ("And here, an Air Force respiratory care practitioner teaches Tanzanian military medical staff to use ventilators, during a training exercise in twenty twenty-six.",
  [C(999485, 1.0), C(999485, 41.0), C(999485, 77.0)], dict(tag=("VENTILATOR TRAINING · JUSTIFIED ACCORD 26", "DAR ES SALAAM, TANZANIA · MARCH 2026"), kind="calm", gap=0.8)),

 # ---------------- VIII. THE LAST TWO ----------------
 ("The rest of the world still had to finish the job.",
  [G("chapter", case="POLIO", n="VIII", t="THE LAST TWO")], dict(kind="calm")),
 ("In nineteen ninety-four, an international commission certified the Western Hemisphere free of native wild poliovirus.",
  [G("stat", a="\u20601994", b="WESTERN HEMISPHERE CERTIFIED FREE OF INDIGENOUS WILD POLIOVIRUS", c="SOURCE: CDC PINK BOOK, CH. 18")], dict(kind="calm")),
 ("Globally, the push had begun in nineteen eighty-eight, with the Global Polio Eradication Initiative. Back then, the World Health Organization estimates, there were about three hundred fifty thousand cases, in more than one hundred twenty-five countries. Since then, wild polio cases have fallen by more than ninety-nine percent.",
  [G("cards3", kicker="GLOBAL POLIO ERADICATION INITIATIVE", title="FROM 350,000 TO A HANDFUL",
     cards=[dict(h="1988", t="Global initiative launched", s="WORLD HEALTH ASSEMBLY RESOLUTION"), dict(h="~350,000", t="cases, estimated, in 1988", s="IN 125+ COUNTRIES", size=96), dict(h=">99%", t="drop in wild polio cases since", s="")],
     footer="SOURCE: WHO POLIOMYELITIS FACT SHEET")], dict(kind="drive")),
 ("Of the three types of wild poliovirus, two have been declared eradicated. Type two in twenty fifteen, and type three in twenty nineteen.",
  [G("timeline", kicker="THREE WILD POLIOVIRUSES", title="TWO DOWN",
     events=[dict(y="1988", t="Global initiative begins"), dict(y="1994", t="Western Hemisphere certified"), dict(y="2015", t="Wild type 2 declared eradicated"), dict(y="2019", t="Wild type 3 declared eradicated")], active=3,
     footer="SOURCE: CDC PINK BOOK, CH. 18")], dict(kind="calm")),
 ("Today, according to the World Health Organization, wild polio is endemic in only two countries. Afghanistan, and Pakistan.",
  [G("map", map=dict(bounds=[[40, 15], [95, 45]], rings=[dict(ll=AFG, r=34, n=2, d=0.5), dict(ll=PAK, r=34, n=2, d=0.8)],
     cities=[dict(ll=AFG, name="AFGHANISTAN", sub="ENDEMIC", d=0.3, color="#6CF29A", anchor="end"), dict(ll=PAK, name="PAKISTAN", sub="ENDEMIC", d=0.6, color="#6CF29A")]),
     kicker="WILD POLIOVIRUS TODAY", title="TWO COUNTRIES LEFT", footer="SOURCE: WHO POLIOMYELITIS FACT SHEET")], dict(kind="slow", gap=0.8)),

 # ---------------- WHAT IT CHANGED ----------------
 ("So, how did wild polio end in America?",
  [G("chapter", case="POLIO", n="IX", t="WHAT IT TOOK")], dict(kind="question")),
 ("Not with the iron lung. The machine kept people alive. It could not stop the virus.",
  [C("ilung1945", 125.0)], dict(tag=("ARCHIVAL FILM · 1945 · U.S. ARMY SIGNAL CORPS", "IRON LUNG EVACUATION · MANILA"), kind="slow")),
 ("That took a nation sending dimes. A trial with almost two million children. Two vaccines. And campaigns that went door to door.",
  [G("steps", kicker="POLIO IN AMERICA", title="FROM THE TANK TO THE LAST WILD CASE",
     items=[["1928", "First iron lung in Boston"], ["1938", "National Foundation founded"], ["1955", "Salk vaccine licensed"], ["1979", "Last local wild cases"]], active=3)], dict(kind="calm")),
 ("And the crisis the iron lung couldn't handle helped give us the modern intensive care unit.",
  [C(997537, 52.0)], dict(tag=("ICU VIRTUAL TOUR · EMPTY ROOM", "U.S. NAVAL HOSPITAL GUAM · 2026"), kind="slow")),
 ("Next time on Kept Alive. Whole blood, and the walking blood bank.",
  [G("stat", a="NEXT", b="WHOLE BLOOD AND THE WALKING BLOOD BANK", c="KEPT ALIVE · HOW IT WORKS · 005")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · FIRST 004", stamp="1928")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("Nineteen forty-five", "1945"), ("Nineteen sixteen", "1916"), ("one hundred fifty thousand", "150,000"), ("fifteen thousand", "15,000"), ("forty-four", "44"), ("nineteen forty-five", "1945"), ("twenty-five years", "25 years"), ("seventy percent", "70 percent"),
 ("one in two hundred", "1 in 200"), ("five to ten percent", "5 to 10 percent"), ("nineteen fifty-two", "1952"), ("twenty-one thousand", "21,000"),
 ("nineteen forties", "1940s"), ("nineteen thirties", "1930s"), ("thirty-five thousand", "35,000"), ("October twelfth, nineteen twenty-eight", "October 12, 1928"),
 ("nineteen thirty-one", "1931"), ("nineteen thirty-three", "1933"), ("a thousand dollars", "$1,000"), ("nineteen fifty-nine", "1959"),
 ("twelve hundred", "1,200"), ("August nineteen twenty-one", "August 1921"), ("thirty-nine", "39"), ("nineteen twenty-four", "1924"),
 ("nineteen thirty-eight", "1938"), ("nineteen forty-four", "1944"), ("nineteen fifties", "1950s"), ("nineteen fifty-six", "1956"),
 ("April twenty-sixth, nineteen fifty-four", "April 26, 1954"), ("one point eight million", "1.8 million"),
 ("April twelfth, nineteen fifty-five", "April 12, 1955"), ("eighty to ninety percent", "80 to 90 percent"), ("nineteen fifty-five", "1955"),
 ("two hundred fifty", "250"), ("nineteen fifty-seven", "1957"), ("nineteen sixty-one", "1961"), ("nineteen sixties", "1960s"),
 ("nineteen seventy-nine", "1979"), ("Since two thousand", "Since 2000"), ("December nineteen fifty-three", "December 1953"),
 ("twenty twenty-six", "2026"), ("nineteen ninety-four", "1994"), ("nineteen eighty-eight", "1988"), ("three hundred fifty thousand", "350,000"),
 ("one hundred twenty-five", "125"), ("ninety-nine percent", "99 percent"), ("twenty fifteen", "2015"), ("twenty nineteen", "2019"),
 ("Thomas Francis Junior", "Thomas Francis Jr."), ("J. H. Emerson", "J.H. Emerson"), ("Kept Alive", "KEPT ALIVE"), ("two million", "2 million"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · FIRST",
    title="The Iron Lung and the End of Polio",
    voice="am_fenrir",
    mute_nat=["ilung1945", "unc1956", "bab1961", "kan1957", "dimes1944", "fdr1930", "999485", "861320", "997537", "813274"],
    training=["999485", "861320"],
    credit=("Footage: U.S. Air Force/U.S. Army (SETAF-AF), Brooke Army Medical Center, U.S. Naval Hospital Guam, Operation Allies Welcome via DVIDS (public domain);"
            r"\NU.S. Army Signal Corps \"Iron Lung Evacuation\" (1945, National Archives) and FDR Library film (Internet Archive, CC0);"
            r"\N\"Unconditional Surrender\" (1956), \"Babies and Breadwinners\" (1961), Universal Newsreels (1944, 1957), public domain via Internet Archive."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, NIH, CDC or WHO."
            r"\NFor education only. This is not medical advice."),
)
