import re
s=open('p/list/wfE.html').read()
s=s.replace('<title>聊天 · 灰稿 E 景深</title>','<title>聊天 · 灰稿 E + 猫猫滴奶成云</title>')
s=s.replace('<div class="catf"></div>','<img class="catf" id="catf" src="catfoam.png" alt="">')
s=re.sub(r'\.catf\{[^}]*\}\n\.catf::before,\.catf::after\{[^}]*\}\.catf::before\{[^}]*\}\.catf::after\{[^}]*\}\n','',s)
css='''.catf{flex:none;width:clamp(130px,40vw,165px);height:auto;margin-top:6px}
.app{background:linear-gradient(180deg,#d9c3a8 0,#c4a483 40%,#ad8a68 100%)}
.ann{color:#b0124a}.hd h1,.today b{color:#3a2a20}.today small,.mid .tt,.co small{color:#6d5444!important}.today p,.co,.co a{color:#3a2a20!important}
.ice{background:rgba(255,255,255,.35);border-color:rgba(255,255,255,.6)}.prl{background:#4a3226}
.ln{display:none}
#cloud{position:fixed;z-index:1;pointer-events:none}
.pl.mid,.pl.far{z-index:2}.near{z-index:3}
#drop{position:fixed;z-index:20;width:16px;height:20px;margin:-14px 0 0 -8px;border-radius:50% 50% 50% 50%/62% 62% 40% 40%;background:radial-gradient(circle at 35% 62%,#fffdf6 0,#f6ecd9 45%,#e2cfb2 100%);transform-origin:50% 30%;will-change:transform;cursor:pointer}
#drop{transition:opacity .35s}
.prl.hug{animation:hug .7s cubic-bezier(.3,1.6,.5,1)}@keyframes hug{0%{scale:1}30%{scale:1.25 .85;translate:0 -6px}60%{scale:.92 1.08}100%{scale:1}}
#fps{position:fixed;right:8px;bottom:88px;z-index:60;font:11px monospace;color:#b0124a}
@media (prefers-reduced-motion:reduce){#cloud,#drop{display:none}}
'''
s=s.replace('</style>',css+'</style>')
ann='<p class="ann" style="padding:6px 24px 0;position:relative;z-index:6"><span class="lab">4</span>猫猫奶盖垂着一滴奶。往下滑，奶滴掉进奶茶边沉边散成奶云，经过选中那块冰开一朵，滑到底落到选中的珍珠上，珍珠蹦一下（奶奶见到乖孙）；奶云慢慢卷边、变淡。点奶滴会晃一下。背景临时铺奶茶色只为看清奶云</p>'
s=s.replace('<section class="pl near"',ann+'<section class="pl near"',1)
s=s.replace('<nav class="nav">','<canvas id="cloud"></canvas><div id="drop"></div><div id="fps"></div>\n<nav class="nav">')
js=r'''
// —— 猫猫滴奶成云 ——
const cv=$('#cloud'),cx=cv.getContext('2d'),drop=$('#drop');let DPR=Math.min(2,devicePixelRatio||1),VW=0,VH=0,AR;
const SP=document.createElement('canvas');SP.width=SP.height=64;{const g=SP.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,32);gr.addColorStop(0,'rgba(255,250,238,1)');gr.addColorStop(.45,'rgba(252,244,228,.55)');gr.addColorStop(1,'rgba(250,240,222,0)');g.fillStyle=gr;g.fillRect(0,0,64,64)}
function size(){AR=app.getBoundingClientRect();VW=AR.width;VH=AR.height;cv.style.left=AR.left+'px';cv.style.top=AR.top+'px';cv.width=VW*DPR;cv.height=VH*DPR;cv.style.width=VW+'px';cv.style.height=VH+'px';cx.setTransform(DPR,0,0,DPR,0,0)}
const P=[];let dx=null,dyC=null,prevY=null,st0=0,wob=0,wv=0,bloomed={};
function anchors(){const st=app.scrollTop,o=[];AR=app.getBoundingClientRect();
 const c=$('#catf').getBoundingClientRect();o.push([c.left-AR.left+c.width*.42,c.bottom-AR.top+st-4,'c']);
 const i=document.querySelector('.ice.on');if(i){const r=i.getBoundingClientRect();o.push([r.left-AR.left+r.width/2,r.top-AR.top+st+r.height/2,'w'+i.dataset.w])}
 const p=document.querySelector('.prl.on');if(p){const r=p.getBoundingClientRect();o.push([r.left-AR.left+r.width/2,r.top-AR.top+st+r.height/2,'k'+p.dataset.k])}
 return o}
function xAt(y,o){if(y<=o[0][1])return o[0][0];for(let k=0;k<o.length-1;k++){const[a,ay]=o[k],[b,by]=o[k+1];if(y<=by){let t=(y-ay)/(by-ay);t=t*t*(3-2*t);return a+(b-a)*t+Math.sin(t*Math.PI)*24*(k%2?-1:1)}}return o[o.length-1][0]}
function puff(x,y,r,vx,vy,life){if(P.length>260)P.shift();P.push({x,y,r,g:r*(2.2+Math.random()*1.4),vx,vy,t:0,life,a:.55+Math.random()*.25,ph:Math.random()*6})}
let lt=performance.now();
function frame(now){const dt=Math.min(50,now-lt)/1000;lt=now;const st=app.scrollTop,o=anchors();
 const mx=Math.max(1,app.scrollHeight-VH),pr=Math.min(1,st/mx),L=o[o.length-1][1];let y=o[0][1]+(L-o[0][1])*pr;y=Math.max(y,Math.min(L,st+VH*.12));const tx=xAt(y,o),arrive=L-y<3;dx=dx==null?tx:dx+(tx-dx)*.3;
 const vy=prevY==null?0:y-prevY;prevY=y;
 // 沿途吐奶雾：走得越慢吐得越浓
 if(dyC!=null){const d=Math.hypot(dx-dyC[0],y-dyC[1]);const n=Math.min(6,Math.floor(d/5));for(let k=1;k<=n;k++){const t=k/n;puff(dyC[0]+(dx-dyC[0])*t+(Math.random()-.5)*4,dyC[1]+(y-dyC[1])*t,4+Math.random()*3,(Math.random()-.5)*6,-4-Math.random()*6,3+Math.random()*2)}if(n)dyC=[dx,y]}else dyC=[dx,y];
 if(Math.abs(vy)<.3&&y>o[0][1]+2&&Math.random()<.25)puff(dx,y,3,(Math.random()-.5)*4,2,2.5);
 // 到选中那天开一朵
 for(const a of o.slice(1)){if(Math.abs(y-a[1])<14&&!bloomed[a[2]]){bloomed[a[2]]=1;if(a[2][0]=='k'){const e=document.querySelector('.prl.on');e.classList.remove('hug');void e.offsetWidth;e.classList.add('hug')}for(let k=0;k<14;k++){const ang=k/14*6.283+Math.random()*.3,sp=14+Math.random()*16;puff(a[0],a[1],6+Math.random()*4,Math.cos(ang)*sp,Math.sin(ang)*sp*.7,4+Math.random()*2)}}if(Math.abs(y-a[1])>60)bloomed[a[2]]=0}
 // 画奶云
 cx.clearRect(0,0,VW,VH);
 for(let k=P.length-1;k>=0;k--){const p=P[k];p.t+=dt;if(p.t>p.life){P.splice(k,1);continue}const u=p.t/p.life;
  p.x+=(p.vx+Math.sin(p.ph+p.t*1.6)*5)*dt;p.y+=p.vy*dt;p.vx*=.985;p.vy*=.985;
  const r=p.r+(p.g-p.r)*(1-Math.pow(1-u,2.2)),sy=p.y-st;if(sy<-60||sy>VH+60)continue;
  cx.globalAlpha=p.a*(u<.12?u/.12:1)*(1-u)*(1-u*.3);cx.drawImage(SP,p.x-r,sy-r,r*2,r*2)}
 cx.globalAlpha=1;
 // 奶滴：静止时垂着晃，下落按速度拉长
 const atRest=y<=o[0][1]+1;wv+=-wob*.12;wv*=.88;wob+=wv;
 const stretch=Math.min(.6,Math.abs(vy)/18),sc=atRest?1:Math.max(.7,1-(y-o[0][1])/2000);
 drop.style.opacity=arrive?0:1;drop.style.left=(AR.left+dx)+'px';drop.style.top=(AR.top+y-st)+'px';
 drop.style.transform=`scale(${sc*(1-stretch*.35)},${sc*(1+stretch)+(atRest?Math.sin(now/600)*.05:0)}) rotate(${wob}deg)`;
}
let run=true,fc=0,ft=performance.now();
function loop(t){if(!run)return;frame(t);fc++;if(t-ft>1000){$('#fps').textContent=fc+'fps';fc=0;ft=t}requestAnimationFrame(loop)}
drop.onclick=()=>{wv=9};
document.addEventListener('visibilitychange',()=>{run=!document.hidden;lt=performance.now();if(run)requestAnimationFrame(loop)});
addEventListener('resize',size);
function go(){size();requestAnimationFrame(loop)}
if($('#catf').complete)go();else $('#catf').onload=go;
'''
s=s.replace('</script></body>',js+'</script></body>')
open('p/list/milk.html','w').write(s)
