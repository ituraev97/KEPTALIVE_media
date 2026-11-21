import sys,os
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1]; files=sys.argv[2:]
tw,th=560,790; cols=4
rows=(len(files)+cols-1)//cols
S=Image.new('RGB',(cols*tw,rows*(th+24)),'white'); d=ImageDraw.Draw(S)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
fs=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11)
for i,p in enumerate(files):
    im=Image.open(p).convert('RGB'); im=im.resize((tw-10,th-10)); dd=ImageDraw.Draw(im)
    W,H=im.size
    for k in range(1,20):
        c=(255,0,0) if k%2==0 else (0,160,255)
        dd.line([(0,H*k/20),(W,H*k/20)],fill=c,width=1); dd.line([(W*k/20,0),(W*k/20,H)],fill=c,width=1)
        if k%2==0: dd.text((2,H*k/20-12),str(k*5),fill='red',font=fs); dd.text((W*k/20+2,2),str(k*5),fill='red',font=fs)
    x=(i%cols)*tw; y=(i//cols)*(th+24)
    S.paste(im,(x+5,y+5)); d.text((x+5,y+th),os.path.basename(p),fill='blue',font=f)
S.save(out,quality=85)
