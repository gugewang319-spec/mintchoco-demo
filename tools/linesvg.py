# 线稿 PNG → 单色 SVG（pip install potracer）。用法：改末尾文件名后 python3 tools/linesvg.py
import potrace,numpy as np,sys
from PIL import Image,ImageFilter
def vec(src,out,thr=70,scale=1):
  g=Image.open(src).convert('L')
  bg=np.percentile(np.array(g),90)
  a=np.array(g.filter(ImageFilter.GaussianBlur(.6))).astype(float)
  m=(bg-a)>thr*(bg/255)
  ys,xs=np.where(m);y0,y1,x0,x1=ys.min()-4,ys.max()+4,xs.min()-4,xs.max()+4
  m=m[y0:y1,x0:x1]
  pl=potrace.Bitmap(~m).trace(turdsize=6,turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY,alphamax=1.0,opticurve=True,opttolerance=0.3)
  d=[]
  for c in pl:
    s=c.start_point;p=[f'M{s.x:.1f} {s.y:.1f}']
    for seg in c.segments:
      if seg.is_corner:p.append(f'L{seg.c.x:.1f} {seg.c.y:.1f}L{seg.end_point.x:.1f} {seg.end_point.y:.1f}')
      else:p.append(f'C{seg.c1.x:.1f} {seg.c1.y:.1f} {seg.c2.x:.1f} {seg.c2.y:.1f} {seg.end_point.x:.1f} {seg.end_point.y:.1f}')
    d.append(''.join(p)+'Z')
  h,w=m.shape
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><path fill="#2f7d64" fill-rule="evenodd" d="{"".join(d)}"/></svg>'
  open(out,'w').write(svg);print(out,w,h,len(svg))
for f in ['l-sprig','l-latte','l-emblem','l-flourish','l-pitcher']:
  vec(f+'.png',f+'.svg',thr=55)
