# 样板间 v2 页面壳 + 字体子集（字取自 app.jsx）
import os,subprocess
R=os.path.dirname(os.path.abspath(__file__))+'/../../../'
H=R+'p/kit/';F='/workspace/work/fonts/'
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>样板间</title>
<style>@font-face{font-family:ZK;src:url(adm-zk.ttf)}@font-face{font-family:WK;src:url(adm-wk.ttf)}@font-face{font-family:Baloo;src:url(../snd/baloo.ttf);font-weight:100 900}@font-face{font-family:BalooX;src:url(../max/baloo800.ttf)}@font-face{font-family:Sofia;src:url(../max/sofia.ttf)}</style>
<link rel="stylesheet" href="mck-adm.css"><link rel="stylesheet" href="mck-parts.css"><link rel="stylesheet" href="adm-base.css"><link id="skin" rel="stylesheet" href="adm-skin-mint.css"></head>
<body><div id="root"></div><script src="../ui.js"></script><script src="mck.js"></script><script src="adm.js"></script></body></html>'''
open(H+'adm.html','w').write(html)
txt=open(R+'tools/kit/adm/app.jsx').read()+'确定取消再想想撤销存好了换成黑巧薄荷巧克力「」，。'
ch=''.join(sorted(set(c for c in txt if ord(c)>127)))+''.join(chr(i) for i in range(32,127))
open('/tmp/adm.txt','w').write(ch)
for s,d in [('zkfull.ttf','adm-zk.ttf'),('wkfull.ttf','adm-wk.ttf')]:
  subprocess.run(['pyftsubset',F+s,'--text-file=/tmp/adm.txt','--output-file='+H+d,'--layout-features=*'],check=True)
print('ok',len(ch))
