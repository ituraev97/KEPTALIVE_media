# Fact-check report: KEPT ALIVE · War Medicine Ep 1, "What Being Wounded in WWI Actually Felt Like"

**Checked on 2026-11-18 by the independent fact-checker.**

**What was reviewed:**
- `/home/claude/work/script_for_factcheck.md`: lines L001 to L273, with their VO, GFX, footage and lower thirds.
- `shorts_spec.py` and `make_cards.py`: the three Shorts and their cards.
- `packaging.md`: the titles and thumbnails.

**How it was checked:**
- About 60 source pages were opened directly. These include LOC, NPS, CRS, ABMC (×3), the Encyclopedia of Cleveland History, HMS, the AMEDD "Medical Operations" chapter, AMEDD nurse history ch. 3 and ch. 4, *Skilled and Resolute*, Heller/DTIC, Byerly/PHR, the National Guard article, nine KUMC essays, the UK National Archives (×2), Stanford Blood Center, *Invention & Technology*, JSOM, RJAH, *Stand To!*, Ellis 2015, Carey 2011, Pols & Oak 2007, Jones 2007, Jones 2014, NLM *Circulating Now*, AHCF (×2), the U. Illinois Press blog, the USAF Museum, DVIDS, NHHC, APTA, Borden, the WWI Museum (×2), ANCA (×2), Becker/WashU, Bruce 1920, IEEE Spectrum, the Association of Anaesthetists, *Psychiatric News*, the Pitt/Cannon article and the Army Chemical Corps history.
- Footage was checked against FOOTAGE_LOG plus the clip cut table in `/home/claude/work/excerpts.py`. Each clip's in-point maps to source start + offset. Frames were extracted from the three DVIDS clips and from the arg_mud, arg_mg, bac_aid and bac_barrage clips at the script's in-points.

---

## REQUIRED FIXES

### A. Factual errors

1. **L235: wrong state, and the next line's "She" points to the wrong person.**
   - **Problem:** Camp Grant is in **Illinois**, not Kentucky. The source says "Camp Sherman, Ohio, and Camp Grant, Illinois."
   - **Source:** AMEDD nurse history ch. 3, https://medcoeckapwstorprd01.blob.core.usgovcloudapi.net/pfw-images/dbimages/ATC%20ch%203.pdf
   - **Fix:** "Then, nine of them served at Army camps in Ohio and Illinois."
   - **Related fix to L236:** the line opens "She wrote:" straight after the Black-nurses line, so it reads as if one of those nurses said it. Change to: "Julia Stimson wrote: one need never tell me that women can't do as much, stand as much, and be as brave as men." Better still, move L236 to directly after L233.

2. **L241 (VO and GFX): the 46 French trains are misread.**
   - **Problem:** The AMEDD text says the Americans "had only seventeen of their own trains and three borrowed from the British." They then "borrowed forty-six more from the French." The 408 figure counts trainloads (151,045 patients "on 408 trains"). It is not a fleet of which 46 were French.
   - **Source:** https://medcoeckapwstorprd01.blob.core.usgovcloudapi.net/achh/chapter4_9849.pdf
   - **VO fix:** "During the Meuse-Argonne alone, four hundred and eight trainloads carried more than a hundred and fifty-one thousand patients. The Army had only seventeen hospital trains of its own, and borrowed forty-six from the French."
   - **GFX fix:** card 1 becomes h "408", t "Trainloads", s "17 U.S. trains + 46 borrowed from the French".

3. **L173 (VO and GFX): two separate events are merged.**
   - **Problem:** Evacuation Hospital No. 6's 1,100 admissions in one day came during the influenza epidemic, when it had 1,600 patients the next day against 900 nominal beds. Its record of 350 operations in a day is a separate event in the Meuse-Argonne.
   - **Source:** AMEDD ch. 4, same URL as fix 2.
   - **VO fix:** "In the Meuse-Argonne, Evacuation Hospital Number Six set a record: its surgeons operated on three hundred and fifty men in a single day."
   - **GFX fix:** c becomes "MEUSE-ARGONNE, 1918 · A RECORD · SOURCE: ARMY MEDICAL DEPARTMENT HISTORY". Drop "1,100 ADMISSIONS IN A DAY", or label it "DURING THE FLU EPIDEMIC".

4. **L196 (GFX and VO): the quote is altered.**
   - **Problem:** Carey's text reads "nothing original about (his) procedure." The script changes the editor's insertion to "[the]."
   - **Source:** Carey, *J Neurosurg* 2011, https://d1xe7tfg0uwul9.cloudfront.net/cbc-portal/wp-content/uploads/2013/07/01062011-JNS.pdf
   - **GFX fix:** q = "Aside, possibly, from the principle of track suction there is nothing original about [his] procedure."
   - **VO fix:** "...there is nothing original, he wrote, about his procedure."

5. **L232: "first letter" is wrong.**
   - **Problem:** The 12 April 1918 letter itself says "I last wrote April 6 just after I got my orders to move."
   - **Source:** https://beckerexhibits.wustl.edu/mowihsp/words/Stimson2fam04121918.htm
   - **Fix:** "In a letter home from Paris in April nineteen eighteen, a week into the new job, she was honest. I have been, she wrote, simply floundering."

6. **L157: the source does not say "mobile hospital."**
   - **Problem:** The source is a nurse's diary entry of 23 March 1918: "I received 68 on my floor, mostly mustard gas burns," from a convoy of "about 300 all 42nd div." The page does not say what kind of hospital it was.
   - **Source:** AMEDD nurse history ch. 4 pt 1, https://medcoeckapwstorprd01.blob.core.usgovcloudapi.net/pfw-images/dbimages/ATC%20ch%204%20pt%201.pdf
   - **Fix:** "In March nineteen eighteen, one Army nurse wrote in her diary that she received sixty-eight gassed men on her floor, mostly mustard burns, from a single convoy of about three hundred men of the Forty-Second Division."

7. **L208: the 4 a.m. inspection is not tied to Base Hospital 117.**
   - **Problem:** ANCA describes patients "standing at their bed side for inspection at 4:00 a.m." on psychiatric wards. It mentions Base Hospital 117 only in a different paragraph.
   - **Source:** https://e-anca.org/History/Topics-in-ANC-History/Psychiatric-Nursing-during-WWI
   - **Fix:** "On the Army's psychiatric wards, patients stood by their beds for inspection at four in the morning. Nurses were taught that the social atmosphere of the ward was all important."

8. **L137: "Of one patient" is wrong, and the start date conflicts.**
   - **Problem:** The UK National Archives quote describes a class of cases ("severe primary haemorrhage accompanied by shock"), not one patient. The date is also doubtful. The UK National Archives says spring 1917, but L. B. Robertson had already published on transfusions in war surgery in the *BMJ* in 1916.
   - **Source:** https://blog.nationalarchives.gov.uk/three-men-saved-countless-lives-blood-transfusion-first-world-war
   - **Fix:** "A Canadian doctor with a similar name, Lawrence Bruce Robertson, was already giving blood transfusions at the front. In men bleeding heavily and in shock, he reported an immediate and almost incredible improvement."

9. **L134: the paraphrase goes beyond the quote.**
   - **Problem:** Robertson wrote that the effect was "fully as striking." He did not say stored blood "worked fully as well."
   - **Source:** UK National Archives, same URL as fix 8.
   - **Fix:** "In a British medical journal in June nineteen eighteen, he reported that the effect of stored blood was fully as striking as that of fresh blood."

10. **L001: "in October… more than a million… are fighting" is wrong.**
    - **Problem:** NPS says 1.2 million "over 47 days." That is the total across the campaign, not the number fighting at one time. LOC gives more than 600,000 American and French troops at the start.
    - **Sources:** https://www.nps.gov/wwim/wwioverview.htm and https://www.loc.gov/exhibitions/world-war-i-american-experiences/about-this-exhibition/over-there/meuse-argonne/
    - **Fix:** "October, nineteen eighteen. In the Meuse-Argonne, in northeastern France, the American army is fighting its greatest battle. Over forty-seven days, more than a million Americans will take part."

11. **L152: "Most were British" is not supported.**
    - **Problem:** The source says only that the War Department "decided to purchase and issue British small-box respirators" because U.S. masks were not ready.
    - **Source:** https://www.press.uillinois.edu/wordpress/the-word-discomfort-is-a-weak-description/
    - **Fix:** "So every American carried a mask. At first they were British small box respirators, because American masks were not ready."

12. **L153 and L154: "They" now refers to the wrong thing.**
    - **Problem:** L153 (Gas Service, mustard share) sits between the masks line (L152) and "They worked, but they were miserable." As written, "They" refers to the Americans gassed.
    - **Fix:** Move L153 before L152, or change the opening of L154 to "The masks worked, but they were miserable."

13. **L162: British data is presented as general.**
    - **Problem:** The 2.5 per 100 figure is BEF data (4,086 deaths among 160,526 casualties).
    - **Source:** Jones, *War in History* 2014, https://pmc.ncbi.nlm.nih.gov/articles/PMC5131841
    - **Fix:** "In the British Army, later research found, mustard killed about two and a half of every hundred men it injured, the lowest death rate of the main war gases."

14. **L197: British data is presented as general.**
    - **Problem:** The figure comes from British case series: Fraser & Drummond 1917 (80% falling to 60%) and Ellis (50–60%).
    - **Sources:** *Stand To!* PDF and Ellis 2015.
    - **Fix:** "Some wounds stayed deadly no matter what. In British hospitals, even with surgery, more than half of the men with penetrating wounds of the abdomen died."

15. **L180 (VO and footer): the attribution is wrong.**
    - **Problem:** In *Stand To!*, the sentence "5–6 per cent of all wounds in 1915 to a little over 1 per cent in 1918" has no footnote and names no army. Butler is cited only for the separate 22% mortality figure.
    - **Source:** https://www.friendsofmillbank.org/downloads/Saving_Life_%26_Limb_Stand_To.pdf
    - **VO fix:** "And on the British front, by one historian's count, gas gangrene fell from about five or six percent of all wounds in nineteen fifteen to just over one percent in nineteen eighteen."
    - **GFX fix:** kicker "GAS GANGRENE · BRITISH FRONT"; footer "SOURCE: M. SCOTLAND, STAND TO! (WESTERN FRONT ASSOCIATION)"; right num "1%+".

16. **L179: Milligan was Australian.**
    - **Problem:** Gray and Milligan were the first to publish on wound excision in 1915, and Edward Milligan was a young Australian surgeon.
    - **Source:** *Stand To!*, same URL as fix 15.
    - **Fix:** "...and was written up by surgeons serving with the British forces in nineteen fifteen."

17. **L143 and L147 footers: wrong institution.**
    - **Problem:** armyheritage.org is published by the **Army Heritage Center Foundation** (a private nonprofit), not the U.S. Army Heritage and Education Center.
    - **Source:** https://www.armyheritage.org/soldier-stories-information/gas-warfare-in-world-war-i/
    - **Fix:** replace "U.S. ARMY HERITAGE AND EDUCATION CENTER" with "ARMY HERITAGE CENTER FOUNDATION."

18. **L077 footer: the cited source does not mention Arras.**
    - **Problem:** JSOM gives "15.6% of 1009 cases" but does not mention Arras. Arras, April–May 1917, is in *Stand To!* (citing Gray 1919).
    - **Sources:** https://www.jsomonline.com/Flipbook/Journals/1402-Summer/files/basic-html/page60.html and the *Stand To!* PDF.
    - **Fix:** footer "SOURCE: H. M. W. GRAY (1919) · VIA STAND TO! (WFA) AND J. SPECIAL OPERATIONS MEDICINE, 2014."

19. **L247 (VO and map title): "beds" is not the source's wording.**
    - **Problem:** ABMC says Army medical facilities "could treat 403,000 bed cases." It does not say "hold 403,000 bed patients" or "403,000 beds."
    - **Source:** https://abmc.gov/news-events/news/caring-sick-and-wounded-establishing-first-us-army-medical-units-france-and-england
    - **VO fix:** "By the end of the war, American hospitals in France could treat four hundred and three thousand bed cases."
    - **GFX fix:** title "403,000 BED CASES."

20. **L242: "for hours" is not in the source.**
    - **Problem:** The source says only that trains being sidetracked "led to preventable deaths."
    - **Source:** *Skilled and Resolute*, ch. 1, https://medcoeckapwstorprd01.blob.core.usgovcloudapi.net/pfw-images/dbimages/MASH%20Ch%201.pdf
    - **Fix:** "Sometimes a train was sidetracked on the way. The Army's own history admits that some of those delays cost lives."

21. **L049 and L050 (VO and GFX): the bearers' nationality is not stated.**
    - **Problem:** The KUMC stretcher-bearer essay never names a nationality. Its text comes from Mayhew's *Wounded*, a general Western Front book. The ten-week course, the teams of four to six, the blisters and the trench maps are not documented as A.E.F. practice.
    - **Source:** https://www.kumc.edu/school-of-medicine/academics/departments/history-and-philosophy-of-medicine/archives/wwi/essays/military-medical-operations/stretcher-bearers.html
    - **VO fix (L049):** "That was the work of the stretcher bearers. On the Western Front, they trained for ten weeks. They worked in teams of four to six. And they went forward unarmed."
    - **GFX fix (L049):** kicker "STRETCHER BEARERS · WESTERN FRONT."

### B. Unsupported inferences, superlatives, and causal claims (channel rule: associations are not causes)

22. **L033: the table does not show an "artillery war."**
    - **Problem:** In Heller's table, gas (31.5%) and "gun, misc." (33.4%) each exceed shrapnel plus shells (22.9%). The heading "gun, misc." is not defined.
    - **Source:** Heller, https://apps.dtic.mil/sti/tr/pdf/ADA189331.pdf
    - **Fix:** "Another third were listed only as gun wounds, with no weapon named. Other counts fill in the picture. This was an artillery war."

23. **L034: "gunshot" contradicts the category.**
    - **Problem:** Heller's category is "gun, misc.", weapon not named. Calling these deaths "gunshots" contradicts that.
    - **Fix:** "...thousands of deaths from fragments and gun wounds, against about twelve hundred from gas."

24. **L081: unsourced superlative.**
    - **Fix:** "Now you had to get to a surgeon. And between you and him were some of the most jammed roads of the war."

25. **L195: causal claim.**
    - **Problem:** The death rate fell in monthly series of only about 44 patients. "What practice under fire could do" claims the practice caused the fall.
    - **Fix:** "...But the numbers suggest what practice under fire could do."

26. **L206: "two that could end a man's career" has no source.**
    - **Fix:** "...shell fright, gas fright, hysteria, fatigue, malingering and cowardice. About two thirds were kept with their division."

27. **L270: the source wording is narrower.**
    - **Problem:** ABMC says the cemetery holds "the largest number of our military dead in Europe."
    - **Source:** https://abmc.gov/Meuse-Argonne
    - **Fix:** "In the Meuse-Argonne American Cemetery, which holds more American war dead than any other in Europe, fourteen thousand two hundred and forty-six Americans are buried."

### C. Footage and lower-third pairing

28. **L047: arg_mg is drill footage with no TRAINING label.**
    - **Problem:** arg_mg (111-H-1419, 3:08–3:44) is the 315th MG Battalion *practicing*. The frame at @6 shows men lying prone on a mound, which can read as casualties. The lower third, "A PATROL MOVES FORWARD · LORRAINE," is wrong for this clip.
    - **Fix:** Cut arg_mg and use bac_crawl only. If it stays, give it its own lower third: "MACHINE-GUN PRACTICE · 80TH DIVISION · TRAINING / ARCHIVAL FILM · 1918 · U.S. ARMY SIGNAL CORPS."

29. **L015: the lower third is wrong.**
    - **Problem:** bac_barrage is film 111-H-1299, Baccarat sector, Lorraine (March–June 1918). It is not St. Mihiel. At @4 the frame shows only woods and wire. Artillery footage under a line about a German *air raid* is also misleading.
    - **Fix:** Replace the shot with fis_tents alone, or relabel it "AMERICAN ARTILLERY · BACCARAT SECTOR, LORRAINE / ARCHIVAL FILM · 1918 · U.S. ARMY SIGNAL CORPS."

30. **L033: the lower third covers two films.**
    - **Problem:** bac_barrage is Lorraine; sm_barrage @30 is St. Mihiel infantry advancing behind a barrage.
    - **Fix:** "AMERICAN ARTILLERY · LORRAINE AND ST. MIHIEL / ARCHIVAL FILM · 1918 · U.S. ARMY SIGNAL CORPS."

31. **L001: the lower third does not match the first shot.**
    - **Problem:** The first shot, sm_barrage @2, is a St. Mihiel smoke barrage from September 1918. The lower third reads "THE MEUSE VALLEY · NOV. 1918."
    - **Fix:** Open on arg_pan only, or give the sm_barrage shot "ST. MIHIEL · SEPT. 1918."

32. **L066 and L079: the shots are not the aid-station dugout.**
    - **Problem:** bac_aid @26 and @32 (source 8:02 and 8:08) show U.S. ambulances on a road near Bertrichamp, not the dugout. The frames were checked.
    - **Fix:** lower third "AMBULANCES NEAR BERTRICHAMP · 42ND DIVISION / ARCHIVAL FILM · 1918 · U.S. ARMY SIGNAL CORPS." Alternatively, use bac_aid @14 (the dugout with the Red Cross flag).

33. **L154: two films share one lower third.**
    - **Problem:** The single lower third "BRITISH TRAINING FILM · TRAINING" covers am_gas, which is American Signal Corps footage of a gas alarm in the Aisne-Marne.
    - **Fix:** Give am_gas its own lower third, as in L158: "A GAS ALARM · AMERICAN TROOPS · AISNE-MARNE / ARCHIVAL FILM · 1918 · U.S. ARMY SIGNAL CORPS."

34. **L269: nh_unload has no French-army label.**
    - **Problem:** nh_unload is Norton-Harjes footage of French-army patients, but it plays under "STRETCHER BEARERS · 42ND DIVISION."
    - **Fix:** Add a second lower third, "AMERICAN VOLUNTEER DRIVERS WITH THE FRENCH / ARCHIVAL FILM · 1917–18 · RED CROSS / SIGNAL CORPS," or drop the clip.

35. **L090: "Their Fords" is not verified.**
    - **Problem:** Norton-Harjes sections used mixed vehicles.
    - **Fix:** "Their ambulances and their roads looked much the same."

36. **L097: possible German ambulance.**
    - **Problem:** The arg_mud frame at @2 shows a U.S.-marked ambulance, which is fine. By @6 a different vehicle with men in greatcoats appears. The NARA catalog notes a "German ambulance" in this sequence.
    - **Fix:** Trim the clip to end before about 4.0 s, or check the markings at full resolution.

37. **L163: burned-in caption contradicts the VO.**
    - **Problem:** 1029569 shows a burned-in caption, "SGT DEVIN WILLIAMS · NETWORK COMMUNICATIONS SYSTEMS SPECIALIST, 11TH SIGNAL BDE," from about 79.5 s. That is 2 s after the @77.5 in-point. It contradicts "Army medical units still drill."
    - **Fix:** End the second shot before 79.4 s, or use a different in-point.

38. **L268 (VO and lower third): the frames do not show medical testing.**
    - **Problem:** The 1029639 frames at @45 and @93 show prone soldiers with rifles writing on forms, and a low crawl dragging a sandbag. These look like Expert Soldier or Infantryman lanes, with no medical task visible. Calling it Field Medical Badge testing is not supported by the frames.
    - **VO fix:** "Today, soldiers testing for the Army's expert badges, including the Expert Field Medical Badge, are still tested on their skills in the field."
    - **Lower-third fix:** "TODAY: EXPERT BADGE TESTING (E3B) · TRAINING / FORT HOOD, TEXAS · NOV. 7, 2026 · U.S. ARMY."

39. **L140 and Short s2 line 4: the footage shows a Japanese Red Cross bus.**
    - **Problem:** 1029529 shows a **Japanese Red Cross** blood collection bus ("Blood Collection Bus No1," Japanese signage). The AFN Sasebo bug and the reporter credit "PO2 SYLVIE CARAFIOL REPORTING" are burned in near @2–5. Under "the U.S. military still relies on that idea," viewers will read the scene as a military blood program.
    - **Fix:** lower third "TODAY: A RED CROSS BLOOD DRIVE AT A U.S. NAVY BASE / SASEBO, JAPAN · OCT. 21, 2026 · AFN SASEBO (U.S. NAVY)." Start after the reporter credit, at 6 s or later.

40. **L039 and L040: the lines are in the wrong order.**
    - **Problem:** L039 cites gas-gangrene cases before L040 introduces gas gangrene, and L040's "some of them" no longer points back to L038's bacteria.
    - **Fix:** Swap the order to L038, L040, L039.

### D. Precision and wording

41. **L072: Thomas was a surgeon.**
    - **Problem:** RJAH calls Thomas a "Liverpool surgeon and bone-setter."
    - **Source:** https://www.rjah.nhs.uk/media/qmjhtqh4/the-thomas-splint.pdf
    - **Fix:** "...designed in Liverpool in the eighteen seventies by a surgeon and bone-setter named Hugh Owen Thomas."

42. **L088 and L087 callcard: "shell hole" is not in the source.**
    - **Problem:** The USAF Museum says "If stuck in a hole, a group of soldiers could lift one."
    - **Source:** https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/197425/ford-model-t-ambulance/
    - **VO fix:** "It was light enough that when it got stuck in a hole, a few soldiers could simply lift it out."
    - **Callcard fix:** "Light enough for soldiers to lift out of a hole."

43. **L012 map title: "the first Americans" is too broad.**
    - **Problem:** American volunteers and ambulance drivers were in France before these units.
    - **Fix:** title "THE FIRST A.E.F. HOSPITALS IN FRANCE."

44. **L005: "brand new" overstates.**
    - **Problem:** Direct transfusion predates the war. What was new in 1917 was stored blood used at the front, which is what the card already says.
    - **Fix:** "Blood transfusion is brand new on the battlefield."

45. **L262 attribution: "D. W." is not verified.**
    - **Problem:** The museum says only "the Chicago-based Dorrance Artificial Limb Company… in late 1918."
    - **Source:** https://www.theworldwar.org/learn/educator-resource/bespoke-bodies-educators-guide-digital-timeline
    - **Fix:** w = "ADVERTISEMENT, DORRANCE ARTIFICIAL LIMB CO., 1918 · VIA NATIONAL WWI MUSEUM AND MEMORIAL."

46. **L166: the distance is stated as fact.**
    - **Problem:** L093 says that at the start of the Argonne drive, evacuation hospitals were 30–60 km behind the *field hospitals*. That is much farther than 9–15 miles.
    - **Fix:** "On paper, the evacuation hospitals stood nine to fifteen miles behind the front."

### E. Shorts, titles, thumbnails

47. **s3 title, hook and card_156: estimate rule and causation.**
    - **Problem:** "4 in 5 died" is an early-war estimate (Gray via Watson). Channel rule: estimated or modelled numbers must say "estimated." "Then Came an Iron Splint" plus the card's "WITH THE SPLINT" implies the splint alone caused the fall. JSOM warns that ambulances and casualty clearing stations "cloud the effect."
    - **Title fix:** "An Estimated 4 in 5 Died of This WWI Wound. Then Came a Splint"
    - **Hook fix:** "~4 IN 5 DIED (EST.)<br>[THEN: A SPLINT]"
    - **card_156 fix:** "SPLINT IN WIDE USE"
    - **s3 line 3 fix:** "At Arras in nineteen seventeen, Henry Gray followed one thousand and nine of these fractures. About one in six died. Faster evacuation helped too."

48. **s1 line 2: wrong season framing.**
    - **Problem:** The 340,000 hospitalizations cover all of 1918. The autumn was the deadliest wave.
    - **Fix:** "Its deadliest wave hit in the autumn, during the Meuse-Argonne offensive."

49. **s1 card_45k: overstated comparison.**
    - **Problem:** "ABOUT AS MANY AS COMBAT" overstates 45,000 against 53,402 combat deaths.
    - **Source:** https://www.nationalguard.mil/News/Article-View/Article/1616713/flu-outbreak-killed-45000-us-soldiers-during-world-war-i
    - **Fix:** "NEARLY AS MANY AS COMBAT (53,402)." Matching VO change in L223 (optional): "...killed nearly as many soldiers as enemy fire did."

50. **Thumb A: "WOUND TO SURGERY" under "12 HRS" reads as the actual delay.**
    - **Problem:** Twelve hours was the surgeons' goal, not the time men actually waited.
    - **Fix:** label "GOAL: WOUND TO SURGERY."

51. **Thumb C: 70,552 is a hospital count.**
    - **Problem:** 70,552 counts gas cases treated in hospital (Heller). It does not count all Americans gassed: about 200 more died on the battlefield.
    - **Fix:** label "AMERICANS IN HOSPITAL FOR GAS." Keep the chip "1918 BRITISH TRAINING FILM", which already contains TRAINING.

Titles A, B and C are true and supported. No change is needed.

---

## VERIFIED OK (selected key claims, checked at source)

**Casualty totals and the Meuse-Argonne**
- LOC: 26,277 Americans died in the Meuse-Argonne, "the highest American death toll for any single battle in U.S. history."
- NPS: 53,402 battle deaths "in less than six months of fighting"; 1.2 million troops over 47 days.
- CRS: 53,402 battle deaths and 204,002 wounds not mortal.
- AMEDD ch. 4: 1,910,934 men in Europe in Nov. 1918; a Medical Department of 18,146 officers, 10,081 nurses and 145,815 enlisted men; 224,089 wounded.
- All four Ayres quotes (seven others; 6 per cent; five out of every six; pneumonia) match word for word.

**The first medical units and casualties**
- Base Hospital No. 4: left 6 May 1917; 26 officers, 64 nurses, 156 men; reached Rouen 25 May; 82,179 cases in 20 months; "first contingent" (Encyclopedia of Cleveland History). ABMC: "one of six mobilized immediately to assist the British Expeditionary Force."
- Genella: first combat casualty of the A.E.F., southwest of Arras, 14 July 1917 (ABMC).
- 4 Sept 1917 Camiers raid: "Lieutenant William T. Fitzsimmons and Privates Oscar C. Tugo, Rudolph Rubino, Jr., and Leslie G. Woods… the first A.E.F. casualties by enemy action" (AMEDD). HMS confirms "less than a full month" and "over 45,000 British and American" patients. Spelling differs: AMEDD has "Fitzsimmons", KUMC and HMS have "Fitzsimons", and KUMC has "Letugo." The current spelling is fine.

**Wound causes and gas (Heller)**
- Table 2: bayonets 235 (0.1%), rifle 9.1%, shrapnel 15.1%, shells 7.8%, gas 70,552 (31.5%).
- Hospital deaths: gun, misc. 7,474; shrapnel 1,985; shells 1,703; gas 1,221.
- 31.4% of wounded treated in hospital for gas; mustard caused 39% of gas casualties.
- 26 Feb 1918: 225 exposed, 85 casualties, 8 died. The Pershing quote is verbatim (from his Final Report).

**Other figures**
- WWI Museum: "60% of the battlefield casualties… caused by artillery shells."
- Kyler quote verbatim (Sgt., 1st Division).
- KUMC aid-station details: packet contents and sizes, two aid men per company, 40% walking, 500–1,000 yards, staffing, 12–30 patients, iodine, antitoxin, Thomas splint, eight card categories, 12 hours, night evacuation.
- KUMC sanitary train: 950 men, 12 horse-drawn and 36 motor ambulances; dressing station distances.
- KUMC triage: 82nd Division field hospitals 325–328 at Dieulouard, 8 hours, "first save lives," 14 days, six labels, 65% kept.
- KUMC: evacuation hospital 432 to 1,000 beds, 34/237 staff, 9–15 miles, ninety trucks or 30 rail cars, 2 surgeons + 1 anesthetist + 2 nurses, up to 14 teams, 35–40 operations a shift.
- KUMC: mobile hospitals 12 units, 1%, St. Mihiel plan 33,000/10/5/9.
- Ivens: 2,267 French soldiers / 107 / 25. BH28 gasoline-can incubator. BH28 3,601 X-rays (2,012 of extremities) and bare-hand burns.
- Bruce: 9 per 1,000 (Sept 1914) to 1.4 (Dec 1914).
- Model T: 20 hp, hand crank, 3 litters or 4 seated, 4,362 shipped. White ambulance: 4 litters, driver and corpsman, 20 mph.
- AMEDD timing: Soissons within six hours; St. Mihiel within three hours; 7 June 1918 Paris, 700 cases (about 500 not yet operated on, many died along the way).
- AMEDD workload: shock team at Field Hospital 27; Evacuation Hospital 7 on the four tables of Mobile Hospital No. 1; 72 hours at Evacuation Hospital 4; 1,500 waiting and 24-hour shifts for eight days at Soissons.
- AMEDD Meuse-Argonne: 907,910 km; 132,065 carried; 72,467 / 18,664 / 2,029; hospital deaths 4–5% rising to over 6.6%; St. Mihiel 282 shell-shock cases / 225 returned; four gas hospitals.
- Nurse history: "constantly jammed," "oftentimes impossible to remove the wounded until dark," 3–8 hours to a field hospital, 30–60 km.
- Thomas splint: 12 stages, team of three, introduced 1916, Jones was Thomas's nephew (UK National Archives); 1875 (RJAH); Gray roughly 80% and 15.6% of 1,009 at Arras, April–May 1917 (JSOM, *Stand To!*); Ellis on crawling out at night, about 5-day delayed closure, abdominal mortality 50–60%.
- Blood and shock:
  - The MRC 1917 shock definition is verbatim.
  - Cannon studied shock at Béthune; his conclusion was inadequate oxygen supply to the tissues.
  - KUMC on Hustin, Agote and Lewisohn; Rous and Turner; group O donors; glass bottles on ice.
  - UK National Archives on 26 days, *Lancet* 22 June 1918, "fully as striking," 20–40 points, DSO, 36 cases, "immediate and almost incredible improvement."
  - Stanford Blood Center: 22 units to 20 soldiers "too injured to withstand surgery."
  - *Invention & Technology*: the quote is verbatim, *BMJ* 22 June 1918.
- Gas and mustard:
  - NLM: 14,000 cases at British casualty clearing stations, about 500 died, delayed symptoms, clothing and leather, slow-healing burns.
  - AHCF: 22 April 1915; phosgene December 1915; mustard 12 July 1917; blisters up to four weeks.
  - Jones 2014: "most blinded servicemen recovered."
  - KUMC BH28: "crayoned cross," two-minute shower, "high morbidity, low mortality."
  - Crowell quote. Chemical Warfare Service created 28 June 1918.
- Dakin and Carrel: Nobel 1912; NYT headline wording; antibiotics in the 1940s.
- Curie: 20 vehicles, October 1914, 200 fixed units, Irène 17 (IEEE).
- Cushing: CCS 46, 54.5%, 40.9% and 28.8% by month, magnetized nail (Carey).
- Anaesthesia: Marshall on ether and chloroform; needles reused.
- Psychiatry: Salmon in May 1917, "as near the front as military exigency will permit," 3 weeks / Base Hospital 117 / 6 months, 27% in 1921 (Pols & Oak). Jones 2007: "less than 20%," "both inaccurate and misleading." *Psychiatric News*: "war neurosis."
- Influenza:
  - Byerly: 26% of the Army, more than 1 million sick, almost 30,000 deaths before reaching France, 9,500 to 120,000 beds.
  - Byerly and National Guard: 340,000 vs 227,000.
  - National Guard: 1,451 flu deaths and 45,000 by the end of 1918.
- Nurses:
  - ANCA: 403 and 170 in April 1917; 21,480 total, more than 10,000 overseas; none killed by enemy action; 272 died of disease; awards 28 / 69 / 3; Base Hospital 20 (2,275 patients for 500 beds) and Base Hospital 10 (1,400 in its first week); Stimson's career and quote.
  - Becker: "simply floundering."
  - ABMC: McDonald; Stimson's "rows and rows."
  - Army School of Nursing: 25 May 1918, 11,000 applications, Goodrich.
- Rest of the chain and the return home:
  - *Skilled and Resolute*: two tables per team, 400 per train against 4 per ambulance, 12th Evacuation Hospital at Royaumeix (2,700 patients in 56 days, 1,000 seriously wounded, arrivals after the armistice).
  - Base Hospital 28 about 200 miles from the front (KUMC).
  - USS *Mercy*: 4 round trips from 3 Nov. 1918, 1,977 by 25 March 1919 (NHHC).
  - Walter Reed: 80 beds, 121 patients, 2,500 beds, 13,752 admissions, more than 2,000 flu admissions and more than 150 deaths, *The Come-Back* from Dec. 1918 (Borden).
  - WWI Museum: over 4,400 prosthetic cases, 94% of firms used wood, Walter Reed's prosthetic lab, Dorrance's "Arm that Arms You."
  - APTA: 14-hour days; active military status some 60 years later.
  - Meuse-Argonne cemetery: 14,246 graves.

**Rules check**
- No VO line gives dosages or medical advice, and the closing disclaimer is present.
- No patient is named. The named people are staff and historical figures from official or published histories.
- The British gas film is labelled TRAINING · BRITISH throughout.
- The DVIDS CBRN and E3B clips carry TRAINING, but see fixes 37 and 38.

## COULD NOT VERIFY

- **L184–L186 (D. F. Jones, *Annals of Surgery* 1918):** the PMC page (PMC10211230) was blocked when the permission prompt timed out. The quote, the 80% closed within 10 days, and British patients arriving after about 3 days rest on research note A only. Check on PMC before air.
- **L022 / L263:** the Borden *Rehabilitation of the Injured Combatant* page (35 general + 18 base hospitals, "complete physical and functional restoration") was not opened. These rest on research note A.
- **L244:** "the Army turned the grand hotels into hospital wards" at Vichy. No narrative source was opened. It is consistent with the V2 caption "Hotel des Bains, part of Vichy hospital center."
- **L166:** "where most wounded Americans had their real operation." This is a reasonable reading of KUMC, but the phrase is not in the source.
- **L168:** "in a big push." KUMC says teams "could be up to fourteen" by mid-1918, without saying a push.
- **L170:** "arrived without its operating equipment" and "next door." AMEDD confirms only that the surgeons used "the four tables of Mobile Hospital No. 1."
- **L153:** Gas Service "set up in France in July 1917." General Order 8 of 5 July 1917 created the post of Chief of the Gas Service; the organization was formalized on 3 Sept 1917. This is acceptable as written.
- **L016 GFX:** "Pvt. Rudolph Rubino Jr." and the middle initials match AMEDD ch. 4. KUMC spells the first private "Oscar Letugo." The current spelling follows the official history and is fine.
- **Footage, whole duration:** every DVIDS and archival shot should still be checked at full resolution over its whole on-air duration. Only frames at the in-points were checked here; the footage log itself warns that its 4-second contact sheets can miss short inserts.
