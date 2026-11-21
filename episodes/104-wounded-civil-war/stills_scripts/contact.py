import json,sys
from PIL import Image,ImageDraw,ImageFont
d=json.load(open('/home/claude/work/stills301/index.json'))
tw,th=300,190; cols=8; rows=(len(d)+cols-1)//cols
S=Image.new('RGB',(cols*tw,rows*(th+30)),'white'); dr=ImageDraw.Draw(S)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11)
for i,x in enumerate(d):
    im=Image.open('/home/claude/work/stills301/'+x['file']).convert('RGB'); im.thumbnail((tw-6,th-6))
    X=(i%cols)*tw; Y=(i//cols)*(th+30)
    S.paste(im,(X+3,Y+3))
    col='red' if not x['safe'] else 'black'
    n=x['file'][:-4]; dr.text((X+3,Y+th-2),n[:44],fill=col,font=f); dr.text((X+3,Y+th+11),n[44:88]+(' [UNSAFE]' if not x['safe'] else ''),fill=col,font=f)
S.save('/home/claude/work/stills301/contact.jpg',quality=82); print(S.size)
