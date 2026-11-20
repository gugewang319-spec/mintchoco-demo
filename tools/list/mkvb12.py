import re
import os
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../p/list/')  # 读 p/list/index.html，写出 vb12.html
s=open(P+'index.html').read()
s=s.replace('<title>','<title>vb12 · ',1) if '<title>' in s else s
CSS=r'''
<style>
/* vb10：聊天列表 = 一列迷你聊天室（通用组件：饮品卡 / 奶冻·果冻气泡 / 巧克力计数牌） */
.list{padding:0 16px 170px!important}
.sec{display:flex;align-items:baseline;gap:8px;margin:30px 4px 4px}
.sec b{font:20px/1 ZK;color:#5b3a2c;letter-spacing:.08em}.sec small{font:12px/1 ZK;color:#8a6b5c;letter-spacing:.06em}
.sec small em{font:700 13px/1 Baloo,ZK;font-style:normal;color:#8a5c46}
.thr{display:flex;flex-direction:column}
.day{display:flex;flex-direction:column;position:relative;margin-top:14px}
.dh{align-self:center;display:flex;align-items:center;gap:8px;margin:12px 0 4px}
.dh .counter{margin:0!important}
.dh small{font:12px/1 ZK;color:#8a6b5c;letter-spacing:.06em}.dh small em{font:700 13px/1 Baloo,ZK;font-style:normal;color:#8a5c46;margin-right:2px}
.day .me,.day .him{max-width:80%}
.day .me{margin-top:8px}
.bub{font:15px/1.7 var(--body)!important}
.unsaid{align-self:flex-start;margin:6px 0 0 6px;font:13px/1.5 var(--body);color:#6b4a3c;filter:blur(3.2px);transition:filter .45s cubic-bezier(.23,1,.32,1);background:none;border:0;padding:0;text-align:left}
.unsaid.on{filter:none}.unsaid i{font:11px/1 ZK;font-style:normal;color:#2f6e58;margin-right:6px;letter-spacing:.06em}
.dry{opacity:.55}.dry .counter{filter:saturate(.6)}
/* 饮品卡（组件页 02，原样） */
.dcups{display:grid;gap:12px;margin-top:10px}
.dcup{position:relative;z-index:2;display:block;width:100%;text-align:left;overflow:hidden;isolation:isolate;border-radius:18px 18px 22px 22px;padding:11px 14px 24px;background:#fffaf0;box-shadow:0 0 0 1.5px #8a5c46,inset 0 0 0 4px #fffaf0,inset 0 0 0 5.2px rgba(159,211,191,.9)}
.dcups .dcup:nth-child(even){width:94%;margin-left:6%}
.dcup .t{position:relative;z-index:3;display:flex;justify-content:space-between;align-items:center;font:12px/1 ZK;color:#8a5c46;letter-spacing:.14em}
.dcup .t em{font:700 13px/1 Baloo,ZK;font-style:normal;color:#2f6e58;letter-spacing:0}
.dcup p{position:relative;z-index:3;margin-top:7px;font:14px/1.5 var(--body);color:#4a3027}
.dcup .lq{position:absolute;z-index:1;left:0;right:0;bottom:0;height:var(--h,36%);background:var(--lc);transition:height .5s cubic-bezier(.3,1.6,.5,1)}
.dcup .lq::before{content:"";position:absolute;left:0;right:0;top:-7px;height:8px;background:var(--wv) repeat-x 0 0/56px 8px;animation:dwv var(--wd,6s) linear infinite}
.dcup.slosh .lq{animation:dslo .7s}
@keyframes dwv{to{background-position:56px 0}}
@keyframes dslo{30%{transform:skewY(-3deg)}60%{transform:skewY(2deg)}}
.dcup.cocoa{--lc:rgba(150,98,72,.30);--wv:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='8'%3E%3Cpath d='M0 4 Q14 0 28 4 T56 4 V8 H0Z' fill='rgba(150,98,72,.30)'/%3E%3C/svg%3E")}
.dcup.boba{--h:42%;--wd:7.4s;--lc:rgba(214,170,128,.34);--wv:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='8'%3E%3Cpath d='M0 4 Q14 1 28 4 T56 4 V8 H0Z' fill='rgba(214,170,128,.34)'/%3E%3C/svg%3E")}
.dcup.soda{--h:100%;--lc:linear-gradient(180deg,rgba(166,217,196,.08),rgba(140,205,180,.42))}
.dcup.soda .lq::before{display:none}
.dcup .mm{position:absolute;z-index:2;bottom:5px;width:13px;height:11px;border-radius:4px;background:#fffdf7;box-shadow:0 0 0 1px rgba(107,74,59,.55);animation:dbob var(--d,3.4s) ease-in-out infinite alternate}
.dcup .pe{position:absolute;z-index:2;bottom:5px;width:11px;height:11px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#a57658 0 14%,#4b2c1f 60%);animation:dbob var(--d,3.4s) ease-in-out infinite alternate}
.dcup .sb{position:absolute;z-index:2;width:7px;height:7px;border-radius:50%;box-shadow:0 0 0 1px rgba(47,110,88,.45);background:rgba(255,255,255,.6);animation:dup var(--d,4s) linear infinite}
@keyframes dup{from{transform:translateY(0);opacity:0}15%{opacity:1}to{transform:translateY(-70px);opacity:0}}
@keyframes dbob{from{translate:0 0}to{translate:0 -2px}}
.dcup.boba.slosh .pe{animation:djp .6s cubic-bezier(.3,1.6,.5,1)}
@keyframes djp{40%{transform:translateY(-16px)}}
/* 今天：大一号的饮品卡，顶上淋巧克力酱（同聊天室奶冻的酱） */
.today{padding:30px 16px 30px;overflow:visible!important}
.today .sauce{border-radius:18px 18px 0 0}
.today .t{font-size:13px}.today .t em{font-size:15px}
.today p{font-size:17px;line-height:1.55;margin-top:10px}
.today p.m{font-size:14px;color:#24443a;text-align:right;margin-top:6px}
.today p.m i,.today p.h i{font:11px/1 ZK;font-style:normal;color:#8a5c46;letter-spacing:.12em;margin-right:6px}.today p.m i{color:#2f6e58}
.today .shell{display:none}
.tlink{position:relative;z-index:3;display:inline-block;margin-top:8px;font:12px/1 ZK;color:#8a5c46;letter-spacing:.06em;border-bottom:1px dashed #8a5c46;padding-bottom:3px}
/* 装饰冰块（借聊天页冰块的弹簧漂浮） */
.icd{position:absolute;pointer-events:none;z-index:1;aspect-ratio:546/583}
.icd .im{opacity:.9}

/* vb12：行底全部用 CSS/SVG 画，不用位图。他最后说话＝奶冻慕斯条，我最后说话＝薄荷慕斯条；左边一截蘸巧克力写日期，右边计数牌，底部夹层，角上画的小料 */
.wrows{display:flex;flex-direction:column;gap:16px;margin-top:8px}
.wrow{position:relative;z-index:2;display:flex;align-items:stretch;width:100%;min-height:84px;padding:0;margin:0;border:0;text-align:left;border-radius:20px 22px 22px 20px;overflow:visible;transform-origin:50% 60%;
 background:
  radial-gradient(60% 55% at 30% 18%,rgba(255,255,255,.8),rgba(255,255,255,0) 70%),
  radial-gradient(circle,rgba(122,80,58,.26) 1.1px,transparent 1.6px) right 14px bottom 16px/9px 9px no-repeat,
  radial-gradient(circle,rgba(122,80,58,.2) 1px,transparent 1.5px) right 30px bottom 22px/8px 8px no-repeat,
  radial-gradient(circle,rgba(122,80,58,.22) 1px,transparent 1.5px) right 22px bottom 30px/8px 8px no-repeat,
  linear-gradient(180deg,rgba(255,251,243,.97),rgba(246,234,216,.94));
 box-shadow:inset 0 -12px 0 #cfe9dc,inset 0 -14px 0 #fff8ee,inset 0 -17px 0 #e8d3bb,inset 0 2px 0 #fff,0 12px 20px -14px rgba(74,48,39,.55)}
.wrow.mt{background:
  radial-gradient(55% 50% at 28% 20%,rgba(255,255,255,.75),rgba(255,255,255,0) 70%),
  radial-gradient(circle,rgba(255,255,255,.9) 1.3px,transparent 1.9px) right 16px bottom 18px/10px 10px no-repeat,
  radial-gradient(circle,rgba(255,255,255,.75) 1px,transparent 1.6px) right 34px bottom 26px/8px 8px no-repeat,
  linear-gradient(180deg,rgba(214,240,229,.97),rgba(170,220,199,.94));
 box-shadow:inset 0 -12px 0 #8a5c46,inset 0 -14px 0 #f3e3cc,inset 0 -17px 0 #93ccb5,inset 0 2px 0 rgba(255,255,255,.9),0 12px 20px -14px rgba(47,110,88,.6)}
.wrow:nth-child(4n+2),.wrow:nth-child(4n+3){width:95%;margin-left:5%}
.wrow .dip{position:relative;flex:none;width:62px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 8px 14px 0;color:#fff6e8}
.wrow .dip svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.wrow .dip svg .s{fill:#5b3a2c;stroke:#3b2219;stroke-width:1.1;stroke-linejoin:round}
.wrow .dip svg .h{fill:none;stroke:rgba(255,236,220,.55);stroke-width:1.6;stroke-linecap:round}
.wrow .dip svg .sp{fill:#cfe9dc}
.wrow .dip b{position:relative;font:800 25px/1 Baloo;text-shadow:0 1px 0 rgba(30,16,10,.5)}
.wrow .dip small{position:relative;margin-top:4px;font:10px/1 ZK;color:#d8f1e6;letter-spacing:.06em;white-space:nowrap}
.wrow .tx{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:center;gap:3px;padding:12px 4px 24px 6px}
.wrow .h{font:15px/1.5 var(--body);color:#4a3027;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-wrap:pretty}
.wrow .m{font:13px/1.4 var(--body);color:#8a6b5c;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.wrow.mt .h{color:#24443a}.wrow.mt .m{color:#3f6b5c}
.wrow .m i{font:600 10px/1 var(--body);font-style:normal;margin-right:4px;letter-spacing:.08em}
.wrow .ct{flex:none;align-self:flex-start;margin:12px 12px 0 0;display:inline-flex;gap:2px;padding:3px;border-radius:5px;background:#5b3a2c;box-shadow:0 2px 3px -1px rgba(74,48,39,.4)}
.wrow .ct span{min-width:11px;padding:1px 2px;border-radius:2px;background:#fdf9f0;font:700 13px/1.3 Baloo;text-align:center;color:#4a3027}
.wrow .ct b{align-self:center;font:12px/1 ZK;color:#fdf9f0;padding:0 2px}
.gar svg{display:block;width:100%;height:auto;overflow:visible}
.wrow .unsaid{margin:4px 0 0;font-size:12px}
.wrow:active{transform:scale(.98)}
.today p.m i,.today p.h i{font-family:var(--body)!important;font-weight:600}
.nil{display:flex;align-items:center;gap:8px;margin:2px 0 2px 18px;font:12px/1 ZK;color:#8a6b5c;letter-spacing:.06em}
.nil b{font:700 13px/1 Baloo;color:#a88a7a}
.nil::before{content:"";width:22px;height:8px;border-radius:3px;background:#c9ad9a;opacity:.6}
.dcups .dcup{padding-bottom:30px}.dcups .dcup p{text-wrap:pretty}
.dcup{--h:24%!important}.dcup.soda{--h:30%!important}
.today{--h:22%!important;padding-bottom:40px!important}
.today .unsaid{margin:10px 0 0;position:relative;z-index:3}

@media (prefers-reduced-motion:reduce){.dcup .lq::before,.dcup .sb,.dcup .mm,.dcup .pe{animation:none!important}}
</style>'''
s=s.replace('</head>',CSS+'</head>',1)

# ----- content
def counter(d):
  a,b=d.split('/');a=a.rjust(2,'0');b=b.rjust(2,'0')
  return f'<p class="counter" aria-label="{d}"><span>{a[0]}</span><span>{a[1]}</span><b>/</b><span>{b[0]}</span><span>{b[1]}</span></p>'
WEEK=[('11/10','周二',12,'你说明天会不会下雪呀','要是真下雪，我去楼下给你堆一只小猫',None),
('11/9','周一',8,'今天的会开了三个小时，脑袋好空','那今晚什么都不想，陪你发呆','要不要打个电话呀'),
('11/8','周日',9,'那家的薄荷冰淇淋超好吃','下次还去，换你点单',None),
('11/7','周六',0,'','',None),
('11/6','周五',2,'晚安～','晚安',None),
('11/5','周四',0,'','',None)]
OLD=[('cocoa','10/29 – 11/4',5,'万圣节那天他给你讲了一个超吓人的故事'),('boba','10/22 – 10/28',3,'这周你一直在忙期中'),('soda','10/15 – 10/21',4,'第一次一起看的那部电影'),('boba','10/8 – 10/14',2,'你说秋天最适合喝热可可')]
def extras(kind,seed):
  import random;r=random.Random(seed);o=''
  if kind=='cocoa':
    for k,l in enumerate([62,70,78]):o+=f'<i class="mm" style="left:{l}%;--d:{r.uniform(2.8,4.6):.1f}s;{"bottom:8px;rotate:18deg;" if k==1 else ""}"></i>'
  elif kind=='boba':
    for k,l in enumerate([14,30,46,62]):o+=f'<i class="pe" style="left:{l}px;--d:{r.uniform(2.8,4.6):.1f}s;{"bottom:8px" if k%2 else ""}"></i>'
  else:
    for l,d,dl in [(30,3.6,0),(52,4.6,1.2),(70,3.1,2)]:o+=f'<i class="sb" style="left:{l}%;bottom:6px;--d:{d}s;animation-delay:{dl}s"></i>'
  return o
h='<button class="dcup boba today" aria-label="进今天的聊天"><i class="shell"></i><svg class="sauce" aria-hidden="true"></svg><i class="lq"></i>'+extras('boba',1)+\
  '<span class="t">今天 · 11/11 周三<em>6 轮 · 19:45</em></span><p class="h"><i>他</i>那我先把奶煮上，你到家刚好能喝</p><p class="m"><i>我</i>要加棉花糖！</p><span class="unsaid" role="button"><i>写了又擦掉 ·</i>其实今天有点想你</span></button>'

h+='<div class="sec"><b>本周</b><small>11/5 – 11/10 · <em>31</em> 轮</small></div><div class="wrows">'
for d,w,n,me,him,un in WEEK:
  if not n:
    h+=f'<div class="nil"><b>{d}</b>{w} · 没聊</div>';continue
  u=f'<span class="unsaid" role="button"><i>擦掉的 ·</i>{un}</span>' if un else ''
  dip='<svg viewBox="0 0 62 84" preserveAspectRatio="none"><path class="s" d="M20 0 H50 C54 10 47 16 52 26 C57 36 49 44 53 54 C56 62 50 68 54 74 L54 84 H20 C8 84 0 76 0 64 V20 C0 8 8 0 20 0Z"/><path class="h" d="M44 6 C47 12 43 16 46 22"/><circle class="sp" cx="12" cy="12" r="1.6"/><circle class="sp" cx="20" cy="8" r="1.2"/><circle class="sp" cx="9" cy="72" r="1.3"/></svg>'
  ct=''.join(f'<span>{c}</span>' for c in str(n))
  ri=locals().get('ri',-1)+1;me_last=ri%3==1
  h+=f'<button class="wrow{" mt" if me_last else ""}" aria-label="{d} {w}"><span class="dip">{dip}<b>{d.split("/")[1]}</b><small>{w}</small></span><span class="tx"><span class="h">{him}</span><span class="m"><i>我</i>{me}</span>{u}</span><span class="ct">{ct}<b>轮</b></span></button>'
h+='</div><div class="sec"><b>更早</b><small>一周一杯</small></div><div class="dcups">'
NAME={'cocoa':'热可可','boba':'珍珠奶茶','soda':'薄荷苏打'}
for k,(kind,rg,n,o) in enumerate(OLD):
  h+=f'<button class="dcup {kind}" aria-label="{rg}：{o}"><i class="lq"></i>{extras(kind,k+5)}<span class="t">{rg}<em>{n} 天</em></span><p>{o}</p></button>'
h+='</div>'
ICES='<span class="cube icd" style="width:120px;right:-50px;top:520px"><span class="body"><span class="im"><img src="ice.png" alt=""></span></span></span><span class="cube icd" style="width:86px;left:-34px;top:900px"><span class="body"><span class="im"><img src="ice.png" alt=""></span></span></span><span class="cube icd" style="width:104px;right:-40px;top:1180px;opacity:.85"><span class="body"><span class="im"><img src="ice.png" alt=""></span></span></span>'
H=(ICES+h).replace('\\','\\\\').replace('`','\\`').replace('${','\\${')
# replace generation block
a=s.index("let h=`<div class=\"wk\"><b>今天</b>")
b=s.index("L.innerHTML=h+'</div>';")+len("L.innerHTML=h+'</div>';")
s=s[:a]+"let h=`"+H+"`;\nL.innerHTML=h;"+s[b:]
# drop capw garnish line
s=re.sub(r"\[\['bit1\.png',26,'right:22px;top:-14px',-16\].*?\n","",s,count=1)
s=s.replace("const walls=['#wall2']","const walls=[]")
s=s.replace("capShape();addEventListener('resize',capShape);$('.cap').addEventListener('click',()=>(window._cg||[]).forEach((q,i)=>q.sp.v+=i?8:-8));","")
s=s.replace("$('.cap').addEventListener('click',()=>{CAP.k=performance.now()/1000});","")
s=s.replace("capSauce(s,on);","")
s=s.replace("rot:POS[i][3]","rot:[8,-12,5][i%3]")
s=s.replace('[".cap", "push:room", 1, 300]','[".today", "push:room", 1, 300], [".wrow", "push:room", 1, 380]')
# interactions + parallax
JS=r'''<script>(()=>{const $$=s=>[...document.querySelectorAll(s)];
$$('.unsaid').forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();b.classList.toggle('on')}));
$$('.dcup').forEach(c=>c.addEventListener('click',()=>{c.classList.remove('slosh');void c.offsetWidth;c.classList.add('slosh')}));
if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;const sc=document.querySelector('#sc');const Z=$$('[data-z]');let q=0;
function f(){q=0;const H=innerHeight/2;for(const e of Z){const r=e.getBoundingClientRect(),o=r.top+r.height/2-H;e.style.translate='0 '+(o*parseFloat(e.dataset.z)).toFixed(1)+'px'}}
sc.addEventListener('scroll',()=>{if(!q)q=requestAnimationFrame(f)},{passive:true});f()})()</script>'''
s=s.replace('<script>window.__DEMO_MAP',JS+'<script>window.__DEMO_MAP',1)
s=s.replace("const sauces=$$('.bub-him')","const sauces=$$('.bub-him,.today')",1)
s=s.replace("const gars=[];$$('.bub-him').forEach","const gars=[];$$('.wrow,.today').forEach",1)
s=s.replace("$$('.bub-him,.bub-me').forEach(b=>b.addEventListener('click',()=>gars","$$('.wrow,.today,.dcup').forEach(b=>b.addEventListener('click',()=>gars",1)
s=s.replace('const GH=','const DR='+'{"bit1.png": "<svg viewBox=\\"0 0 24 24\\"><path d=\\"M3 21C3 10 10 3 21 3C21 14 14 21 3 21Z\\" fill=\\"#a8d8c2\\" stroke=\\"#4f8f76\\" stroke-width=\\"1.1\\" stroke-linejoin=\\"round\\"/><path d=\\"M4 20C9 14 13 10 18 6M9 15l-1-4M12 12l3 0\\" fill=\\"none\\" stroke=\\"#4f8f76\\" stroke-width=\\".9\\" stroke-linecap=\\"round\\"/></svg>", "bit2.png": "<svg viewBox=\\"0 0 24 24\\"><path d=\\"M12 2C13 6 20 10 20 16C20 20 16 22 12 22C8 22 4 20 4 16C4 10 11 6 12 2Z\\" fill=\\"#5b3a2c\\" stroke=\\"#3b2219\\" stroke-width=\\"1.1\\" stroke-linejoin=\\"round\\"/><path d=\\"M8.5 13C8.5 11 10 9.5 11 8.5\\" fill=\\"none\\" stroke=\\"rgba(255,236,220,.6)\\" stroke-width=\\"1.4\\" stroke-linecap=\\"round\\"/></svg>", "bit4.png": "<svg viewBox=\\"0 0 24 24\\"><defs><radialGradient id=\\"gp\\" cx=\\".34\\" cy=\\".3\\" r=\\".75\\"><stop offset=\\".1\\" stop-color=\\"#e6f6ee\\"/><stop offset=\\".45\\" stop-color=\\"#9fd4bd\\"/><stop offset=\\"1\\" stop-color=\\"#5f9f86\\"/></radialGradient></defs><circle cx=\\"12\\" cy=\\"12\\" r=\\"9\\" fill=\\"url(#gp)\\" stroke=\\"#4f8f76\\" stroke-width=\\"1.1\\"/><circle cx=\\"9\\" cy=\\"8.5\\" r=\\"2\\" fill=\\"#fff\\" opacity=\\".85\\"/></svg>", "bit5.png": "<svg viewBox=\\"0 0 24 24\\"><rect x=\\"3\\" y=\\"3\\" width=\\"18\\" height=\\"18\\" rx=\\"2.5\\" fill=\\"#5b3a2c\\" stroke=\\"#3b2219\\" stroke-width=\\"1.1\\"/><rect x=\\"6.5\\" y=\\"6.5\\" width=\\"11\\" height=\\"11\\" rx=\\"1.5\\" fill=\\"none\\" stroke=\\"#7a5040\\" stroke-width=\\"1.2\\"/><path d=\\"M6 6.5l2 2\\" stroke=\\"rgba(255,236,220,.55)\\" stroke-width=\\"1.2\\" stroke-linecap=\\"round\\"/></svg>", "bit19.png": "<svg viewBox=\\"0 0 24 24\\"><path d=\\"M12 20C6 16 3 12.5 3 9C3 6 5.2 4 7.8 4C9.6 4 11 5 12 6.5C13 5 14.4 4 16.2 4C18.8 4 21 6 21 9C21 12.5 18 16 12 20Z\\" fill=\\"#e8a3a3\\" stroke=\\"#a25c5c\\" stroke-width=\\"1.1\\" stroke-linejoin=\\"round\\"/><path d=\\"M6.5 8.5C6.8 7.3 7.6 6.6 8.6 6.5\\" fill=\\"none\\" stroke=\\"#fff\\" stroke-width=\\"1.3\\" stroke-linecap=\\"round\\" opacity=\\".8\\"/></svg>", "bit3.png": "<svg viewBox=\\"0 0 24 24\\"><defs><radialGradient id=\\"gp\\" cx=\\".34\\" cy=\\".3\\" r=\\".75\\"><stop offset=\\".1\\" stop-color=\\"#e6f6ee\\"/><stop offset=\\".45\\" stop-color=\\"#9fd4bd\\"/><stop offset=\\"1\\" stop-color=\\"#5f9f86\\"/></radialGradient></defs><circle cx=\\"12\\" cy=\\"12\\" r=\\"9\\" fill=\\"url(#gp)\\" stroke=\\"#4f8f76\\" stroke-width=\\"1.1\\"/><circle cx=\\"9\\" cy=\\"8.5\\" r=\\"2\\" fill=\\"#fff\\" opacity=\\".85\\"/></svg>"}'+';const GH=',1)
s=s.replace('e.innerHTML=`<img src="${src}" alt="">`','e.innerHTML=DR[src]',1)
assert 'DR[src]' in s
open(P+'vb12.html','w').write(s)
print('ok')
