import sys,json,os
sys.path.insert(0,'/home/claude/work/scripts301')
import numpy as np
from PIL import Image
from refine import refine
from detect import boxes
spec=__import__(sys.argv[1]).S; src=sys.argv[2]; outd=sys.argv[3]; ident=sys.argv[4]; bk=json.load(open(sys.argv[5])) if len(sys.argv)>5 else {}
os.makedirs(outd,exist_ok=True); meta=[]
for name,leaf,box,rot,cap,date,ev,note in spec:
    p=f"{src}/l{leaf}.jpg"; im=Image.open(p).convert('RGB'); W,H=im.size
    if box[0]=='auto':
        b=bk[f"l{leaf}.jpg"][box[1]]; r=refine(np.asarray(im).astype(int),b); m=8
        c=im.crop((r[0]+m,r[1]+m,r[2]-m,r[3]-m))
    else:
        c=im.crop((int(box[0]*W/100),int(box[1]*H/100),int(box[2]*W/100),int(box[3]*H/100)))
    if rot: c=c.rotate(rot,expand=True)
    c.save(f"{outd}/{name}.jpg",quality=92)
    meta.append(dict(file=name+".jpg",leaf=leaf,caption=cap,date=date,event=ev,note=note,size=c.size))
json.dump(meta,open(f"{outd}/_meta_{ident}.json","w"),indent=1)
print(len(meta))
