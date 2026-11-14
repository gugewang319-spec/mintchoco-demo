/* 11-14 真机修（v17 改）：淋酱跟内容一起滚走，像 X 的页头；模糊层滚动后才渐显；吸顶页头换成分层渐进模糊，左右铺满 */
(function(){
  const css=`.pfx-drz{position:fixed!important;left:0!important;right:0!important;top:0!important;width:100%!important;z-index:30!important;pointer-events:none}
.pfx-pb{position:fixed;left:0;right:0;top:0;height:30px;z-index:60;pointer-events:none;opacity:0}
.pfx-pb i{position:absolute;inset:0;display:block}
.pfx-on::before{display:none!important}
.pfx-hb{position:absolute;left:-40px;right:-40px;top:-60px;bottom:-34px;z-index:-1;pointer-events:none;opacity:0;transition:opacity .2s}
.pfx-hb i{position:absolute;inset:0;display:block}
/* emil-design-eng：按下要有回应（WAAPI 改独立的 scale 属性，不碰原有 transition 和 JS 写的 transform）；底栏高亮 240ms 强 ease-out */
:root{--ease-out:cubic-bezier(.23,1,.32,1)}
.pnav .pill{transition:transform 240ms var(--ease-out),width 240ms var(--ease-out)!important}
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
    h.style.position='sticky';h.style.top='0';h.classList.add('pfx-on');
    const sc=h.closest('#sc,.scroller,.vp,.app,.page,.menu')||document.scrollingElement;
    const pb=document.createElement('div');pb.className='pfx-pb pfx-strip';pb.setAttribute('aria-hidden','true');
    const L=[[6,'0%','45%'],[3,'25%','75%'],[1,'50%','100%']];
    pb.innerHTML=L.map(([b,s0,e])=>`<i style="-webkit-backdrop-filter:blur(${b}px);backdrop-filter:blur(${b}px);-webkit-mask-image:linear-gradient(180deg,#000 ${s0},transparent ${e});mask-image:linear-gradient(180deg,#000 ${s0},transparent ${e})"></i>`).join('')+
      `<i style="background:linear-gradient(180deg,rgba(232,246,240,.45),rgba(232,246,240,0))"></i>`;
    document.body.appendChild(pb);
    const tgt=sc===document.scrollingElement?window:sc;const f=()=>{pb.style.opacity=Math.min(1,(sc.scrollTop||0)/60)};tgt.addEventListener('scroll',f,{passive:true});f();
    /* v19：像 X，往下划页头滚走；往回划一点，页头带着渐进模糊滑回来 */
    const hb=document.createElement('div');hb.className='pfx-hb';hb.setAttribute('aria-hidden','true');
    const HL=[[9,'45%','70%'],[5,'60%','85%'],[2,'75%','100%']];
    hb.innerHTML=HL.map(([b,s0,e])=>`<i style="-webkit-backdrop-filter:blur(${b}px);backdrop-filter:blur(${b}px);-webkit-mask-image:linear-gradient(180deg,#000 ${s0},transparent ${e});mask-image:linear-gradient(180deg,#000 ${s0},transparent ${e})"></i>`).join('')+
      `<i style="background:linear-gradient(180deg,rgba(232,246,240,.6),rgba(232,246,240,.35) 60%,rgba(232,246,240,0))"></i>`;
    h.insertBefore(hb,h.firstChild);if(getComputedStyle(h).isolation!=='isolate')h.style.isolation='isolate';
    let hh=h.offsetTop+h.offsetHeight,last=sc.scrollTop||0,rev=false,ty=0;
    const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
    const put=(v,anim)=>{h.style.transition=anim&&!RM?'transform .26s cubic-bezier(.2,.8,.2,1)':'none';ty=v;h.style.transform=v?`translate3d(0,${v}px,0)`:''};
    if(window.ResizeObserver)new ResizeObserver(()=>{hh=h.offsetTop+h.offsetHeight}).observe(h);
    const g=()=>{const st=sc.scrollTop||0,dy=st-last;last=st;
      if(st<=0){rev=false;hb.style.opacity=0;put(0,false);return}
      if(rev){if(dy>3){rev=false;hb.style.opacity=0;put(-Math.min(st,hh+40),true)}return}
      if(dy<-3&&st>hh){rev=true;hb.style.opacity=1;put(-(hh+40),false);requestAnimationFrame(()=>put(0,true));return}
      put(-Math.min(st,hh+40),false)};
    tgt.addEventListener('scroll',g,{passive:true});g();
  }
  /* 底栏高亮跟着当前标签走（有的页没写定位脚本） */
  function pill(){const pl=document.querySelector('.pnav .pill'),on=document.querySelector('.pnav .tab.on');if(pl&&on&&on.offsetWidth){pl.style.width=on.offsetWidth+'px';pl.style.transform=`translateX(${on.offsetLeft-5}px)`}}
  addEventListener('load',pill);addEventListener('resize',pill);if(window.ResizeObserver){const n=document.querySelector('.pnav');n&&new ResizeObserver(pill).observe(n)}
  /* 按下 .97、松开回弹；松开比按下快 */
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches){const SEL='button,.tab,.lt,.dk,[role=button]',E='cubic-bezier(.23,1,.32,1)';let cur=null;
    addEventListener('pointerdown',e=>{const b=e.target.closest&&e.target.closest(SEL);if(!b||b.disabled)return;cur=b;b.animate({scale:['1','.97']},{duration:160,easing:E,fill:'forwards'})},{passive:true});
    const up=()=>{if(!cur)return;const b=cur;cur=null;b.getAnimations().filter(a=>a.effect&&a.effect.getKeyframes().some(k=>'scale' in k)).forEach(a=>a.cancel());b.animate({scale:['.97','1']},{duration:140,easing:E})};
    addEventListener('pointerup',up,{passive:true});addEventListener('pointercancel',up,{passive:true})}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
})();
