import re
import os
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../p/list/')  # 读 p/list/index.html，写出 vb11.html
s=open(P+'index.html').read()
s=s.replace('<title>','<title>vb11 · ',1) if '<title>' in s else s
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

/* vb11：QQ 主题式列表。一天一行，行底就是皮：本周＝巧克力威化（点 9 拉伸），更早＝小号饮品卡；小料挂在角上 */
.wrows{display:flex;flex-direction:column;gap:14px;margin-top:6px}
.wrow{position:relative;display:flex;align-items:center;gap:12px;width:100%;min-height:86px;border-style:solid;border-width:0 30px;border-image:url(wafer.png) 0 136 fill / 0 30px stretch;padding:12px 0 26px;margin:0;background:none;text-align:left;color:#fff6e8;transform-origin:50% 60%;z-index:2}
.wrow:nth-child(even){width:96%;margin-left:4%}
.wrow .dd{flex:none;width:40px;margin-left:-14px;text-align:center}
.wrow .dd b{display:block;font:800 25px/1 Baloo;color:#fff6e8;text-shadow:0 1px 0 rgba(59,34,25,.55)}
.wrow .dd small{display:block;margin-top:4px;font:10px/1 ZK;color:#d8f1e6;letter-spacing:.06em;white-space:nowrap}
.wrow .tx{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px;padding-left:12px;border-left:1px dashed rgba(255,246,232,.35)}
.wrow .h{font:15px/1.5 var(--body);color:#fff6e8;text-shadow:0 1px 0 rgba(59,34,25,.45);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-wrap:pretty}
.wrow .m{font:13px/1.4 var(--body);color:#d8f1e6;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.wrow .m i{font:600 10px/1 var(--body);font-style:normal;margin-right:4px;letter-spacing:.08em}
.wrow .ct{flex:none;margin-right:-12px;text-align:right}.wrow .ct b{font:800 20px/1 Baloo;color:#fff6e8}.wrow .ct small{font:10px/1 ZK;color:#d8f1e6;margin-left:2px}
.wrow .unsaid{margin:4px 0 0;color:#d8f1e6;font-size:12px}.wrow .unsaid i{color:#bfe6d6}
.wrow:active{transform:scale(.98)}
.icd{z-index:0!important}
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
  h+=f'<button class="wrow" aria-label="{d} {w}"><span class="dd"><b>{d.split("/")[1]}</b><small>{w}</small></span><span class="tx"><span class="h">{him}</span><span class="m"><i>我</i>{me}</span>{u}</span><span class="ct"><b>{n}</b><small>轮</small></span></button>'
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
open(P+'vb11.html','w').write(s)
print('ok')
