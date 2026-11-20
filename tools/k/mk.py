# 纯组件页：生成 p/k/<页>.html，字体子集取自 tools/k/*.jsx
import os,subprocess,sys,glob
R=os.path.dirname(os.path.abspath(__file__))+'/../../';K=R+'p/k/';F='/workspace/work/fonts/'
TPL='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{t}</title>
<style>@font-face{{font-family:WK;src:url(k-wk.ttf)}}</style>
<link rel="stylesheet" href="../kit/mck-adm.css"><link rel="stylesheet" href="k-base.css"></head>
<body><div id="root"></div><script src="../ui.js"></script><script src="../kit/mck.js"></script><script src="{p}.js"></script></body></html>'''
for p,t in [('chn','渠道'),('set','设置'),('snd','声音')]:
  open(K+p+'.html','w').write(TPL.format(t=t,p=p))
txt=''.join(open(f).read() for f in glob.glob(R+'tools/k/*.js*'))+'确定取消撤销「」，。'
ch=''.join(sorted(set(c for c in txt if ord(c)>127)))+''.join(chr(i) for i in range(32,127))
open('/tmp/k.txt','w').write(ch)
for a,b in [('zkfull.ttf','k-zk.ttf'),('wkfull.ttf','k-wk.ttf')]:
  subprocess.run(['pyftsubset',F+a,'--text-file=/tmp/k.txt','--output-file='+K+b,'--layout-features=*'],check=True)
print('ok',len(ch))
