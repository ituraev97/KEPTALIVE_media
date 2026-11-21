import sys,os,json
sys.path.insert(0,'/home/claude/work/scripts301')
from detect import boxes
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1]; files=sys.argv[2:]
tw,th=330,460; cols=7
rows=(len(files)+cols-1)//cols
S=Image.new('RGB',(cols*tw,rows*(th+20)),'white'); d=ImageDraw.Draw(S)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
res={}
for i,p in enumerate(files):
    W,H,bx=boxes(p); res[os.path.basename(p)]=bx
    im=Image.open(p).convert('RGB'); dd=ImageDraw.Draw(im)
    for k,b in enumerate(bx):
        dd.rectangle(b,outline='red',width=18); dd.text((b[0]+30,b[1]+30),str(k),fill='red',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',150))
    im.thumbnail((tw-6,th-6)); x=(i%cols)*tw; y=(i//cols)*(th+20)
    S.paste(im,(x+3,y+3)); d.text((x+3,y+th),os.path.basename(p),fill='blue',font=f)
S.save(out,quality=80)
json.dump(res,open(out+'.json','w'))
