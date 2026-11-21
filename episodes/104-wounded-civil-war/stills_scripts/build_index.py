import json,os,shutil,glob
from PIL import Image
D='/home/claude/work/dl301'; O='/home/claude/work/stills301'
os.makedirs(O,exist_ok=True)
hwids={}
for f in glob.glob(D+'/hw/pg/sim_*.jpg'):
    b=os.path.basename(f)[:-4]; import re
    m=re.match(r'(.*_(\d{4}-\d{2}-\d{2})_.*)_(\d+)$',b); hwids[f"{m.group(2)}_{m.group(3)}"]=(m.group(1),m.group(3))
groups={
 'out7':('m7',"The Photographic History of the Civil War, Vol. 7 'Prisons and Hospitals' (F. T. Miller, ed.; Review of Reviews Co., 1911) - archive.org millersphotographic07franrich",'Miller vol.7 photo'),
 'out2':('m2',"The Photographic History of the Civil War, Vol. 2 'Two Years of Grim War' (Miller, 1911) - archive.org photographichist02mill",'Miller vol.2 photo (Antietam/Gettysburg)'),
 'outms':('ms',"The Medical and Surgical History of the War of the Rebellion, Part III Vol. II (Surgical), 1883, Chap. XV 'Transportation of the Wounded' (U.S. Government) - archive.org MSHWRSurgical3",'MSHWR engraving (ambulances/trains/steamers)'),
 'outmd':('md',"The Medical and Surgical History of the War of the Rebellion, Part III Vol. I (Medical), 1888, section 'The General Hospitals' (U.S. Government) - archive.org MSHWRMedical3",'MSHWR hospital plan'),
 'outhw':('hw',"Harper's Weekly",'Harper\'s Weekly engraving'),
 'outp':('p',None,'portrait / Letterman book / Miller vol.9'),
}
psrc={26:("The Photographic History of the Civil War, Vol. 9 'Poetry and Eloquence' (Miller, 1911) - archive.org millersphotographic09franrich",'n26'),
 138:("Miller, Photographic History Vol. 9 (1911) - archive.org millersphotographic09franrich",'n138'),
 140:("Miller, Photographic History Vol. 9 (1911) - archive.org millersphotographic09franrich",'n140'),
 'c7':("L. P. Brockett & M. C. Vaughan, Woman's Work in the Civil War (Philadelphia: Zeigler, McCurdy & Co., 1867), frontispiece - archive.org womanswork00brocrich",'n7'),
 'b167':("Brockett & Vaughan, Woman's Work in the Civil War (1867), plate facing p.~165 - archive.org womanswork00brocrich",'n167'),
 'g7':("Jonathan Letterman, Medical Recollections of the Army of the Potomac (New York: D. Appleton, 1866) - archive.org medicalrecollec00dgoog (Google/Bodleian scan)",'n7'),
 'b6':("Letterman, Medical Recollections of the Army of the Potomac (1866) - archive.org b28709299 (Wellcome copy)",'n6'),
 't8':("Letterman, Medical Recollections of the Army of the Potomac (1866) - archive.org medicalrecollect00lettuoft (Toronto copy)",'n8')}
idx=[]
for g,(ident,src,cat) in groups.items():
    meta=json.load(open(f"{D}/{g}/_meta_{ident}.json"))
    for m in meta:
        fp=f"{D}/{g}/{m['file']}"
        if not os.path.exists(fp): continue
        shutil.copy(fp,f"{O}/{m['file']}")
        w,h=Image.open(fp).size
        leaf=m['leaf']
        if g=='outhw':
            iid,lf=hwids[leaf]; s=f"Harper's Weekly, {m['date']} - archive.org {iid}, leaf n{lf}"; date=m['date'].split(', ',1)[1] if ', ' in m['date'] else m['date']
            date="published "+m['date'].replace("Harper's Weekly, ","")
        elif g=='outp':
            s0,l=psrc[leaf]; s=f"{s0}, leaf {l}"; date=m['date']
        else:
            s=f"{src}, leaf n{leaf}"; date=m['date']
        note=m['note']; safe=not note.lower().startswith(('check','borderline')) and 'editor' not in note and 'use with care' not in note
        idx.append(dict(file=m['file'],category=cat,subject=note.split(':',1)[1].strip() if ':' in note and note.startswith('safe') else note,
            caption_original=m['caption'],source=s,date_of_image=date,event=m['event'],
            safe=safe,safe_note=note,width=w,height=h,ge1600=w>=1600,public_domain="pre-1930 publication / U.S. Government work"))
json.dump(idx,open(f"{O}/index.json",'w'),indent=1,ensure_ascii=False)
print(len(idx))
