/* 11-14 真机修：淋酱固定在顶上不随滚动走；吸顶页头换成分层渐进模糊，左右铺满 */
(function(){
  const css=`.pfx-drz{position:fixed!important;left:0!important;right:0!important;top:0!important;width:100%!important;z-index:30!important;pointer-events:none}
.pfx-pb{position:absolute;left:-40px;right:-40px;top:0;bottom:-40px;z-index:-1;pointer-events:none}
.pfx-pb i{position:absolute;inset:0;display:block}
.pfx-on::before{display:none!important}
.pfx-drz.under{z-index:1!important}`;
  const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  function scrolls(el){for(let p=el.parentElement;p&&p!==document.body;p=p.parentElement){const o=getComputedStyle(p).overflowY;if(/(auto|scroll)/.test(o))return true}return false}
  function run(){document.querySelectorAll('#sc,.scroller,.vp,.app,.page,.menu').forEach(e=>{if(/(auto|scroll)/.test(getComputedStyle(e).overflowY))e.style.overflowX='hidden'});
    const d=document.querySelector('img.drizzle');
    if(d&&scrolls(d)){d.classList.add('pfx-drz');document.body.appendChild(d)}
    const h=[...document.querySelectorAll('.lhead,.head')].find(e=>getComputedStyle(e).position==='sticky');
    if(!h)return;
    h.classList.add('pfx-on');if(d&&d.classList.contains('pfx-drz'))d.classList.add('under');
    const pb=document.createElement('div');pb.className='pfx-pb';pb.setAttribute('aria-hidden','true');
    // 由上到下：模糊逐层减弱，每层的遮罩终点依次下移
    const L=[[16,'40%','58%'],[8,'55%','72%'],[4,'68%','86%'],[2,'80%','100%']];
    pb.innerHTML=L.map(([b,s,e])=>`<i style="-webkit-backdrop-filter:blur(${b}px);backdrop-filter:blur(${b}px);-webkit-mask-image:linear-gradient(180deg,#000 ${s},transparent ${e});mask-image:linear-gradient(180deg,#000 ${s},transparent ${e})"></i>`).join('')+
      `<i style="background:linear-gradient(180deg,rgba(232,246,240,.9),rgba(232,246,240,.62) 55%,rgba(232,246,240,0) 100%)"></i>`;
    h.insertBefore(pb,h.firstChild);
    if(getComputedStyle(h).isolation!=='isolate')h.style.isolation='isolate';
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
})();
