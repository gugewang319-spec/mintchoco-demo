/* 11-14 真机修（v17 改）：淋酱跟内容一起滚走，像 X 的页头；模糊层滚动后才渐显；吸顶页头换成分层渐进模糊，左右铺满 */
(function(){
  const css=`.pfx-drz{position:fixed!important;left:0!important;right:0!important;top:0!important;width:100%!important;z-index:30!important;pointer-events:none}
.pfx-pb{position:fixed;left:0;right:0;top:0;height:30px;z-index:60;pointer-events:none;opacity:0}
.pfx-pb i{position:absolute;inset:0;display:block}
.pfx-on::before{display:none!important}
.pfx-drw{position:relative;height:0;margin:0 -16px;z-index:-1;pointer-events:none}
.pfx-drin{position:absolute!important;left:0!important;top:0!important;width:100%!important;z-index:auto!important}`;
  const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  function scrolls(el){for(let p=el.parentElement;p&&p!==document.body;p=p.parentElement){const o=getComputedStyle(p).overflowY;if(/(auto|scroll)/.test(o))return true}return false}
  function run(){document.querySelectorAll('#sc,.scroller,.vp,.app,.page,.menu').forEach(e=>{if(/(auto|scroll)/.test(getComputedStyle(e).overflowY)){e.style.overflowX='hidden';[...e.children].forEach(c=>{if(c.classList.contains('content')||c.offsetWidth>=e.clientWidth-2)c.style.overflowX='clip'});e.addEventListener('scroll',()=>{if(e.scrollLeft)e.scrollLeft=0},{passive:true})}});
    const d=document.querySelector('img.drizzle');
    const h=[...document.querySelectorAll('.lhead,.head')].find(e=>getComputedStyle(e).position==='sticky');
    if(d&&scrolls(d)){
      if(h){ /* 有吸顶页头：淋酱当背景钉在滚动层顶上，和内容一起被渐进模糊 */
        const w=document.createElement('div');w.className='pfx-drw';w.setAttribute('aria-hidden','true');
        h.parentNode.insertBefore(w,h.parentNode.firstChild);w.appendChild(d);d.classList.add('pfx-drin');
      }
    }
    if(!h)return;
    /* v18：像 X 一样，页头跟内容一起滚走；只在最顶上留一条很薄的渐进模糊，滚动后才出现 */
    h.style.position='relative';h.style.top='auto';h.classList.add('pfx-on');
    const sc=h.closest('#sc,.scroller,.vp,.app,.page,.menu')||document.scrollingElement;
    const pb=document.createElement('div');pb.className='pfx-pb pfx-strip';pb.setAttribute('aria-hidden','true');
    const L=[[6,'0%','45%'],[3,'25%','75%'],[1,'50%','100%']];
    pb.innerHTML=L.map(([b,s0,e])=>`<i style="-webkit-backdrop-filter:blur(${b}px);backdrop-filter:blur(${b}px);-webkit-mask-image:linear-gradient(180deg,#000 ${s0},transparent ${e});mask-image:linear-gradient(180deg,#000 ${s0},transparent ${e})"></i>`).join('')+
      `<i style="background:linear-gradient(180deg,rgba(232,246,240,.45),rgba(232,246,240,0))"></i>`;
    document.body.appendChild(pb);
    const tgt=sc===document.scrollingElement?window:sc;const f=()=>{pb.style.opacity=Math.min(1,(sc.scrollTop||0)/60)};tgt.addEventListener('scroll',f,{passive:true});f();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
})();
