import asyncio,sys
from playwright.async_api import async_playwright
async def main():
  svg=open('watch_s.svg').read()
  html=f'<html><head><style>@font-face{{font-family:Sofia;src:url(script.ttf)}}body{{margin:0;background:transparent}}</style></head><body>{svg}</body></html>'
  open('r.html','w').write(html)
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page(viewport={'width':816,'height':1176})
    await pg.goto('file:///workspace/work/watch/r.html');await pg.wait_for_timeout(600)
    await pg.locator('svg').screenshot(path='watch_s.png',omit_background=True)
    await pg.set_viewport_size({'width':816,'height':1176})
    await b.close()
asyncio.run(main())
