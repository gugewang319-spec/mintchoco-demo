/* Mint Choco 共用组件库 · 脚本。先引 ../ui.js（MC.toast / MC.confirm），再引本文件。
   说明书：docs/KIT.md   图鉴：p/mc/index.html */
(function(){
const MC=window.MC=window.MC||{};
const INK='#5b3a2c',C='#8a5c46',P='#fbf6ea';
const BASE=(document.currentScript&&document.currentScript.src||'').replace(/mc\.js.*$/,'');
MC.INK=INK;MC.C=C;MC.P=P;MC.BASE=BASE;

/* ── 六态（签条 / 小票 / 普通行共用，改色只改这里） ── */
MC.STATES={
 ok:    {band:['#7cc4ad','#3f9a80'],tint:'#c4e8da',dia:'#9fd6c3',cup:'mint'},
 making:{band:['#b07a5e','#8a5c46'],tint:'#e9dccd',dia:'#d6c0aa',cup:'cocoa'},
 fail:  {band:['#e3a08f','#c9786a'],tint:'#f3d6cc',dia:'#e9b5a7',cup:'berry'},
 warn:  {band:['#f0cf8f','#c99a48'],tint:'#f5e4c3',dia:'#ecd09c',cup:'caramel'},
 empty: {band:['#d9cbbd','#bfae9e'],tint:'#ece4da',dia:'#d9cbbd',cup:'empty'}};
const S=k=>MC.STATES[k]||MC.STATES.empty;
MC.cup=k=>BASE+'img/cup-'+(MC.STATES[k]?S(k).cup:k)+'.png';   // 状态小杯，或直接给 mint/berry/leaf…
let uid=0;MC.uid=p=>(p||'u')+(uid++);

/* ── 状态记号：勾 / 叉 / 转圈 ── */
MC.mark=function(k){
 if(k==='making')return `<g><circle r="5" fill="none" stroke="${INK}" stroke-width="4.4" stroke-dasharray="8 4.5" stroke-linecap="round"/><circle r="5" fill="none" stroke="${P}" stroke-width="2.4" stroke-dasharray="8 4.5" stroke-linecap="round"/><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="2.4s" repeatCount="indefinite"/></g>`;
 const g=k==='ok'?`<path d="M-5 0-1.5 3.8 5.5-4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`:`<path d="M-4.5-4.5 4.5 4.5M4.5-4.5-4.5 4.5" stroke-linecap="round"/>`;
 return `<g stroke="${INK}" stroke-width="5">${g}</g><g stroke="${P}" stroke-width="2.8">${g}</g>`};
MC.markSVG=(k,size=18)=>`<svg width="${size}" height="${size}" viewBox="-9 -9 18 18">${MC.mark(k)}</svg>`;

/* ── info 图标（配 .tip 用） ── */
MC.info=(label='怎么办')=>`<button class="ii" aria-label="${label}"><svg width="14" height="14" viewBox="-7 -7 14 14"><circle r="6" fill="${P}" stroke="${INK}" stroke-width="1.2"/><circle cy="-2.6" r=".85" fill="${INK}"/><path d="M0-.6v3.6" stroke="${INK}" stroke-width="1.3" stroke-linecap="round"/></svg></button>`;
addEventListener('click',e=>{const b=e.target.closest('.ii'),box=b&&(b.closest('[data-tipbox]')||b.parentNode.parentNode),mine=box&&box.querySelector('.tip');
 document.querySelectorAll('.tip.on').forEach(t=>{if(t!==mine)t.classList.remove('on')});if(mine){e.stopPropagation();mine.classList.toggle('on')}});

/* ── 签条（竖版，奶油波浪底 + 吸管夹） ──
   MC.tag({name,state,count,unit,sel,add,h})  → 元素 */
MC.tagSVG=function(state,h,add){const s=S(state),id=MC.uid('t'),W=62,T=14,x0=4,x1=W-4,r=10,k=4,st=(x1-x0)/k,b=st/2,y1=T+h;
 let d=`M${x0} ${y1}V${T+r}Q${x0} ${T} ${x0+r} ${T}H${x1-r}Q${x1} ${T} ${x1} ${T+r}V${y1}`;for(let i=0;i<k;i++)d+=`A${b} ${b} 0 0 1 ${x1-st*(i+1)} ${y1}`;d+='Z';
 if(add)return `<svg width="${W}" height="${y1+10}"><path d="${d}" fill="rgba(252,250,244,.5)" stroke="${C}" stroke-width="1.3" stroke-dasharray="5 4"/><rect x="${W/2-7}" y="0" width="14" height="22" rx="3" fill="${C}" stroke="${INK}" stroke-width="1.2"/><path d="M${W/2} ${y1-30}v14M${W/2-7} ${y1-23}h14" stroke="${C}" stroke-width="2" stroke-linecap="round"/></svg>`;
 return `<svg width="${W}" height="${y1+10}"><defs><linearGradient id="f${id}" x1="0" y1="0" x2="0" y2="1"><stop offset=".25" stop-color="${P}"/><stop offset="1" stop-color="${s.tint}"/></linearGradient>
 <linearGradient id="mk${id}" x1="0" y1="0" x2="0" y2="1"><stop offset=".45" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient><mask id="m${id}"><rect width="${W}" height="${y1+10}" fill="url(#mk${id})"/></mask>
 <pattern id="d${id}" width="16" height="14" patternUnits="userSpaceOnUse" patternTransform="translate(${x0} ${T})"><rect x="1.5" y="1.5" width="13" height="11" rx="2.5" fill="${s.dia}" opacity=".55"/></pattern>
 <linearGradient id="b${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${s.band[0]}"/><stop offset="1" stop-color="${s.band[1]}"/></linearGradient><clipPath id="c${id}"><path d="${d}"/></clipPath></defs>
 <path d="${d}" transform="translate(0 3)" fill="${INK}" opacity=".16"/><path d="${d}" fill="url(#f${id})"/>
 <g clip-path="url(#c${id})"><rect x="0" y="${T}" width="${W}" height="${h}" fill="url(#d${id})" mask="url(#m${id})"/><rect x="0" y="${T}" width="${W}" height="9" fill="url(#b${id})"/></g>
 <path d="${d}" fill="none" stroke="${INK}" stroke-width="1.4" ${state==='empty'?'stroke-dasharray="6 4"':''}/>
 <path d="M${x0+4} ${T+13}H${x1-4}" stroke="${C}" stroke-width=".7" opacity=".4"/>
 <rect x="${W/2-7}" y="0" width="14" height="22" rx="3" fill="url(#b${id})" stroke="${INK}" stroke-width="1.2"/><path d="M${W/2-3} 4v13" stroke="${P}" stroke-width="1" opacity=".6" stroke-linecap="round"/></svg>`};
MC.tag=function(o){const h=o.h||(o.sel?182:160),e=document.createElement(o.add?'button':'div');
 e.className='tg'+(o.sel?' sel':'')+(o.add?' add':'');
 if(o.add){e.setAttribute('aria-label',o.name||'新建');e.innerHTML=MC.tagSVG(null,h,1)+`<span class="nm">${o.name||'新建'}</span>`;return e}
 e.setAttribute('role','option');e.setAttribute('aria-selected',!!o.sel);e.tabIndex=0;
 e.setAttribute('aria-label',o.name+(o.count!=null?'，'+o.count+' '+(o.unit||''):''));
 e.innerHTML=MC.tagSVG(o.state,h)+`<span class="nm">${o.name}</span><img class="cp" src="${MC.cup(o.state)}" style="top:${h-22}px" alt="">`+(o.count!=null?`<span class="kc" style="top:${h-42}px">${o.count}<small>${o.unit||''}</small></span>`:'');
 e.onkeydown=ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();e.click()}};return e};

/* ── 普通行 ──  MC.row({cup,k,sub,v,vs})  vs: ok | bad | '' */
MC.row=o=>`<div class="rw"><img src="${MC.cup(o.cup||'empty')}" alt=""><span class="k">${o.k}${o.sub?`<small>${o.sub}</small>`:''}</span>${o.v!=null?`<span class="v ${o.vs||''}">${o.v}</span>`:''}</div>`;

/* ── 模型小签 ──  MC.chips([[名, 开?, 新?]]) */
MC.chips=list=>`<div class="chips">${list.map(m=>`<span class="${m[1]?'':'off'}${m[2]?' nw':''}"><i></i>${m[0]}</span>`).join('')}</div>`;

/* ── 小圆章：MC.seal(字,英文环字,类名,读屏名)，颜色跟 currentColor ── */
MC.seal=function(w,en,cls,label){const id=MC.uid('se');return `<button class="seal ${cls}" aria-label="${label}"><i class="sl"><svg viewBox="0 0 100 100" aria-hidden="true"><defs><path id="${id}" d="M50 50 m-37 0 a37 37 0 1 1 74 0 a37 37 0 1 1 -74 0"/></defs><circle cx="50" cy="50" r="47" fill="none" stroke="currentColor" stroke-width="2.6"/><circle cx="50" cy="50" r="42" fill="none" stroke="currentColor" stroke-width="1"/><text font-family="Baloo" font-size="9" font-weight="700" fill="currentColor"><textPath href="#${id}" textLength="226" lengthAdjust="spacing">MINT CHOCO ◆ ${en} ◆</textPath></text></svg><b>${w}</b></i></button>`};

/* ── 店章 ──  MC.stamp('存'|'开')；没改时 .mute 淡着，盖下加 .inked */
MC.stamp=function(w){const id=MC.uid('sr'),en=w=='开'?'NEW ORDER':'ORDER SAVED';
 return `<button class="sv st mute" aria-label="${w=='开'?'开单':'保存'}"><i class="sl"><svg viewBox="0 0 100 100" aria-hidden="true"><defs><path id="${id}" d="M50 50 m-37 0 a37 37 0 1 1 74 0 a37 37 0 1 1 -74 0"/></defs><circle cx="50" cy="50" r="47" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="50" cy="50" r="43" fill="none" stroke="currentColor" stroke-width=".9"/><circle cx="50" cy="50" r="27" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="1.2 2.6"/><text font-family="Baloo" font-size="8.2" font-weight="700" fill="currentColor"><textPath href="#${id}" textLength="226" lengthAdjust="spacing">MINT CHOCO ◆ ${en} ◆ TEA ATELIER ◆</textPath></text></svg><b>${w}</b></i></button>`};

/* ── 小票纸卷 ──  MC.roll(el,[{st,t,c,m,tm,tip,nw}],{more:'更早的'}) */
MC.roll=function(R,SEG,o={}){const W=208,SH=96,N=SEG.length,L=68,H=L+N*SH+40,n=5,ST=MC.STATES;
 let d=`M0 0H${W}`;for(let i=1;i<=N;i++){const y=L+i*SH;d+=`V${y-n}A${n} ${n} 0 0 0 ${W} ${y+n}`}d+=`V${H}H0`;for(let i=N;i>=1;i--){const y=L+i*SH;d+=`V${y+n}A${n} ${n} 0 0 0 0 ${y-n}`}d+='Z';
 let tears='';for(let i=1;i<N;i++)tears+=`<path d="M${n+6} ${L+i*SH}H${W-n-6}" stroke="${C}" stroke-width="1.2" stroke-dasharray="2 4" stroke-linecap="round" opacity=".55"/>`;
 const bands=SEG.map((s,i)=>`<rect x="0" y="${L+i*SH}" width="${W}" height="${SH}" fill="url(#rt${s.st})"/>`).join('');
 const grads=Object.keys(ST).map(k=>`<linearGradient id="rt${k}" x1="0" x2="1"><stop offset=".55" stop-color="${P}" stop-opacity="0"/><stop offset="1" stop-color="${ST[k].tint}" stop-opacity=".75"/></linearGradient>`).join('');
 R.classList.add('roll');
 R.innerHTML=`<svg class="paper" width="${W}" height="${H}" aria-hidden="true"><defs>${grads}<linearGradient id="pf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fdfaf2"/><stop offset="${(H-60)/H}" stop-color="#fdfaf2"/><stop offset="1" stop-color="#fdfaf2" stop-opacity="0"/></linearGradient><linearGradient id="po" x1="0" y1="0" x2="0" y2="1"><stop offset="${(H-90)/H}" stop-color="${INK}"/><stop offset="1" stop-color="${INK}" stop-opacity="0"/></linearGradient><linearGradient id="ps" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${INK}" stop-opacity=".22"/><stop offset=".12" stop-color="${INK}" stop-opacity="0"/></linearGradient><clipPath id="pc"><path d="${d}"/></clipPath></defs>
 <path d="${d}" transform="translate(3 3)" fill="${INK}" opacity=".12"/><path d="${d}" fill="url(#pf)"/><g clip-path="url(#pc)">${bands}<rect y="0" width="${W}" height="30" fill="url(#ps)"/><rect y="${L-4}" width="${W}" height="${SH*.4}" fill="url(#ps)" opacity=".5"/></g>${tears}<path d="${d}" fill="none" stroke="url(#po)" stroke-width="1.3"/></svg>`
 +'<div class="lead"></div>'+SEG.map(s=>`<div class="seg ${s.st}${s.nw?' new':''}" data-tipbox><img class="cp" src="${MC.cup(s.st)}" alt=""><svg class="mk" viewBox="-9 -9 18 18">${MC.mark(s.st)}</svg><div class="st">${s.t}${s.tip?' '+MC.info():''}</div><div class="mt"><span style="flex:none">${s.c}</span><span>${s.m}</span></div><span class="tm">${s.tm}</span>${s.tip?`<div class="tip" role="tooltip">${s.tip}</div>`:''}</div>`).join('')
 +(o.more===false?'':`<button class="more">${o.more||'更早的'}</button>`)};

/* ── 页顶 ──  MC.head({title,en,back:'回到设置',right:[{icon:'search',label:'找渠道',id}]}) */
const ICON={back:'<svg width="22" height="22" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"><path d="m15 18-6-6 6-6"/></svg>',
 search:'<svg width="19" height="19" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="6.8" cy="6.8" r="4.6"/><path d="M10.3 10.3l3.6 3.6"/></svg>',
 plus:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'};
MC.ICON=ICON;
MC.head=function(o){const h=document.createElement('header');h.className='lhead';
 h.innerHTML=`<div class="lf">${o.back?`<button class="pb glass" aria-label="${o.back}" data-act="back">${ICON.back}</button>`:''}<div class="ttl">${o.en?`<span class="sc" aria-hidden="true">${o.en}</span>`:''}<h1>${o.title}</h1></div></div>`
  +(o.right||[]).map(r=>`<button class="pb glass" aria-label="${r.label}"${r.id?` id="${r.id}"`:''}>${ICON[r.icon]||r.icon}</button>`).join('');
 return h};

/* ── 底栏 ──  MC.nav('设置', {dots:['记忆']})  挂到 body 末尾，自带渐隐 */
const TABS=[
 ['今天','<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#5b3a2c" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 13C5 8.6 8.4 6.6 12 6.6s7 2 9.5 6.4C19 17.3 15.6 19.2 12 19.2S5 17.3 2.5 13Z" fill="#c4e8da"/><circle cx="12" cy="12.9" r="3.3" fill="#5b3a2c"/><circle cx="13.2" cy="11.8" r="0.9" fill="#fbf6ea" stroke="none"/><path d="M8 6.1 7 4.2M12 5.4V3.3M16 6.1l1-1.9"/></svg>','today'],
 ['记忆','<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#5b3a2c" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="16.5" rx="2.6" fill="#c4e8da"/><path d="M8.2 3v16.5"/><path d="M13.7 13.4c-1.9-1.3-2.9-2.3-2.9-3.4a1.45 1.45 0 0 1 2.9-.5 1.45 1.45 0 0 1 2.9.5c0 1.1-1 2.1-2.9 3.4Z" fill="#5b3a2c" stroke="none"/><path d="M14.6 19.5v3l1.3-1 1.3 1v-3" fill="#fbf6ea"/></svg>','mem'],
 ['聊天','<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#5b3a2c" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4.2c4.7 0 8.5 3.1 8.5 7s-3.8 7-8.5 7c-1 0-1.9-.1-2.8-.4L4.8 19.6l1.3-3.5C4.6 14.8 3.5 13.1 3.5 11.2c0-3.9 3.8-7 8.5-7Z" fill="#c4e8da"/><circle cx="8.6" cy="11.3" r="1.1" fill="#5b3a2c" stroke="none"/><circle cx="12" cy="11.3" r="1.1" fill="#5b3a2c" stroke="none"/><circle cx="15.4" cy="11.3" r="1.1" fill="#5b3a2c" stroke="none"/></svg>','list'],
 ['人格','<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#5b3a2c" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 21c.5-3.8 3.6-6.3 7.5-6.3s7 2.5 7.5 6.3Z" fill="#c4e8da"/><circle cx="12" cy="8.6" r="4.6" fill="#c4e8da"/><circle cx="10.3" cy="8.4" r="0.75" fill="#5b3a2c" stroke="none"/><circle cx="13.7" cy="8.4" r="0.75" fill="#5b3a2c" stroke="none"/><ellipse cx="9.4" cy="10.3" rx="0.9" ry="0.55" fill="#e7b4a4" stroke="none"/><ellipse cx="14.6" cy="10.3" rx="0.9" ry="0.55" fill="#e7b4a4" stroke="none"/></svg>','role'],
 ['设置','<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.2" stroke="#5b3a2c" stroke-width="3.2" stroke-dasharray="2.7 3.74"/><circle cx="12" cy="12" r="6.6" fill="#c4e8da" stroke="#5b3a2c" stroke-width="1.5"/><circle cx="12" cy="12" r="2.3" fill="#fbf6ea" stroke="#5b3a2c" stroke-width="1.5"/></svg>','set']];
MC.nav=function(cur,o={}){const dots=o.dots||['记忆'];
 const f=document.createElement('div');f.className='navfade';f.setAttribute('aria-hidden','true');
 const n=document.createElement('nav');n.className='pnav';n.setAttribute('aria-label','主导航');
 n.innerHTML='<span class="pill" aria-hidden="true"></span>'+TABS.map(([t,svg,p])=>{const on=t===cur,dot=dots.includes(t);
  return `<button class="tab${on?' on':''}"${on?' aria-current="page"':''} data-page="${p}">${dot?`<span style="position:relative;display:inline-flex">${svg}<span class="dot"></span></span>`:svg}<span>${t}</span></button>`}).join('');
 document.body.append(f,n);
 const pill=n.querySelector('.pill'),place=b=>{pill.style.left=b.offsetLeft+'px';pill.style.width=b.offsetWidth+'px'};
 requestAnimationFrame(()=>{const b=n.querySelector('.tab.on');b&&place(b)});
 n.querySelectorAll('.tab').forEach(b=>b.onclick=()=>{if(b.classList.contains('on'))return;place(b);(o.go||MC.go)(b.dataset.page)});
 return n};
/* 跳页：在外壳里就让外壳换页，单独打开就直接跳 */
MC.go=p=>{try{if(parent!==window&&parent.MCgo){parent.MCgo(p);return}}catch(e){}location.href=BASE+'../'+p+'/index.html'};

/* 选单元素小工具 */
MC.$=q=>document.querySelector(q);MC.$$=q=>[...document.querySelectorAll(q)];
MC.now=()=>{const d=new Date();return String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0')};
})();
