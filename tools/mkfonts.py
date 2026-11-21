#!/usr/bin/env python3
"""重切共用字体子集 p/mc/zk.ttf 与 p/mc/wk.ttf。
扫描：p/mc/ 下所有 html/js，以及所有引用了 mc/mc.css 的页面。页面加了新字就跑一次。
用法：python3 tools/mkfonts.py [WK 源字体路径]
  ZK 源：p/list/zk.ttf（仓库里有全量）
  WK 源：霞鹜文楷 Lite Medium（13MB，不进仓库），默认 /workspace/work/LXGWWenKaiLite-Medium.ttf
"""
import glob, os, re, subprocess, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WK = sys.argv[1] if len(sys.argv) > 1 else '/workspace/work/LXGWWenKaiLite-Medium.ttf'
ZK = os.path.join(R, 'p/list/zk.ttf')
files = glob.glob(os.path.join(R, 'p/mc/*.html')) + glob.glob(os.path.join(R, 'p/mc/*.js'))
for f in glob.glob(os.path.join(R, 'p/**/*.html'), recursive=True):
    if 'mc/mc.css' in open(f, encoding='utf-8').read():
        files.append(f)
txt = ''.join(open(f, encoding='utf-8').read() for f in set(files))
base = ''.join(chr(c) for c in range(0x20, 0x7f)) + '，。、；：？！…—·「」『』（）《》“”‘’％＋－×÷＝～￥①②③④⑤⑥⑦⑧⑨⑩›‹←→↑↓'
chars = sorted(set(c for c in txt if ord(c) > 0x7f) | set(base))
open('/tmp/mc_chars.txt', 'w', encoding='utf-8').write(''.join(chars))
for src, out in [(ZK, 'p/mc/zk.ttf'), (WK, 'p/mc/wk.ttf')]:
    subprocess.run(['pyftsubset', src, '--text-file=/tmp/mc_chars.txt', '--output-file=' + os.path.join(R, out),
                    '--layout-features=*', '--no-hinting'], check=True)
    print(out, os.path.getsize(os.path.join(R, out)) // 1024, 'KB')
print(len(chars), 'chars from', len(set(files)), 'files')
