# 由 rec.html 生成 vbD.html：一天手帐页按灰稿 D（斜贴拼贴）上装饰，方法照设置页（L2 远景线稿 + 生图物件写字 + L5 小料贴屏幕边）
import os,re
H=os.path.dirname(os.path.abspath(__file__))+'/../../p/hlt/'
s=open(H+'rec.html').read()
css='''
/* —— vbD：一天=一页手帐（灰稿 D 斜贴拼贴）—— */
#res .day.jd{position:relative;margin:34px 0 0;padding:0;background:none!important;box-shadow:none!important;border:0!important;min-height:0}
#res .day.jd::before,#res .day.jd::after{display:none}
.jd .pp{position:relative;width:calc(100% - 78px);margin-top:30px;padding:86px 18px 16px 16px;rotate:var(--pr,-1.6deg);z-index:1}
.jd .pp::before{content:"";position:absolute;inset:-6px -6px -6px -6px;border:solid transparent;border-width:64px 44px 14px 36px;border-image:url(jd-paper.png) 128 88 28 72 fill / 64px 44px 14px 36px stretch;transform:scaleX(-1);opacity:.93;z-index:-1}
.jd.mr .pp{margin-left:70px;width:calc(100% - 92px);--pr:1.4deg}.jd.mr .pp::before{transform:none}
.jd .plq{position:absolute;left:-6px;top:0;width:128px;height:90px;background:url(jd-plaque.png) center/100% 100% no-repeat;rotate:-5deg;z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:center;padding-top:2px}
.jd.mr .plq{left:auto;right:-4px;rotate:4deg}
.jd .plq b{font:800 30px/1 Baloo;color:#f4e6d2;letter-spacing:-.01em;text-shadow:0 1px 0 rgba(58,36,25,.5)}
.jd .plq small{font:12px/1 ZK;color:#e6cfb4;margin-top:6px;letter-spacing:.12em}
.jd .tin{position:absolute;right:-6px;top:58px;width:92px;height:92px;background:url(jd-tin.png) center/contain no-repeat;rotate:5deg;z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:center}
.jd.mr .tin{right:auto;left:-6px;rotate:-6deg}
.jd .tin b{font:800 19px/1 Baloo;color:var(--ch)}.jd .tin small{font:11px/1 ZK;color:var(--cocoa);margin-top:3px;letter-spacing:.1em}
.jd .prl{position:absolute;right:20px;top:160px;display:flex;flex-direction:column;align-items:center;gap:7px;z-index:2}
.jd.mr .prl{right:auto;left:22px}
.jd .prl i{display:block;width:var(--d,22px);height:var(--d,22px);border-radius:50%;background:radial-gradient(circle at 34% 30%,#c49a7c 0 10%,#7a4c35 46%,#3e2519 100%);box-shadow:inset -2px -3px 4px rgba(30,16,10,.35)}
.jd .prl em{font:11px/1 Baloo;color:var(--cocoa);font-style:normal;margin-top:2px}
.jd .strip{margin:0 0 2px}
.jd .r{display:flex;align-items:center;gap:8px;min-height:34px}
.jd .r .tm{display:flex;flex-direction:column;font:600 13px/1.25 Baloo;color:var(--ch);white-space:nowrap;position:static}.jd .r .tm small{display:block;position:static;font:11px/1.2 ZK;color:rgba(74,48,39,.55);margin:1px 0 0}
.jd .r .ld{flex:1;border-bottom:1.5px dotted rgba(138,92,70,.4);margin-top:6px;min-width:12px}
.jd .r .vl{font:800 16px/1 Baloo;color:var(--ch);white-space:nowrap;text-align:right}.jd .r .vl small{font:11px/1 ZK;color:var(--cocoa);margin-left:2px;font-weight:400}
.jd .stk2{position:absolute;z-index:4;pointer-events:none}
'''
s=s.replace('</style>',css+'</style>',1)
new=r'''function render(){const N=+rng;const g=[];let tot=0;
 for(let n=0;n<N;n++){const h=merge(D[n].filter(r=>!kd||r[0]===kd));if(h.length){g.push({n,h});tot+=h.length}}
 $('#cnt').innerHTML=`<b>${tot}</b> 条健康记录`;
 const show=g.slice(0,days);$('#more').hidden=g.length<=days;
 $('#res').innerHTML=show.map((x,k)=>{const d=ago(x.n);const lab=`${d.getMonth()+1}/${d.getDate()}`;
  const st=D[x.n].filter(r=>r[0]==='steps').reduce((a,r)=>a+ +r[3].replace(/[+,]/g,''),0);
  const sl=D[x.n].find(r=>r[0]==='sleep');const slh=sl?+sl[3].split('<')[0]:0;
  const full=Math.min(9,Math.floor(st/1000)),rem=(st%1000)/1000;
  let pr='';for(let i=0;i<full;i++)pr+=`<i style="--d:${22-i*1.2}px"></i>`;if(rem>.15&&full<9)pr+=`<i style="--d:${Math.max(7,(22-full*1.2)*rem).toFixed(1)}px"></i>`;
  const mr=k%2?' mr':'';
  return `<section class="day jd${mr}" data-l="${lab}">
 <div class="plq"><b>${lab}</b><small>周${WK[d.getDay()]}${x.n===0?' · 今天':x.n===1?' · 昨天':''}</small></div>
 ${kd&&kd!=='steps'?'':`<div class="tin" aria-label="当天 ${st} 步"><b>${st.toLocaleString('en')}</b><small>步</small></div><div class="prl" aria-hidden="true">${pr}<em>×1k</em></div>`}
 <div class="pp">${k===0?'<img class="stk2" src="st-star.png" alt="" style="left:-14px;bottom:-14px;width:32px;rotate:-14deg">':''}${slh>=7?`<img class="stk2" src="st-moon.png" alt="睡够了" style="${mr?'left':'right'}:-12px;bottom:-16px;width:44px;rotate:10deg">`:''}
 <div class="strip">${x.h.map(r=>`<i class="pn p-${r[0]}" style="left:${hx(r[1])}%"></i>`).join('')}</div><div class="sax"><span>0</span><span>6</span><span>12</span><span>18</span><span>24</span></div>${
  x.h.map(r=>`<div class="r" aria-label="${r[1]} ${r[2]} ${r[3].replace(/<[^>]+>/g,'')}${r[4]}">${IC[r[0]]}<span class="tm">${r[5]?`${r[1].slice(0,2)}–${String(+r[1].slice(0,2)+1).padStart(2,'0')} 时<small>${r[5].match(/(\d+) 笔/)[1]} 笔</small>`:r[1]}</span><span class="ld"></span><span class="vl">${r[3]}<small>${r[4]}</small></span></div>`).join('')}</div></section>`}).join('');
 rail();
 $('#empty').hidden=!!g.length}
'''
a=s.index('function render(){');b=s.index("$('#more').onclick",a)
s=s[:a]+new+s[b:]
s=s.replace('<title>','<title>vbD · ',1)
open(H+'vbD.html','w').write(s)
print('ok')
