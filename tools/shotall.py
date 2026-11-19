import asyncio
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(358,622),(412,715)]:
      pg=await b.new_page(viewport={'width':w,'height':h});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto('http://localhost:8811/p/chn/index.html'); await pg.wait_for_timeout(1300)
      await pg.eval_on_selector('#fsb','e=>e.click()'); await pg.wait_for_timeout(500)
      await pg.fill('#fsI','可可'); await pg.wait_for_timeout(900)
      await pg.screenshot(path=f'a1_{w}.png')
      await pg.fill('#fsI','zzz'); await pg.wait_for_timeout(500); await pg.screenshot(path=f'a2_{w}.png')
      await pg.eval_on_selector('#fsx','e=>e.click()'); await pg.wait_for_timeout(400)
      await pg.click('.tk >> nth=0',force=True,position={'x':26,'y':60}); await pg.wait_for_timeout(1400)
      await pg.eval_on_selector('#open .mo','e=>e.click()'); await pg.wait_for_timeout(900)
      await pg.fill('#open .msI','claude'); await pg.wait_for_timeout(900)
      await pg.eval_on_selector('#open .msI','e=>e.scrollIntoView({block:"start"})'); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f'a3_{w}.png')
      await pg.eval_on_selector('#open .rip','e=>e.click()'); await pg.wait_for_timeout(600); await pg.screenshot(path=f'a4_{w}.png')
      await pg.eval_on_selector('.mc-dlg .ok','e=>e.click()'); await pg.wait_for_timeout(900); await pg.screenshot(path=f'a5_{w}.png')
      print(w,errs,flush=True); await pg.close()
asyncio.run(main())
