import sys,json,os
sys.path.insert(0,'/home/claude/work/scripts301')
import numpy as np
from PIL import Image
from refine import refine
src,boxjson,outd=sys.argv[1:4]
bx=json.load(open(boxjson)); os.makedirs(outd,exist_ok=True)
for f,bl in bx.items():
    im=Image.open(os.path.join(src,f)).convert('RGB'); a=np.asarray(im).astype(int)
    for k,b in enumerate(bl):
        r=refine(a,b); m=8
        c=im.crop((r[0]+m,r[1]+m,r[2]-m,r[3]-m))
        c.save(f"{outd}/{f[:-4]}_{k}.jpg",quality=92)
