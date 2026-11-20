# 样板间 p/kit/yb.html：骨架 base.css + 皮肤 skin-*.css（茶茶 11-20：像酒馆美化，做好基础、自己换皮）
# UI 语言照 Gemini 模型页旧稿：薄荷染底行 + 可可细边 + 左可可竖条 + 右侧 K/M 大数字 + 巧克力条主钮 + 花体英文
import os,subprocess,re
H=os.path.dirname(os.path.abspath(__file__))+'/../../p/kit/'
F='/workspace/work/fonts/'
LEAF='<svg class="ico" viewBox="0 0 16 16" fill="#a6d9c4" stroke="#5b8a74" stroke-width="1"><path d="M2.5 13.5C2.5 6 7 2.5 13.5 2.5 13.5 9 10 13.5 2.5 13.5Z"/><path d="M3 13 10 6" fill="none"/></svg>'
STAR='<svg class="ico" viewBox="0 0 16 16" fill="#f6e3b8" stroke="#a9825f" stroke-width="1" stroke-linejoin="round"><path d="M8 1.8 9.8 6l4.4.4-3.3 2.9 1 4.4L8 11.4l-3.9 2.3 1-4.4L1.8 6.4 6.2 6Z"/></svg>'
def I(d):return f'<svg viewBox="0 0 20 20" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
BACK=I('<path d="M12.5 4 6.5 10l6 6"/>');PLUS=I('<path d="M10 4v12M4 10h12"/>');SRCH=I('<circle cx="8.8" cy="8.8" r="5"/><path d="m12.6 12.6 3.6 3.6"/>');PEN=I('<path d="m4 16 1-4 8-8 3 3-8 8Z"/>');BIN=I('<path d="M4.5 6h11M8 6V4h4v2M6 6l1 10h6l1-10"/>')
CK='<svg class="ck" viewBox="0 0 14 14" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m2.5 7.5 3 3 6-7"/></svg>'
CHEV='<svg viewBox="0 0 10 10" fill="none" stroke-width="1.6" stroke-linecap="round"><path d="m2 3.5 3 3 3-3"/></svg>'
WARN='<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#8a5c46" stroke-width="1.3" stroke-linejoin="round"><path d="M12 3 22 20H2Z" fill="#f6d7cb"/><path d="M12 9.5v5" stroke="#b8573c" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="17.3" r="1.2" fill="#b8573c" stroke="none"/></svg>'
def dec(src,st,cls='sway',o='50% 90%',a='4deg'):return f'<img class="dec {cls}" src="{src}" alt="" style="{st};--o:{o};--a:{a}">'
def grp(n,name,ct,end=''):return f'<div class="grp"><span class="no">{n}</span><span class="rib"><h2>{name}</h2><span class="ct">{ct}</span></span><span class="end">{end}</span></div>'
def row(nm,ic,sub,num,u,small,on=False):return f'<button class="row{" on" if on else ""}"><span class="nm"><b>{nm}</b>{ic}</span><span class="sub">{sub}</span><span class="sep"></span><span class="num">{num}<sup>{u}</sup><small>{small}</small></span></button>'
body=f'''
<img class="drip" src="../max/drizzle.png" alt="">
<header class="hd sec">
 <button class="b3 mt" aria-label="返回">{BACK}</button>
 <div class="t"><h1>样板间</h1><span class="en">Kit</span></div>
 <span class="plate"><b>14</b>件</span>
</header>

<section class="sec">
 {dec('../set/sprig.png','right:-96px;top:-34px;width:200px;opacity:.9','sway d2','100% 50%','2deg')}
 {grp('00','换皮','两套','')}
 <div class="fld"><label>皮肤</label><div class="pick" id="skin"><button class="cur"><span class="v"><span>薄荷巧克力</span>{CHEV}</span></button>
 <div class="opts"><button class="opt on" data-s="skin-mint.css"><span>薄荷巧克力</span>{CK}</button><button class="opt" data-s="skin-dark.css"><span>黑巧</span>{CK}</button></div></div></div>
</section>

<section class="sec">
 {dec('../max/leaves.png','left:-34px;top:-26px;width:62px','sway','80% 80%','6deg')}
 {grp('01','列表行','3 杯',f'<button class="b4">拉新的</button>')}
 <div class="rows">
 {row('gpt-4o',LEAF+STAR,'窗口 128K · 输出 16K · 能看图 · 流式','128','K','中杯 56%',True)}
 {row('claude-sonnet-4',LEAF+STAR,'窗口 200K · 输出 64K · 备用 gpt-4o','200','K','大杯 72%')}
 {row('gemini-2.5-pro',STAR,'窗口 1M · 输出 64K','1','M','满格 100%')}
 </div>
</section>

<section class="sec">
 {dec('../max/truf.png','right:-22px;bottom:-38px;width:52px','sway d3','50% 100%','5deg')}
 {dec('../max/bit3.png','right:10px;top:4px;width:26px','sway d2','50% 50%','12deg')}
 {grp('02','按钮','四级')}
 <div class="b2s"><button class="b2">{LEAF}试听</button><button class="b2">设默认</button><button class="b2 dg">删掉</button></div>
 <div style="display:flex;align-items:center;gap:12px;margin-top:14px">
  <button class="b3" aria-label="新建">{PLUS}</button><button class="b3 mt" aria-label="搜索">{SRCH}</button><button class="b3 mt" aria-label="编辑">{PEN}</button>
  <span style="margin-left:auto;display:flex;gap:2px"><button class="b4">再想想</button><button class="b4 dg">撕掉</button></span>
 </div>
 <p class="note">一级巧克力牌每屏只放一个，在下面「保存」。二级薄荷排块几格连着；三级圆形小甜点放图标；四级只是字。</p>
</section>

<section class="sec">
 {dec('../max/m_curls.png','right:-60px;top:6px;width:150px;opacity:.9','sway d2','30% 50%','-3deg')}
 {grp('03','填写','改了才能存')}
 <div class="fld"><label>名字</label><input class="in" id="f1" value="小鲸鱼中转"></div>
 <div class="fld"><label>地址</label><input class="in" id="f2" value="https://example.local/v1" inputmode="url"></div>
 <div class="fld"><label>钥匙 API Key</label><div class="key"><input class="in" id="f4" type="password" value="demo-key-123" autocomplete="off" spellcheck="false"><button class="eye" aria-label="显示/隐藏"><svg class="on" viewBox="0 0 20 20"><path d="M2 10s3-5.5 8-5.5S18 10 18 10s-3 5.5-8 5.5S2 10 2 10Z"/><circle cx="10" cy="10" r="2.4"/></svg><svg class="off" viewBox="0 0 20 20"><path d="M2 10s3-5.5 8-5.5S18 10 18 10s-3 5.5-8 5.5S2 10 2 10Z"/><circle cx="10" cy="10" r="2.4"/><path d="M3.5 3.5l13 13"/></svg></button></div></div>
 <div class="fld"><label>格式</label>
 <div class="pick" id="fmt"><button class="cur"><span class="v"><span>OpenAI</span>{CHEV}</span></button>
 <div class="opts"><button class="opt on"><span>OpenAI</span><small>/chat/completions</small>{CK}</button><button class="opt"><span>Anthropic</span><small>/v1/messages</small>{CK}</button><button class="opt"><span>Gemini</span><small>:generateContent</small>{CK}</button></div></div></div>
 <div class="fld"><label>备注</label><textarea class="in" id="f3" placeholder="写给自己看的，可不填"></textarea></div>
 <button class="b1" id="save" disabled><span>保存</span></button>
</section>

<section class="sec">
 {dec('../max/m_macaron.png','right:-18px;top:2px;width:50px','sway','50% 100%','-5deg')}
 {grp('04','筛选 · 搜索','')}
 <div style="display:flex;gap:8px;align-items:center;margin-bottom:10px"><input class="in" placeholder="搜模型名" style="flex:1"><button class="b3" aria-label="搜索">{SRCH}</button></div>
 <div class="flt"><button class="fp on">全部 <i>5</i></button><button class="fp">小鲸鱼 <i>2</i></button><button class="fp">Anthropic <i>2</i></button><button class="fp">Gemini <i>1</i></button></div>
</section>

<section class="sec">
 {dec('../max/whip.png','right:-14px;top:-14px;width:54px','sway d3','50% 100%','4deg')}
 {grp('05','做完 · 危险','')}
 <div class="b2s"><button class="b2" id="tst">响出餐铃</button><button class="b2 dg" id="cfm">{BIN}删一条</button></div>
</section>

<section class="sec">
 {dec('../max/cookie.png','left:-46px;bottom:-96px;width:96px','sway d2','50% 100%','3deg')}
 {grp('06','空 · 等 · 错','')}
 <div class="state"><img src="../max/m_bonbon.png" alt="" style="width:62px">
  <span class="t">罐子还空着</span><span class="s">先接一条渠道，模型会自己排进来</span>
  <div class="b2s" style="margin-top:4px"><button class="b2">{PLUS.replace('<svg','<svg class="ico"')}接一条</button></div></div>
 <div class="state" style="margin-top:10px"><div class="ld"><i></i><i></i><i></i></div><span class="s">正在拉模型…</span></div>
 <div class="state err" style="margin-top:10px">{WARN}<span class="s">连不上 example.local，钥匙可能过期</span><button class="b4">重试</button></div>
</section>
'''
CSS='''.note{margin-top:10px;font:var(--f4)/1.6 var(--ff-body);color:var(--ink2)}
.drip{position:absolute}
'''
JS=r'''
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
$$('.row').forEach(r=>r.onclick=()=>r.classList.toggle('on'));
$$('.fp').forEach(f=>f.onclick=()=>{$$('.fp').forEach(x=>x.classList.remove('on'));f.classList.add('on')});
function pick(el,cb){const c=el.querySelector('.cur'),v=el.querySelector('.v span');c.onclick=e=>{e.stopPropagation();document.querySelectorAll('.pick.open').forEach(p=>p!==el&&p.classList.remove('open'));el.classList.toggle('open')};
 el.querySelectorAll('.opt').forEach(o=>o.onclick=()=>{el.querySelectorAll('.opt').forEach(x=>x.classList.remove('on'));o.classList.add('on');v.textContent=o.querySelector('span').textContent;el.classList.remove('open');cb&&cb(o)})}
document.addEventListener('click',e=>{if(!e.target.closest('.pick'))document.querySelectorAll('.pick.open').forEach(p=>p.classList.remove('open'))});
pick($('#skin'),o=>{$('#skinlink').href=o.dataset.s;MC.toast('换成「'+o.querySelector('span').textContent+'」了')});
const save=$('#save'),fs=['#f1','#f2','#f4','#f3'].map($);let base=fs.map(f=>f.value),fmt0='OpenAI';
const dirty=()=>fs.some((f,i)=>f.value!==base[i])||$('#fmt .v span').textContent!==fmt0;
const upd=()=>save.disabled=!dirty();
$('.key .eye').onclick=()=>{const k=$('.key'),i=$('#f4');k.classList.toggle('show');i.type=k.classList.contains('show')?'text':'password'};fs.forEach(f=>f.oninput=upd);pick($('#fmt'),upd);
save.onclick=()=>{const old=base,of=fmt0;base=fs.map(f=>f.value);fmt0=$('#fmt .v span').textContent;upd();
 MC.toast('存好了',{undo:()=>{base=old;fmt0=of;upd()}})};
$('#tst').onclick=()=>MC.toast('模型拉好了，新来 2 杯',{undo:()=>MC.toast('撤回了')});
$('#cfm').onclick=async()=>{if(await MC.confirm({title:'删掉这条？',body:'<b>claude-sonnet-4</b> 会从渠道里拿掉，用它的人格会换成备用。',ok:'删掉',cancel:'再想想'}))MC.toast('删掉了',{undo:()=>MC.toast('放回去了')})};
'''
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>样板间</title>
<style>@font-face{{font-family:ZK;src:url(yb-zk.ttf)}}@font-face{{font-family:WK;src:url(yb-wk.ttf)}}@font-face{{font-family:Baloo;src:url(../snd/baloo.ttf);font-weight:100 900}}@font-face{{font-family:BalooX;src:url(../max/baloo800.ttf)}}@font-face{{font-family:Sofia;src:url(../max/sofia.ttf)}}</style>
<link rel="stylesheet" href="base.css"><link id="skinlink" rel="stylesheet" href="skin-mint.css"><style>{CSS}</style></head>
<body><div class="vp"><main class="app">{body}</main></div><script src="../ui.js"></script><script>{JS}</script></body></html>'''
open(H+'yb.html','w').write(html)
txt=re.sub(r'<[^>]+>','',html)+'确定吗？再想想撤销存好了换成了模型拉好新来杯撤回删掉放回去「」'
chars=''.join(sorted(set(c for c in txt if ord(c)>127)))+'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;!?-·…/%()'
open('/tmp/ybch.txt','w').write(chars)
for src,dst in [('zkfull.ttf','yb-zk.ttf'),('wkfull.ttf','yb-wk.ttf')]:
  subprocess.run(['pyftsubset',F+src,'--text-file=/tmp/ybch.txt','--output-file='+H+dst,'--layout-features=*'],check=True)
print('ok',len(chars))
