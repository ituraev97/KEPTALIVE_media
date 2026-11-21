import sys,os
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1]; files=sys.argv[2:]
tw,th=330,260; cols=7
rows=(len(files)+cols-1)//cols
S=Image.new('RGB',(cols*tw,rows*(th+22)),'white'); d=ImageDraw.Draw(S)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15)
for i,p in enumerate(files):
    im=Image.open(p); w,h=im.size; im.thumbnail((tw-6,th-6))
    x=(i%cols)*tw; y=(i//cols)*(th+22)
    S.paste(im,(x+3,y+3)); d.text((x+3,y+th),f"{os.path.basename(p)} {w}x{h}",fill='red',font=f)
S.save(out,quality=80)
