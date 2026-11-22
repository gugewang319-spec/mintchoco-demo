# V62：健康页正式页 = vb16b（连上手环）+ vbD 观测手帐（撤 rec 二级页、撤今天时间轴托盘）+ ?empty 空态（vb16）
import os,re
H=os.path.dirname(os.path.abspath(__file__))+'/../../p/hlt/'
b=open(H+'vb16b.html').read(); d=open(H+'vbD.html').read(); e=open(H+'vb16.html').read()
# ---------- 1. 手帐 CSS：rec/vbD 样式加 #jn 前缀 ----------
rc=re.findall(r'<style>(.*?)</style>',d,re.S)[0]
SKIP=re.compile(r'^\s*(html|body|\*|:root|button|img|\.vp|\.app|\.drizzle|\.pearls|canvas#fx|\.o\b|\.bit|\.ground|\.sp\b|\.lhead|\.ttl|\.counter|\.pearlbtn|\.navfade|\.pnav|\.pill|\.tab\b|\.page|\.far|\.fl\b|\.scn|#app|\.k\b|\.k |\.lnk|\.data|\.stale|\.blk|\.steps|\.big|#sync|\.stalenote|#hours)')
KEEP=re.compile(r'\.idx|\.goo|\.tobot')
def walk(css):
  out='';i=0
  while i<len(css):
    j=css.find('{',i)
    if j<0:break
    sel=css[i:j].strip()
    if sel.startswith('@font-face'):k=css.index('}',j)+1;i=k;continue
    if sel.startswith('@'):
      dep=1;k=j+1
      while dep:dep+=css[k]=='{';dep-=css[k]=='}';k+=1
      inner=css[j+1:k-1]
      if sel.startswith('@keyframes'):out+=sel+'{'+inner+'}\n'
      else:out+=sel+'{'+walk(inner)+'}\n'
      i=k;continue
    k=css.index('}',j)+1;body=css[j:k];i=k
    sels=[s.strip() for s in sel.split(',') if s.strip()]
    keep=[]
    for s in sels:
      if KEEP.search(s):keep.append(s)
      elif SKIP.match(s):continue
      else:keep.append('#jn '+s)
    if keep:out+=','.join(keep)+body+'\n'
  return out
jcss=walk(rc).replace('ZK','ZJ').replace(' .pp',' .jp')
jcss='@font-face{font-family:ZJ;src:url(../srch/zk.ttf)}\n'+jcss+'''
#jn{position:relative;margin:34px 22px 0}
#jn .jhd{display:flex;align-items:flex-end;justify-content:space-between;margin:0 0 6px}
#jn .jhd .tt{position:relative}
#jn .jhd h2{font:26px/1 ZJ;color:var(--ch);letter-spacing:.06em;position:relative;z-index:1}
#jn .jhd .sc{position:absolute;left:62px;top:-16px;font:22px/1 Script;color:rgba(63,154,128,.55);rotate:-8deg;white-space:nowrap}
#jn .sv{position:relative;margin:0}\n#jn .jd.nt .jp{width:100%}\n#jn .sv .row{justify-content:flex-start;margin-top:0}
'''
# 1b. 删掉健康页底样式里旧记录区的死规则（.r/.sax 等），免得漏进手帐
JL={'r','sax','strip','tm','vl','ld','day','dh','num','pn','ik','opts','op','cal','more','more2','empty','box','fbar','sv','hr','cn','cd','ch','cg','idx','goo','ks','kh','kr','km','rows','rec','flt','ft','kd','cut','hide','rh','rs','hd','at','rest'}
def dead(sel):
  return all(set(re.findall(r'\.([a-zA-Z][\w-]*)',x))&JL for x in sel.split(','))
bc=re.findall(r'<style>(.*?)</style>',b,re.S)[0]
def prune(css):
  out='';i=0
  while True:
    j=css.find('{',i)
    if j<0:out+=css[i:];break
    sel=css[i:j]
    if sel.strip().startswith('@'):
      dep=1;k=j+1
      while dep:dep+=css[k]=='{';dep-=css[k]=='}';k+=1
      inner=css[j+1:k-1]
      out+=sel+'{'+(inner if sel.strip().startswith(('@keyframes','@font-face')) else prune(inner))+'}';i=k;continue
    k=css.index('}',j)+1
    if not dead(sel):out+=css[i:k]
    i=k
  return out
b=b.replace(bc,prune(bc),1)
# ---------- 2. HTML：去掉今天时间轴托盘，接手帐 ----------
body_rec=d[d.index('<main class="page" id="page">')+len('<main class="page" id="page">'):d.index('</main>')]
jn='<section id="jn" aria-label="观测手帐"><div class="jhd"><div class="tt"><span class="sc" aria-hidden="true">journal</span><h2>观测手帐</h2></div></div>'+body_rec+'</section>'
a=b.index('<section class="tray tl2">');z=b.index('</section>',a)+len('</section>')
b=b[:a]+jn+b[z:]
assert 'rec.html' not in b, 'allb link left'
# 字体加 Script（若无）
if 'font-family:Script' not in b: jcss='@font-face{font-family:Script;src:url(../set/script.ttf)}\n'+jcss
b=b.replace('</style>',jcss+'</style>',1)
# ---------- 3. 手帐 JS：包进 IIFE ----------
js=d[d.rindex('<script>\nconst $=s=>'):]
js=js[len('<script>\n'):js.index('</script>')]
js=js[:js.index("$('.back').onclick")]
# 不要「到底」小圆钮（健康页本来没有）
a=js.index('{const DB=');z=js.index('draw();',a)
js=js[:a]+js[z:]
js=js.replace("$('#cnt').innerHTML","$('#cnt').innerHTML")
# 今天那页不放铁盒/珍珠（上面杯子已经是今天步数）
js=js.replace("${kd&&kd!=='steps'?'':","${(kd&&kd!=='steps')||x.n===0?'':")
js=js.replace('class="pp"','class="jp"').replace('<section class="day jd${mr}"','<section class="day jd${mr}${x.n===0?\' nt\':\'\'}"')
js='<script>(()=>{\nif(document.documentElement.classList.contains("emp"))return;\n'+js+'\n})()</script>'
# ---------- 4. 空态 ?empty（vb16）----------
ec=re.search(r'/\* vb16 空态 \*/(.*?)</style>',e,re.S).group(1)
ec='\n'.join(('' if l.startswith('@') else '') + l for l in ec.split('\n'))
def pre(css):
  out=[]
  for line in css.strip().split('\n'):
    if line.startswith('@keyframes') or not line.strip():out.append(line);continue
    if line.startswith('@media'):out.append(line.replace('.etag','.emp .etag'));continue
    sel,rest=line.split('{',1);out.append(','.join('.emp '+s.strip() for s in sel.split(','))+'{'+rest)
  return '\n'.join(out)
ecss=pre(ec)+'\n.etag,.ego,.ehint{display:none}.emp .etag,.emp .ego{display:block}.emp .ego{display:inline-flex}.emp .ehint{display:block;position:relative;margin:40px 34px 0;padding:62px 22px 20px;rotate:-1.4deg;z-index:1}.emp .ehint::before{content:"";position:absolute;inset:-6px;border:solid transparent;border-width:64px 44px 14px 36px;border-image:url(jd-paper.png) 128 88 28 72 fill / 64px 44px 14px 36px stretch;opacity:.93;z-index:-1}.emp #jn{display:none}\n'
ecss=ecss.replace('.emp .tl2 .tl,.emp .tl2 .tax,.emp .tl2 .pick,.emp .tl2 .allb,','')
b=b.replace('</style>',ecss+'</style>',1)
# 空态元素（默认藏）
m=re.search(r'<div class="etag">.*?</button>(?=<div class="big">)',e,re.S).group(0)
b=b.replace('<div class="big">',m+'<div class="big">',1)
b=b.replace('<section id="jn"','<div class="ehint"><b>今天还没有记录</b>心率、睡眠和每一笔步数，接上手环以后都会落在这里。</div><section id="jn"',1)
b=b.replace('<head>','<head><script>if(/[?&]empty/.test(location.search))document.documentElement.classList.add("emp")</script>',1)
emjs='''<script>if(document.documentElement.classList.contains("emp")){const c=document.querySelector('.counter');if(c){c.setAttribute('aria-label','手环没连上');c.querySelectorAll('span').forEach(s=>s.textContent='-')}
const cp=document.querySelector('.cup');if(cp)cp.setAttribute('aria-label','杯子还空着，目标八千步');
document.querySelectorAll('section').forEach(s=>{const t=s.querySelector('.tt');if(t&&s.textContent.includes('最近收到')){s.querySelector('small').textContent='还没收到过';t.textContent='--:--';const o=s.querySelector('.ok');o.classList.add('no');o.lastChild.textContent='往左滑，填地址'}})}</script>'''
# ---------- 5. 拼 ----------
b=b.replace('</main>','</main>'+js,1)
b=b.replace('</body>',emjs+'</body>',1)
open(H+'index.html','w').write(b)
print('ok',len(b))
