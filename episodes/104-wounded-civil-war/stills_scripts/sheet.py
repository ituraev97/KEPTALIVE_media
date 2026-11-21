import sys,os
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1]; files=sys.argv[2:]
tw,th=300,400; cols=8
rows=(len(files)+cols-1)//cols
S=Image.new('RGB',(cols*tw,rows*(th+20)),'white'); d=ImageDraw.Draw(S)
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
except: f=None
for i,p in enumerate(files):
    im=Image.open(p); im.thumbnail((tw-6,th-6))
    x=(i%cols)*tw; y=(i//cols)*(th+20)
    S.paste(im,(x+3,y+3)); d.text((x+3,y+th),os.path.basename(p),fill='red',font=f)
S.save(out,quality=80)
