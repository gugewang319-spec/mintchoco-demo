# vb12 = vb11 + 今天页的饮品卡毛玻璃（液面 lq2.js）+ 今天页画法的小料。用法：python3 tools/list/mkvb12.py（仓库根）
import re,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../p/list/')
s=open(R+'vb11.html').read()
s=s.replace('<title>vb11 · ','<title>vb12 · ',1)
# 去掉雾里水珠（today 的杯子没有）
s=re.sub(r'<div class="drops"[^>]*>(?:<i [^>]*></i>)*</div>','',s)
MM='<i class="mm"></i><i class="mm"></i><i class="mm"></i>'
def W(inner):return '<i class="lqw" aria-hidden="true">'+inner+'</i>'
# 今天：珍珠奶茶，6 轮 = 6 颗珍珠
s=s.replace('<button class="tod gl tap"','<button class="tod gl dk boba tap" data-lv=".36"',1)
s=s.replace('aria-label="进今天的聊天">','aria-label="进今天的聊天">'+'<span class="tdz" aria-hidden="true"><img src="today-bg.png" alt=""></span><i class="tdd"></i><i class="tdd"></i><i class="tdd"></i>'+W('<i class="pearl"></i>'*6),1)
# 本周：他=热可可（棉花糖），我=薄荷苏打（叶子+气泡）
s=s.replace('<div class="gl his"','<div class="gl his dk cocoa"')
s=s.replace('<div class="gl mine"','<div class="gl mine dk soda"')
s=re.sub(r'(<div class="gl his dk cocoa"[^>]*>)',lambda m:m.group(1)+W(MM),s)
s=re.sub(r'(<div class="gl mine dk soda"[^>]*>)',lambda m:m.group(1)+W('<img class="sodaleaf" src="bit19.png" alt="">'),s)
# 更早：轮流 拿铁 / 热可可 / 珍珠 / 苏打
fl=iter(['latte','cocoa','boba','soda'])
def ice(m):
  f=next(fl);inner={'latte':'<i class="foam"><b>♥</b></i>','cocoa':MM,'boba':'<i class="pearl"></i>'*5,'soda':'<img class="sodaleaf" src="bit19.png" alt="">'}[f]
  return m.group(1).replace('class="ice gl','class="ice gl dk '+f)+W(inner)
s=re.sub(r'(<button class="ice gl[^>]*>)',ice,s)
CSS=r'''
/* ===== vb12：卡片 = 今天页那只装奶茶的毛玻璃（同款 .glass + 液面），小料照今天页画法 ===== */
.gl,.duo .his,.duo .mine,.ice.dp1,.tod{background:linear-gradient(160deg,rgba(255,255,255,.8),rgba(250,252,248,.58))!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important;border:1px solid rgba(255,255,255,.9)!important;box-shadow:inset 0 1px 0 #fff,0 10px 22px -16px rgba(74,48,39,.5)!important}
.duo .his{box-shadow:inset 0 1px 0 #fff,0 6px 16px -14px rgba(74,48,39,.4)!important}
.duo .mine{box-shadow:inset 0 1px 0 #fff,0 14px 24px -14px rgba(74,48,39,.5)!important}
.gl::before{display:none!important}
.dk{isolation:isolate}
.dk>*:not(.lqw):not(.dc):not(.bh){position:relative;z-index:3}
.lqw{position:absolute!important;inset:0;border-radius:inherit;overflow:hidden;z-index:1!important;pointer-events:none}
.lqc{position:absolute;inset:0;width:100%;height:100%;z-index:1;pointer-events:none}
.mm{position:absolute;z-index:2;width:13px;height:11px;border-radius:4px;background:linear-gradient(160deg,#fffdf7,#f1e6d6);box-shadow:inset -1px -1px 0 rgba(138,92,70,.25),0 0 0 .6px rgba(138,92,70,.35);will-change:transform}
.pearl{position:absolute;z-index:2;bottom:4px;width:11px;height:11px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#a57658 0 14%,#4b2c1f 60%);box-shadow:0 0 0 .6px rgba(60,35,25,.5);will-change:transform}
.foam{position:absolute;z-index:2;right:10px;top:7px;width:34px;height:34px;border-radius:50%;background:radial-gradient(circle,#fff8ec 0 55%,#e9d2b6 56% 64%,#b98a66 66%)}
.foam b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:20px/1 system-ui;color:#c99f7d;padding-top:2px}
.sodaleaf{position:absolute;z-index:2;right:14px;bottom:3px;width:22px;transform-origin:50% 100%;will-change:transform}
.lqw .bub{position:absolute;z-index:2;bottom:-8px;border-radius:50%;border:1.2px solid rgba(255,255,255,.95);background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.9) 0 18%,rgba(255,255,255,.15) 30%);will-change:transform}
.ice.latte p,.ice.latte b,.ice.latte small{padding-right:30px}
.tdz{position:absolute!important;left:0;right:0;top:0;z-index:4!important;border-radius:22px 22px 0 0;overflow:hidden;pointer-events:none}
.tdz img{display:block;width:100%}
main .tod.dk .in{padding-top:54px!important}
.tdd{position:absolute!important;z-index:5!important;width:8px;height:11px;margin-left:-4px;border-radius:50% 50% 50% 50%/62% 62% 38% 38%;background:radial-gradient(circle at 35% 30%,#9c6a50,#43261a 72%);pointer-events:none;opacity:0}
.duo p,.ice p,.tod .key,.tod .sub{font-family:var(--body)!important}
.duo p,.ice p{font-weight:400!important}
.tod .key{font-weight:700!important}
'''
s=s.replace('</style>',CSS+'</style>',1)
JS=r'''<script src="lq2.js"></script><script>
/* 饮品卡里的小料：照今天页，各自周期、错开；减少动效时静止 */
(()=>{const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,$$=(q,r=document)=>[...r.querySelectorAll(q)],D=[];
const V=new Set(),io=new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting?V.add(e.target):V.delete(e.target)),{rootMargin:'60px'});
$$('.dk').forEach((el,ci)=>{const k=el.dataset.lq,w=el.querySelector('.lqw');if(!w)return;io.observe(el);const P=f=>D.push(T=>{if(V.has(el))f(T)});const W=()=>w.offsetWidth,H=()=>w.offsetHeight,lv=()=>(window.LQlv?LQlv(k):.4);
 $$('.mm',w).forEach((m,i)=>{const fx=[.56,.68,.8][i],per=[3.1,3.9,2.7][i],pr=[4.3,3.3,5.1][i],r0=[8,-12,20][i];P(T=>{const x=W()*fx,y=Math.sin(T*6.283/per+i*2+ci)*2.4,r=Math.sin(T*6.283/pr+i+ci)*14;m.style.left=x+'px';m.style.bottom=(H()*lv()-6+y+(window.LQ?LQ(k,x+6):0))+'px';m.style.transform=`rotate(${(r+r0).toFixed(1)}deg)`})});
 $$('.pearl',w).forEach((m,i,a)=>{const per=2.4+i*.37;P(T=>{const x=W()*(.5+i*.08)+(i%2)*4;const y=Math.max(0,Math.sin(T*6.283/per+i*1.3+ci))*6;m.style.left=x+'px';m.style.transform=`translate(${(window.LQu?LQu(k,x+5):0).toFixed(1)}px,${(-y).toFixed(1)}px)`})});
 const lf=w.querySelector('.sodaleaf');if(lf){const per=4.6+ci%3*.7;P(T=>{lf.style.transform=`rotate(${(Math.sin(T*6.283/per+ci)*9).toFixed(1)}deg)`})}
 const fm=w.querySelector('.foam');if(fm){P(T=>{fm.style.transform=`rotate(${(Math.sin(T*6.283/7.2)*6).toFixed(1)}deg) translateY(${(Math.sin(T*6.283/3.6)*1.2).toFixed(1)}px)`})}
 if(el.classList.contains('soda')&&!RM){for(let j=0;j<3;j++){const b=document.createElement('i');b.className='bub';const z=3+Math.random()*4;b.style.width=b.style.height=z+'px';w.appendChild(b);const o={x:.08+Math.random()*.6,sp:14+Math.random()*16,ph:Math.random()*60,per:1.2+Math.random()*1.4,wb:1.5+Math.random()*2.5};P(T=>{const h=H()*lv(),y=((T+o.ph)*o.sp)%(h+8);b.style.left=(W()*o.x)+'px';b.style.transform=`translate(${(Math.sin(T*6.283/o.per)*o.wb).toFixed(1)}px,${(-y).toFixed(1)}px)`;b.style.opacity=y>h-4?0:1})}}
});
/* 巧克力滴落：照今天页，从淋酱最长的三处尖端轮流滴，各自间隔 4.5–8.5 秒 */
const tod=document.querySelector('.tod'),TIP=[[75,118],[624,123],[1060,125]],tdd=$$('.tdd',tod);let nx=[2.2,5.1,7.6];
function drip(i){const d=tdd[i],w=tod.offsetWidth,k=w/1170;d.style.left=(TIP[i][0]*k)+'px';d.style.top=(TIP[i][1]*k-3)+'px';
 d.animate([{opacity:0,transform:'translateY(0) scale(.3)'},{opacity:1,transform:'translateY(0) scale(1)',offset:.45},{opacity:1,transform:'translateY(4px) scale(1.05,1.15)',offset:.6},{opacity:0,transform:'translateY(48px) scale(.8,1.25)'}],{duration:2200,easing:'cubic-bezier(.5,0,.8,.6)'})}
if(!RM)D.push(T=>{for(let i=0;i<3;i++)if(T>nx[i]){drip(i);nx[i]=T+4.5+Math.random()*4}});
let T0=performance.now();let on=true;function f(now){if(!on)return;const T=RM?0:(now-T0)/1000;for(const d of D)d(T);if(!RM)requestAnimationFrame(f)}requestAnimationFrame(f);document.addEventListener('visibilitychange',()=>{on=!document.hidden;if(on)requestAnimationFrame(f)});
})();</script>'''
s=s.replace('<script src="../pfix.js',JS+'<script src="../pfix.js',1)
# 轮次用聊天室的巧克力计数牌 .counter（巧克力底、奶白数字格）
def ctr(n,unit='轮'):return '<span class="counter" aria-label="'+n+' '+unit+'">'+''.join('<span>'+d+'</span>' for d in n)+'<b>'+unit+'</b></span>'
s=re.sub(r'<em><b>(\d+)</b>轮</em>',lambda m:ctr(m.group(1)),s)
s=re.sub(r'<div><em>(\d+)</em><small>轮 · ([\d:]+)</small></div>',lambda m:'<div><small style="display:block;margin-bottom:5px">'+m.group(2)+'</small>'+ctr(m.group(1))+'</div>',s,count=1)
CTR=""".counter{display:inline-flex;gap:2px;padding:3px;border-radius:5px;background:#5b3a2c;box-shadow:0 2px 3px -1px rgba(74,48,39,.4);vertical-align:middle}
.counter span{display:inline-block;min-width:12px;padding:1px 2px;border-radius:2px;background:#fdf9f0;font:700 13px/1.3 Baloo,ZK!important;text-align:center;color:#4a3027}
main .counter>b{align-self:center;font:500 12px/1 var(--body)!important;color:#fdf9f0!important;margin:0!important;padding:0 2px 0 3px}
.rw .lb .counter{margin-left:auto}
.tod .side small{position:relative;z-index:4}
.tod .side .counter span{font-size:17px!important;min-width:15px}
"""
s=s.replace('</style>',CTR+'</style>',1)
# —— 05:05 茶茶：大卡不贴淋酱、轮次不用巧克力牌（字+装饰）；去「写了又擦掉」；奶茶热气雾；冰块水中浮沉；贴纸
s=s.replace('<span class="tdz" aria-hidden="true"><img src="today-bg.png" alt=""></span><i class="tdd"></i><i class="tdd"></i><i class="tdd"></i>','<i class="steam" aria-hidden="true"><i></i><i></i><i></i><i></i></i>',1)
s=s.replace("if(!RM)D.push(T=>{for(let i=0;i<3;i++)if(T>nx[i]){drip(i);nx[i]=T+4.5+Math.random()*4}});","")
s=re.sub(r'<button class="wh"[^>]*>.*?</button>','',s)
s=re.sub(r'<span class="wh"[^>]*>.*?</span></span>|<span class="wh"[^>]*><i>[^<]*</i>[^<]*</span>','',s)
s=re.sub(r'<div><small style="display:block;margin-bottom:5px">([\d:]+)</small><span class="counter" aria-label="(\d+) 轮">.*?</b></span></div>',
 lambda m:'<div class="rds" aria-label="'+m.group(2)+' 轮"><img class="bre" src="stk_mm.png" alt="" style="--r:-10deg;--d:4.6s;--dl:-1.3s"><em>'+m.group(2)+'</em><b>轮</b><i>rounds</i><small>'+m.group(1)+'</small></div>',s,count=1)
s=s.replace('<div class="brk" style="margin-top:56px"><b>更早</b></div>','<div class="brk" style="margin-top:56px"><b>更早</b><img class="stk bre" src="stk_tag.png" alt="" style="width:40px;right:4px;top:-50px;--r:12deg;--d:5.2s;--dl:-2s"></div>',1)
s=s.replace('<main','<img class="bgi bre stkp" src="stk_mac.png" alt="" style="width:62px;left:-16px;top:122px;--r:-14deg;--d:6.4s;--dl:-3s"><main',1)
CSS2=""".tdz,.tdd{display:none!important}
main .tod.dk .in{padding-top:22px!important}
.rds{position:relative;text-align:right;line-height:1}
.rds em{font:800 46px/1 BalooX,Baloo,ZK;font-style:normal;color:#5b3a2c;position:relative;z-index:2}
.rds b{font:15px ZK;color:#5b3a2c;margin-left:2px;position:relative;z-index:2}
.rds i{display:block;font:15px/1 Script;color:#3f9a80;margin-top:-4px;position:relative;z-index:2;opacity:.85}
.rds small{display:block;margin-top:6px;font:12px Baloo,ZK;color:#8a6b5c;position:relative;z-index:2}
.rds img{position:absolute;width:44px;right:44px;top:-14px;z-index:1;opacity:.95}
.brk .stk{position:absolute}
.stkp{z-index:1;pointer-events:none}
/* 冰块浮力：在水里上下浮沉、轻轻打转（只动 translate/rotate） */
.bgi.ic,.bh.ic{--an:bob;animation-direction:normal!important;animation-timing-function:ease-in-out!important}
@keyframes bob{0%{translate:0 0;rotate:calc(var(--r,0deg) - .8deg)}28%{translate:1px -7px;rotate:calc(var(--r,0deg) + 1.2deg)}55%{translate:-1px 1px;rotate:calc(var(--r,0deg) - .4deg)}78%{translate:0 -3px;rotate:calc(var(--r,0deg) + .5deg)}100%{translate:0 0;rotate:calc(var(--r,0deg) - .8deg)}}
/* 奶茶热气雾在玻璃内侧：几团淡白雾慢慢往上飘、散开 */
.steam{position:absolute!important;inset:0;z-index:3!important;overflow:hidden;border-radius:inherit;pointer-events:none}
.steam i{position:absolute;left:var(--x);bottom:28%;width:var(--w);aspect-ratio:1.5;border-radius:50%;background:radial-gradient(closest-side,rgba(255,255,255,.55),rgba(255,255,255,.22) 55%,rgba(255,255,255,0));opacity:0;animation:stm var(--d) ease-out var(--dl) infinite}
.steam i:nth-child(1){--x:6%;--w:46%;--d:9s;--dl:-1s}
.steam i:nth-child(2){--x:34%;--w:40%;--d:11s;--dl:-5s}
.steam i:nth-child(3){--x:58%;--w:44%;--d:10s;--dl:-8s}
.steam i:nth-child(4){--x:20%;--w:52%;--d:12s;--dl:-3s}
@keyframes stm{0%{opacity:0;transform:translateY(20px) scale(.7,.6)}25%{opacity:.9}70%{opacity:.5}100%{opacity:0;transform:translateY(-120px) scale(1.25,1.1)}}
@media (prefers-reduced-motion:reduce){.steam i{animation:none;opacity:.5}}
"""
s=s.replace('</style>',CSS2+'</style>',1)
# —— 05:05 茶茶：纯色字在毛玻璃上怪 → 排版手法：加粗、压字内描边（同色细描加粗 + 下沿白唇像刻在玻璃上）、光晕把字和玻璃分开、大引号、他/我小标签荧光笔
CSS3="""main .gl .key,main .gl .sub,main .duo p,main .ice p{color:#4a3027;-webkit-text-stroke:.35px #4a3027;text-shadow:0 1px 0 rgba(255,255,255,.85),0 0 8px rgba(255,252,244,.75),0 0 2px rgba(255,252,244,.9)}
main .tod .key{font:700 21px/1.5 var(--body)!important;text-wrap:balance;letter-spacing:.02em;position:relative}
main .tod .key::before{content:'\\201C';position:absolute;left:-14px;top:-22px;font:52px/1 Script,serif;color:rgba(63,154,128,.45);-webkit-text-stroke:0;text-shadow:none;pointer-events:none}
main .tod .sub{font:600 15px/1.5 var(--body)!important}
main .duo p,main .ice p{font-weight:500!important;text-wrap:pretty;font-family:var(--body)!important}
main .tod i.k,main .duo p i{display:table!important;margin-bottom:4px!important;font:12px/1.2 ZK!important;color:#5b3a2c!important;-webkit-text-stroke:0;text-shadow:none;letter-spacing:.12em;padding:0 3px 0 2px;background:linear-gradient(100deg,transparent 2%,rgba(63,154,128,.32) 6%,rgba(63,154,128,.26) 90%,rgba(63,154,128,.4) 95%,transparent 98%) 0 100%/100% 52% no-repeat}
main .ice b{text-shadow:0 1px 0 rgba(255,255,255,.85)}
"""
s=s.replace('</style>',CSS3+'</style>',1)
open(R+'vb12.html','w').write(s)
print(s.count('class="lqw"'),s.count(' dk '))
