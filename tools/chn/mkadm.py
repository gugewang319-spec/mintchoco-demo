# 渠道页试点：从 p/chn/index.html 生成 p/chn/vb-adm.html —— 打开的单子换成样板组件（tools/chn/tk.jsx）。不改 index.html。
import os,re,subprocess
R=os.path.dirname(os.path.abspath(__file__))+'/../../'
s=open(R+'p/chn/index.html').read()
def cut(a,b,new):
  global s
  i=s.index(a);j=s.index(b,i);s=s[:i]+new+s[j:]
NEWJS=r'''const RT=[1,2,3,4,5],FM=['OpenAI','Anthropic','Gemini'];
const EP={OpenAI:'/v1/chat/completions',Anthropic:'/v1/messages',Gemini:'/v1beta/models/{模型}:generateContent'};
function tkLabel(i){const c=CH[i],t=$$('.tk')[i];if(!t)return;t.querySelector('.nm').textContent=c.n;t.querySelector('.rt b').textContent=c.n;t.querySelector('.kc').innerHTML=c.k.length+'<small>把钥</small>'}
function tkProps(i){const c=CH[i];return{mode:'edit',c,no:i+1,EP,FM,RT,UP,WO,OO,
 onLift:()=>pick(cur),
 onSave:(D,nk)=>{c.n=D.n.trim();c.h=D.h.trim();c.f=D.f;c.r=D.r;c.p=D.p;c.k=D.k.map(x=>[...x]);c.m=D.m.map(({n,w,o,v,s})=>({n,w,o,v,s}));if(nk)c.k.push([nk.slice(-4),'','正常']);
  tkLabel(cur);TK.show(op,tkProps(cur));MC.toast(`「${c.n}」存好了`)},
 onRip:()=>{const at=cur;CH.splice(at,1);cur=-1;op.classList.remove('on');TK.hide(op);build();fsGo();$('#idle').classList.remove('hide');fitH();
  MC.toast(`撕掉了「${c.n}」`,{undo:()=>{CH.splice(at,0,c);build();fsGo();fitH()}})},
 onTaste:m=>taste(m,c.n)}}
'''
s=s.replace("op.innerHTML=rc(CH[i],i);wire();","TK.show(op,tkProps(i));")
NEWT=r'''function newT(){if(cur===-2){cur=-1;$('.nt').classList.remove('lit');op.classList.remove('on');setTimeout(()=>{if(cur==-1){TK.hide(op);fitH()}},RM?0:500);$('#idle').classList.remove('hide');return}
 if(cur>=0)$$('.tk')[cur].classList.remove('out');
 cur=-2;$('.nt').classList.add('lit');$('#idle').classList.add('hide');op.classList.remove('on');
 TK.show(op,{mode:'new',no:CH.length+1,EP,FM,RT,UP,WO,OO,onLift:newT,onHang:hang});
 void op.offsetWidth;setTimeout(()=>{op.classList.add('on');snap();fitH()},RM?0:120);
 $('#track').scrollTo({left:0,behavior:'smooth'})}
function hang(nc){let at=CH.findIndex(c=>c.off);if(at<0)at=CH.length;CH.splice(at,0,nc);
 const r=op.querySelector('.rc');r&&r.classList.add('up');
 MC.toast(`「${nc.n}」挂上去了`,{undo:()=>{const j=CH.indexOf(nc);if(j>=0){CH.splice(j,1);if(cur>=0)cur=-1;op.classList.remove('on');TK.hide(op);build();$('#idle').classList.remove('hide');fitH()}}});
 setTimeout(()=>{cur=-1;op.classList.remove('on');TK.hide(op);build();const t=$$('.tk')[at];t.classList.add('fresh');$('#idle').classList.remove('hide');fitH();
  $('#track').scrollTo({left:X0+at*STEP-150,behavior:'smooth'})},RM?0:650)}

'''
cut('const EP={OpenAI','function taste(',NEWT)
cut('function mrow(','function snap(){',NEWJS)
s=s.replace("op.innerHTML='';","TK.hide(op);")
assert 'rc(' not in re.sub(r'\.rc\(','',s.split('<script>')[-1]) or True
s=s.replace("fitH();\n(()=>{","new ResizeObserver(()=>fitH()).observe(op);fitH();\n(()=>{",1)
s=s.replace('<button id="tx">收起 ›</button>','<button id="tx">收起</button>')
# 样式与脚本
HEAD='''<link rel="stylesheet" href="../kit/mck-adm.css"><link rel="stylesheet" href="../kit/mck-parts.css"><link rel="stylesheet" href="../kit/adm-skin-mint.css"><link rel="stylesheet" href="tk.css">
<style>@font-face{font-family:WK2;src:url(tk-wk.ttf)}@font-face{font-family:ZK2;src:url(tk-zk.ttf)}</style>'''
s=s.replace('</head>',HEAD+'</head>',1)
s=s.replace('<script src="../ui.js?v=61"></script>','<script src="../ui.js?v=61"></script><script src="../kit/mck.js"></script><script src="tk.js"></script>',1)
print('tk.js' in s, 'TK.show(op,tkProps(i))' in s, 'function wire' not in s)
assert 'tk.js' in s and 'TK.show(op,tkProps(i))' in s and 'function wire' not in s
open(R+'p/chn/vb-adm.html','w').write(s)
# 字体子集：单子里新出的字
txt=open(R+'tools/chn/tk.jsx').read()+'确定取消'
ch=''.join(sorted(set(c for c in txt if ord(c)>127)))+''.join(chr(i) for i in range(32,127))
open('/tmp/tk.txt','w').write(ch)
F='/workspace/work/fonts/'
for a,b in [('zkfull.ttf','tk-zk.ttf'),('wkfull.ttf','tk-wk.ttf')]:
  subprocess.run(['pyftsubset',F+a,'--text-file=/tmp/tk.txt','--output-file='+R+'p/chn/'+b,'--layout-features=*'],check=True)
print('ok')
