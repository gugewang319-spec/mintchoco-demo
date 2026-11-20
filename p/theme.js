/* Mint Choco 主题：按页把装字的块穿成甜点糖片（实色面 + 白描边 + 角落贴纸）（只加 class 和两个装饰子元素，不改结构）。 */
(function(){
  const pg=(location.pathname.match(/\/p\/([^/]+)\//)||[])[1]||'';
  const KINDS=['latte','soda','cocoa','boba'];
  // 每页：[选择器, 选项]；o.k 指定饮品，o.pad 加统一内边距，o.r 右收角
  const MAP={
    set:[['.cmp',{k:'latte',pad:1}],['.ingr button',{mini:1}]],
    mem:[['article.mi',{pad:1}],['.sec h2',{lb:1}]],
    use:[['#cl>li .tx',{pad:1}],['p.cs2',{k:'soda',pad:1}]],
    hlt:[['.jp',{pad:1}],['section.tray',{k:'soda'}]],
    role:[['section.sheet',{k:'latte'}]],
    chn:[['.kpi',{k:'cocoa',pad:1}]],
    snd:[['.info',{k:'latte',pad:1}],['.say',{k:'soda',pad:1}],['#tracks',{k:'soda',pad:1}],['.chs',{k:'cocoa',pad:1}]],
    srch:[['button.hit',{pad:1,nowm:1}]],
    msrch:[['button.hit',{pad:1,nowm:1,nost:1}]],
    conn:[['#card',{k:'latte'}]],
  };
  const FILL={latte:'var(--mc-f2)',soda:'var(--mc-f1)',cocoa:'var(--mc-f2)',boba:'var(--mc-f3)'};
  const STK=['leaf','heart','cherry'],WM=['mint choco','sweet notes','fresh mint','choco & cream'];let cnt=0;
  function dress(el,k,o){
    if(el.dataset.mcp)return;el.dataset.mcp=1;
    const S=el.style,imp=(a,v)=>S.setProperty(a,v,'important');
    imp('-webkit-backdrop-filter','none');imp('backdrop-filter','none');
    if(o.mini){el.classList.add('mc-mini');return}
    const n=cnt++;el.classList.add('mc-pl','mc-'+STK[n%3]);if(o.pad)el.classList.add('mc-pad');
    if(getComputedStyle(el).position==='static')S.position='relative';
    // 页面里有带 id / !important 的旧皮，用行内 important 盖住（只盖皮，不碰尺寸位置）
    imp('background',FILL[k]);imp('border','2px solid #fff');
    imp('box-shadow','0 0 0 1.2px rgba(138,92,70,.55),0 6px 14px -8px rgba(74,48,39,.35)');
    imp('border-radius','16px');
    for(const c of el.children){if(getComputedStyle(c).position==='static')c.style.position='relative'}
    if(!o.nost){const st=document.createElement('i');st.className='mc-st';st.setAttribute('aria-hidden','true');el.prepend(st)}
    if(o.pad&&!o.nowm){const w=document.createElement('i');w.className='mc-wm';w.setAttribute('aria-hidden','true');w.textContent=WM[n%4];el.prepend(w)}
  }
  function run(){document.documentElement.classList.add('mc-'+pg);
    const list=MAP[pg];if(!list)return;
    list.forEach(([sel,o])=>{
      document.querySelectorAll(sel).forEach((el,i)=>{
        if(o.lb){el.classList.add('mc-lb');return}
        dress(el,o.k||KINDS[i%4],o);
      });
    });
  }
  const css=document.createElement('link');css.rel='stylesheet';css.href=(document.currentScript&&document.currentScript.src||'').replace(/theme\.js.*$/,'theme.css?v=2');document.head.appendChild(css);
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
  // 列表是脚本后渲染的：再穿几次，并盯着 DOM 变化
  let n=0;const iv=setInterval(()=>{run();if(++n>8)clearInterval(iv)},250);
  new MutationObserver(()=>{clearTimeout(window.__mcT);window.__mcT=setTimeout(run,60)}).observe(document.documentElement,{childList:true,subtree:true});
})();
