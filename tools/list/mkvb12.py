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
open(R+'vb12.html','w').write(s)
print(s.count('class="lqw"'),s.count(' dk '))
