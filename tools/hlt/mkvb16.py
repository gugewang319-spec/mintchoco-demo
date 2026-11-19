# 健康页「没连手环」空态样张：由 p/hlt/index.html 生成 p/hlt/vb16.html
import re
R='p/hlt/'
s=open(R+'index.html').read()
css='''
/* vb16 空态 */
.tea,.ln.yd,.tag.yd,.lead.yd,#hrb,.tray[aria-label="睡眠"],.tl2 .tl,.tl2 .tax,.tl2 .pick,.tl2 .allb,.big{display:none!important}
.pp u,.pp u.e{background:none!important;border:1.2px dashed rgba(138,92,70,.42)!important;box-shadow:none!important}
.pp u::before,.pp u::after{display:none!important}
.etag{position:absolute;left:24px;top:136px;width:calc(100% - 186px);max-width:190px;padding:16px 16px 14px 26px;border-radius:6px 16px 16px 6px;background:rgba(251,244,230,.86);border:1.2px solid #8a5c46;box-shadow:inset 0 0 0 4px rgba(233,214,194,.6),0 3px 0 rgba(91,58,44,.16);rotate:-2deg;transform-origin:0 50%;animation:etg 5.6s ease-in-out infinite}
.etag::before{content:"";position:absolute;left:9px;top:50%;width:8px;height:8px;margin-top:-4px;border-radius:50%;background:rgba(196,232,218,.9);border:1.2px solid #8a5c46}
.etag b{display:block;font:24px/1.2 ZK;color:var(--ch)}
.etag span{display:block;margin-top:8px;font:14px/1.55 WK;color:var(--ink)}
@keyframes etg{50%{rotate:-.6deg}}
.ego{position:absolute;left:24px;top:250px;z-index:3;display:inline-flex;align-items:center;gap:6px;height:40px;padding:0 18px;border-radius:12px;border:1.2px solid #8a5c46;background:linear-gradient(180deg,#d4efe3,#b5e0cf);box-shadow:inset 0 1.5px 0 rgba(255,255,255,.7),0 3px 0 rgba(91,58,44,.2);font:15px/1 ZK;color:var(--ch);cursor:pointer;transition:transform .12s,box-shadow .12s}
.ego:active{transform:translateY(2px);box-shadow:inset 0 1.5px 0 rgba(255,255,255,.7),0 1px 0 rgba(91,58,44,.2)}
.ego svg{width:14px;height:14px}
.ehint{position:relative;padding:4px 0 2px;font:14px/1.6 WK;color:var(--ink)}
.ehint b{display:block;font:16px/1.3 ZK;color:var(--ch);margin-bottom:4px}
.ok.no i{background:#d9705f!important}.wbk .bd{background:#d9705f!important}\n@media (prefers-reduced-motion:reduce){.etag{animation:none}}
'''
s=s.replace('</style>',css+'</style>',1)
# 页顶翻牌钟：没同步过
s=re.sub(r'<div class="counter" aria-label="最近同步 10:52">.*?</div>','<div class="counter" aria-label="手环没连上"><span>-</span><span>-</span><b>:</b><span>-</span><span>-</span></div>',s,1,re.S)
# 主角区：纸签 + 薄荷排块
s=s.replace('<div class="big">','<div class="etag"><b>杯子还空着</b><span>接上手环，<br>就开始装珍珠</span></div><button type="button" class="ego" onclick="document.getElementById(\'wbk\').click()">接上手环<svg viewBox="0 0 14 14" fill="none" stroke="#5b3a2c" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m5 3 4 4-4 4"/></svg></button><div class="big">',1)
s=s.replace('aria-label="一颗珍珠一千步，目标八千，昨天五千五"','aria-label="杯子还空着，目标八千步"')
# 最后一只托盘收成一句提示
s=s.replace('<div class="tl">','<div class="ehint"><b>今天还没有记录</b>心率、睡眠和每一笔步数，接上手环以后都会落在这里。</div><div class="tl">',1)
s=s.replace('<section><small>最近收到</small><b class="tt">10:52</b><span class="ok"><i></i>连着 · v1.4.2</span></section>','<section><small>还没收到过</small><b class="tt">--:--</b><span class="ok no"><i></i>往左滑，填地址</span></section>',1)
s=s.replace('onclick="document.getElementById(\'wbk\').click()"','onclick="document.getElementById(\'wbk\').click();setTimeout(()=>{const c=document.getElementById(\'scr\');c.scrollTo({left:c.clientWidth,behavior:\'smooth\'})},700)"',1)
open(R+'vb16.html','w').write(s)
print('ok')

# 05:47 茶茶：装进杯里的珍珠要和聊天/今天页代码画的珍珠一样有体积，不能纯平 → vb16b = 连上手环状态
t=open(R+'index.html').read()
t=t.replace('</style>','.pp u:not(.e){background:radial-gradient(circle at 35% 30%,#b88566 0 9%,#8a5a40 20%,#4b2c1f 58%,#33201a 100%)!important;box-shadow:0 0 0 .8px rgba(60,35,25,.55),inset -2px -3px 4px rgba(30,18,12,.35)!important}\n</style>',1)
open(R+'vb16b.html','w').write(t)
print('ok b')

# 06:00 茶茶：手势要像手机「侧滑返回」——从屏幕左/右边往里划放回手表；系统返回手势/返回键也只放回手表（pushState），不离开页面。05:51 的下拖放回作废。
SW=r"""<i class="wedge l" aria-hidden="true"></i><i class="wedge r" aria-hidden="true"></i><i class="wba" id="wba" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#5b3a2c" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m14 6-6 6 6 6"/></svg></i>
<style>.wedge{position:fixed;top:0;bottom:0;width:26px;z-index:70;touch-action:none;display:none}.wedge.l{left:0}.wedge.r{right:0}.wup.on~.wedge{display:block}
.wba{position:fixed;left:0;top:50%;z-index:71;width:40px;height:40px;margin:-20px 0 0 -44px;border-radius:50%;display:grid;place-items:center;background:rgba(252,250,244,.9);box-shadow:inset 0 1px 0 #fff,0 6px 14px -8px rgba(74,48,39,.5);opacity:0;pointer-events:none;transform:translateX(calc(var(--p,0)*58px)) scale(calc(.6 + var(--p,0)*.4))}
.wba.r{left:auto;right:0;margin:-20px -44px 0 0;transform:translateX(calc(var(--p,0)*-58px)) scale(calc(.6 + var(--p,0)*.4))}.wba.r svg{rotate:180deg}.wba.on{opacity:calc(var(--p,0)*1.6)}.wba.go{background:#c4e8da}</style>
<script>
(()=>{const $=q=>document.getElementById(q),up=$('wup'),big=$('wbig'),put=$('wput'),arr=$('wba');let pushed=false;
new MutationObserver(()=>{const on=up.classList.contains('on');if(on&&!pushed){history.pushState({w:1},'');pushed=true}else if(!on&&pushed){pushed=false;history.back()}}).observe(up,{attributes:true,attributeFilter:['class']});
addEventListener('popstate',()=>{if(pushed){pushed=false;if(up.classList.contains('on'))put.click()}});
let sx=0,dir=0,id=null,p=0;
document.querySelectorAll('.wedge').forEach(w=>w.addEventListener('pointerdown',e=>{if(!up.classList.contains('on'))return;dir=w.classList.contains('l')?1:-1;sx=e.clientX;id=e.pointerId;p=0;try{w.setPointerCapture(id)}catch(_){}
 arr.style.top=e.clientY+'px';arr.classList.toggle('r',dir<0);arr.classList.add('on');arr.style.setProperty('--p',0)}));
addEventListener('pointermove',e=>{if(e.pointerId!==id)return;p=Math.max(0,Math.min(1,(e.clientX-sx)*dir/140));arr.style.setProperty('--p',p.toFixed(3));arr.classList.toggle('go',p>=.55);
 big.style.scale=(1-.1*p).toFixed(3);big.style.translate=`${(dir*p*26).toFixed(1)}px 0`});
function end(e){if(e.pointerId!==id)return;id=null;arr.classList.remove('on','go');arr.style.setProperty('--p',0);const sc=big.style.scale||'1',tr=big.style.translate||'0 0';big.style.scale='';big.style.translate='';
 if(p>=.55){if(pushed)history.back();else put.click()}else big.animate({scale:[sc,'1'],translate:[tr,'0 0']},{duration:260,easing:'cubic-bezier(.3,1.3,.5,1)'});p=0}
addEventListener('pointerup',end);addEventListener('pointercancel',end);
})();</script>"""
for f in ['vb16.html','vb16b.html']:
  t=open(R+f).read();t=t.replace('</body>',SW+'</body>',1);open(R+f,'w').write(t)
print('ok swipe')

# 06:00 茶茶：手表用生图的彩铅水彩技法重画 SVG（tools/hlt/watch.svg / watch_s.svg，滤镜：抖线、铅笔颗粒描边、水彩边缘积色+纸纹、阴影侧彩铅排线、光从左上），用 r.py/rs.py 烘成 webp（动画元素不挂实时滤镜）
import re as _re
for f in ['vb16.html','vb16b.html']:
  t=open(R+f).read()
  t=_re.sub(r'<svg class="wsv".*?</svg>','<img class="wsv" src="watch.webp" alt="" style="left:-6px;top:-6px;width:272px;height:536px;inset:auto">',t,1,flags=_re.S)
  t=_re.sub(r'(<button type="button" class="wbk"[^>]*>)<svg viewBox="0 0 72 96".*?</svg>',r'\1<img src="watch_s.webp" alt="" style="display:block;height:89px;width:auto;margin:-3px auto 0">',t,1,flags=_re.S)
  open(R+f,'w').write(t)
print('ok watch')

# 06:00 茶茶：「1 颗 = 1000 步」不直观 → 改成地图比例尺：黑白分段尺，每格 = 杯里一颗珍珠宽（24px），格上坐珍珠，刻度 0/1k/2k/3k 步
SC='<div class="mscl" aria-label="比例尺：一颗珍珠等于一千步"><div class="mscp"><u></u><u></u><u></u></div><div class="mscb"><i></i><i></i><i></i></div><div class="mscn"><span>0</span><span>1k</span><span>2k</span><span>3k<em>步</em></span></div></div>'
SCC='''<style>.key{display:none!important}.mscl{position:absolute;left:24px;top:140px;width:72px;z-index:2}.mscp{display:flex}.mscp u{width:24px;height:24px;margin-bottom:2px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#b88566 0 9%,#8a5a40 20%,#4b2c1f 58%,#33201a 100%);box-shadow:0 0 0 .8px rgba(60,35,25,.55),inset -2px -3px 4px rgba(30,18,12,.35)}
.mscb{display:flex;height:7px;border:1.2px solid #8a5c46;border-radius:1.5px;background:#fbf6ea}.mscb i{flex:1}.mscb i:nth-child(odd){background:#8a5c46}
.mscn{position:relative;height:16px;margin-top:3px;font:800 11px/1 BalooX;color:var(--cocoa)}.mscn span{position:absolute;top:0;translate:-50% 0;white-space:nowrap}.mscn span:nth-child(1){left:0}.mscn span:nth-child(2){left:33.33%}.mscn span:nth-child(3){left:66.67%}.mscn span:nth-child(4){left:100%;translate:-28% 0}.mscn em{font:12px/1 ZK;font-style:normal;margin-left:3px}</style>'''
for f in ['vb16.html','vb16b.html']:
  t=open(R+f).read();t=t.replace('<section class="hero2">','<section class="hero2">'+SC,1).replace('</body>',SCC+'</body>',1);open(R+f,'w').write(t)
print('ok scale')

# 05:54 茶茶：加个神经的提示语「粒粒皆千步」→ 杯身奶白小纸签
LL='<span class="ll">粒粒皆千步</span>'
LC='<style>.ll{position:absolute;left:50%;top:30px;z-index:2;translate:-50% 0;rotate:-4deg;padding:5px 7px 4px;border-radius:4px 7px 7px 4px;background:rgba(251,244,230,.92);box-shadow:inset 0 0 0 2.5px rgba(233,214,194,.6),0 1.5px 0 rgba(91,58,44,.16);font:12px/1 ZK;color:var(--ch);white-space:nowrap;letter-spacing:.04em}</style>'
for f in ['vb16.html','vb16b.html']:
  t=open(R+f).read();t=t.replace('<div class="glass">','<div class="glass">'+LL,1).replace('</body>',LC+'</body>',1);open(R+f,'w').write(t)
print('ok ll')
# 空态：比例尺挪到手表右边，别压纸签
t=open(R+'vb16.html').read();t=t.replace('</body>','<style>.mscl{left:112px!important;top:30px!important}</style></body>',1);open(R+'vb16.html','w').write(t)
