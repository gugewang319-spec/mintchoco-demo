# 样板间第一步：选择题页 p/kit/pick.html（11-20 茶茶：美术有了但整体好乱 → 先定 Tokens 再拼页）
# 现状统计（p/*/index.html）：圆角 14 种以上、字号 14 种以上、颜色二十多种 → 每题 2–3 个实物让她挑
import os,subprocess
H=os.path.dirname(os.path.abspath(__file__))+'/../../p/kit/'
Q=[
 ('1','圆角','现在各页用了 14 种圆角（2、4、5、12、14、22、26、31px…）',[
   ('A','方糖','纸 2 · 物件 6 · 面板 12','--r1:2px;--r2:6px;--r3:12px;--rp:12px'),
   ('B','软糖','纸 4 · 物件 10 · 面板 20','--r1:4px;--r2:10px;--r3:20px;--rp:20px'),
   ('C','混搭','纸 2 · 物件 12 · 按钮全圆','--r1:2px;--r2:12px;--r3:16px;--rp:99px')]),
 ('2','间距','8 点网格，页边距 24',[
   ('A','紧','行距 8 · 组内 12 · 组间 24','--g1:8px;--g2:12px;--g3:24px'),
   ('B','松','行距 12 · 组内 16 · 组间 32','--g1:12px;--g2:16px;--g3:32px')]),
 ('3','字号','现在有 14 种字号（11、11.5、12、12.5、13…）；收成四级',[
   ('A','杂志','标题 32 · 段名 20 · 正文 15 · 注 12','--f1:32px;--f2:20px;--f3:15px;--f4:12px'),
   ('B','收敛','标题 28 · 段名 18 · 正文 15 · 注 12','--f1:28px;--f2:18px;--f3:15px;--f4:12px'),
   ('C','大标题','标题 40 · 段名 20 · 正文 14 · 注 12','--f1:40px;--f2:20px;--f3:14px;--f4:12px')]),
 ('4','点缀色','底色固定：深巧、可可、薄荷、奶白、薄荷深；再挑一个点缀',[
   ('A','不加','只用五色 + 警示红','--ac:#2f6e58;--acb:#c4e8da'),
   ('B','莓粉','加 #e7b4a4','--ac:#b8695a;--acb:#f2d3c8'),
   ('C','焦糖','加 #c9a07e','--ac:#8a5c46;--acb:#ecd6bd')]),
 ('5','装字的容器','代替白底纸卡，全站只留一种',[
   ('A','毛玻璃','底栏同款，条纹透得出来','glass'),
   ('B','巧克力板','深巧底、奶白字、点线框','choc'),
   ('C','不装','字直接写在条纹上，薄荷描边分组','bare')]),
]
def sample(qn,o):
  st=o[3] if qn!='5' else ''
  cls={'glass':' glass','choc':' choc','bare':' bare'}.get(o[3],' glass') if qn=='5' else ' glass'
  return f'''<button class="op" data-q="{qn}" data-o="{o[0]}" style="{st}"><span class="tag"><b>{o[0]}</b>{o[1]}</span>
<span class="box{cls}"><span class="t1">晚风</span><span class="t4">MiniMax</span>
<span class="row"><span class="t3">语速</span><span class="num">0.95<small>×</small></span></span>
<span class="b2">试听</span></span><span class="cap">{o[2]}</span></button>'''
body=''.join(f'''<section class="q" id="q{q[0]}"><h2><i>{q[0]}</i>{q[1]}</h2><p class="why">{q[2]}</p><div class="ops n{len(q[3])}">{''.join(sample(q[0],o) for o in q[3])}</div></section>''' for q in Q)
html=r'''<!doctype html><html lang="zh"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>样板间 · 选择题</title><style>
@font-face{font-family:ZK;src:url(pk-zk.ttf)}@font-face{font-family:WK;src:url(pk-wk.ttf)}
@font-face{font-family:Baloo;src:url(../snd/baloo.ttf);font-weight:100 900}@font-face{font-family:BalooX;src:url(../snd/baloo800.ttf)}
*{box-sizing:border-box;margin:0;padding:0}button{all:unset;cursor:pointer;-webkit-tap-highlight-color:transparent}
:root{--ink:#5b3a2c;--co:#8a5c46;--mint:#c4e8da;--mintd:#2f6e58;--cream:#fbf6ea}
html,body{height:100%}body{color:var(--ink);font:15px/1.5 WK;background:repeating-linear-gradient(90deg,#d7eee5 0,#d7eee5 18px,#edf8f3 18px,#edf8f3 36px)}
.app{max-width:412px;margin:0 auto;padding:28px 24px 140px}
header h1{font:32px/1.1 ZK;letter-spacing:.04em}header p{font:13px/1.6 WK;color:var(--co);margin-top:8px}
.q{margin-top:32px}.q h2{display:flex;align-items:center;gap:10px;font:20px/1 ZK}
.q h2 i{font:800 13px/1 BalooX;font-style:normal;width:26px;height:26px;display:grid;place-items:center;border-radius:50%;background:linear-gradient(165deg,#704534,#4b2d21);color:var(--cream);box-shadow:0 2px 0 #33201a}
.why{font:12px/1.5 WK;color:var(--co);margin:8px 0 12px}
.ops{display:grid;gap:8px}.ops.n3{grid-template-columns:repeat(3,1fr)}.ops.n2{grid-template-columns:repeat(2,1fr)}
.op{display:flex;flex-direction:column;gap:6px;border-radius:12px;padding:6px;transition:box-shadow .25s,transform .25s cubic-bezier(.3,1.4,.5,1)}
.op:active{transform:scale(.97)}
.op.on{box-shadow:0 0 0 2px var(--mintd),0 0 0 6px rgba(196,232,218,.9)}
.tag{display:flex;align-items:center;gap:5px;font:13px/1 WK;color:var(--ink)}.tag b{font:800 12px/1 BalooX;color:var(--mintd)}
.cap{font:11px/1.4 WK;color:var(--co)}
/* 样本：默认 token */
.op{--r1:4px;--r2:10px;--r3:16px;--rp:99px;--g1:10px;--g2:14px;--g3:24px;--f1:22px;--f2:18px;--f3:14px;--f4:11px;--ac:#2f6e58;--acb:#c4e8da}
.box{display:flex;flex-direction:column;gap:var(--g1);padding:var(--g2) 10px;border-radius:var(--r3);min-height:150px}
.glass{background:rgba(252,250,244,.62);-webkit-backdrop-filter:blur(18px) saturate(120%);backdrop-filter:blur(18px) saturate(120%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.8),inset 0 1px 0 rgba(255,255,255,.95),0 2px 0 rgba(91,58,44,.08)}
.choc{background:linear-gradient(165deg,#704534,#4f2f22 60%,#472a1e);box-shadow:0 3px 0 #33201a;position:relative;color:#f6e8d4}
.choc::before{content:"";position:absolute;inset:4px;border:1.6px dotted rgba(201,160,126,.7);border-radius:calc(var(--r3) - 3px);pointer-events:none}
.choc .t4,.choc .t3{color:#e8d2b8}.choc .num{color:#fbf6ea}
.bare{background:none;box-shadow:inset 0 0 0 1.3px rgba(47,110,88,.55)}
.t1{font:var(--f1)/1.05 ZK;letter-spacing:.03em}
.q[id=q3] .ops{grid-template-columns:1fr}.q[id=q3] .box{flex-direction:row;flex-wrap:wrap;align-items:flex-end;gap:12px 20px;min-height:0}.q[id=q3] .t1{flex-basis:100%}.q[id=q3] .b2{margin:0 0 0 auto;align-self:center}
.t4{font:var(--f4)/1.3 WK;color:var(--co)}
.row{display:flex;flex-direction:column;gap:2px;white-space:nowrap}
.t3{font:var(--f3)/1.2 WK}
.num{font:800 calc(var(--f3) + 2px)/1 BalooX;color:var(--ink)}.num small{font-size:.6em;margin-left:1px}
.b2{align-self:flex-start;margin-top:auto;font:12px/1 WK;padding:7px 12px;border-radius:var(--rp);background:var(--acb);color:var(--ac);box-shadow:inset 0 0 0 1.2px var(--ac),0 2px 0 rgba(91,58,44,.15)}
.q[id=q1] .box{border-radius:var(--r3)}.q[id=q1] .b2{border-radius:var(--rp)}
/* 底部结果条：底栏同款毛玻璃 */
.res{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);width:min(calc(100% - 32px),380px);display:flex;align-items:center;gap:10px;padding:12px 12px 12px 16px;border-radius:26px;background:rgba(252,250,244,.62);-webkit-backdrop-filter:blur(18px) saturate(120%);backdrop-filter:blur(18px) saturate(120%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.8),inset 0 1px 0 rgba(255,255,255,.95),0 6px 18px rgba(91,58,44,.12)}
.res span{flex:1;font:13px/1.4 WK;color:var(--co)}.res span b{font:800 13px/1 BalooX;color:var(--ink);letter-spacing:.06em}
.res button{font:14px/1 WK;color:#f6e8d4;background:linear-gradient(165deg,#704534,#4b2d21);padding:11px 16px;border-radius:8px;box-shadow:0 2.5px 0 #33201a}
.res button[aria-disabled=true]{opacity:.45}
</style></head><body><div class="app">
<header><h1>样板间 · 选择题</h1><p>每题点一个。同一张「音色」小样，只换这一项，看哪个顺眼。</p></header>
BODY
</div>
<div class="res"><span id="rs">还没选</span><button id="cp" aria-disabled="true">抄下来</button></div>
<script>
const S={};const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
$$('.op').forEach(b=>b.onclick=()=>{S[b.dataset.q]=b.dataset.o;$$('.op[data-q="'+b.dataset.q+'"]').forEach(x=>x.classList.toggle('on',x===b));up()});
function up(){const k=Object.keys(S).sort();$('#rs').innerHTML=k.length?'选了 <b>'+k.map(q=>q+S[q]).join(' ')+'</b>'+(k.length<5?'，还差 '+(5-k.length)+' 题':''):'还没选';$('#cp').setAttribute('aria-disabled',k.length<5)}
$('#cp').onclick=()=>{const k=Object.keys(S).sort();if(k.length<5)return;const t='样板间选择题：'+k.map(q=>q+S[q]).join(' ');(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(()=>{$('#cp').textContent='抄好了'},()=>prompt('复制这行发给我',t))};
</script></body></html>'''
out=html.replace('BODY',body)
open(H+'pick.html','w').write(out)
txt=''.join(sorted(set(c for c in out if ord(c)>0x2000)))
open('/tmp/pk.txt','w').write(txt)
for src,dst in [('/workspace/work/fonts/zkfull.ttf','pk-zk.ttf'),('/workspace/work/fonts/wkfull.ttf','pk-wk.ttf')]:
  subprocess.run(['pyftsubset',src,'--text-file=/tmp/pk.txt','--unicodes=U+0020-007E,U+00D7','--output-file='+H+dst,'--layout-features=*'],check=True)
print('ok',len(txt))
