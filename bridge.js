(()=>{const P=window.parent;if(P===window)return;
const TABS=['today','mem','list','role','set'];const MAP=window.__DEMO_MAP||[];
const go=(a,d)=>setTimeout(()=>P.postMessage({demo:a},'*'),d||0);
document.addEventListener('click',e=>{
 const tab=e.target.closest('.pnav .tab');
 if(tab){e.stopPropagation();e.preventDefault();const i=[...tab.parentNode.querySelectorAll('.tab')].indexOf(tab);if(!tab.classList.contains('on'))go('tab:'+TABS[i]);return}
 for(const [sel,a,keep,d] of MAP){const el=e.target.closest(sel);if(el){if(!keep){e.stopPropagation();e.preventDefault()}go(a,d);return}}
},true);})();
