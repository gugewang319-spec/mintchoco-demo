R='/workspace/projects/8ff64c4f-1e42-4bee-a321-ff12731f7d96/mintchoco-demo/p/list/'
s=open(R+'index.html').read()
s=s.replace('<title>','<title>vb3 · ',1) if '<title>' in s else s
CSS=r'''
/* ===== vb3：景深 + 猫奶奶滴奶成云 ===== */
.list{display:none!important}
#scene{position:relative;z-index:3;padding:0 4px 170px}
#liq{position:absolute;left:-40px;right:-40px;z-index:0;pointer-events:none;background:linear-gradient(180deg,rgba(214,186,155,.38) 0,rgba(196,164,131,.24) 30%,rgba(173,138,104,.14) 100%);-webkit-mask:linear-gradient(180deg,#000 0,#000 80%,transparent);mask:linear-gradient(180deg,#000 0,#000 80%,transparent)}
#liq svg{position:absolute;left:0;top:-12px;width:100%;height:14px}
#cloud{position:absolute;left:0;top:0;z-index:4;pointer-events:none}
.near{position:relative;z-index:2;display:flex;align-items:flex-start;gap:4px;padding:6px 0 0;transition:padding-top .9s cubic-bezier(.3,1.3,.5,1)}
.catw{flex:none;position:relative;width:clamp(132px,40vw,168px);transform-origin:50% 75%;cursor:pointer;-webkit-tap-highlight-color:transparent}
.catw img{width:100%;display:block;user-select:none;-webkit-user-drag:none}
.catw .sub{position:absolute;left:2%;right:2%;height:30%;bottom:-2px;pointer-events:none;background:linear-gradient(180deg,rgba(214,186,155,0) 0,rgba(214,186,155,0) 16%,rgba(210,180,148,.5) 32%,rgba(204,172,140,.78) 100%);-webkit-mask:radial-gradient(50% 100% at 50% 100%,#000 55%,transparent 100%);mask:radial-gradient(50% 100% at 50% 100%,#000 55%,transparent 100%)}
.catw .ring{position:absolute;left:0;right:0;height:14px;bottom:28%;border-radius:50%;background:radial-gradient(closest-side,rgba(255,250,238,.85),rgba(255,250,238,0));pointer-events:none}
.catw .sh{position:absolute;left:12%;right:12%;height:16px;bottom:20%;border-radius:50%;background:radial-gradient(closest-side,rgba(110,78,52,.25),rgba(110,78,52,0));pointer-events:none}
/* 字落在漂着的奶泡上（无描边，靠明暗） */
.raft{position:relative;padding:16px 18px 18px;isolation:isolate}
.raft::before{content:"";position:absolute;inset:0;z-index:-1;border-radius:30px 38px 34px 26px/26px 30px 36px 28px;background:radial-gradient(120% 90% at 34% 28%,rgba(255,253,247,.92) 0,rgba(253,247,236,.84) 55%,rgba(240,226,206,.7) 100%);box-shadow:inset -6px -8px 14px -8px rgba(150,112,82,.35),inset 4px 5px 10px -6px rgba(255,255,255,.9)}
.raft .k{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.raft .k b{font:22px/1 ZK;color:var(--ch);letter-spacing:.04em}
.raft .k span{font:600 13px/1 Baloo;color:var(--cocoa)}
.raft .k i{font:12px/1 WK;font-style:normal;color:var(--mint3)}
.raft .ln{display:flex;gap:6px;margin-top:7px;font:15px/1.55 WK;color:var(--ink)}
.raft .ln em{flex:none;font:12px/1.9 WK;font-style:normal;color:var(--mint3);width:16px}
.raft .ln.mine em{color:var(--cocoa)}
.today{flex:1;min-width:0;margin-top:10px;margin-right:-6px}
.go{position:relative;margin:12px 0 0 6px;height:40px;padding:0 20px;border-radius:12px;background:linear-gradient(180deg,#6f4738,#56362a);border:1.2px solid #3b2219;box-shadow:inset 0 1.5px 0 rgba(255,236,220,.25),inset 0 -3px 0 rgba(0,0,0,.18),0 6px 12px -8px rgba(46,26,18,.7);font:15px/1 WK;color:#fff3e2;letter-spacing:.12em}
.go:active{transform:translateY(1px)}
.sec{position:relative;z-index:2;will-change:transform}
.sec .hd{display:flex;align-items:baseline;gap:8px;padding:0 14px}
.sec .hd b{font:16px/1 ZK;color:var(--ch)}
.sec .hd span{font:600 12px/1 Baloo;color:var(--cocoa)}
.mid{margin-top:26px;height:300px}
.far{margin-top:4px;height:290px}
.ice{position:absolute;width:46px;height:48px;padding:0;transform:rotate(var(--r));transition:transform .25s cubic-bezier(.3,1.5,.5,1)}
.ice img{width:100%;height:100%;object-fit:contain;pointer-events:none}
.ice.e{cursor:default}.ice.e img{opacity:0}.ice.e::after{content:"";position:absolute;inset:4px 5px 6px;border-radius:9px;border:1.3px dashed rgba(138,92,70,.3)}
.ice.on,.prl.on{transform:translateY(-3px) rotate(var(--r))}
.ice.on::before,.prl.on::before{content:"";position:absolute;inset:-10px;border-radius:50%;z-index:-1;background:radial-gradient(closest-side,rgba(255,226,150,.55),rgba(255,226,150,0))}
.prl{position:absolute;width:24px;height:24px;padding:0;--r:0deg;opacity:.82}
.prl img{width:100%;height:100%;pointer-events:none}
.prl.on{opacity:1}
.prl.hug{animation:hug .7s cubic-bezier(.3,1.6,.5,1)}@keyframes hug{0%{scale:1}30%{scale:1.3 .82;translate:0 -6px}60%{scale:.9 1.1}100%{scale:1}}
.co{position:absolute;left:10px;right:10px}
.co .raft{padding:12px 16px 14px;max-width:320px}
.co .raft p{margin-top:6px;font:15px/1.55 WK;color:var(--ink)}
.co .raft a{display:inline-block;margin-top:2px;font:13px/1 WK;color:var(--ch);letter-spacing:.06em;padding:6px 0}
.far .co .raft{opacity:.92}
/* L5 贴纸小物：信息写在上面，贴屏幕边 */
.stk{position:absolute;z-index:3;pointer-events:none;display:grid;place-items:center;transform-origin:50% 20%;animation:sway 5.5s ease-in-out infinite alternate}
.stk img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}
.stk b{position:relative;font:700 15px/1 Baloo;color:#fff3e2;text-align:center}.stk b small{display:block;font:10px/1.2 WK;font-weight:400;margin-top:1px}
.stk.st b{color:var(--ch)}
@keyframes sway{from{rotate:-4deg}to{rotate:4deg}}
.bub{position:absolute;z-index:1;width:6px;height:6px;border-radius:50%;background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.9) 0 20%,rgba(255,255,255,.15) 45%);border:1px solid rgba(255,255,255,.7);animation:rise linear infinite;pointer-events:none}
@keyframes rise{from{transform:translateY(0);opacity:0}15%{opacity:1}to{transform:translateY(-160px);opacity:0}}
#drop{position:fixed;z-index:30;width:15px;height:19px;margin:-13px 0 0 -7.5px;border-radius:50% 50% 50% 50%/62% 62% 40% 40%;background:radial-gradient(circle at 36% 62%,#fffdf6 0,#f6ecd9 45%,#e0ccae 100%);transform-origin:50% 30%;will-change:transform;pointer-events:none;opacity:0;transition:opacity .35s}
@media (prefers-reduced-motion:reduce){#cloud,#drop{display:none}.stk,.bub{animation:none}}
'''
s=s.replace('</style>',CSS+'</style>',1)
HTML='''<div id="scene">
 <div id="liq"><svg viewBox="0 0 400 14" preserveAspectRatio="none"><path d="M0 10 C40 4 80 13 130 8 S220 3 270 9 S350 12 400 6 V14 H0Z" fill="rgba(214,186,155,.42)"/><path d="M0 10 C40 4 80 13 130 8 S220 3 270 9 S350 12 400 6" stroke="rgba(255,250,238,.85)" stroke-width="2" fill="none"/></svg></div>
 <canvas id="cloud"></canvas>
 <section class="near" id="near">
  <div class="catw" id="catw"><div class="sh"></div><img id="catf" src="catfoam.png" alt="今天"><div class="ring"></div><div class="sub"></div></div>
  <div class="today"><div class="raft"><div class="k"><b>今天</b><span>11/11</span><i>周三 · <em id="rn" style="font-style:normal">6</em> 轮 · 19:45</i></div>
   <div class="ln"><em>他</em><span>那我先把奶煮上，你到家刚好能喝</span></div><div class="ln mine"><em>我</em><span>要加棉花糖！</span></div></div>
   <button class="go">接着聊</button></div>
 </section>
 <section class="sec mid" id="mid"><div class="hd"><b>本周</b><span>11/5 – 11/10</span></div><div id="ices"></div><div class="stk" style="left:-18px;top:102px;width:36px;height:42px;animation-delay:-3.4s"><img src="bit1.png" alt=""></div>
  <div class="stk" style="right:-6px;top:-14px;width:58px;height:58px"><img src="bit6.png" alt=""><b>31<small>轮</small></b></div></section>
 <section class="sec far" id="far"><div class="hd"><b>更早</b><span>10/8 – 11/4</span></div><div id="pls"></div><div class="stk" style="left:-14px;top:104px;width:44px;height:32px;animation-delay:-1.2s"><img src="bit2.png" alt=""></div>
  <div class="stk st" style="right:-4px;top:-26px;width:56px;height:56px;animation-delay:-2s"><img src="bit3.png" alt=""><b style="font-size:13px;margin-top:4px">4<small>周</small></b></div></section>
</div>
<div id="drop"></div>'''
s=s.replace('<div class="list" id="list"></div>','<div class="list" id="list"></div>'+HTML,1)
JS=r'''
<script>
(()=>{
const $=q=>document.querySelector(q),SC=$('#sc');
const W=[["11/5 周四",4,"下雨没带伞，聊到小时候"],["11/6 周五",7,"加班到很晚，陪你等末班车"],["11/7 周六",0,""],["11/8 周日",12,"带你去吃了那家新开的甜品店"],["11/9 周一",3,"周一早八，起不来"],["11/10 周二",5,"复习到一半一起背单词"]];
const K=[["10/29 – 11/4",6,"这周你一直在忙期中，我每天都在等你下课"],["10/22 – 28",5,"楼下的猫生了小猫，你天天去看"],["10/15 – 21",7,"帮你列搬家清单，纸箱不够"],["10/8 – 14",4,"第一次聊天，你给我起了名字"]];
const IP=[[4,26,-8],[62,70,6],[118,22,-4],[176,62,10],[234,24,-12],[290,66,4]],PP=[[30,40],[112,72],[196,34],[278,62]];let wi=3,ki=0;
function draw(){const mw=$('#mid').clientWidth-40,sc=mw/340;
 $('#ices').innerHTML=W.map((x,i)=>{const[p,q,r]=IP[i];return `<button class="ice${x[1]?'':' e'}${i==wi?' on':''}" data-w="${i}" aria-label="${x[0]}" style="left:${14+p*sc}px;top:${q+20}px;--r:${r}deg"><img src="ice.png" alt=""></button>`}).join('')+
 `<div class="co" style="top:158px"><div class="raft"><div class="k"><b style="font:15px/1 WK">${W[wi][0]}</b><span>${W[wi][1]} 轮</span></div><p>${W[wi][2]}</p><a>接着这天聊 ›</a></div></div>`;
 $('#pls').innerHTML=K.map((x,i)=>{const[a,b]=PP[i];return `<button class="prl${i==ki?' on':''}" data-k="${i}" aria-label="${x[0]}" style="left:${14+a*sc}px;top:${b+20}px"><img src="pearl.png" alt=""></button>`}).join('')+
 `<div class="co" style="top:136px"><div class="raft"><div class="k"><b style="font:15px/1 WK">${K[ki][0]}</b><span>${K[ki][1]} 天</span></div><p>${K[ki][2]}</p><a>看这一周 ›</a></div></div>`;
 document.querySelectorAll('[data-w]').forEach(e=>e.onclick=()=>{if(W[+e.dataset.w][1]){wi=+e.dataset.w;draw();bloomed={}}});
 document.querySelectorAll('[data-k]').forEach(e=>e.onclick=()=>{ki=+e.dataset.k;draw();bloomed={}});
}
draw();
// 小气泡（L3，便宜的 transform 动画）
for(let i=0;i<9;i++){const b=document.createElement('i');b.className='bub';const z=4+Math.random()*5;b.style.cssText=`left:${8+Math.random()*84}%;top:${260+Math.random()*560}px;width:${z}px;height:${z}px;animation-duration:${6+Math.random()*6}s;animation-delay:${-Math.random()*10}s`;$('#scene').appendChild(b)}
// 视差
SC.addEventListener('scroll',()=>{const y=SC.scrollTop;$('#mid').style.transform=`translateY(${y*.1}px)`;$('#far').style.transform=`translateY(${y*.18}px)`},{passive:true});
// 水位 = 今天轮数
const rounds=6;$('#near').style.paddingTop=(6+Math.round((20-Math.min(rounds,20))*3.4))+'px';
const cv=$('#cloud'),cx=cv.getContext('2d'),drop=$('#drop'),scene=$('#scene');let DPR=Math.min(2,devicePixelRatio||1),VW=0,VH=0;
const SP=document.createElement('canvas');SP.width=SP.height=64;{const g=SP.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,32);gr.addColorStop(0,'rgba(255,250,238,1)');gr.addColorStop(.45,'rgba(252,244,228,.55)');gr.addColorStop(1,'rgba(250,240,222,0)');g.fillStyle=gr;g.fillRect(0,0,64,64)}
function size(){VW=scene.clientWidth;VH=SC.clientHeight;cv.width=VW*DPR;cv.height=VH*DPR;cv.style.width=VW+'px';cv.style.height=VH+'px';cx.setTransform(DPR,0,0,DPR,0,0);place()}
function sy0(){return scene.getBoundingClientRect().top-SC.getBoundingClientRect().top+SC.scrollTop}
function place(){const c=$('#catw').getBoundingClientRect(),s=scene.getBoundingClientRect(),y=c.top-s.top+c.height*.7;const L=$('#liq');L.style.top=y+'px';L.style.height=(scene.scrollHeight-y)+'px'}
function anchors(){const s=scene.getBoundingClientRect(),o=[];const c=$('#catw').getBoundingClientRect();o.push([c.left-s.left+c.width*.42,c.top-s.top+c.height*.9,'c']);
 for(const q of ['.ice.on','.prl.on']){const e=document.querySelector(q);if(e){const r=e.getBoundingClientRect();o.push([r.left-s.left+r.width/2,r.top-s.top+r.height/2,q])}}return o}
function xAt(y,o){if(y<=o[0][1])return o[0][0];for(let k=0;k<o.length-1;k++){const[a,ay]=o[k],[b,by]=o[k+1];if(y<=by){let t=(y-ay)/(by-ay);t=t*t*(3-2*t);return a+(b-a)*t+Math.sin(t*Math.PI)*24*(k%2?-1:1)}}return o[o.length-1][0]}
const P=[];let dx=null,last=null,prevY=null,bloomed={},lt=performance.now();
function puff(x,y,r,vx,vy,life){if(P.length>240)P.shift();P.push({x,y,r,g:r*(2.2+Math.random()*1.4),vx,vy,t:0,life,a:.6+Math.random()*.25,ph:Math.random()*6})}
function frame(now){const dt=Math.min(50,now-lt)/1000;lt=now;const st=SC.scrollTop,top=sy0(),o=anchors(),Lend=o[o.length-1][1];
 const mx=Math.max(1,SC.scrollHeight-VH),pr=Math.min(1,st/mx);let y=o[0][1]+(Lend-o[0][1])*pr;
 const tx=xAt(y,o);dx=dx==null?tx:dx+(tx-dx)*.3;const vy=prevY==null?0:y-prevY;prevY=y;const atRest=pr<.004,arrive=Lend-y<3;
 if(!atRest&&last){const d=Math.hypot(dx-last[0],y-last[1]),n=Math.min(6,Math.floor(d/5));for(let k=1;k<=n;k++){const t=k/n;puff(last[0]+(dx-last[0])*t+(Math.random()-.5)*4,last[1]+(y-last[1])*t,4+Math.random()*3,(Math.random()-.5)*6,-4-Math.random()*6,3+Math.random()*2)}if(n)last=[dx,y]}else last=[dx,y];
 for(const a of o.slice(1)){if(Math.abs(y-a[1])<14&&!bloomed[a[2]]){bloomed[a[2]]=1;for(let k=0;k<14;k++){const g=k/14*6.283,sp=14+Math.random()*16;puff(a[0],a[1],6+Math.random()*4,Math.cos(g)*sp,Math.sin(g)*sp*.7,4+Math.random()*2)}
  if(a[2]=='.prl.on'){const e=document.querySelector('.prl.on');e.classList.remove('hug');void e.offsetWidth;e.classList.add('hug')}}if(Math.abs(y-a[1])>60)bloomed[a[2]]=0}
 const vt=st-top;cv.style.transform=`translateY(${vt}px)`;cx.clearRect(0,0,VW,VH);
 for(let k=P.length-1;k>=0;k--){const p=P[k];p.t+=dt;if(p.t>p.life){P.splice(k,1);continue}const u=p.t/p.life;p.x+=(p.vx+Math.sin(p.ph+p.t*1.6)*5)*dt;p.y+=p.vy*dt;p.vx*=.985;p.vy*=.985;
  const r=p.r+(p.g-p.r)*(1-Math.pow(1-u,2.2)),yy=p.y-vt;if(yy<-60||yy>VH+60)continue;cx.globalAlpha=p.a*(u<.12?u/.12:1)*(1-u)*(1-u*.3);cx.drawImage(SP,p.x-r,yy-r,r*2,r*2)}
 cx.globalAlpha=1;
 const sr=scene.getBoundingClientRect(),stretch=Math.min(.6,Math.abs(vy)/18),sc=Math.max(.7,1-(y-o[0][1])/2000);
 drop.style.opacity=(arrive||atRest)?0:1;drop.style.left=(sr.left+dx)+'px';drop.style.top=(sr.top+y)+'px';drop.style.transform=`scale(${sc*(1-stretch*.35)},${sc*(1+stretch)})`;
}
let run=true;function loop(t){if(!run)return;frame(t);requestAnimationFrame(loop)}
document.addEventListener('visibilitychange',()=>{run=!document.hidden;lt=performance.now();if(run)requestAnimationFrame(loop)});
addEventListener('resize',size);
// 猫奶奶 Duang：弹簧挤压，只改 transform
const cw=$('#catw');let sp=0,sv=0,ca=false;cw.onclick=()=>{sv-=.09;if(!ca){ca=true;requestAnimationFrame(function f(){sv+=-sp*.2;sv*=.84;sp+=sv;cw.style.transform=`scale(${1-sp*.6},${1+sp})`;if(Math.abs(sp)+Math.abs(sv)>.0005)requestAnimationFrame(f);else{cw.style.transform='';ca=false}})}};
function go(){size();requestAnimationFrame(loop)}if($('#catf').complete)go();else $('#catf').onload=go;
})();
</script>'''
s=s.replace('</body>',JS+'</body>') if '</body>' in s else s+JS
open(R+'vb3.html','w').write(s)
print('ok')
