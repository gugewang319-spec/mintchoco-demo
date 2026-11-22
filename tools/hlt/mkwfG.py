R=[("12–13","+1,468"),("09:55","82"),("09:00","+2,263"),("08:10","56"),("07:14","6h30")]
def rows(x,y,w,gap=30,big=None):
  h=""
  for i,(t,v) in enumerate(R):
    yy=y+i*gap
    if big==i:
      h+=f'<div class="b d" style="left:{x}px;top:{yy-6}px;width:{w}px;height:{gap+14}px"></div><span class="t big2" style="left:{x+10}px;top:{yy}px">{v}</span><span class="t s" style="left:{x+w-48}px;top:{yy+12}px">{t}</span>'
      continue
    h+=f'<i class="dot" style="left:{x}px;top:{yy+5}px"></i><span class="t s" style="left:{x+16}px;top:{yy}px">{t}</span><i class="ln" style="left:{x+64}px;width:{w-120}px;top:{yy+10}px"></i><span class="t v" style="left:{x+w-54}px;top:{yy}px">{v}</span>'
  return h
def note(n,x,y,txt):return f'<span class="no" style="left:{x}px;top:{y}px">{n}</span><span class="nt" style="left:{x+22}px;top:{y-2}px">{txt}</span>'
F=[]
# A 大字压底
F.append(("A 大字压底 · 对比",f'''
<span class="huge" style="left:-14px;top:150px">20</span>
<div class="b m rot" style="left:24px;top:28px;width:118px;height:58px;--r:-3deg"></div><span class="t date" style="left:36px;top:38px">11/20</span>
<span class="t s" style="left:150px;top:62px">周五 · 今天</span>
<div class="col" style="left:24px;top:116px">{''.join('<div class="b l sq"></div>' for _ in range(3))}</div>
<div class="b p" style="left:132px;top:104px;width:202px;height:186px"></div>{rows(146,118,176)}
<div class="b k circ" style="left:298px;top:12px;width:56px;height:56px"></div>
{note(1,40,330,"「20」异形字素压底，半透明")}{note(2,40,356,"左窄列：珍珠数/月相/心率 缩小版")}{note(3,40,382,"右边纸面写记录；角上贴纸")}'''))
# B 横幅出血
F.append(("B 横幅出血 · 亲密",f'''
<div class="b m" style="left:60px;top:22px;width:320px;height:74px"></div><span class="t s" style="left:72px;top:30px">0 ─ 6 ─ 12 ─ 18 ─ 24 时间轴横幅（出血到右边）</span>
<div class="b k circ" style="left:-40px;top:40px;width:120px;height:120px"></div>
<div class="b d rot" style="left:56px;top:78px;width:126px;height:58px;--r:2deg"></div><span class="t date" style="left:70px;top:86px;color:#fff">11/20</span>
<span class="t s" style="left:196px;top:110px">周五 · 5 条</span>
<div class="b p" style="left:110px;top:150px;width:224px;height:162px"></div>{rows(124,164,198)}
{note(1,24,330,"时间轴做成一条出血横幅当头图")}{note(2,24,356,"月相大圆半截出屏，压住日期签")}{note(3,24,382,"记录缩进右侧，和左边留白对比")}'''))
# C 竖排侧标
F.append(("C 竖排侧标 · 对齐",f'''
<div class="b d" style="left:0;top:0;width:44px;height:320px"></div><span class="t vt" style="left:12px;top:20px">{"".join("<b>"+c+"</b>" for c in "十一月二十日·周五")}</span>
<span class="t date" style="left:64px;top:22px">11/20</span>
<div class="b k circ" style="left:268px;top:-26px;width:110px;height:110px"></div>
<i class="rule" style="left:64px;top:84px;width:270px"></i>
{rows(64,104,270,big=4)}
<div class="b l" style="left:64px;top:270px;width:84px;height:30px"></div><div class="b l" style="left:156px;top:270px;width:84px;height:30px"></div><div class="b l" style="left:248px;top:270px;width:86px;height:30px"></div>
{note(1,24,330,"左侧竖排日期条，所有字对齐一条线")}{note(2,24,356,"当天最突出那条（睡眠）放大成一块")}{note(3,24,382,"底下三块：珍珠/月相/心率小结")}'''))
# D 斜贴拼贴
F.append(("D 斜贴拼贴 · 重复",f'''
<div class="b p rot" style="left:20px;top:58px;width:250px;height:236px;--r:-2.5deg"></div>{rows(38,104,214)}
<div class="b d rot" style="left:24px;top:22px;width:130px;height:58px;--r:-5deg"></div><span class="t date" style="left:36px;top:30px;color:#fff">11/20</span>
<div class="b m rot" style="left:228px;top:4px;width:112px;height:86px;--r:4deg"></div><span class="t big2" style="left:240px;top:18px">3,731</span><span class="t s" style="left:240px;top:58px">步 · 今日</span>
<div class="b k circ" style="left:286px;top:150px;width:44px;height:44px"></div><div class="b k circ" style="left:300px;top:206px;width:30px;height:30px"></div><div class="b k circ" style="left:292px;top:248px;width:20px;height:20px"></div>
{note(1,24,330,"记录纸斜贴，日期签压在角上")}{note(2,24,356,"当天总数单独一块再斜贴一层")}{note(3,24,382,"同形小圆重复递减：珍珠滚出去")}'''))
body="".join(f'<h3>{t}</h3><div class="fr">{c}</div>' for t,c in F)
html=f'''<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>健康 · 一天手帐页灰块构图</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#e9ecea;font-family:system-ui,"PingFang SC","Noto Sans SC",sans-serif;color:#555;padding:24px 0 48px}}
h1{{font-size:20px;color:#444;padding:24px 24px 4px}}.sub{{font-size:12px;color:#999;padding:0 24px 8px}}
h3{{font-size:14px;color:#444;padding:24px 24px 8px}}
.fr{{position:relative;width:min(100%,358px);height:412px;margin:0 auto;background:#f4f5f4;overflow:hidden;box-shadow:0 1px 0 #d6d9d7}}
.b{{position:absolute}}.p{{background:#e3e5e4}}.l{{background:#d6d9d7}}.m{{background:#c4c7c5}}.d{{background:#8f9390}}.k{{background:#b3b6b4}}
.circ{{border-radius:50%}}.rot{{transform:rotate(var(--r))}}
.col{{position:absolute;display:flex;flex-direction:column;gap:12px}}.sq{{position:static;width:84px;height:52px}}
.t{{position:absolute;white-space:nowrap}}.date{{font:800 34px/1 system-ui;color:#333}}.s{{font-size:12px;color:#888}}.v{{font-size:13px;font-weight:800;color:#444}}.big2{{font:800 30px/1 system-ui;color:#333}}
.vt{{display:flex;flex-direction:column;gap:6px;width:20px;text-align:center;font-size:15px;line-height:1;color:#fff;font-weight:700}}
.huge{{position:absolute;font:900 230px/1 system-ui;color:rgba(0,0,0,.07);letter-spacing:-.04em}}
.dot{{position:absolute;width:9px;height:9px;border-radius:2px;background:#9a9e9b}}.ln{{position:absolute;border-top:1px dotted #bbb}}.rule{{position:absolute;border-top:1.5px solid #bbb}}
.no{{position:absolute;display:inline-flex;width:16px;height:16px;border-radius:50%;border:1.2px solid #e0336a;font:10px/1 monospace;color:#e0336a;align-items:center;justify-content:center;background:#fff}}
.nt{{position:absolute;font:11px/20px system-ui;color:#e0336a;white-space:nowrap}}
</style><body><h1>一天手帐页 · 灰块构图</h1><p class="sub">同一天 11/20、同样 5 条记录，只换构图。挑一张再上装饰。</p>{body}</body></html>'''
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'../../p/hlt/wfG.html'),'w').write(html)
