import numpy as np
from PIL import Image
D='/workspace/projects/8ff64c4f-1e42-4bee-a321-ff12731f7d96/mintchoco-demo/p/set/'
def key(p):
  a=np.asarray(Image.open(p).convert('RGB')).astype(float)
  r,g,b=a[...,0],a[...,1],a[...,2]
  d=g-np.maximum(r,b)
  al=np.clip(1-(d-45)/(125-45),0,1)
  # despill only semi-transparent edges
  edge=(al<1)&(al>0)
  m=np.maximum(r,b); g2=np.where(edge|(d>20),np.minimum(g,m+8),g)
  out=np.dstack([r,g2,b,al*255]).astype(np.uint8)
  return Image.fromarray(out,'RGBA')
s=key('/workspace/work/g-scale.png'); s=s.crop(s.getbbox()); s.thumbnail((560,560)); s.save(D+'u-scale.png',optimize=True); print('scale',s.size)
k=key('/workspace/work/g-sacks.png'); W,H=k.size; print(W,H)
import numpy as np
A=np.asarray(k)[...,3]
rows=np.where(A.max(1)>40)[0]
# find vertical gaps
gaps=[y for y in range(1,H) if A[y].max()<=40 and A[y-1].max()>40]
print(gaps)
D2=D
regs=[(0,0,W,700),(0,700,W,1190),(0,1190,330,H),(330,1190,W,H)]
for i,b in enumerate(regs):
  c=k.crop(b); c=c.crop(c.getbbox()); c.thumbnail((320,320)); c.save(D2+f'u-sack{i+1}.png',optimize=True); print(i,c.size)
