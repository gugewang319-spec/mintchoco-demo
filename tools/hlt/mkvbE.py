# vbE：由 p/hlt/index.html（V62）生成。茶茶 09:31/09:34：筛选原地折叠怪 → 底部毛玻璃抽屉；日历用记忆搜索页的糖粉选中；手帐物件改代码画
import os,re
H=os.path.dirname(os.path.abspath(__file__))+'/../../p/hlt/'
s=open(H+'index.html').read()
css=r'''
/* ===== vbE：手帐物件代码画 ===== */
#jn .jd .jp::before{border:0!important;border-image:none!important;transform:none!important;opacity:1!important;inset:0!important;border-radius:3px 2px 5px 4px;
 background:radial-gradient(circle at 20% 30%,rgba(160,120,80,.05) 0 1px,transparent 1.5px) 0 0/7px 7px,radial-gradient(circle at 70% 60%,rgba(160,120,80,.04) 0 .8px,transparent 1.3px) 0 0/5px 5px,linear-gradient(170deg,rgba(252,247,236,.9),rgba(246,236,216,.86));
 -webkit-mask:linear-gradient(225deg,transparent 0 22px,#000 22px);mask:linear-gradient(225deg,transparent 0 22px,#000 22px);box-shadow:none}
#jn .jd .jp::after{content:"";position:absolute;right:0;top:0;width:31px;height:31px;z-index:-1;border-radius:0 0 0 4px;background:linear-gradient(225deg,transparent 50%,#e9d6bc 50%,#f3e6d0 78%);filter:none}
#jn .jd .jp{box-shadow:none}
#jn .jd .jp .edge{position:absolute;left:0;right:0;bottom:-5px;height:6px;z-index:-1;background:radial-gradient(circle at 5px 0,rgba(246,236,216,.86) 4.6px,transparent 5px) 0 0/10px 6px repeat-x}
/* 巧克力牌：可可板 + 一圈牛奶巧克力裱花点 + 板厚 */
#jn .jd .plq{background:linear-gradient(165deg,#704534,#54321f 58%,#472a1e)!important;width:112px;height:74px;border-radius:8px;box-shadow:0 3.5px 0 #33201a,0 0 0 1.2px #3a2419}
#jn .jd .plq::before{content:"";position:absolute;inset:6px;border-radius:5px;border:2.4px dotted #c9a07e;opacity:.9;pointer-events:none}
#jn .jd .plq b{font:800 28px/1 BalooX;color:#f6e8d4;text-shadow:none}
#jn .jd .plq small{font:11.5px/1 ZJ;color:#e3c9aa;margin-top:5px}
/* 薄荷糖铁盒盖：外圈薄荷边 + 压印点圈 + 奶白中心 */
#jn .jd .tin{width:86px;height:86px;border-radius:50%;background:radial-gradient(circle,#fbf6ea 0 54%,#8a5c46 54% calc(54% + 1.2px),#c4e8da calc(54% + 1.2px) 80%,#a8d8c4 80% 100%)!important;box-shadow:0 0 0 1.3px #8a5c46,0 3px 0 #7fb59f,0 3px 0 1.3px #8a5c46}
#jn .jd .tin::before{content:"";position:absolute;inset:7px;border-radius:50%;border:1.6px dotted rgba(47,110,88,.55);pointer-events:none}
#jn .jd .tin b{font:800 17px/1 BalooX;position:relative}#jn .jd .tin small{position:relative}
/* 珍珠：同杯里珍珠（有体积 + 可可细边） */
#jn .jd .prl i{position:absolute;display:block;border-radius:50%;background:radial-gradient(circle at 35% 30%,#b88566 0 9%,#8a5a40 20%,#4b2c1f 58%,#33201a 100%);box-shadow:0 0 0 .9px rgba(60,35,25,.6),inset -2px -3px 4px rgba(30,18,12,.35)}
#jn .box{display:none!important}
#jn .fbar button{cursor:pointer}
/* ===== 底部毛玻璃抽屉（同记忆页月历容器） ===== */
.jsh{position:fixed;inset:0;z-index:60}.jsh[hidden]{display:none}
.jsh .jbg{position:absolute;inset:0;background:rgba(74,48,39,.18);opacity:0;transition:opacity .26s}
.jsp{position:absolute;left:12px;right:12px;max-width:388px;margin:0 auto;bottom:calc(14px + env(safe-area-inset-bottom,0px));padding:16px 18px 14px;border-radius:24px;background:rgba(252,250,244,.84);backdrop-filter:blur(18px) saturate(120%);-webkit-backdrop-filter:blur(18px) saturate(120%);border:1px solid rgba(255,255,255,.85);box-shadow:inset 0 1px 0 rgba(255,255,255,.95),0 16px 30px -16px rgba(74,48,39,.5);transform:translateY(28px);opacity:0;transition:transform .28s cubic-bezier(.23,1,.32,1),opacity .2s}
.jsh.on .jbg{opacity:1}.jsh.on .jsp{transform:none;opacity:1}
.jsp .row{display:flex;gap:14px;align-items:baseline;padding:6px 0 8px}
.jsp .row>span{flex:none;width:30px;font:12px/1 ZJ;color:var(--cocoa);letter-spacing:.12em}
.jsp .opts{display:flex;flex-wrap:wrap;gap:6px 18px}
.jsp .op{position:relative;display:inline-flex;align-items:center;gap:5px;font:15px/1.6 ZJ;color:rgba(74,48,39,.62);padding:2px 1px}
.jsp .op.on{color:var(--ch)}
.jsp .op svg{position:absolute;left:-8px;top:-4px;width:calc(100% + 16px);height:calc(100% + 8px);overflow:visible;pointer-events:none}
.jsp .op svg path{stroke-dasharray:1.02;stroke-dashoffset:1.02;transition:stroke-dashoffset .45s ease-out}
.jsp .op.on svg path{stroke-dashoffset:0}
/* 糖粉日历（照记忆搜索页：选中铺糖粉点点，两头手绘圈） */
.mcal2{margin-top:6px;padding-top:8px;border-top:1.2px dashed rgba(138,92,70,.25)}
.mcal2 .mrow{display:flex;align-items:center;justify-content:space-between;margin:0 0 2px}
.mcal2 .mrow h3{font:700 15px/1 Baloo,ZJ;color:var(--ch)}
.mcal2 .mrow button{width:34px;height:34px;font:18px/1 system-ui;color:var(--cocoa)}
.mcal2 .mrow button[aria-disabled=true]{opacity:.25}
.mcal2 .wkd,.mcal2 .days{display:grid;grid-template-columns:repeat(7,1fr);text-align:center}
.mcal2 .wkd span{font:11.5px/2 WK;color:rgba(122,90,76,.75)}
.mcal2 .days{isolation:isolate}
.mcal2 .d{position:relative;height:38px;font:600 14px/38px Baloo,ZJ;color:var(--ink)}
.mcal2 .d.off{color:rgba(74,48,39,.22)}
.mcal2 .d.td{color:var(--mint3);font-weight:800}
.mcal2 .d .dot{position:absolute;left:50%;bottom:3px;width:4px;height:4px;margin-left:-2px;border-radius:50%;background:var(--mintb)}
.mcal2 .d.in::before{content:"";position:absolute;inset:5px -1px;z-index:-1;background-color:rgba(196,232,218,.6);background-image:radial-gradient(circle,#fffdf8 0 1.1px,transparent 1.7px),radial-gradient(circle,#fffdf8 0 .8px,transparent 1.3px);background-size:6px 6px,5px 5px;background-position:0 0,3px 2px}
.mcal2 .d.ed::after{content:"";position:absolute;inset:4px 6px;border:1.6px solid var(--ch);border-radius:50% 46% 52% 48%;transform:rotate(-8deg)}
.mcal2 .tip{text-align:center;font:12px/1.6 WK;color:#8a6a5a;margin-top:2px}
'''
ik=''.join(m for m in re.findall(r'#jn \.(?:ik|ks|kh|kr|km)[^{]*\{[^}]*\}',s))
ik=ik.replace('#jn ','.jsp ')
css+=ik+'\n.jsp .op .ik{margin-right:0}\n'
s=s.replace('</style>',css+'</style>',1)
# 纸底加一道波浪边
s=s.replace('<div class="jp">','<div class="jp"><i class="edge" aria-hidden="true"></i>',1)
# 珍珠换代码画
s=re.sub(r'pr\+=`<img src="jd-pr\$\{PI\[\(i\+k\)%5\]\}\.png" alt="" style="left:\$\{q\[0\]\}px;top:\$\{q\[1\]\}px;width:28px;rotate:\$\{q\[2\]\}deg">`',
 'pr+=`<i style="left:${q[0]+2}px;top:${q[1]+2}px;width:24px;height:24px"></i>`',s)
s=re.sub(r'pr\+=`<img src="jd-pr\$\{PI\[\(full\+k\)%5\]\}\.png" alt="" style="left:\$\{q\[0\]\+\(28-w\)/2\}px;top:\$\{q\[1\]\+\(28-w\)/2\}px;width:\$\{w\.toFixed\(1\)\}px">`',
 'pr+=`<i style="left:${q[0]+(28-w)/2}px;top:${q[1]+(28-w)/2}px;width:${w.toFixed(1)}px;height:${w.toFixed(1)}px"></i>`',s)
s=s.replace('const w=Math.max(12,28*Math.sqrt(rem))','const w=Math.max(10,24*Math.sqrt(rem))')
assert s.count('<i style="left:${q[0]')==2
# ---- 筛选：抽屉 + 糖粉日历 ----
old_a=s.index("let kd='',rng='7'");old_b=s.index('/* 侧边小球')
blk=s[old_a:old_b]
rend=blk[blk.index('function render(){'):blk.index("$('#more').onclick")]
rend=rend.replace("function render(){const N=+rng;const g=[];let tot=0;\n for(let n=0;n<N;n++){","function render(){const g=[];let tot=0;\n for(let n=0;n<30;n++){if(!inR(n))continue;")
new=r'''let kd='',rng='7',days=3,cs=null,ce=null;const mon=new Date(T.getFullYear(),T.getMonth(),1);
const inR=n=>{if(rng!=='c')return n<+rng;const d=ago(n);return d>=cs&&d<=ce};
const fmt=d=>`${d.getMonth()+1}/${d.getDate()}`;
/* 09:31 茶茶：原地折叠怪 → 底部毛玻璃抽屉（同记忆页月历容器），点遮罩收 */
const SH=document.createElement('div');SH.className='jsh';SH.hidden=true;
SH.innerHTML=`<div class="jbg"></div><div class="jsp" role="dialog" aria-label="筛选记录"><div class="row"><span>类型</span><div class="opts" id="kds2"></div></div><div class="row"><span>日期</span><div class="opts" id="dts2"></div></div>
<div class="mcal2"><div class="mrow"><button type="button" id="pm2" aria-label="上个月">‹</button><h3 id="mt2"></h3><button type="button" id="nm2" aria-label="下个月">›</button></div><div class="wkd">${'一二三四五六日'.split('').map(w=>`<span>${w}</span>`).join('')}</div><div class="days" id="days2"></div><p class="tip">点两头选一段，同一天点两下只看那天</p></div></div>`;
$('#app').appendChild(SH);
const openSh=()=>{SH.hidden=false;requestAnimationFrame(()=>SH.classList.add('on'));$('#flb').setAttribute('aria-expanded',true)};
const closeSh=()=>{SH.classList.remove('on');$('#flb').setAttribute('aria-expanded',false);setTimeout(()=>SH.hidden=true,260)};
$('#flb').onclick=openSh;SH.querySelector('.jbg').onclick=closeSh;
function opts(el,list,cur,on){el.innerHTML=list.map((e,i)=>`<button type="button" class="op${e[0]===cur?' on':''}" data-v="${e[0]}">${IC[e[0]]||''}${e[1]}${ring(i)}</button>`).join('');el.querySelectorAll('.op').forEach(b=>b.onclick=()=>on(b.dataset.v))}
function draw(){opts($('#kds2'),Object.entries(NM),kd,v=>{kd=v;days=3;draw()});
 opts($('#dts2'),[['7','最近 7 天'],['30','最近 30 天']],rng,v=>{rng=v;cs=ce=null;days=3;draw()});cal();
 $('#sum').textContent=`${NM[kd]} · ${rng==='c'?(+cs===+ce?fmt(cs):fmt(cs)+'–'+fmt(ce)):'最近 '+rng+' 天'}`;render()}
'''+rend+r'''$('#more').onclick=()=>{days+=3;render()};
/* 09:34 茶茶：日历用记忆搜索页的糖粉选中（全站统一）：点两头选一段，铺糖粉；两头手绘圈；有记录的日子下面薄荷小点 */
function cal(){const y=mon.getFullYear(),m=mon.getMonth();$('#mt2').textContent=`${y} 年 ${m+1} 月`;
 const lead=(new Date(y,m,1).getDay()+6)%7,n=new Date(y,m+1,0).getDate();let h='<span></span>'.repeat(lead);
 for(let d=1;d<=n;d++){const dt=new Date(y,m,d),fut=dt>T,k=Math.round((T-dt)/864e5),has=k>=0&&k<30&&D[k].some(r=>!kd||r[0]===kd);let c='d';if(fut||!has)c+=' off';if(+dt===+T)c+=' td';
  const a=cs,b=ce||cs;if(a&&dt>=a&&dt<=b)c+=' in';if((cs&&+dt===+cs)||(ce&&+dt===+ce))c+=' ed';
  h+=`<button type="button" class="${c}" data-d="${d}" ${fut?'disabled':''}>${d}${has?'<i class="dot"></i>':''}</button>`}
 $('#days2').innerHTML=h;$('#nm2').setAttribute('aria-disabled',y===T.getFullYear()&&m===T.getMonth());
 $$('#days2 .d').forEach(b=>b.onclick=()=>{const dt=new Date(y,m,+b.dataset.d);if(dt>T)return;
  if(!cs||(ce&&rng==='c')||ce){cs=dt;ce=null;cal();return}
  ce=dt;if(ce<cs)[cs,ce]=[ce,cs];rng='c';days=3;draw();setTimeout(closeSh,380)})}
$('#pm2').onclick=()=>{mon.setMonth(mon.getMonth()-1);cal()};
$('#nm2').onclick=()=>{if($('#nm2').getAttribute('aria-disabled')==='true')return;mon.setMonth(mon.getMonth()+1);cal()};
'''
s=s[:old_a]+new+s[old_b:]
s=s.replace('<title>','<title>vbE · ',1)
open(H+'vbE.html','w').write(s)
print('ok')
