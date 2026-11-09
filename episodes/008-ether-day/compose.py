from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import sys
def compose(src, out, rot=0, crop=None, fill=0.92, autocrop=True):
    im = Image.open(src).convert("RGB")
    if rot: im = im.rotate(rot, expand=True)
    if crop: w,h=im.size; im = im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    W,H = 3840,2160
    bg = ImageOps.fit(im,(W//8,H//8)).filter(ImageFilter.GaussianBlur(6)).resize((W,H))
    bg = ImageEnhance.Brightness(bg).enhance(0.35)
    s = min(W*0.94/im.width, H*fill/im.height)
    fg = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
    bg.paste(fg, ((W-fg.width)//2, (H-fg.height)//2))
    bg.save(out, quality=92)
if __name__ == "__main__":
    pass
