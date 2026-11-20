# 纯组件页：生成 p/k/<页>.html，字体子集取自 tools/k/*.jsx
import os,subprocess,sys,glob
R=os.path.dirname(os.path.abspath(__file__))+'/../../';K=R+'p/k/';F='/workspace/work/fonts/'
TPL='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{t}</title>
<style>@font-face{{font-family:ZK;src:url(k-zk.ttf)}}@font-face{{font-family:WK;src:url(k-wk.ttf)}}@font-face{{font-family:Baloo;src:url(../snd/baloo.ttf);font-weight:100 900}}@font-face{{font-family:BalooX;src:url(../max/baloo800.ttf)}}@font-face{{font-family:Sofia;src:url(../max/sofia.ttf)}}</style>
<link rel="stylesheet" href="../kit/mck-adm.css"><link rel="stylesheet" href="../kit/mck-parts.css"><link rel="stylesheet" href="../kit/adm-skin-mint.css"><link rel="stylesheet" href="k.css"></head>
<body><div id="root"></div><script src="../ui.js"></script><script src="../kit/mck.js"></script><script src="{p}.js"></script></body></html>'''
for p,t in [('chn','渠道')]:
  open(K+p+'.html','w').write(TPL.format(t=t,p=p))
txt=''.join(open(f).read() for f in glob.glob(R+'tools/k/*.js*'))+'确定取消撤销「」，。'
ch=''.join(sorted(set(c for c in txt if ord(c)>127)))+''.join(chr(i) for i in range(32,127))
open('/tmp/k.txt','w').write(ch)
for a,b in [('zkfull.ttf','k-zk.ttf'),('wkfull.ttf','k-wk.ttf')]:
  subprocess.run(['pyftsubset',F+a,'--text-file=/tmp/k.txt','--output-file='+K+b,'--layout-features=*'],check=True)
print('ok',len(ch))
