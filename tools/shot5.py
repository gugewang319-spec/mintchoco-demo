import asyncio,sys
from playwright.async_api import async_playwright
q=sys.argv[1] if len(sys.argv)>1 else ''
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(358,622),(412,715)]:
      pg=await b.new_page(viewport={'width':w,'height':h})
      errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto('file:///workspace/work/mc/p/role/index.html'+q); await pg.wait_for_timeout(1500)
      await pg.screenshot(path=f'/workspace/work/s7_{w}_0.png')
      await pg.evaluate("document.querySelector('#sc').scrollTop=160"); await pg.wait_for_timeout(300)
      y0=await pg.evaluate("document.querySelector('#c2').getBoundingClientRect().top")
      await pg.click('#c2'); await pg.wait_for_timeout(500)
      y1=await pg.evaluate("document.querySelector('#c2').getBoundingClientRect().top")
      await pg.screenshot(path=f'/workspace/work/s7_{w}_1.png')
      print(w,errs,round(y0),round(y1))
    await b.close()
asyncio.run(main())
