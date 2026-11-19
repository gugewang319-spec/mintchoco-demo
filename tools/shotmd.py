import asyncio
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(358,622),(412,715)]:
      pg=await b.new_page(viewport={'width':w,'height':h});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto('http://localhost:8811/p/chn/index.html'); await pg.wait_for_timeout(1300)
      await pg.click('.tk >> nth=0',force=True,position={'x':26,'y':60}); await pg.wait_for_timeout(1400)
      await pg.eval_on_selector('#open .mo','e=>e.click()'); await pg.wait_for_timeout(900)
      await pg.eval_on_selector('#open .mw .mh','e=>e.click()'); await pg.wait_for_timeout(500)
      await pg.eval_on_selector('#open .mw .md[data-k="o"]','e=>e.click()'); await pg.wait_for_timeout(400)
      await pg.eval_on_selector('#open .mw.ex .pk.on button:last-child','e=>e.click()'); await pg.wait_for_timeout(500)
      await pg.eval_on_selector('#open .mw','e=>e.scrollIntoView({block:"start"})'); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f'b1_{w}.png')
      await pg.eval_on_selector('#open .mw:nth-of-type(2) .mh','e=>e.click()'); await pg.wait_for_timeout(400)
      await pg.eval_on_selector('#open .mw.ex .mdel','e=>e.click()'); await pg.wait_for_timeout(500)
      await pg.eval_on_selector('#open .pullb','e=>e.click()'); await pg.wait_for_timeout(400)
      await pg.fill('#open .puI','gpt'); await pg.wait_for_timeout(300)
      await pg.eval_on_selector_all('#open .pul .ck:not(.has)','es=>{es[0].click()}'); await pg.wait_for_timeout(200)
      await pg.eval_on_selector('#open .pull','e=>e.scrollIntoView({block:"center"})'); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f'b2_{w}.png')
      await pg.eval_on_selector('#open .pug','e=>e.click()'); await pg.wait_for_timeout(500)
      await pg.eval_on_selector('#open .sv','e=>e.scrollIntoView({block:"end"})'); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f'b3_{w}.png')
      await pg.eval_on_selector('#open .sv','e=>e.click()'); await pg.wait_for_timeout(900)
      await pg.screenshot(path=f'b4_{w}.png')
      print(w,errs,await pg.eval_on_selector('.mo .sec b','e=>e.textContent'),flush=True); await pg.close()
asyncio.run(main())
