# 生成 p/list/vb4.html：vb4_src.html + vb3 的页顶和底栏
import os
R=os.path.dirname(os.path.abspath(__file__));P=os.path.join(R,'..','..','p','list')
s=open(os.path.join(P,'vb3.html')).read()
a=s.find('<header class="lhead">');hdr=s[a:s.find('</header>',a)+9]
a=s.find('<div class="navfade"');nav=s[a:s.find('</nav>',a)+6]
src=open(os.path.join(R,'vb4_src.html')).read().replace('%%HEADER%%',hdr).replace('%%NAV%%',nav)
open(os.path.join(P,'vb4.html'),'w').write(src)
