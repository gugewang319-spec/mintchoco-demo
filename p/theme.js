/* Mint Choco 主题：按页把装字的块穿成饮品卡（只加 class 和两个装饰子元素，不改结构）。 */
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
    srch:[['button.hit',{pad:1}]],
    msrch:[['button.hit',{pad:1}]],
    conn:[['#card',{k:'latte'}]],
  };
  const TOP={latte:0,soda:0,cocoa:2,boba:4};
  function dress(el,k,o){
    if(el.classList.contains('mc-dk'))return;
    el.classList.add('mc-dk','mc-'+k);if(o.pad)el.classList.add('mc-pad');if(o.r)el.classList.add('mc-r');if(o.mini)el.classList.add('mc-mini');
    if(getComputedStyle(el).position==='static')el.style.position='relative';
    // 页面里有带 id / !important 的旧皮，用行内 important 盖住（只盖皮，不碰尺寸位置）
    const S=el.style,imp=(k,v)=>S.setProperty(k,v,'important');
    imp('background','linear-gradient(160deg,rgba(255,255,255,.74),rgba(236,248,242,.56))');
    imp('border','1px solid rgba(255,255,255,.95)');
    imp('box-shadow','inset 0 1px 0 #fff,0 0 0 .6px rgba(138,92,70,.22),0 12px 24px -18px rgba(74,48,39,.55)');
    imp('backdrop-filter','none');imp('-webkit-backdrop-filter','none');imp('overflow','hidden');
    imp('border-radius',o.mini?'14px 14px 14px 5px':(o.r?'20px 20px 7px 20px':'20px 20px 20px 7px'));
    for(const c of el.children){if(getComputedStyle(c).position==='static')c.style.position='relative'}
    const l=document.createElement('i');l.className='mc-liq';l.setAttribute('aria-hidden','true');
    const t=document.createElement('i');t.className='mc-tp';t.setAttribute('aria-hidden','true');
    for(let i=0;i<TOP[k];i++)t.appendChild(document.createElement('i'));
    el.prepend(t);el.prepend(l);
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
  const css=document.createElement('link');css.rel='stylesheet';css.href=(document.currentScript&&document.currentScript.src||'').replace(/theme\.js.*$/,'theme.css');document.head.appendChild(css);
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
  // 列表是脚本后渲染的：再穿几次，并盯着 DOM 变化
  let n=0;const iv=setInterval(()=>{run();if(++n>8)clearInterval(iv)},250);
  new MutationObserver(()=>{clearTimeout(window.__mcT);window.__mcT=setTimeout(run,60)}).observe(document.documentElement,{childList:true,subtree:true});
})();
