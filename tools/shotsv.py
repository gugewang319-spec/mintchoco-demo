import asyncio
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(358,622),(412,715)]:
      pg=await b.new_page(viewport={'width':w,'height':h})
      errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto('http://localhost:8811/p/chn/index.html'); await pg.wait_for_timeout(1300)
      await pg.click('.tk >> nth=0',force=True,position={'x':26,'y':60}); await pg.wait_for_timeout(1400)
      await pg.fill('#open .nmI','新主渠道'); await pg.wait_for_timeout(200)
      print('idle',await pg.eval_on_selector('#open .sv','e=>e.className'))
      await pg.eval_on_selector('#open .sv','e=>e.scrollIntoView({block:"center"})'); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f'/workspace/work/v1_{w}.png')
      await pg.eval_on_selector('#open .sv','e=>e.click()'); await pg.wait_for_timeout(700)
      print(await pg.eval_on_selector('.tk .nm','e=>e.textContent'))
      await pg.screenshot(path=f'/workspace/work/v2_{w}.png')
      await pg.fill('#open .hostI','x.example'); await pg.eval_on_selector('#open .lift','e=>e.click()'); await pg.wait_for_timeout(600)
      await pg.screenshot(path=f'/workspace/work/v3_{w}.png')
      await pg.eval_on_selector('.mc-dlg .ok','e=>e.click()'); await pg.wait_for_timeout(600)
      await pg.eval_on_selector('.nt','e=>e.click()'); await pg.wait_for_timeout(1500)
      await pg.eval_on_selector('#open .sv','e=>e.scrollIntoView({block:"center"})'); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f'/workspace/work/v4_{w}.png')
      print(w,errs)
    await b.close()
asyncio.run(main())
