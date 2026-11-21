import numpy as np
from PIL import Image
def refine(a,b,pad=60):
    # a: RGB int array; b box from block detector; tighten to pixel rows/cols that are mostly non-paper
    H,W,_=a.shape
    x0,y0,x1,y1=[max(0,b[0]-pad),max(0,b[1]-pad),min(W,b[2]+pad),min(H,b[3]+pad)]
    sub=a[y0:y1,x0:x1]
    nonpaper=((sub[...,0]-sub[...,2])<28)|(sub.mean(-1)<200)
    r=nonpaper.mean(1); c=nonpaper.mean(0)
    ys=np.where(r>0.5)[0]; xs=np.where(c>0.5)[0]
    if len(ys)<10 or len(xs)<10: return b
    return [x0+xs[0],y0+ys[0],x0+xs[-1],y0+ys[-1]]
