s=open('p/list/milk.html').read()
s=s.replace('<title>聊天 · 灰稿 E + 猫猫滴奶成云</title>','<title>聊天 · 灰稿 E + 猫奶奶融进奶茶</title>')
s=s.replace('.app{background:linear-gradient(180deg,#d9c3a8 0,#c4a483 40%,#ad8a68 100%)}',
'''.app{background:#f3ece2 url(grain.png);background-blend-mode:multiply}
#liq{position:absolute;left:0;right:0;z-index:0;pointer-events:none;background:url(grain.png),linear-gradient(180deg,#cfb08f 0,#c4a483 18%,#ad8a68 100%);background-blend-mode:multiply,normal}
#liq svg{position:absolute;left:0;top:-13px;width:100%;height:14px}
.catw{flex:none;position:relative;width:clamp(130px,40vw,165px);margin-top:6px}
.catw .catf{width:100%;display:block;margin:0}
.catw .sub{position:absolute;left:-6%;right:-6%;height:34%;bottom:-2px;pointer-events:none;background:linear-gradient(180deg,rgba(207,176,143,0) 0,rgba(207,176,143,.0) 18%,rgba(201,170,136,.55) 34%,rgba(196,164,131,.82) 100%);-webkit-mask:radial-gradient(60% 120% at 50% 100%,#000 60%,transparent 100%);mask:radial-gradient(60% 120% at 50% 100%,#000 60%,transparent 100%)}
.catw .ring{position:absolute;left:2%;right:2%;height:14px;bottom:30%;border-radius:50%;background:radial-gradient(closest-side,rgba(255,248,234,.75),rgba(255,248,234,0));pointer-events:none}
.catw .sh{position:absolute;left:10%;right:10%;height:16px;bottom:22%;border-radius:50%;background:radial-gradient(closest-side,rgba(110,78,52,.28),rgba(110,78,52,0));pointer-events:none}
.near{transition:padding-top .9s cubic-bezier(.3,1.3,.5,1)}
.tg2{position:fixed;top:12px;right:max(68px,calc(50% - 138px));z-index:60;font-size:11px;color:#b0124a;background:#fff;border:1px solid #b0124a;border-radius:4px;padding:2px 6px}''')
s=s.replace('<img class="catf" id="catf" src="catfoam.png" alt="">','<div class="catw" id="catw"><div class="sh"></div><img class="catf" id="catf" src="catfoam.png" alt=""><div class="ring"></div><div class="sub"></div></div>')
s=s.replace('<canvas id="trail"></canvas>','')
s=s.replace('<div class="app" id="app">','<div class="app" id="app"><div id="liq"><svg viewBox="0 0 400 14" preserveAspectRatio="none"><path d="M0 10 C40 4 80 13 130 8 S220 3 270 9 S350 12 400 6 V14 H0Z" fill="#cfb08f"/><path d="M0 10 C40 4 80 13 130 8 S220 3 270 9 S350 12 400 6" stroke="rgba(255,248,234,.7)" stroke-width="2" fill="none"/></svg></div>',1)
s=s.replace('<button class="tg"','<button class="tg2" id="lvb">水位 6 轮</button><button class="tg"',1)
s=s.replace('背景临时铺奶茶色只为看清奶云','整屏就是一杯：今天聊得越多液面越高、猫猫浮得越高（右上「水位」切 0/6/20 轮看）。融合：背景铺同款纸纹；猫猫底部泡进奶茶里（液体半透明盖住下沿）、水线一圈奶泡、水下一点影子；没有饮品卡')
js=r'''
// —— 水位 = 今天轮数；液面在猫猫 70% 高处 ——
const LV=[0,6,20];let li=1;
function level(){const r=LV[li];$('#near').style.paddingTop=(16+Math.round((20-Math.min(r,20))*4.2))+'px';$('#lvb').textContent='水位 '+r+' 轮';$('.today small').textContent=`11/11 周三 · ${r} 轮 · 19:45`;setTimeout(place,950);place()}
function place(){const c=$('#catw'),ar=app.getBoundingClientRect(),r=c.getBoundingClientRect(),y=r.top-ar.top+app.scrollTop+r.height*.7;const L=$('#liq');L.style.top=y+'px';L.style.height=(app.scrollHeight-y)+'px'}
$('#lvb').onclick=()=>{li=(li+1)%3;level();let t0=performance.now();(function f(t){place();if(t-t0<1000)requestAnimationFrame(f)})(t0)};
addEventListener('resize',place);
if($('#catf').complete)level();else $('#catf').addEventListener('load',level);
'''
s=s.replace('drop.style.opacity=arrive?0:1;','drop.style.opacity=(arrive||atRest)?0:1;')
s=s.replace('</script></body>',js+'</script></body>')
# drop starts at waterline
s=s.replace("o.push([c.left-AR.left+c.width*.42,c.bottom-AR.top+st-4,'c'])","o.push([c.left-AR.left+c.width*.42,c.top-AR.top+st+c.height*.9,'c'])")
open('p/list/blend.html','w').write(s)
