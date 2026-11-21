#!/usr/bin/env python3
"""交付前自查：python3 tools/check.py p/chn/vc.html [p/xxx/index.html ...] [--out 目录]
两个尺寸（358×622、412×715）各截首屏+滚到底，并查：
  1 脚本报错   2 横向溢出   3 文字被裁（没省略号却被截）   4 缺字（ZK/WK 子集里没有，会落系统字）
  5 点击区小于 32px   6 图片加载失败
需要本地服务：python3 -m http.server 8811（仓库根目录）。全过才给茶茶看。"""
import asyncio, os, sys, json
from playwright.async_api import async_playwright
from fontTools.ttLib import TTFont
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:]]
out = '/tmp/check'
if '--out' in args:
    i = args.index('--out'); out = args[i + 1]; del args[i:i + 2]
os.makedirs(out, exist_ok=True)
CMAP = {}
for fam, f in [('ZK', 'p/mc/zk.ttf'), ('WK', 'p/mc/wk.ttf')]:
    p = os.path.join(R, f)
    if os.path.exists(p): CMAP[fam] = set(TTFont(p).getBestCmap())
JS = r"""()=>{const r={clip:[],small:[],fam:{},img:[],ow:0};
 const de=document.documentElement;r.ow=Math.max(0,de.scrollWidth-innerWidth);
 for(const e of document.querySelectorAll('body *')){const cs=getComputedStyle(e);if(cs.display==='none'||cs.visibility==='hidden')continue;
  const t=[...e.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim();
  if(t){const f=cs.fontFamily.split(',')[0].replace(/["']/g,'').trim();(r.fam[f]=r.fam[f]||new Set());for(const c of t)r.fam[f].add(c);
   if(cs.overflow!=='visible'&&e.scrollWidth>e.clientWidth+1&&cs.textOverflow!=='ellipsis')r.clip.push(t.slice(0,20))}
  if(e.matches('button,a,[role=option],[tabindex="0"]')){const b=e.getBoundingClientRect(),pb=getComputedStyle(e,'::before'),ex=pb.content!=='none'&&pb.position==='absolute'?28:0;if(b.width&&b.height&&(b.width+ex<32||b.height+ex<24)&&e.offsetParent)r.small.push((e.getAttribute('aria-label')||e.textContent||e.className).trim().slice(0,16)+` ${b.width|0}×${b.height|0}`)}
  if(e.tagName==='IMG'&&e.complete&&!e.naturalWidth)r.img.push(e.getAttribute('src'))}
 for(const k in r.fam)r.fam[k]=[...r.fam[k]].join('');return r}"""
async def run(page_path):
    name = page_path.replace('/', '_').replace('.html', '')
    probs, shots = [], []
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--no-sandbox'])
        for w, h in [(358, 622), (412, 715)]:
            pg = await b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
            await pg.goto(f'http://localhost:8811/{page_path}'); await pg.wait_for_timeout(1800)
            r = await pg.evaluate(JS)
            f1 = f'{out}/{name}_{w}_top.png'; await pg.screenshot(path=f1)
            await pg.evaluate("(()=>{const a=document.getElementById('app')||document.scrollingElement;a.scrollTop=a.scrollHeight})()")
            await pg.wait_for_timeout(400)
            f2 = f'{out}/{name}_{w}_end.png'; await pg.screenshot(path=f2); shots += [f1, f2]
            tag = f'{w}px'
            for e in errs: probs.append(f'{tag} 报错：{e[:120]}')
            if r['ow'] > 0: probs.append(f'{tag} 横向溢出 {r["ow"]}px')
            for t in r['clip']: probs.append(f'{tag} 文字被裁：{t}')
            for t in r['small']: probs.append(f'{tag} 点击区太小：{t}')
            for t in r['img']: probs.append(f'{tag} 图片坏了：{t}')
            for fam, cs in r['fam'].items():
                if fam in CMAP:
                    miss = ''.join(c for c in cs if ord(c) > 0x20 and ord(c) not in CMAP[fam])
                    if miss: probs.append(f'{tag} {fam} 缺字（跑 tools/mkfonts.py）：{miss[:30]}')
            await pg.close()
        await b.close()
    ims = [Image.open(s) for s in shots]; H = max(i.height for i in ims)
    sheet = Image.new('RGB', (sum(i.width for i in ims) + 12 * (len(ims) - 1), H), 'white'); x = 0
    for i in ims: sheet.paste(i, (x, 0)); x += i.width + 12
    sheet.save(f'{out}/{name}_sheet.png')
    print(f'── {page_path}：' + ('全过 ✓' if not probs else f'{len(set(probs))} 个问题'))
    for q in sorted(set(probs)): print('  ·', q)
    print('  截图', f'{out}/{name}_sheet.png')
    return not probs
ok = all([asyncio.run(run(a)) for a in args])
sys.exit(0 if ok else 1)
