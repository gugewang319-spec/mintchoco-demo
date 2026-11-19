import os,sys
R=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../..'))
OUT=sys.argv[1] if len(sys.argv)>1 else '.'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in [(358,740),(412,860)]:
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=1.5);e=[];pg.on('pageerror',lambda x:e.append(str(x)))
        pg.goto('file://'+R+'/p/list/vb10.html');pg.wait_for_timeout(900)
        H=pg.evaluate("document.querySelector('#sc').scrollHeight")
        for k,y in enumerate([0,700,1400,H]):
            pg.evaluate(f"document.querySelector('#sc').scrollTop={y}");pg.wait_for_timeout(400)
            pg.screenshot(path=f'{OUT}/v10_{w}_{k}.png')
        print(w,H,e)
    b.close()
