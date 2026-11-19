import asyncio,sys
from playwright.async_api import async_playwright
url=sys.argv[1]; tag=sys.argv[2]; js=sys.argv[3] if len(sys.argv)>3 else ''
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(358,622),(412,715)]:
      pg=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=2)
      errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto('http://localhost:8811/'+url); await pg.wait_for_timeout(1500)
      await pg.screenshot(path=f'/workspace/work/{tag}_{w}_a.png')
      if js:
        await pg.evaluate(js); await pg.wait_for_timeout(900)
        await pg.screenshot(path=f'/workspace/work/{tag}_{w}_b.png')
      print(w,errs)
    await b.close()
asyncio.run(main())
