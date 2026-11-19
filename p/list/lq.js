/* 杯格液体：一维浅水方程，物理部分移植自 slosh (MIT, Pavel Železný)，渲染用 Canvas2D 自画 */
(()=>{
const N=48,DX=1/N,G=6,H0=0.5,NU=0.09,DRAG=2.3,SUB=1/300,AT=2.6,FT=4.5,ST=0.09;
const clamp=(v,a,b)=>v<a?a:v>b?b:v;
class Liquid{constructor(){this.h=new Float32Array(N);this.u=new Float32Array(N+1);this.aer=new Float32Array(N);this.foam=new Float32Array(N);this.slope=0;this._tu=new Float32Array(N+1);this._ta=new Float32Array(N);this._acc=0}
 advance(dt,target,ax,shake){this.slope+=(target-this.slope)*(1-Math.exp(-dt/ST));const gx=G*this.slope+ax;this._acc=Math.min(this._acc+dt,.1);while(this._acc>=SUB){this._acc-=SUB;this._f(gx)}this._air(dt,shake)}
 _f(gx){const{h,u,_tu:tu,aer,_ta:ta}=this,dt=SUB;for(let i=1;i<N;i++)u[i]+=((G*(h[i-1]-h[i]))/DX+gx)*dt;u[0]=0;u[N]=0;tu.set(u);const d=1-DRAG*dt;for(let i=1;i<N;i++)u[i]=(tu[i]+NU*(tu[i-1]-2*tu[i]+tu[i+1]))*d;const k=(H0/DX)*dt;for(let i=0;i<N;i++)h[i]-=(u[i+1]-u[i])*k;const c=dt/DX;for(let i=0;i<N;i++){const x=i-.5*(u[i]+u[i+1])*c,i0=Math.floor(x),f=x-i0,j0=clamp(i0,0,N-1),j1=clamp(i0+1,0,N-1);ta[i]=aer[j0]+(aer[j1]-aer[j0])*f}aer.set(ta)}
 _air(dt,shake){const{u,h,aer,foam}=this,da=Math.exp(-dt/AT),df=Math.exp(-dt/FT),s=this.slope;for(let i=0;i<N;i++){const sh=Math.abs(u[i+1]-u[i])/DX,ia=i>0?i-1:0,ib=i<N-1?i+1:N-1,ra=h[ia]-s*((ia+.5)*DX-.5),rb=h[ib]-s*((ib+.5)*DX-.5),st=Math.abs(rb-ra)/((ib-ia)*DX),t=Math.min(1,sh*.05+st*.6),brk=Math.max(0,st-.35);aer[i]=Math.min(1,aer[i]*da+shake*t*dt*2.4);foam[i]=Math.min(1,foam[i]*df+(shake*.7+brk)*t*dt*1.8)}}
 get energy(){let e=0;for(let i=0;i<=N;i++)e+=this.u[i]**2;for(let i=0;i<N;i++){const r=this.h[i]-this.slope*((i+.5)*DX-.5);e+=G/H0*r*r}return e/N}}

const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
/* 每杯：液面高度、颜色、待机周期 */
const SPEC={
 cocoa:{lv:.34,top:'rgba(150,98,72,.34)',bot:'rgba(110,70,52,.44)',film:'rgba(255,240,226,.55)',P:6.2,ph:.3,A:.10},
 boba:{lv:.44,top:'rgba(214,170,128,.40)',bot:'rgba(190,140,100,.48)',film:'rgba(255,246,232,.6)',P:7.4,ph:1.9,A:.12,back:'rgba(214,170,128,.22)'},
 latte:{lv:.61,top:'rgba(196,150,112,.24)',bot:'rgba(170,120,88,.34)',film:'rgba(255,248,236,.75)',P:8.3,ph:3.1,A:.08},
 mint:{lv:.5,top:'rgba(166,217,196,.30)',bot:'rgba(120,196,168,.55)',film:'rgba(255,255,255,.75)',P:5.8,ph:.8,A:.10},
 tea:{lv:.5,top:'rgba(214,170,128,.40)',bot:'rgba(190,140,100,.50)',film:'rgba(255,246,232,.6)',P:7.4,ph:1.9,A:.12,back:'rgba(214,170,128,.22)'},
 soda:{lv:.80,top:'rgba(166,217,196,.16)',bot:'rgba(140,205,180,.42)',film:'rgba(255,255,255,.7)',P:5.6,ph:4.4,A:.09}};
const cups={};let tilt=0;
document.querySelectorAll('.dk').forEach(el=>{
 const k=['mint','tea','cocoa','boba','latte','soda'].find(c=>el.classList.contains(c));if(!k)return;
 const cv=document.createElement('canvas');cv.className='lqc';cv.setAttribute('aria-hidden','true');el.insertBefore(cv,el.firstChild);
 const c={k,el,cv,ctx:cv.getContext('2d'),sim:new Liquid(),s:SPEC[k],kick:0,kdir:0,w:0,h:0};cups[k]=c;
 el.addEventListener('pointerdown',e=>{const r=el.getBoundingClientRect();const t=clamp((e.clientX-r.left)/r.width,0,1);poke(c,t)});
});
function size(c){const r=c.el.getBoundingClientRect(),d=Math.min(2,devicePixelRatio||1);c.w=c.el.offsetWidth;c.h=c.el.offsetHeight;c.cv.width=Math.round(c.w*d);c.cv.height=Math.round(c.h*d);c.d=d}
/* 点一下：点到的那一侧液面被按下去，同时整杯受一下横向冲击，往另一边撞 */
function poke(c,t){const{h,u}=c.sim;let m=0;for(let i=0;i<N;i++){const x=(i+.5)/N,g=Math.exp(-((x-t)**2)/.006);h[i]-=.05*g;m+=.05*g}for(let i=0;i<N;i++)h[i]+=m/N;
 c.kdir=t<.5?1:-1;c.kick=.14;}
/* 手机倾斜（要 HTTPS 才有数据） */
let gx=0;addEventListener('devicemotion',e=>{const a=e.accelerationIncludingGravity;if(!a||a.x==null)return;gx+=(a.x-gx)*.12;tilt=clamp(-gx/9.8*.9,-.35,.35)});
function surf(c,x){/* x: 0..1, 返回液面相对静止的位移（容器单位），Catmull-Rom */const{h}=c.sim;const f=x*N-.5,i=Math.floor(f),t=f-i;const p=j=>h[clamp(j,0,N-1)];const p0=p(i-1),p1=p(i),p2=p(i+1),p3=p(i+2);return .5*(2*p1+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t*t+(-p0+3*p1-3*p2+p3)*t*t*t)}
const AMP=.55;/* 容器单位换成像素时的缩放：卡片很扁，波高按宽度的 0.55 画 */
window.LQ=(k,px)=>{const c=cups[k];if(!c||!c.w)return 0;return surf(c,clamp(px/c.w,0,1))*c.w*AMP};
window.LQu=(k,px)=>{const c=cups[k];if(!c||!c.w)return 0;const i=clamp(Math.round(px/c.w*N),0,N);return c.sim.u[i]*10};
const bubs=[];
function draw(c,T){const{ctx,w,h,d,s,sim}=c;ctx.setTransform(d,0,0,d,0,0);ctx.clearRect(0,0,w,h);
 const base=h*(1-s.lv),M=40,pts=[];
 for(let j=0;j<=M;j++){const x=j/M;pts.push([x*w,clamp(base-surf(c,x)*w*AMP,3,h-2)])}
 if(s.back){ctx.beginPath();ctx.moveTo(0,h);pts.forEach(([x,y],j)=>ctx.lineTo(x,y+3+Math.sin(j*.5+T*1.7)*1.2));ctx.lineTo(w,h);ctx.closePath();ctx.fillStyle=s.back;ctx.fill()}
 ctx.beginPath();ctx.moveTo(0,h);pts.forEach(([x,y])=>ctx.lineTo(x,y));ctx.lineTo(w,h);ctx.closePath();
 const g=ctx.createLinearGradient(0,base-12,0,h);g.addColorStop(0,s.top);g.addColorStop(1,s.bot);ctx.fillStyle=g;ctx.fill();
 /* 液面那层膜 */ctx.beginPath();pts.forEach(([x,y],j)=>j?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.strokeStyle=s.film;ctx.lineWidth=1.3;ctx.stroke();
 /* 泡沫：撞得猛的地方浮起小白点 */for(let i=0;i<N;i+=2){const f=sim.foam[i];if(f<.08)continue;const x=(i+.5)/N;const y=clamp(base-surf(c,x)*w*AMP,3,h-2);ctx.fillStyle=`rgba(255,252,246,${Math.min(.85,f*1.6)})`;ctx.beginPath();ctx.arc(x*w,y-.5,1+f*2.2,0,6.283);ctx.fill()}
 /* 被卷进去的气泡 */for(let i=0;i<N;i++){if(sim.aer[i]>.12&&Math.random()<sim.aer[i]*.25&&bubs.length<60)bubs.push({c,x:(i+.5)/N*w,y:h-2-Math.random()*(h-base)*.6,r:.8+Math.random()*1.8,v:10+Math.random()*16})}
 for(const b of bubs){if(b.c!==c)continue;ctx.strokeStyle='rgba(255,255,255,.85)';ctx.lineWidth=.9;ctx.beginPath();ctx.arc(b.x,b.y,b.r,0,6.283);ctx.stroke()}
}
let last=performance.now(),T0=last;
function loop(now){const dt=Math.min(.05,(now-last)/1000);last=now;const T=(now-T0)/1000;
 for(let i=bubs.length-1;i>=0;i--){const b=bubs[i];b.y-=b.v*dt;const c=b.c;if(b.y<c.h*(1-c.s.lv)-surf(c,b.x/c.w)*c.w*AMP+1)bubs.splice(i,1)}
 for(const k in cups){const c=cups[k];if(!c.w)size(c);if(c.s.lvT!=null)c.s.lv+=(c.s.lvT-c.s.lv)*(1-Math.exp(-dt*2.2));
  let ax=0,shake=0;
  if(c.kick>0){ax=c.kdir*7;shake=.9;c.kick-=dt}
  /* 待机：各杯有自己的周期和相位，轻轻晃 */
  if(!RM)ax+=Math.sin(T*6.283/c.s.P+c.s.ph)*c.s.A*G*.6;
  if(!RM)c.sim.advance(dt,tilt,ax,shake);
  draw(c,T)}
 requestAnimationFrame(loop)}
window.LQlv=(k,v,now)=>{const c=cups[k];if(!c)return;c.s.lvT=v;if(now)c.s.lv=v};window.LQpoke=(k,t)=>{const c=cups[k];if(c)poke(c,t)};window.LQh=k=>{const c=cups[k];return c&&c.w?c.h*c.s.lv:0};
addEventListener('resize',()=>{for(const k in cups)size(cups[k])});
requestAnimationFrame(loop);
})();
