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
