# sk9 「QQ 主题式列表」灰稿生成
import os
R=os.path.dirname(os.path.abspath(__file__))
week=[("10","周二",12,"要是真下雪，我去楼下给你堆一只小猫","你说明天会不会下雪呀",None),
("9","周一",8,"那今晚什么都不想，陪你发呆","今天的会开了三个小时，脑袋好空","要不要打个电话呀"),
("8","周日",9,"下次还去，换你点单","那家的薄荷冰淇淋超好吃",None),
("7","周六",0,"","",None),
("6","周五",2,"晚安","晚安～",None),
("5","周四",0,"","",None)]
early=[("10/29 – 11/4",5,"万圣节那天他给你讲了一个超吓人的故事"),
("10/22 – 10/28",3,"这周你一直在忙期中"),
("10/15 – 10/21",4,"第一次一起看的那部电影"),
("10/8 – 10/14",2,"你说秋天最适合喝热可可")]
G={ # 小料（灰稿里只是形状）
"leaf":'<svg viewBox="0 0 40 40"><path d="M6 34C4 18 16 6 34 6C36 22 24 34 6 34Z" fill="#fff" stroke="#888" stroke-width="2"/><path d="M8 32L28 12" stroke="#888" stroke-width="1.6" fill="none"/></svg>',
"pearl":'<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="14" fill="#888"/><circle cx="15" cy="15" r="3" fill="#d0d0d0"/></svg>',
"ice":'<svg viewBox="0 0 40 40"><rect x="7" y="7" width="26" height="26" rx="7" fill="#fff" stroke="#888" stroke-width="2"/></svg>',
"roll":'<svg viewBox="0 0 40 40"><rect x="4" y="14" width="32" height="12" rx="6" fill="#d0d0d0" stroke="#888" stroke-width="2"/><path d="M12 14v12M20 14v12M28 14v12" stroke="#888" stroke-width="1.2"/></svg>'}
kinds=["leaf","pearl","roll","ice"]
corners=["tr","bl","br","tl"]
def gar(i,big=False):
    k=kinds[i%4];c=corners[i%4];d=(2.6+((i*7)%5)*0.45);dl=-((i*1.3)%3)
    opp={"tr":"bl","bl":"tr","br":"tl","tl":"br"}[c]
    return (f'<i class="gar {c}{" big" if big else ""}" style="--d:{d:.2f}s;--dl:{dl:.1f}s" data-z="{0.06+0.03*(i%3):.2f}">{G[k]}</i>'
            f'<i class="dot {opp}" style="--d:{d+1.1:.2f}s;--dl:{dl-0.6:.1f}s"></i>')
rows=[]
for i,(d,w,n,his,me,uns) in enumerate(week):
    if n==0:
        rows.append(f'<div class="nil"><span class="num">11/{d}</span> {w} · 没聊</div>');continue
    u=f'<span class="uns" role="button" onclick="event.stopPropagation();this.classList.toggle(\'on\')"><i>写了又擦掉 ·</i>{uns}</span>' if uns else ''
    rows.append(f'''<button class="row tap"><span class="dt"><b class="num">{d}</b><small>11月 {w}</small></span><span class="tx"><span class="his">{his}</span><span class="me">我：{me}</span>{u}</span><span class="ct"><b class="num">{n}</b><small>轮</small></span>{gar(i+1)}</button>''')
erows=[]
for i,(r,n,l) in enumerate(early):
    erows.append(f'''<button class="row wk tap"><span class="tx"><span class="lab">{r}</span><span class="his">{l}</span></span><span class="ct"><b class="num">{n}</b><small>天</small></span>{gar(i+2) if i%2==0 else ""}</button>''')
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>聊天 灰稿 sk9 · QQ 主题式列表</title><style>
@font-face{{font-family:Baloo;src:url(baloo.ttf)}}@font-face{{font-family:ZK;src:url(zk.ttf)}}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}}
:root{{--body:system-ui,-apple-system,"PingFang SC","Noto Sans SC",sans-serif}}
html,body{{height:100%;overflow:hidden;background:#d9d9d9;font-family:var(--body);color:#222}}
button{{font:inherit;color:inherit;background:none;border:0;cursor:pointer;text-align:inherit}}
.num{{font-family:Baloo,var(--body);font-variant-numeric:tabular-nums}}
.app{{position:fixed;inset:0;margin:0 auto;width:min(100%,440px);overflow:hidden;background:#f4f4f4}}
/* 背景层：竖条纹＋底栏后面的珍珠，不进字区 */
.bg{{position:absolute;inset:0;z-index:0;pointer-events:none;background:repeating-linear-gradient(90deg,#f4f4f4 0 22px,#ececec 22px 44px)}}
.bg .pb{{position:absolute;border-radius:50%;background:#888;animation:bob var(--d) ease-in-out infinite;animation-delay:var(--dl)}}
.bg .pb.l{{background:#d0d0d0}}
.scroller{{position:absolute;inset:0;z-index:2;overflow-y:auto;overflow-x:hidden;scrollbar-width:none}}.scroller::-webkit-scrollbar{{display:none}}
.lhead{{position:sticky;top:0;z-index:20;display:flex;align-items:flex-end;justify-content:space-between;padding:58px 18px 10px;background:linear-gradient(#f4f4f4 82%,rgba(244,244,244,0))}}
.lhead h1{{font-family:ZK,var(--body);font-size:30px;font-weight:400;color:#222}}.lhead h1 small{{font:italic 14px serif;color:#888;margin-left:6px}}
.lbtns{{display:flex;gap:10px}}.rb{{width:42px;height:42px;border-radius:50%;background:#fff;box-shadow:0 0 0 1.5px #d0d0d0 inset}}
main{{position:relative;padding:6px 18px 150px}}
/* 分段标签：小号巧克力牌（灰稿里是深灰小牌） */
.sec{{display:flex;align-items:baseline;gap:8px;margin:36px 0 12px 2px}}
.sec b{{font-family:ZK,var(--body);font-weight:400;font-size:14px;color:#fff;background:#222;border-radius:6px;padding:3px 9px 2px;letter-spacing:.1em}}
.sec span{{font-size:12px;color:#888}}
/* 列表行＝主题里的行底（点 9）：白纸、文字区干净，装饰只挂四角 */
.row{{position:relative;display:flex;align-items:center;gap:14px;width:100%;min-height:76px;margin-top:10px;padding:14px 16px;background:#fff;border-radius:18px;box-shadow:0 0 0 1.5px #d0d0d0 inset;text-align:left}}
.row:active{{background:#f0f0f0}}
.dt{{flex:none;width:44px;text-align:center}}.dt b{{display:block;font-size:26px;line-height:1;color:#222}}.dt small{{display:block;font-family:ZK,var(--body);font-size:10px;color:#888;margin-top:4px;white-space:nowrap}}
.tx{{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}}
.his{{font-size:15px;line-height:1.5;color:#222;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-wrap:pretty}}
.me{{font-size:13px;line-height:1.4;color:#888;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.lab{{font-family:ZK,var(--body);font-size:11px;color:#888}}
.ct{{flex:none;text-align:right;min-width:30px}}.ct b{{font-size:20px;color:#222;line-height:1}}.ct small{{font-family:ZK,var(--body);font-size:10px;color:#888;margin-left:2px}}
.uns{{display:block;margin-top:4px;font-size:12px;color:#888;filter:blur(3px);transition:filter .4s;text-align:left}}.uns.on{{filter:none}}.uns i{{font-style:normal;font-family:ZK,var(--body);font-size:10px;margin-right:4px}}
.nil{{margin:12px 0 2px 16px;font-size:12px;color:#888}}.nil .num{{font-size:13px;margin-right:4px}}
.row.wk{{min-height:64px;padding-left:18px}}.row.wk .his{{font-size:14px}}
/* 今天：大一号，顶上淋酱（只在这里），主锚点在右上角 */
.today{{position:relative;display:block;width:100%;margin-top:34px;padding:30px 18px 18px;background:#fff;border-radius:22px;box-shadow:0 0 0 1.5px #d0d0d0 inset;text-align:left}}
.today .sauce{{position:absolute;left:0;top:0;width:100%;height:30px;pointer-events:none}}
.today .top{{display:flex;align-items:baseline;gap:8px;margin-bottom:10px}}
.today .top b{{font-family:ZK,var(--body);font-weight:400;font-size:15px}}.today .top small{{font-size:12px;color:#888}}
.today .top em{{margin-left:auto;font-style:normal;font-size:12px;color:#888}}.today .top em b{{font-family:Baloo;font-size:26px;color:#222;margin-right:2px}}
.today .his{{font-size:18px;font-weight:600;line-height:1.5;-webkit-line-clamp:3}}
.today .me{{font-size:14px;margin-top:6px}}
.today .uns{{font-size:13px;margin-top:10px}}
.today .cat{{position:absolute;right:-6px;top:-42px;width:78px;transform-origin:50% 100%;animation:sway 4.2s ease-in-out infinite}}
/* 小料：跨在框边上（约 1/3 在框内），绕自己的支点呼吸，周期错开 */
.gar{{position:absolute;width:34px;height:34px;pointer-events:none;z-index:3;animation:sway var(--d) ease-in-out infinite;animation-delay:var(--dl)}}
.gar svg{{width:100%;height:100%;display:block}}
.gar.tr{{right:-14px;top:-14px;transform-origin:20% 80%}}.gar.tl{{left:-14px;top:-14px;transform-origin:80% 80%}}
.gar.br{{right:-14px;bottom:-14px;transform-origin:20% 20%}}.gar.bl{{left:-14px;bottom:-14px;transform-origin:80% 20%}}
.dot{{position:absolute;width:7px;height:7px;border-radius:50%;background:#d0d0d0;box-shadow:0 0 0 1.5px #888 inset;pointer-events:none;animation:bob var(--d) ease-in-out infinite;animation-delay:var(--dl)}}
.dot.tr{{right:10px;top:-4px}}.dot.tl{{left:12px;top:-4px}}.dot.br{{right:12px;bottom:-4px}}.dot.bl{{left:12px;bottom:-4px}}
@keyframes sway{{0%,100%{{rotate:-4deg}}50%{{rotate:5deg}}}}
@keyframes bob{{0%,100%{{translate:0 0}}50%{{translate:0 -3px}}}}
.pnav{{position:absolute;left:16px;right:16px;bottom:20px;height:62px;border-radius:31px;background:rgba(255,255,255,.9);box-shadow:0 0 0 1.5px #d0d0d0 inset;z-index:30;display:flex;align-items:center;padding:0 5px}}
.pnav .tab{{flex:1;height:52px;font-family:ZK,var(--body);font-size:11px;color:#888;text-align:center}}.pnav .tab.on{{color:#222;background:#e2e2e2;border-radius:26px}}
.tap{{transition:transform .25s ease-out}}.tap:active{{transform:scale(.98)}}
.end{{text-align:center;font-size:12px;color:#888;margin-top:30px;letter-spacing:.1em}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style></head><body><div class="app">
<div class="bg" aria-hidden="true">{"".join(f'<i class="pb{" l" if j%3==1 else ""}" style="width:{s}px;height:{s}px;left:{x}%;bottom:{y}px;--d:{3+j*.4:.1f}s;--dl:-{j*.7:.1f}s"></i>' for j,(s,x,y) in enumerate([(22,6,96),(16,18,70),(26,74,92),(14,88,120),(18,52,64),(12,34,110)]))}</div>
<div class="scroller" id="sc"><header class="lhead"><h1>聊天<small>chats</small></h1><div class="lbtns"><button class="rb" aria-label="搜索聊天"></button><button class="rb" aria-label="更多"></button></div></header>
<main>
<button class="today tap" aria-label="进今天的聊天">
<svg class="sauce" viewBox="0 0 360 30" preserveAspectRatio="none" aria-hidden="true"><path d="M22 0H338Q360 0 360 22V8Q352 20 340 14Q330 26 318 12Q300 20 286 10Q270 28 254 12Q236 18 220 9Q204 24 188 11Q170 19 152 10Q136 27 120 12Q102 18 86 9Q70 22 54 11Q38 25 22 12Q10 20 0 10V22Q0 0 22 0Z" fill="#888"/></svg>
<svg viewBox="0 0 120 92" class="cat" aria-hidden="true"><path d="M14 80C6 62 12 40 26 30C28 18 34 10 40 8C46 14 48 20 50 24C56 22 64 22 70 24C72 18 76 12 82 8C88 12 92 22 94 30C108 40 114 62 106 80C96 88 24 88 14 80Z" fill="#fff" stroke="#888" stroke-width="2"/><circle cx="46" cy="52" r="3" fill="#222"/><circle cx="74" cy="52" r="3" fill="#222"/></svg>
<div class="top"><b>今天</b><small class="num">11/11 周三 · 19:45</small><em><b>6</b>轮</em></div>
<span class="tx"><span class="his">那我先把奶煮上，你到家刚好能喝</span><span class="me">我：要加棉花糖！</span>
<span class="uns" role="button" onclick="event.stopPropagation();this.classList.toggle('on')"><i>写了又擦掉 ·</i>其实今天有点想你</span></span>
<i class="gar bl big" style="--d:3.4s;--dl:-1s" data-z="0.08">{G["leaf"]}</i><i class="dot tr" style="--d:4.1s;--dl:-.4s"></i>
</button>
<div class="sec"><b>本周</b><span class="num">11/5 – 11/10 · 31 轮</span></div>
{"".join(rows)}
<div class="sec"><b>更早</b><span>一周一行</span></div>
{"".join(erows)}
<div class="end">翻到杯底啦</div>
</main></div>
<nav class="pnav"><button class="tab">今天</button><button class="tab">记忆</button><button class="tab on">聊天</button><button class="tab">人格</button><button class="tab">设置</button></nav>
</div><script>
// 小料随滑动有一点前后视差（离纸面的距离不同）
(function(){{if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;var sc=document.getElementById('sc'),g=[].slice.call(document.querySelectorAll('[data-z]'));
var t=0;sc.addEventListener('scroll',function(){{if(t)return;t=requestAnimationFrame(function(){{t=0;var y=sc.scrollTop;g.forEach(function(e){{var r=e.parentNode.getBoundingClientRect();var c=r.top+r.height/2-innerHeight/2;e.style.translate='0 '+(-c*+e.dataset.z).toFixed(1)+'px'}})}})}},{{passive:true}});}})();
</script></body></html>'''
open(os.path.join(R,'..','..','p','list','sk9.html'),'w').write(html)
print(len(html))
