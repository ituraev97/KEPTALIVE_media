import sys,json
import numpy as np
from PIL import Image
from scipy import ndimage
def boxes(path,B=20,thr=170,minfrac=0.03):
    im=Image.open(path).convert('L'); a=np.asarray(im,dtype=np.float32)
    H,W=a.shape; h,w=H//B,W//B
    m=a[:h*B,:w*B].reshape(h,B,w,B).mean(axis=(1,3))
    sd=a[:h*B,:w*B].reshape(h,B,w,B).std(axis=(1,3))
    mask=(m<thr)
    mask=ndimage.binary_closing(mask,iterations=2)
    mask=ndimage.binary_opening(mask,iterations=2)
    mask=ndimage.binary_fill_holes(mask)
    lab,n=ndimage.label(mask); out=[]
    for sl in ndimage.find_objects(lab):
        y0,y1=sl[0].start*B,sl[0].stop*B; x0,x1=sl[1].start*B,sl[1].stop*B
        if (y1-y0)*(x1-x0) > minfrac*H*W and (x1-x0)>W*0.15 and (y1-y0)>H*0.06:
            out.append([x0,y0,x1,y1])
    out.sort(key=lambda b:(b[1],b[0]))
    return W,H,out
if __name__=='__main__':
    for p in sys.argv[1:]:
        print(p,boxes(p))
