# 声音页样张 vb2（基于 vb1）：茶茶 11:05 嫌封套光秃秃，11:06 选 C 封底图解（试听句变声波，引线编号标音高/语速/音量，学 Blue Note 封底排版）。vb1 原注：茶茶 10:09 嫌光秃秃、唱针看不到、折叠面板和「›」。方向 A 点唱机（10:11「可以呀」）。由 p/snd/index.html 取页头/底栏/字体，内容重写。
import os,re
H=os.path.dirname(os.path.abspath(__file__))+'/../../p/snd/'
s=open(H+'index.html').read()
head=s[:s.index('/* 唱片区 */')]
nav=s[s.index('<div class="navfade"'):s.index('</nav>')+6]
hdr=s[s.index('<header class="lhead">'):s.index('</header>')+9]
tail=s[s.index('<script>window.__DEMO_MAP'):]
css=r'''
@font-face{font-family:WK2;src:url(wk2.ttf)}
.page{z-index:12}
/* ===== L2 远景线稿（固定不随滚动） ===== */
.scn{position:absolute;inset:0;z-index:3;pointer-events:none}
.scn .l2{position:absolute;opacity:.2}
/* ===== L3 场景层：唱片店后墙（半透明、竖木板、顶上可可收边） ===== */
.scn .wall{position:absolute;left:0;right:0;top:46%;bottom:0;background:repeating-linear-gradient(90deg,transparent 0 47px,rgba(138,92,70,.13) 47px 48.2px),linear-gradient(rgba(251,246,234,.32),rgba(251,246,234,.16));border-top:1.3px solid rgba(138,92,70,.55);-webkit-mask:linear-gradient(#000 55%,transparent);mask:linear-gradient(#000 55%,transparent)}
.scn .wall::before{content:"";position:absolute;left:0;right:0;top:0;height:9px;background:rgba(201,160,126,.35);border-bottom:1.2px solid rgba(138,92,70,.4)}
.scn .l5{position:absolute}
.scn .fg{position:absolute;opacity:.9}
/* ===== L4 主角：整台唱机 ===== */
.hero{position:relative;margin:118px auto 0;width:min(86vw,340px)}
.player{position:relative;width:100%;aspect-ratio:700/588}
.player>img{position:absolute;inset:0;width:100%}
.plat{position:absolute;left:calc(100%*(316 - 205)/700);top:calc(100%*(170 - 205)/588);width:calc(100%*410/700);aspect-ratio:1;transform:scaleY(.687)}
#disc{position:absolute;inset:0;border-radius:50%;will-change:transform}
#disc img{width:100%}
#disc .tint{position:absolute;left:34%;top:34%;width:32%;height:32%;border-radius:50%;mix-blend-mode:multiply;opacity:.85}
#disc .lab{position:absolute;left:34%;top:34%;width:32%;height:32%;display:grid;place-content:center;text-align:center;font:15px/1.1 ZK;color:#4a3027}
#disc .lab small{display:block;font:8px/1.4 Baloo;letter-spacing:.2em;color:#8a5c46}
#arm{position:absolute;left:calc(100%*560/700);top:calc(100%*-6/588);width:calc(100%*96/700);overflow:visible;transform-origin:68.9% 10%;transform:rotate(26deg);transition:transform .9s cubic-bezier(.3,1.2,.4,1);pointer-events:none}
.app.playing #arm{transform:rotate(4deg)}
#rec{position:absolute;left:10%;top:0;width:70%;height:62%;border-radius:50%}
/* 唱片封套（当前音色，字写在封套上） */
.slv{position:relative;margin:-26px 0 0 14px;width:min(80vw,306px);padding:14px 16px 16px 24px;rotate:-2deg;background:radial-gradient(rgba(138,92,70,.1) .7px,transparent 1.1px) 0 0/6px 6px,linear-gradient(170deg,#fdf8ee,#f6ecda);border-radius:3px 4px 4px 3px;box-shadow:0 0 0 1.2px rgba(138,92,70,.55),0 3px 0 rgba(91,58,44,.14)}
/* 书脊色带：跟当前音色的唱片标签同色 */
.slv::before{content:"";position:absolute;left:0;top:0;bottom:0;width:10px;background:var(--vc,#cfe9dc);border-right:1.2px solid rgba(138,92,70,.45);border-radius:3px 0 0 3px}
.slv::after{content:"";position:absolute;left:3px;top:10px;bottom:10px;width:3px;background:repeating-linear-gradient(rgba(138,92,70,.35) 0 6px,transparent 6px 11px)}
/* 封底编号（Blue Note 式目录号） */
.slv .cat{position:absolute;right:14px;top:13px;display:flex;align-items:center;gap:6px;font:700 10px/1 Baloo;letter-spacing:.14em;color:#8a5c46}
.slv .cat i{display:grid;place-items:center;width:30px;height:30px;border-radius:50%;border:1.2px solid #8a5c46;font:700 8px/1 Baloo;letter-spacing:0;text-align:center;background:repeating-radial-gradient(circle,transparent 0 2.4px,rgba(138,92,70,.16) 2.4px 3px),#fbf6ea}
.slv .cat i b{display:block;font:800 10px/1 BalooX;color:#4a3027}
/* 声波图解：试听句一字两根条，数据即装饰 */
.wv{position:relative;height:94px;margin:12px 0 2px}
.wv .co{position:absolute;top:0;transform:translateX(-50%);display:flex;align-items:center;gap:3px;white-space:nowrap;font:11px/1 WK2;color:#5b3a2c}
.wv .co.r{transform:translateX(calc(-100% + 8px))}.wv .co.l{transform:translateX(-8px)}
.wv .co u{text-decoration:none;display:grid;place-items:center;width:16px;height:16px;border-radius:50%;background:linear-gradient(165deg,#704534,#4b2d21);color:#fbf6ea;font:800 10px/1 BalooX;box-shadow:0 1.5px 0 #33201a}
.wv .co em{font:700 11px/1 Baloo;font-style:normal;color:#3a8f74}
.wv .ln{position:absolute;top:19px;width:0;border-left:1.2px dotted #8a5c46;pointer-events:none}
.wv .ln::after{content:"";position:absolute;left:-3.6px;bottom:-3px;width:6px;height:6px;border-radius:50%;background:#fbf6ea;border:1.2px solid #8a5c46}
.wv .bars{position:absolute;left:0;right:0;top:28px;height:46px;display:flex;align-items:center;gap:2px}
.wv .bars::before{content:"";position:absolute;left:-4px;right:-4px;top:50%;border-top:1.2px dashed rgba(138,92,70,.35)}
.wv .bars i{position:relative;flex:1;min-width:2px;border-radius:2px;background:#9fd3bf;box-shadow:inset 0 0 0 1px rgba(47,110,88,.25);transition:background .2s}
.wv .bars i.p{background:#e6d5bd;box-shadow:none}
.wv .bars i.on{background:#5b3a2c;box-shadow:none}
.wv .rl{position:absolute;left:0;right:0;bottom:0;height:14px;background:repeating-linear-gradient(90deg,rgba(138,92,70,.55) 0 1.2px,transparent 1.2px 10%) 0 0/100% 5px no-repeat,repeating-linear-gradient(90deg,rgba(138,92,70,.3) 0 1px,transparent 1px 2.5%) 0 0/100% 3px no-repeat;border-top:1.2px solid rgba(138,92,70,.55)}
.wv .rl span{position:absolute;bottom:0;font:700 9px/1 Baloo;color:#8a5c46;letter-spacing:.06em}
.slv .k{font:12px/1 WK2;letter-spacing:.2em}
.slv h2{font:34px/1.15 ZK;color:var(--ch);margin:8px 0 2px;letter-spacing:.04em}
.slv .ch{font:13px/1.4 WK2;color:#3a8f74}
.say{margin:12px 0 0;font:16px/1.75 WK2;color:rgba(74,48,39,.55);outline:0;border-bottom:1.2px dashed rgba(138,92,70,.45);padding-bottom:4px;position:relative;z-index:1}
.say b{font-weight:400;transition:color .2s}.say b.on{color:var(--ink)}
.play{display:flex;align-items:center;gap:10px;margin-top:12px;font:15px/1 WK2;color:var(--ch)}
.play i{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 40% 35%,#704534,#4b2d21);box-shadow:0 2.5px 0 #33201a}
.play i svg{fill:#fbf6ea}
.slv .stk{position:absolute;pointer-events:none}
/* ===== 选曲盒（Seeburg 墙挂点唱机：音色＝选曲条） ===== */
.sec{position:relative;margin:34px 18px 0}
.sh{display:flex;align-items:flex-end;gap:10px;margin:0 0 12px 4px}
.sh b{font:14px/1 WK2;color:#f6e8d4;background:linear-gradient(165deg,#704534,#4b2d21);padding:7px 12px 6px;border-radius:5px;box-shadow:0 2.5px 0 #33201a;rotate:-2deg;position:relative}
.sh b::before{content:"";position:absolute;inset:3px;border:1.6px dotted #c9a07e;border-radius:3px}
.sh em{font:20px/1 Script;color:rgba(63,154,128,.7);font-style:normal;rotate:-6deg}
.wb{position:relative;padding:12px 12px 14px;border-radius:14px;background:linear-gradient(165deg,#704534,#4f2f22 60%,#472a1e);box-shadow:0 4px 0 #33201a,0 0 0 1.2px #3a2419}
.wb::before{content:"";position:absolute;inset:5px;border:2px dotted rgba(201,160,126,.7);border-radius:10px;pointer-events:none}
.gl{position:relative;padding:4px 8px;border-radius:8px;background:linear-gradient(#f6ecda,#efe0c6);box-shadow:inset 0 0 0 1.2px rgba(58,36,25,.7),inset 0 3px 0 rgba(91,58,44,.12)}
.sp{position:relative;display:grid;grid-template-columns:44px 1fr auto;align-items:center;width:100%;min-height:52px;margin:6px 0;padding:0 10px 0 6px;background:#fffaf0;border-top:3px solid #9fd3bf;border-bottom:3px solid #c9a07e;border-radius:2px;text-align:left;transition:transform .3s cubic-bezier(.3,1.4,.5,1),background .3s,box-shadow .3s}
.sp .no{position:relative;font:800 16px/1 BalooX;color:#3a8f74;text-align:center}
.sp .no img{position:absolute;left:-10px;top:-12px;width:58px;max-width:none;pointer-events:none;opacity:0}
.sp.def .no img{opacity:1}
.sp .nm{font:20px/1 ZK;color:var(--ch);letter-spacing:.04em;position:relative;justify-self:start;padding:0 2px}
.sp .pv{font:13px/1 WK2;color:#8a6a5a}
.sp .eq{display:inline-flex;gap:2px;align-items:flex-end;height:12px;margin-left:8px;vertical-align:middle;opacity:0}
.sp .eq u{width:3px;background:#3f9a80;border-radius:1px;height:5px}
.app.playing .sp.cur .eq{opacity:1}.app.playing .sp.cur .eq u{animation:eq .5s ease-in-out infinite alternate}
.sp .eq u:nth-child(2){animation-delay:.15s}.sp .eq u:nth-child(3){animation-delay:.3s}
@keyframes eq{to{height:12px}}
.sp.cur{transform:translateY(-3px);background:rgba(255,246,222,.97);box-shadow:0 3px 0 rgba(91,58,44,.18)}
.sp .nm i{font-style:normal}.sp.cur .nm i{background:linear-gradient(transparent 52%,rgba(63,154,128,.3) 52% 92%,transparent 92%)}
.sp.blank{border-top:3px dashed #9fd3bf;border-bottom:3px dashed #c9a07e;background:rgba(255,250,240,.6)}
.sp.blank .nm{font:15px/1 WK2;color:#a08474}
/* 选曲盒下的一排按键（三级圆形小甜点） */
.keys{display:flex;justify-content:center;gap:22px;margin-top:12px;position:relative}
.ky{display:flex;flex-direction:column;align-items:center;gap:5px;font:12px/1 WK2;color:#e9d3b8}
.ky i{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 40% 35%,#fbf6ea,#e9dcc4);box-shadow:0 0 0 1.2px #3a2419,0 3px 0 #2f1b13}
.ky.mint i{background:radial-gradient(circle at 40% 35%,#dff3ea,#a8d8c4)}
.ky:active i{transform:translateY(2px);box-shadow:0 0 0 1.2px #3a2419,0 1px 0 #2f1b13}
.ky[aria-disabled=true]{opacity:.4}
.ky svg{stroke:#5b3a2c;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
/* 空白条就地变表单（写在条上） */
.ed{display:none;margin:6px 0;padding:12px 12px 14px;background:#fffaf0;border-top:3px solid #9fd3bf;border-bottom:3px solid #c9a07e;border-radius:2px}
.gl.editing .ed{display:block}.gl.editing .sp.blank{display:none}
.fl{display:grid;grid-template-columns:62px 1fr;align-items:center;gap:8px;margin:4px 0}
.fl label{font:13px/1 WK2;color:var(--cocoa);letter-spacing:.08em}
.fl input{width:100%;font:15px/1.6 WK2;color:var(--ink);background:none;border:0;border-bottom:1.2px dashed rgba(138,92,70,.5);outline:0;padding:4px 2px}
.fl input::placeholder{color:rgba(138,92,70,.45)}
.opts{display:flex;flex-wrap:wrap;gap:4px 14px}
.op{position:relative;font:15px/1.7 WK2;color:rgba(74,48,39,.55);padding:0 2px}
.op.on{color:var(--ch);background:linear-gradient(transparent 52%,rgba(63,154,128,.3) 52% 92%,transparent 92%)}
.acts{display:flex;align-items:center;justify-content:flex-end;gap:18px;margin-top:12px}
.btn1{font:15px/1 WK2;color:#f6e8d4;background:linear-gradient(165deg,#704534,#4b2d21);padding:11px 18px 10px;border-radius:6px;box-shadow:0 3px 0 #33201a;position:relative}
.btn1::before{content:"";position:absolute;inset:3px;border:1.6px dotted #c9a07e;border-radius:4px}
.btn2{font:15px/1 WK2;color:#2f6e58;background:#c9ebdc;padding:10px 16px 9px;border-radius:6px;box-shadow:0 2.5px 0 #8fc7b1}
.btn4{font:14px/1 WK2;color:#8a6a5a}
.shake{animation:shk .4s}@keyframes shk{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
/* ===== 投币口（渠道＝薄荷糖币） ===== */
.coins{display:flex;flex-wrap:wrap;gap:16px 14px;padding:4px 2px 0}
.cn{position:relative;width:92px;display:flex;flex-direction:column;align-items:center;transition:transform .3s cubic-bezier(.3,1.4,.5,1)}
.cn>img{width:66px;rotate:var(--r,0deg)}
.cn .tg{margin-top:-6px;width:92px;padding:7px 6px 6px;text-align:center;background:#fdf8ee;border-radius:3px;box-shadow:0 0 0 1.2px rgba(138,92,70,.5),0 2px 0 rgba(91,58,44,.12);rotate:var(--t,1deg)}
.cn .tg b{display:block;font:16px/1.1 ZK;color:var(--ch)}
.cn .tg small{display:block;font:11.5px/1.5 WK2;color:#8a6a5a;white-space:nowrap}
.cn.on{transform:translateY(-4px)}.cn.on .tg{background:rgba(255,246,222,.98)}
.cn.slot>i{width:66px;height:66px;border-radius:50%;border:1.6px dashed rgba(138,92,70,.6);display:grid;place-items:center;background:rgba(251,246,234,.5)}
.cn.slot>i::before{content:"";width:30px;height:6px;border-radius:3px;background:#5b3a2c;box-shadow:0 0 0 2px rgba(201,160,126,.5)}
.cn.slot .tg{background:rgba(253,248,238,.6);box-shadow:0 0 0 1.2px rgba(138,92,70,.35)}
.cn.slot .tg b{font:14px/1.2 WK2;color:#8a6a5a}
.slip{display:none;margin-top:14px;padding:12px 14px 14px;background:#fdf8ee;border-radius:3px;box-shadow:0 0 0 1.2px rgba(138,92,70,.5),0 3px 0 rgba(91,58,44,.12);rotate:-.6deg}
.slip.open{display:block}
.cnx{display:none;margin-top:12px;font:13px/1.6 WK2;color:#8a6a5a}
.cnx.open{display:flex;align-items:center;justify-content:space-between}
.cnx .btn4{color:#a0533c}
.endbit{display:block;width:30px;margin:28px 0 0 auto;rotate:12deg}
'''
body=r'''<body>
<div class="vp"><div class="app" id="app">
<img class="drizzle" src="today-bg.png" alt="">
<div class="scn" aria-hidden="true">
 <img class="l2" src="f-shop.svg" style="left:-70px;bottom:70px;width:380px" alt="">
 <img class="l2" src="../set/f-sprig.svg" style="right:-80px;top:96px;width:220px;rotate:-130deg;opacity:.14" alt="">
 <div class="wall"></div>
 <img class="l5" src="../set/s-jars.png" style="right:-24px;top:calc(46% - 60px);width:150px" alt="">
 <img class="fg" src="../hlt/fg-pearl.png" style="left:-26px;bottom:110px;width:70px" alt="">
 <img class="fg" src="../hlt/fg-curl.png" style="right:-30px;bottom:200px;width:80px;rotate:-20deg" alt="">
</div>
HDR
<main class="page" id="page">
<section class="hero" id="hero">
 <div class="player"><img src="snd-player.png" alt="">
  <div class="plat"><div id="disc"><img src="vinyl.png" alt=""><i class="tint" id="tint"></i><div class="lab" id="lab"></div></div></div>
  <button id="rec" aria-label="试听这张"></button>
  <svg id="arm" viewBox="0 0 90 220" aria-hidden="true" fill="none" stroke="#8a5c46" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="62" cy="22" r="15" fill="#fbf6ea"/><circle cx="62" cy="22" r="5" fill="#cfe9dc"/><path d="M62 37 C62 90 58 140 40 186" stroke="#5b3a2c" stroke-width="5"/><path d="M62 37 C62 90 58 140 40 186" stroke="#fbf6ea" stroke-width="2.2"/><rect x="26" y="182" width="22" height="30" rx="3" transform="rotate(24 37 197)" fill="#fbf6ea"/><path d="M33 212 l-3 7" stroke="#5b3a2c" stroke-width="1.6"/></svg>
 </div>
 <div class="slv">
  <img class="stk" src="st-note.png" style="left:-22px;top:-26px;width:46px;rotate:-14deg" alt="">
  <img class="stk" src="st-puff.png" style="right:-16px;bottom:-22px;width:48px;rotate:10deg" alt="">
  <div class="cat"><span id="catno">MC-A1</span><i><span><b>33</b>RPM</span></i></div>
  <div class="k"><i></i><span id="st">默认</span></div><h2 id="vn"></h2><div class="ch" id="vc"></div>
  <div class="wv" id="wv" aria-hidden="true"></div>
  <div class="say" id="say" contenteditable="true" spellcheck="false" role="textbox" aria-label="试听的话"></div>
  <button class="play" id="play"><i><svg width="12" height="12" viewBox="0 0 12 12"><path id="pi" d="M3 1.5v9l7.5-4.5z"/></svg></i><span id="pt">听一下</span></button>
 </div>
</section>
<section class="sec">
 <div class="sh"><b>选曲</b><em>side A</em></div>
 <div class="wb"><div class="gl" id="gl"><div id="tracks"></div>
  <button class="sp blank" id="newv"><span class="no" id="nno">A4</span><span class="nm">空白条 · 写一首新音色</span><span></span></button>
  <div class="ed" id="vform">
   <div class="fl"><label for="f1">名字</label><input id="f1" placeholder="比如：晚安版"></div>
   <div class="fl"><label>渠道</label><div class="opts" id="f2"></div></div>
   <div class="fl"><label for="f3">音色 ID</label><input id="f3" placeholder="服务商那边的编号"></div>
   <div class="fl"><label for="f4">模型</label><input id="f4" placeholder="可以不填"></div>
   <div class="acts"><button class="btn4" id="vno">算了</button><button class="btn1" id="vgo">建好</button></div>
  </div></div>
  <div class="keys">
   <button class="ky mint" id="kplay"><i><svg width="18" height="18" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#5b3a2c"/></svg></i>听</button>
   <button class="ky" id="kdef"><i><svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.8l-5.2 2.8 1-5.8-4.3-4.1 5.9-.8z"/></svg></i>设默认</button>
   <button class="ky" id="kdel"><i><svg width="18" height="18" viewBox="0 0 24 24"><path d="M5 7h14M10 7V4.5h4V7M7 7l1 13h8l1-13"/></svg></i>删掉</button>
  </div>
 </div>
</section>
<section class="sec">
 <div class="sh"><b>投币口</b><em>coins</em></div>
 <div class="coins" id="chs"></div>
 <div class="cnx" id="cnx"><span id="cnxt"></span><button class="btn4" id="cdel">删掉这枚</button></div>
 <div class="slip" id="cform">
  <div class="fl"><label for="g1">名字</label><input id="g1" placeholder="自己认得就行"></div>
  <div class="fl"><label>服务商</label><div class="opts" id="g2"></div></div>
  <div class="fl"><label for="g3">地址</label><input id="g3" placeholder="https://"></div>
  <div class="fl"><label for="g4">密钥</label><input id="g4" type="password" autocomplete="off" placeholder="存好后只显示末四位"></div>
  <div class="acts"><button class="btn4" id="cno">算了</button><button class="btn2" id="cgo">投进去</button></div>
 </div>
</section>
<img class="endbit" src="st-truf.png" alt="">
</main>
NAV
</div></div>
<script src="../ui.js?v=65"></script>
<script>
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
let CH=[{id:'c1',n:'海螺',t:'MiniMax',k:'a3f2'},{id:'c2',n:'小鱼',t:'Fish Audio',k:'9c01'}];
let V=[{id:'v1',n:'晚风',c:'c1',m:'speech-02-hd',vid:'male-qn-jingying',def:1,col:'#cfe9dc',pitch:.75,rate:.95,vol:1},
 {id:'v2',n:'薄荷',c:'c1',m:'speech-02-turbo',vid:'male-qn-qingse',col:'#f3dcc0',pitch:1.15,rate:1.1,vol:1},
 {id:'v3',n:'奶油',c:'c2',m:'',vid:'7f2a-whisper',col:'#e3d3e6',pitch:.9,rate:.8,vol:.55}];
const COLS=['#cfe9dc','#f3dcc0','#e3d3e6','#d8e6c4','#f0cfc8'],TY=['MiniMax','ElevenLabs','Fish Audio'];
let cur=V[0].id,selC=null,fc=CH[0]&&CH[0].id,ft=TY[0];
const chn=id=>CH.find(c=>c.id===id)||{n:'?',t:''};
function setSay(t){$('#say').innerHTML=[...t].map(c=>'<b>'+c+'</b>').join('');wave()}
/* 声波：每个字两根条，高度由字和音量定；标点是停顿；引线标出音高（最高处）、语速（中段）、音量（尾段） */
function wave(){const v=V.find(x=>x.id===cur);if(!v)return;const t=[...$('#say').textContent].slice(0,40),P='，。？！、…,.?! ';
 const hs=[];t.forEach((c,i)=>{const p=P.includes(c),k=c.codePointAt(0);for(let j=0;j<2;j++){const r=((k*(j?131:197)+i*53)%97)/97;hs.push(p?{h:.1,p:1}:{h:(.3+.7*r)*(.3+.7*v.vol)*(j?.82:1),p:0})}});
 const n=hs.length,x=i=>(i+.5)/n*100,sec=(t.length*.15/(v.rate||1)).toFixed(1);
 const C=[[Math.floor(n*.08),'1','音高',v.pitch.toFixed(2),' l'],[Math.floor(n*.5),'2','语速',v.rate.toFixed(2)+'×',''],[Math.min(n-1,Math.floor(n*.92)),'3','音量',Math.round(v.vol*100)+'%',' r']];
 $('#wv').innerHTML=C.map(([i,no,k,val,cl])=>`<span class="co${cl}" style="left:${x(i)}%"><u>${no}</u>${k}<em>${val}</em></span><i class="ln" style="left:${x(i)}%;height:${10+23*(1-hs[i].h)}px"></i>`).join('')
  +`<div class="bars">${hs.map((b,i)=>`<i class="${b.p?'p':''}" data-c="${i>>1}" style="height:${Math.round(b.h*100)}%"></i>`).join('')}</div><div class="rl"><span style="left:0">0s</span><span style="right:0">${sec}s</span></div>`}
setSay('你好，我是叶铎。今天想听我说什么？');
function show(v,anim){
 const put=()=>{$('#vn').textContent=v.n;$('#vc').textContent=chn(v.c).t+' '+chn(v.c).n+(v.m?' · '+v.m:'');$('#st').textContent=v.def?'默认':'试听中';$('.slv').style.setProperty('--vc',v.col);$('#catno').textContent='MC-A'+(V.indexOf(v)+1);wave();$('#lab').innerHTML=v.n+'<small>SIDE A</small>';$('#tint').style.background=v.col};
 if(!anim||RM){put();return}
 const d=$('#disc');d.animate([{transform:`rotate(${ang}deg)`,opacity:1},{transform:`translateY(-30px) rotate(${ang+140}deg)`,opacity:0}],{duration:260,easing:'cubic-bezier(.5,0,.8,.5)',fill:'forwards'}).finished.then(()=>{put();d.animate([{transform:`translateY(-30px) rotate(${ang-140}deg)`,opacity:0},{transform:`rotate(${ang}deg)`,opacity:1}],{duration:420,easing:'cubic-bezier(.2,.9,.3,1.08)',fill:'forwards'}).finished.then(a=>a.cancel())})}
function render(){
 const T=$('#tracks');$('#cnt').textContent=V.length;$('#nno').textContent='A'+(V.length+1);
 T.innerHTML=V.map((v,i)=>`<button class="sp${v.def?' def':''}${v.id===cur?' cur':''}" data-id="${v.id}" aria-pressed="${v.id===cur}"><span class="no">A${i+1}<img src="circle.png" alt=""></span><span class="nm"><i>${v.n}</i><span class="eq" aria-hidden="true"><u></u><u></u><u></u></span></span><span class="pv">${chn(v.c).n}</span></button>`).join('');
 $$('#tracks .sp').forEach(b=>b.onclick=()=>{const v=V.find(x=>x.id===b.dataset.id);if(v.id===cur)return;stop();cur=v.id;render();show(v,1)});
 const v=V.find(x=>x.id===cur);$('#kdef').setAttribute('aria-disabled',!v||!!v.def);
 renderCh();opts($('#f2'),CH.length?CH.map(c=>[c.id,c.n]):[['','先投一枚币']],fc,x=>fc=x)}
function opts(el,L,c,on){el.innerHTML=L.map(e=>`<button type="button" class="op${e[0]===c?' on':''}" data-v="${e[0]}">${e[1]}</button>`).join('');el.querySelectorAll('.op').forEach(b=>b.onclick=()=>{on(b.dataset.v);el.querySelectorAll('.op').forEach(x=>x.classList.toggle('on',x===b))})}
function renderCh(){
 $('#chs').innerHTML=CH.map((c,i)=>{const n=V.filter(v=>v.c===c.id).length;return `<button class="cn${c.id===selC?' on':''}" data-id="${c.id}" style="--r:${[-12,9,-4,14][i%4]}deg;--t:${[1.5,-1.5,1,-1][i%4]}deg"><img src="st-coin.png" alt=""><span class="tg"><b>${c.n}</b><small>${c.t}</small><small>····${c.k} · ${n} 种</small></span></button>`}).join('')+`<button class="cn slot" id="newc"><i></i><span class="tg"><b>接一条</b><small>投一枚新币</small></span></button>`;
 $$('#chs .cn[data-id]').forEach(b=>b.onclick=()=>{selC=selC===b.dataset.id?null:b.dataset.id;$('#cform').classList.remove('open');renderCh()});
 $('#newc').onclick=()=>{selC=null;renderCh();$('#cform').classList.toggle('open');opts($('#g2'),TY.map(t=>[t,t]),ft,x=>ft=x)};
 const c=CH.find(x=>x.id===selC);$('#cnx').classList.toggle('open',!!c);if(c){const n=V.filter(v=>v.c===c.id).length;$('#cnxt').textContent=`${c.n} · ${c.t} · 管着 ${n} 种音色`}}
$('#kplay').onclick=()=>play();
$('#kdef').onclick=()=>{const v=V.find(x=>x.id===cur);if(!v||v.def)return;V.forEach(x=>x.def=0);v.def=1;render();show(v);window.MC&&MC.toast(`「${v.n}」设成默认了`)};
$('#kdel').onclick=async()=>{const v=V.find(x=>x.id===cur);if(!v)return;
 if(window.MC&&!await MC.confirm({title:`删掉「${v.n}」？`,body:`${v.def?'这是默认音色，<b>删了以后 Telegram 语音回复会退回文字</b>。':''}删掉不能恢复，要用得重新建。`,ok:'删掉'}))return;
 stop();V=V.filter(x=>x!==v);if(v.def&&V[0])V[0].def=1;if(V[0]){cur=V[0].id;show(V[0],1)}render();window.MC&&MC.toast(`「${v.n}」删掉了`)};
$('#cdel').onclick=async()=>{const c=CH.find(x=>x.id===selC);if(!c)return;const n=V.filter(v=>v.c===c.id),hasDef=n.some(v=>v.def);
 if(window.MC&&!await MC.confirm({title:`删掉「${c.n}」这枚币？`,body:`地址和密钥一起删掉${n.length?'，用它的 '+n.length+' 种音色也会跟着删'+(hasDef?'（<b>含默认，Telegram 语音回复会退回文字</b>）':''):''}。不能恢复。`,ok:'删掉'}))return;
 CH=CH.filter(x=>x!==c);V=V.filter(v=>v.c!==c.id);selC=null;if(!V.find(v=>v.id===cur)&&V[0]){cur=V[0].id;show(V[0],1)}if(fc===c.id)fc=CH[0]&&CH[0].id;render()};
/* 唱片：待机慢转，播放时转快，唱臂落下 */
let ang=0,spd=0,tgt=RM?0:4,playing=false,timer=null,last=performance.now(),raf=0;
function loop(now){const dt=Math.min(50,now-last);last=now;spd+=(tgt-spd)*.05;ang=(ang+spd*dt/1000*6)%360;
 const d=$('#disc');if(!d.getAnimations().length)d.style.transform=`rotate(${ang}deg)`;raf=document.hidden?0:requestAnimationFrame(loop)}
raf=requestAnimationFrame(loop);document.addEventListener('visibilitychange',()=>{if(!document.hidden&&!raf){last=performance.now();raf=requestAnimationFrame(loop)}});
function play(){if(playing){stop();return}const v=V.find(x=>x.id===cur);if(!v)return;playing=true;tgt=RM?0:33;$('#app').classList.add('playing');$('#pt').textContent='停';$('#pi').setAttribute('d','M2.5 2h2.6v8H2.5zM7 2h2.6v8H7z');
 const bs=$$('#say b');bs.forEach(b=>b.classList.remove('on'));let i=0;
 timer=setInterval(()=>{if(i<bs.length){bs[i].classList.add('on');$$('#wv .bars i[data-c="'+i+'"]').forEach(b=>b.classList.add('on'));i++}else stop()},v.rate?150/v.rate:150);
 try{const u=new SpeechSynthesisUtterance($('#say').textContent);u.lang='zh-CN';u.pitch=v.pitch;u.rate=v.rate;u.volume=v.vol;speechSynthesis.cancel();speechSynthesis.speak(u)}catch(e){}}
function stop(){if(!playing)return;playing=false;tgt=RM?0:4;$('#app').classList.remove('playing');$('#pt').textContent='听一下';$('#pi').setAttribute('d','M3 1.5v9l7.5-4.5z');clearInterval(timer);try{speechSynthesis.cancel()}catch(e){}setTimeout(()=>$$('#say b,#wv .bars i').forEach(b=>b.classList.remove('on')),600)}
$('#rec').onclick=play;$('#play').onclick=play;
$('#say').addEventListener('focus',stop);
$('#say').addEventListener('blur',()=>setSay($('#say').textContent.trim()||'你好，我是叶铎。'));
/* 空白条：点了就地变成表单（写在条上） */
$('#newv').onclick=()=>{$('#gl').classList.add('editing');$('#f1').focus({preventScroll:true})};
$('#vno').onclick=()=>{$('#gl').classList.remove('editing');['#f1','#f3','#f4'].forEach(s=>$(s).value='')};
$('#vgo').onclick=()=>{const n=$('#f1').value.trim(),id=$('#f3').value.trim(),c=CH.find(x=>x.id===fc);
 if(!n||!id||!c){const f=$('#vform');f.classList.remove('shake');void f.offsetWidth;f.classList.add('shake');return}
 const v={id:'v'+Date.now(),n,c:c.id,m:$('#f4').value.trim(),vid:id,col:COLS[V.length%COLS.length],pitch:1,rate:1,vol:1};V.push(v);cur=v.id;
 ['#f1','#f3','#f4'].forEach(s=>$(s).value='');$('#gl').classList.remove('editing');render();show(v,1);window.MC&&MC.toast(`「${n}」写上选曲条了`)};
$('#cno').onclick=()=>$('#cform').classList.remove('open');
$('#cgo').onclick=()=>{const n=$('#g1').value.trim(),u=$('#g3').value.trim(),k=$('#g4').value;
 if(!n||!u||!k){const f=$('#cform');f.classList.remove('shake');void f.offsetWidth;f.classList.add('shake');return}
 CH.push({id:'c'+Date.now(),n,t:ft,k:k.slice(-4)});['#g1','#g3','#g4'].forEach(s=>$(s).value='');$('#cform').classList.remove('open');if(!fc)fc=CH[CH.length-1].id;render();window.MC&&MC.toast(`「${n}」投进去了`)};
render();show(V[0]);
</script>'''
body=body.replace('HDR',hdr).replace('NAV',nav)
out=head+css+'</style></head>'+body+tail
out=out.replace('src:url(wk.ttf)','src:url(wk2.ttf)')
out=out.replace('<title>声音','<title>vb2 · 声音',1)
open(H+'vb2.html','w').write(out)
# 文楷子集：本页所有中文 + 常用
txt=''.join(sorted(set(c for c in out if ord(c)>0x2000)))+'，。：·？！「」（）、—…＋'
open('/tmp/snd_chars.txt','w').write(txt)
print('ok',len(txt))
