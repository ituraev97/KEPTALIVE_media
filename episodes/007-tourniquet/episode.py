# KEPT ALIVE · HOW IT WORKS 007 — The Tourniquet: From Feared to Lifesaver
# Each entry: (vo_text, shots, opts). shot: C(clip, start, mode="fit"|"fill", fy=..) | G(graphic, **opts) | I(image key, kb="in"|"pan")
# opts: gap (sec after line), tag (lower third: headline, kicker), kind (calm|punch|tense|slow|drive|question)
# Footage honesty:
#  ALL DVIDS footage is TRAINING (badge via META["training"]); no real casualties, no wounds, no blood. Training lanes with moulage (949268) NOT used.
#   111605 = Marines demonstrate the CAT, Regional Command Southwest, Afghanistan, 2011 (instruction, not combat)
#   888808 = Basic Combat Training tourniquet drill, Fort Jackson, S.C. (U.S. Army Training Support Center)
#   886668 = TCCC tourniquet class, Gila Bend AF Aux. Field, Ariz. (944th Fighter Wing), 2023
#   1000551 = TCCC class, Chievres Air Base, Belgium, March 2026 (AFN Benelux)
#   855753 = Stop the Bleed course, Tyndall AFB, Fla., 2022 (325th Fighter Wing)
#   610820 = Stop the Bleed courses, Las Vegas (Nellis AFB 99th Medical Group with UMC), 2018 — memorial photos at 0-8 s NOT used
#   741580 = Basic Military Training TCCC course, JBSA-Lackland, Texas, 2020
#  arm_* = excerpts of War Department Official Training Film No. 71 "The Medical Service with Infantry in Combat" (NARA 111-M-489, reel 1;
#          Internet Archive lists it as produced 1925). A field exercise -> labelled ARMY TRAINING FILM, never presented as a battle.
#  esmarch_* = Friedrich von Esmarch, "Early Aid in Injuries and Accidents" (London, 1883), p. 58, Figs. 10-11; NLM copy via Internet Archive (public domain).
C = lambda i, s, **k: (str(i), s, k)
G = lambda name, **k: ("g:" + name, 0, k)
I = lambda key, **k: ("img:" + key, 0, k)
CASE = "HOW IT WORKS · 007"
S = "<span style=\"color:#2BB3A3\">{}</span>"
ARMF = ("ARCHIVAL ARMY TRAINING FILM · \"THE MEDICAL SERVICE WITH INFANTRY IN COMBAT\"", "WAR DEPARTMENT TRAINING FILM NO. 71 · LISTED AS 1925 · NATIONAL ARCHIVES 111-M-489")
ESM = ("\"EARLY AID IN INJURIES AND ACCIDENTS\" · FRIEDRICH VON ESMARCH · 1883", "FIGS. 10–11 · NATIONAL LIBRARY OF MEDICINE COPY")
AFG = ("MARINES DEMONSTRATE THE COMBAT APPLICATION TOURNIQUET", "REGIONAL COMMAND SOUTHWEST, AFGHANISTAN · 2011 · U.S. MARINE CORPS")
JACK = ("TOURNIQUET TRAINING · BASIC COMBAT TRAINING", "FORT JACKSON, S.C. · 2023 · U.S. ARMY TRAINING SUPPORT CENTER")
GILA = ("TACTICAL COMBAT CASUALTY CARE CLASS", "GILA BEND, ARIZ. · 2023 · 944TH FIGHTER WING")
CHI = ("TACTICAL COMBAT CASUALTY CARE CLASS", "CHIÈVRES AIR BASE, BELGIUM · MARCH 2026 · AFN BENELUX")
TYN = ("STOP THE BLEED COURSE", "TYNDALL AIR FORCE BASE, FLA. · 2022 · 325TH FIGHTER WING")
LV = ("STOP THE BLEED COURSES FOR THE PUBLIC", "LAS VEGAS · 2018 · 99TH MEDICAL GROUP, NELLIS AFB")
BMT = ("TCCC COURSE · BASIC MILITARY TRAINING", "JOINT BASE SAN ANTONIO-LACKLAND, TEXAS · 2020 · U.S. AIR FORCE")

LINES = [
 # ---------------- COLD OPEN ----------------
 ("A tourniquet works by squeezing an arm or a leg so hard that the main artery inside is pressed shut. Blood can no longer flow past it.",
  [C(111605, 59.5), C(111605, 73.0)], dict(tag=AFG, kind="punch")),
 ("It's one of the simplest devices in medicine. And for most of the twentieth century, military doctors were taught to fear it.",
  [C("arm_march", 1.0)], dict(tag=ARMF, kind="tense")),
 ("In nineteen sixteen, a British army surgeon wrote that he was inclined to think tourniquets were an invention of the Evil One.",
  [G("quote", q="…inclined to think that tourniquets are an invention of the Evil One.", w="MAJOR BLACKWOOD · ROYAL ARMY MEDICAL CORPS · 1916 · AS QUOTED BY KRAGH ET AL., 2012")], dict(kind="slow", gap=0.6)),
 ("Ninety years later, in a Baghdad hospital, Army researchers counted who lived. Among casualties who needed a tourniquet, eighty-seven percent of those who got one survived. Of the five who did not get one, none survived.",
  [G("phases", kicker="BAGHDAD · 2006 · U.S. ARMY STUDY", title="WHEN A TOURNIQUET WAS NEEDED", left=dict(label="GOT A TOURNIQUET", num="87%", desc="SURVIVED"),
     right=dict(label="NEEDED ONE · DID NOT GET IT (5 CASUALTIES)", num="0%", desc="SURVIVED"), active=0, footer="SOURCE: KRAGH ET AL., ANNALS OF SURGERY, 2009")], dict(kind="punch", gap=0.6)),
 ("This is how a strap and a stick went from feared, to standard gear for American troops. And how it works.",
  [C(888808, 141.0)], dict(tag=JACK, kind="question", gap=0.5)),
 ("The tourniquet. From feared, to lifesaver.",
  [G("title", kicker=CASE, title="THE " + S.format("TOURNIQUET"), sub="FROM FEARED TO LIFESAVER", size=170)], dict(kind="slow", gap=2.6)),

 # ---------------- I. TO TURN ----------------
 ("The idea is old. The name comes from a French verb.",
  [G("chapter", case="1674–1883", n="I", t="TO TURN")], dict(gap=1.1, kind="calm")),
 ("Roman surgeons used narrow bronze straps. And the arguments began early. The Greek physician Galen criticized tourniquets, saying they forced more blood from the wound.",
  [G("doc", header="ANCIENT ROME", title="BRONZE STRAPS", body="Romans used narrow bronze straps around the limb. Galen criticized tourniquets as forcing more blood from a wound.",
     source="SOURCE: MAHER, JMVH, 2020", stamp="ANTIQUITY")], dict(kind="calm")),
 ("In sixteen seventy-four, a French army surgeon named Morel described a tourniquet used at the siege of Besançon.",
  [G("timeline", kicker="A SHORT HISTORY", title="EARLY TOURNIQUETS",
     events=[dict(y="1674", t="Morel · siege of Besançon"), dict(y="1718", t="Petit · a screw device"), dict(y="1873", t="Esmarch · a rubber bandage")],
     footer="SOURCE: KRAGH ET AL., AMERICAN JOURNAL OF SURGERY, 2012")], dict(kind="calm")),
 ("In seventeen eighteen, the Paris surgeon Jean-Louis Petit built a screw device to tighten a strap around a limb. He coined the word tourniquet, from the French tourner. To turn.",
  [G("doc", header="PARIS · 1718", title="TOURNER: TO TURN", body="Jean-Louis Petit describes a screw device that tightens a strap around the limb, and coins the word tourniquet.",
     source="SOURCES: KRAGH ET AL., 2012 · MAHER, JMVH, 2020", stamp="1718")], dict(kind="calm")),
 ("In eighteen seventy-three, the German surgeon Friedrich von Esmarch reported a rubber bandage wrapped around the limb, that shut the arteries and controlled bleeding.",
  [I("esmarch_page", kb="in")], dict(tag=ESM, kind="calm")),
 ("His first aid lectures, published in English in eighteen eighty-three, described an improvised version. A handkerchief tied loosely around the limb, with a short stick pushed under it. A walking stick, a door key, even a sword in its sheath. The stick was then twisted, round and round.",
  [I("esmarch_fig", kb="in")], dict(tag=ESM, kind="drive")),
 ("That twisting stick is the same idea inside a modern tourniquet. Today it's called the windlass.",
  [C(111605, 173.0)], dict(tag=AFG, kind="slow", gap=0.7)),

 # ---------------- II. FEARED ----------------
 ("So why did doctors turn against it?",
  [G("chapter", case="1861–1980s", n="II", t="FEARED")], dict(gap=1.1, kind="question")),
 ("The complaint was always the same. Troops used them too often, too loosely, or for too long. During the American Civil War, the Confederate surgeon Julian Chisholm noted that troops too often used tourniquets needlessly.",
  [C("arm_field", 6.2), C("arm_map", 0.5)], dict(tag=ARMF, kind="calm")),
 ("In eighteen sixty-two, according to one review, the Union surgeon Samuel Gross made the first recorded recommendation to issue a tourniquet-like device to soldiers. Critics pushed back, often over poor training, and slow transport to a surgeon.",
  [G("callcard", kicker="AMERICAN CIVIL WAR", title="A CIVIL WAR DEBATE",
     rows=[["1861", "CHISHOLM: TROOPS USE THEM NEEDLESSLY"], ["1862", "GROSS: ISSUE A TOURNIQUET-LIKE DEVICE TO SOLDIERS"], ["THE PROBLEM", "TRAINING GAPS · SLOW TRANSPORT"]],
     footer="SOURCES: KRAGH ET AL., 2012 · MAHER, JMVH, 2020")], dict(kind="calm")),
 ("Around the Second World War, the British surgeon Watson-Jones put it bluntly.",
  [C("arm_field", 1.0)], dict(tag=ARMF, kind="calm")),
 ("More limbs have been lost by the use of tourniquets than have been saved.",
  [G("quote", q="More limbs have been lost by the use of tourniquets than have been saved.", w="WATSON-JONES · AS QUOTED BY KRAGH ET AL., 2012")], dict(kind="slow", gap=0.6)),
 ("Not everyone agreed. Late in the same war, two Army doctors, Wolff and Adkins, reported on about two hundred wounded service members who had tourniquets. They reported no gangrene, clots, or nerve damage they could attribute to the devices. The fear stayed anyway.",
  [C("arm_aid", 14.0)], dict(tag=ARMF, kind="calm")),
 ("And the American army absorbed that fear. In the nineteen seventies and early eighties, Army medics were taught that in almost all cases, amputation would follow tourniquet use. A standard military surgery text, Emergency War Surgery, said tourniquets were rarely needed, and should be used only when all other methods fail.",
  [G("doc", header="EMERGENCY WAR SURGERY · U.S. MILITARY TEXTBOOK", title="A LAST RESORT", body="\"Tourniquets are rarely needed for the control of haemorrhage and should be used only when all other methods fail.\"",
     source="SOURCE: MAHER, JMVH, 2020", stamp="LAST RESORT")], dict(kind="calm")),
 ("But Vietnam told a different story. Bleeding from wounds to the arms and legs was the leading cause of potentially preventable deaths on the battlefield. One surgeon's study of those killed in action, published in nineteen seventy, estimated that roughly two thousand six hundred of them, about seven point four percent, might have been saved with better care before the hospital.",
  [G("stat", a="~2,600", b="LIVES THAT MIGHT HAVE BEEN SAVED WITH BETTER PREHOSPITAL CARE · VIETNAM", c="ABOUT 7.4% OF THOSE KILLED IN ACTION · ESTIMATE · MAUGHON, 1970 · VIA KRAGH ET AL., 2012 · ESTIMATE")], dict(kind="punch", gap=0.6)),
 ("Bleeding from a limb is the kind of bleeding a tourniquet can stop.",
  [C("arm_medics", 1.0), C("arm_aid", 2.0)], dict(tag=ARMF, kind="slow", gap=0.7)),
 ("And the lesson came back in nineteen ninety-one. In Operation Desert Storm, of one hundred forty-three soldiers treated in U.S. Army hospitals in one report, three died. Each of those deaths involved bleeding from a limb.",
  [G("stat", a="3 OF 143", b="DIED · EACH DEATH INVOLVED BLEEDING FROM A LIMB", c="U.S. ARMY HOSPITALS · OPERATION DESERT STORM, 1991 · SOURCE: MAHER, JMVH, 2020")], dict(kind="punch", gap=0.6)),

 # ---------------- III. THE REVERSAL ----------------
 ("The turn came from special operations.",
  [G("chapter", case="1993–2005", n="III", t="THE REVERSAL")], dict(gap=1.1, kind="calm")),
 ("Frank Butler was a former Navy SEAL platoon commander, who became an eye surgeon. Starting in nineteen ninety-three, he and his colleagues rethought care on the battlefield from scratch. In nineteen ninety-six, they published Tactical Combat Casualty Care, in the journal Military Medicine.",
  [G("callcard", kicker="SPECIAL OPERATIONS · 1993–1996", title="TACTICAL COMBAT CASUALTY CARE",
     rows=[["THE AUTHOR", "FRANK BUTLER · FORMER NAVY SEAL, EYE SURGEON"], ["1993", "THE WORK BEGINS"], ["1996", "PUBLISHED IN MILITARY MEDICINE"]],
     footer="SOURCES: BUTLER, JSOM, 2015 · MAHER, JMVH, 2020")], dict(kind="calm")),
 ("It split care into phases. Care under fire. Tactical field care. And evacuation. And it put the tourniquet back at the front of the line, for life-threatening bleeding from a limb.",
  [C(886668, 73.0), C(886668, 25.0)], dict(tag=GILA, kind="drive")),
 ("Then came the wars in Afghanistan and Iraq. A study of eighty-two special operations deaths, from late two thousand one through two thousand four, judged twelve of them potentially survivable. Some of those involved bleeding from a limb that a tourniquet could have controlled.",
  [G("stat", a="12 OF 82", b="SPECIAL OPERATIONS DEATHS, 2001–2004, JUDGED POTENTIALLY SURVIVABLE", c="SOME INVOLVED LIMB BLEEDING A TOURNIQUET COULD HAVE CONTROLLED · SOURCE: HOLCOMB ET AL., ANNALS OF SURGERY, 2007")], dict(kind="punch")),
 ("Special operations units that adopted the new rules early kept records. One program documented sixty-seven uses of tourniquets, and not a single limb lost to the tourniquet cutting off blood for too long.",
  [G("stat", a="67", b="TOURNIQUET USES IN SPECIAL OPERATIONS UNITS · NO LIMBS LOST TO TOURNIQUET ISCHEMIA", c="TCCC TRANSITION INITIATIVE · SOURCE: BUTLER, JOURNAL OF SPECIAL OPERATIONS MEDICINE, 2015")], dict(kind="calm")),
 ("In two thousand three, the Army Surgeon General recommended a tourniquet called the Combat Application Tourniquet, as standard issue.",
  [C(886668, 54.8), C(886668, 64.4)], dict(tag=GILA, kind="calm")),
 ("In July two thousand five, an Army news story said another new tourniquet, the SOF Tactical Tourniquet, was being issued to all soldiers serving in Iraq and Afghanistan. It was designed for one-handed use, so a soldier could put it on himself if need be.",
  [G("doc", header="ARMY NEWS · JULY 2005", title="ISSUED TO ALL SOLDIERS", body="The SOF Tactical Tourniquet \"is being issued to all Soldiers serving in Iraq and Afghanistan.\" Designed for one-handed application, so a soldier can apply it to himself if need be.",
     source="SOURCE: DVIDS, JULY 2005", stamp="2005")], dict(kind="calm")),
 ("In two thousand five and two thousand six, tourniquet use spread rapidly across the whole U.S. military.",
  [C(888808, 153.0), C(888808, 205.0)], dict(tag=JACK, kind="drive", gap=0.7)),

 # ---------------- IV. THE PROOF ----------------
 ("But did it work? Army researchers decided to count.",
  [G("chapter", case="BAGHDAD · 2006", n="IV", t="THE PROOF")], dict(gap=1.1, kind="question")),
 ("Army Colonel John Kragh and his colleagues ran a study at a combat support hospital in Baghdad, for seven months in two thousand six. It included two thousand eight hundred thirty-eight casualties with major limb injuries. Two hundred thirty-two of them had tourniquets put on.",
  [G("callcard", kicker="COMBAT SUPPORT HOSPITAL · BAGHDAD · 2006", title="THE KRAGH STUDY",
     rows=[["7 MONTHS", "PROSPECTIVE SURVEY · 2006"], ["2,838", "CASUALTIES WITH MAJOR LIMB TRAUMA"], ["232", "RECEIVED TOURNIQUETS · 428 APPLIED TO 309 LIMBS"]],
     footer="SOURCE: KRAGH ET AL., ANNALS OF SURGERY, 2009")], dict(kind="calm")),
 ("Timing was linked to survival. Among patients whose tourniquet went on before they reached the emergency department, eleven percent died. When it went on in the emergency department, twenty-four percent died.",
  [G("phases", kicker="KRAGH ET AL. · 2009", title="WHERE THE TOURNIQUET WENT ON", left=dict(label="BEFORE THE HOSPITAL", num="11%", desc="DIED · 22 OF 194"),
     right=dict(label="IN THE EMERGENCY DEPARTMENT", num="24%", desc="DIED · 9 OF 38"), active=0, footer="SOURCE: KRAGH ET AL., ANNALS OF SURGERY, 2009")], dict(kind="calm")),
 ("And the old fear did not hold up. In that study, no amputations resulted solely from tourniquet use. Four patients had a temporary nerve problem.",
  [C(1000551, 101.0)], dict(tag=CHI, kind="calm")),
 ("Later, a review of four thousand five hundred ninety-six American battlefield deaths, from two thousand one to two thousand eleven, found that eighty-seven percent happened before the casualty reached a medical facility. Of the deaths before a medical facility that were judged potentially survivable, about nine in ten were associated with bleeding. Most of that bleeding was in the torso, or where limbs meet the body, beyond a tourniquet's reach.",
  [G("cards3", kicker="DEATH ON THE BATTLEFIELD · 2001–2011", title="WHERE AND WHY",
     cards=[dict(h="4,596", t="deaths reviewed", s="U.S. BATTLEFIELD FATALITIES"), dict(h="87.3%", t="before a medical facility", s="PREHOSPITAL"), dict(h="90.9%", t="linked to bleeding", s="OF POTENTIALLY SURVIVABLE PREHOSPITAL DEATHS")],
     footer="SOURCE: EASTRIDGE ET AL., J TRAUMA ACUTE CARE SURG, 2012")], dict(kind="calm")),
 ("And potentially preventable deaths from limb bleeding fell, from seven point eight percent of the combat deaths in an earlier study, to two point six percent in the later review. A drop of sixty-seven percent.",
  [G("phases", kicker="POTENTIALLY PREVENTABLE DEATHS FROM LIMB BLEEDING", title="AN EARLIER STUDY VS. A LATER REVIEW", left=dict(label="EARLIER STUDY (KELLY ET AL., 2008)", num="7.8%", desc="OF COMBAT DEATHS REVIEWED"),
     right=dict(label="EASTRIDGE ET AL., 2012", num="2.6%", desc="OF COMBAT DEATHS REVIEWED · −67%"), active=1, footer="SOURCE: BUTLER, JOURNAL OF SPECIAL OPERATIONS MEDICINE, 2015")], dict(kind="punch")),
 ("Based on Kragh's work, the number of lives saved by tourniquets in those wars has been estimated at between one thousand and two thousand.",
  [G("stat", a="1,000–2,000", b="LIVES SAVED BY TOURNIQUETS IN IRAQ AND AFGHANISTAN · ESTIMATED", c="BASED ON THE WORK OF COL. JOHN KRAGH ET AL. · SOURCE: BUTLER, JSOM, 2015")], dict(kind="slow", gap=0.9)),

 # ---------------- V. HOW IT WORKS ----------------
 ("So what exactly is happening, inside that strap?",
  [G("chapter", case="THE DEVICE", n="V", t="HOW IT WORKS")], dict(gap=1.1, kind="question")),
 ("Your heart pushes blood out through the arteries under pressure. When a major artery in a limb is torn, that pressure keeps pushing blood out.",
  [C(1000551, 29.0)], dict(tag=CHI, kind="calm")),
 ("A tourniquet goes around the limb, above the injury. Tightened enough, it squeezes the limb until the artery inside is pressed flat, and flow beyond it stops. Doctors call this arterial occlusion.",
  [G("steps", kicker="THE PARTS", title="STOPPING THE FLOW", items=[["STRAP", "Goes around the limb, above the wound"], ["WINDLASS", "A rod that twists to tighten it"], ["OCCLUSION", "The artery is pressed shut"]],
     footer="SOURCES: KRAGH ET AL., 2012 · WALL ET AL., JSOM, 2019")], dict(kind="calm")),
 ("The Combat Application Tourniquet adds a rod, the windlass. Twisting it tightens the strap further, until the artery is shut. Then the rod is locked in place, so it can't unwind.",
  [C(111605, 81.0), C(111605, 121.6)], dict(tag=AFG, kind="calm")),
 ("And there's a strap marked time, to record when the tourniquet went on.",
  [C(111605, 193.0)], dict(tag=AFG, kind="slow")),
 ("It takes real force. One review cites pressures of two hundred fifty to four hundred twenty-eight millimeters of mercury, to shut off the artery in an adult thigh.",
  [G("stat", a="250–428", b="MMHG · PRESSURE CITED FOR ARTERIAL OCCLUSION ON NORMOTENSIVE ADULT THIGHS", c="COMBAT APPLICATION TOURNIQUET · SOURCE: WALL ET AL., JOURNAL OF SPECIAL OPERATIONS MEDICINE, 2019")], dict(kind="calm")),
 ("That's why the old complaint had a point. A tourniquet that's too loose can fail to stop the bleeding. The same review says the concept is simple, but technique matters, and usually needs training.",
  [C(888808, 221.0)], dict(tag=JACK, kind="calm")),
 ("So soldiers drill it, over and over.",
  [C(888808, 185.0), C(888808, 145.0)], dict(tag=JACK, kind="drive")),
 ("Air Force recruits learn it too. In twenty twenty, Basic Military Training added a Tactical Combat Casualty Care course for all Airmen. Tourniquet application is one of the skills it teaches.",
  [C(741580, 4.0), C(741580, 32.0)], dict(tag=BMT, kind="calm", gap=0.7)),

 # ---------------- VI. COMING HOME ----------------
 ("Then the lessons of the battlefield came home.",
  [G("chapter", case="2012–2019", n="VI", t="COMING HOME")], dict(gap=1.1, kind="calm")),
 ("After the Sandy Hook school shooting in twenty twelve, the surgeon Lenworth Jacobs brought together national experts. Their recommendations became known as the Hartford Consensus. The goal was to improve survival after mass shootings and other mass violence, by training bystanders to act.",
  [C(855753, 7.5)], dict(tag=TYN, kind="calm")),
 ("Then, in twenty thirteen, came the Boston Marathon bombing. Tourniquets were used in the response. But a later study found that all twenty-seven tourniquets used were makeshift, not commercial devices. Its lead author called them improvised, and rarely effective.",
  [G("callcard", kicker="BOSTON MARATHON · 2013", title="THE MARATHON BOMBING",
     rows=[["27", "TOURNIQUETS USED"], ["ALL", "MAKESHIFT · NONE COMMERCIALLY MADE"], ["THE VERDICT", "\"IMPROVISED AND RARELY EFFECTIVE\""]],
     footer="SOURCES: KING ET AL., J TRAUMA ACUTE CARE SURG, 2015 · STAT VIA PBS NEWSHOUR, 2016")], dict(kind="calm")),
 ("In October twenty fifteen, the White House launched a campaign called Stop the Bleed. It is led by the American College of Surgeons Committee on Trauma, and it runs under a licensing agreement with the Department of Defense.",
  [C(610820, 33.0), C(610820, 13.0)], dict(tag=LV, kind="calm")),
 ("The courses teach ordinary people what military medics learned. Students. Teachers. Even members of Congress. By late August twenty nineteen, the American College of Surgeons said more than one million people had been trained.",
  [C(855753, 41.0), C(610820, 53.0)], dict(tag=TYN, kind="drive")),
 ("This video is not that training. It explains the history, and how the device works. Hands-on courses are where people learn to use one.",
  [C(855753, 49.0)], dict(tag=TYN, kind="calm", gap=0.7)),

 # ---------------- WHAT CHANGED ----------------
 ("For most of a century, the tourniquet was a last resort, blamed for lost limbs.",
  [C("arm_march", 8.0)], dict(tag=ARMF, kind="slow")),
 ("Then special operations doctors rewrote the rules, Army researchers counted the survivors, and troops heading to war were issued one. The idea Esmarch drew in eighteen eighty-three, a strap and a twisting stick, is now in first aid kits far from any battlefield.",
  [I("esmarch_fig", kb="pan"), C(1000551, 42.0)], dict(kind="slow", gap=0.9)),
 ("Next time on Kept Alive. Penicillin. The mold that went to war.",
  [G("stat", a="NEXT", b="PENICILLIN: THE MOLD THAT WENT TO WAR", c="KEPT ALIVE · FIRST · 008")], dict(kind="calm", gap=0.8)),
 ("For education only. This is not medical advice. If you have a health concern, talk to a doctor.",
  [G("end", label="KEPT ALIVE · HOW IT WORKS 007", stamp="TOURNIQUET")], dict(kind="calm", gap=2.6)),
]

DISPLAY = [
 ("nineteen sixteen", "1916"), ("Ninety years later", "90 years later"), ("eighty-seven percent", "87%"), ("sixteen seventy-four", "1674"),
 ("seventeen eighteen", "1718"), ("eighteen seventy-three", "1873"), ("eighteen eighty-three", "1883"), ("nineteen seventies", "1970s"),
 ("nineteen seventy", "1970"), ("seven point four percent", "7.4%"), ("two thousand six hundred", "2,600"), ("nineteen ninety-three", "1993"),
 ("nineteen ninety-six", "1996"), ("eighty-two", "82"), ("twelve of them", "12 of them"), ("late two thousand one through two thousand four", "late 2001 through 2004"),
 ("two thousand three", "2003"), ("two thousand five and two thousand six", "2005 and 2006"), ("two thousand five", "2005"), ("two thousand six", "2006"),
 ("two thousand eight hundred thirty-eight", "2,838"), ("Two hundred thirty-two", "232"), ("eleven percent", "11%"), ("twenty-four percent", "24%"),
 ("four thousand five hundred ninety-six", "4,596"), ("two thousand one to two thousand eleven", "2001 to 2011"), ("seven point eight percent", "7.8%"),
 ("two point six percent", "2.6%"), ("sixty-seven percent", "67%"), ("one thousand and two thousand", "1,000 and 2,000"),
 ("two hundred fifty to four hundred twenty-eight", "250 to 428"), ("twenty twelve", "2012"), ("twenty thirteen", "2013"),
 ("twenty-seven", "27"), ("twenty fifteen", "2015"), ("twenty nineteen", "2019"), ("one million", "1 million"), ("Kept Alive", "KEPT ALIVE"),
 ("seven months", "7 months"), ("Four patients", "4 patients"), ("eighteen sixty-two", "1862"), ("nineteen ninety-one", "1991"), ("one hundred forty-three", "143"), ("sixty-seven uses", "67 uses"), ("two hundred wounded", "200 wounded"), ("twenty twenty", "2020"), ("eighteen eighty-three", "1883"),
]

META = dict(
    case=CASE, label="KEPT ALIVE · HOW IT WORKS",
    title="The Tourniquet",
    voice="am_fenrir",
    imgs={"esmarch_page": "/home/claude/imgs/esmarch_page.c.jpg", "esmarch_fig": "/home/claude/imgs/esmarch_fig.c.jpg"},
    mute_nat=["111605", "888808", "886668", "1000551", "855753", "610820", "741580", "arm_march", "arm_officers", "arm_map", "arm_field", "arm_medics", "arm_aid"],
    training=["111605", "888808", "886668", "1000551", "855753", "610820", "741580"],
    credit=("Footage: U.S. Marine Corps, U.S. Army, U.S. Air Force / AFN via DVIDS (public domain) — all training footage."
            r"\NArchival: War Department Training Film No. 71, National Archives 111-M-489 / Internet Archive. Illustration: Esmarch, 1883, National Library of Medicine copy."
            r"\NAppearance of U.S. government visual information does not imply or constitute endorsement."
            r"\NKEPT ALIVE is an independent channel, not affiliated with the DoD, NIH or CDC."
            r"\NFor education only. This is not medical advice."),
)
