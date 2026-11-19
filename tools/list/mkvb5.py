# 生成 p/list/vb5a/b/c.html：vb5_src.html + vb3 的页顶和底栏；A 奶油挤花 / B 插牌 / C 缎带
import os
R=os.path.dirname(os.path.abspath(__file__));P=os.path.join(R,'..','..','p','list')
s=open(os.path.join(P,'vb3.html')).read()
a=s.find('<header class="lhead">');hdr=s[a:s.find('</header>',a)+9]
a=s.find('<div class="navfade"');nav=s[a:s.find('</nav>',a)+6]
src=open(os.path.join(R,'vb5_src.html')).read().replace('%%HEADER%%',hdr).replace('%%NAV%%',nav)
for v in 'abc':open(os.path.join(P,f'vb5{v}.html'),'w').write(src.replace('%%VAR%%',v))
