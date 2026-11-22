/* 全站反馈：出餐铃（toast）+ 警告弹窗（confirm）。MC.toast(文字,{undo}) / MC.confirm({title,body,ok,cancel}) -> Promise<bool> */
(function(){
const css=`
.mc-bell{position:fixed;left:50%;top:calc(14px + env(safe-area-inset-top,0px));z-index:90;display:flex;align-items:center;gap:10px;max-width:calc(100% - 40px);min-height:46px;padding:6px 8px 6px 14px;border-radius:23px;
background:rgba(252,250,244,.62);backdrop-filter:blur(18px) saturate(120%);-webkit-backdrop-filter:blur(18px) saturate(120%);border:1px solid rgba(255,255,255,.85);box-shadow:inset 0 1px 0 rgba(255,255,255,.95),0 10px 24px -14px rgba(74,48,39,.5);
width:max-content;transform:translate(-50%,-140%);transition:transform .42s cubic-bezier(.3,1.35,.5,1);font:14px/1.3 WK,ZK,sans-serif;color:#4a3027}
.mc-bell.on{transform:translate(-50%,0)}
.mc-bell svg{flex:none;width:24px;height:24px;transform-origin:50% 15%}
.mc-bell.on svg{animation:mcding .9s cubic-bezier(.3,.6,.4,1) .25s}
@keyframes mcding{20%{transform:rotate(14deg)}45%{transform:rotate(-10deg)}70%{transform:rotate(5deg)}100%{transform:none}}
.mc-bell .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mc-bell button{flex:none;min-height:34px;padding:0 12px;border:0;background:none;font:13.5px/1 WK,ZK,sans-serif;color:#8a5c46;text-decoration:underline dashed 1.1px;text-underline-offset:4px;cursor:pointer}
.mc-mask{position:fixed;inset:0;z-index:95;background:rgba(74,48,39,.22);opacity:0;transition:opacity .25s;display:grid;place-items:center;padding:24px}
.mc-mask.on{opacity:1}
.mc-dlg{position:relative;width:min(100%,316px);padding:26px 22px 18px;border-radius:24px;text-align:center;color:#4a3027;
background:rgba(252,250,244,.8);backdrop-filter:blur(18px) saturate(120%);-webkit-backdrop-filter:blur(18px) saturate(120%);border:1px solid rgba(255,255,255,.9);box-shadow:inset 0 1px 0 rgba(255,255,255,.95),0 18px 36px -18px rgba(74,48,39,.55);
transform:scale(.86);transition:transform .38s cubic-bezier(.3,1.5,.5,1)}
.mc-mask.on .mc-dlg{transform:none}
.mc-dlg .ic{width:44px;height:44px;margin:0 auto 10px}
.mc-dlg h4{font:21px/1.2 ZK,WK,sans-serif;font-weight:400;color:#5b3a2c;letter-spacing:.04em}
.mc-dlg p{margin:10px 0 0;font:14px/1.7 WK,ZK,sans-serif;color:#6f5446}
.mc-dlg p b{font-weight:400;color:#b8573c;background:linear-gradient(transparent 62%,rgba(194,102,74,.22) 62% 92%,transparent 92%)}
/*V67 茶茶：巧克力实心块和下划线字不搭 → 两枚圆章（同渠道页「存」章）：左薄荷「留」= 取消，右莓果 = 确定*/
.mc-dlg .acts{display:flex;justify-content:center;gap:34px;margin:18px 0 2px}
.mc-dlg .acts button{position:relative;width:78px;height:78px;border:0;background:none;padding:0;cursor:pointer;-webkit-tap-highlight-color:transparent}
.mc-dlg .no{color:#2f7e68}.mc-dlg .ok{color:#b8573c}
.mc-dlg .acts .sl{position:absolute;inset:0;display:block;transition:translate .25s cubic-bezier(.3,1.3,.5,1),scale .25s}
.mc-dlg .no .sl{rotate:8deg}.mc-dlg .ok .sl{rotate:-10deg}
.mc-dlg .acts svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.mc-dlg .acts b{position:absolute;inset:0;display:grid;place-items:center;font:700 25px/1 ZK,WK,sans-serif;color:currentColor;padding-bottom:2px}
.mc-dlg .acts button::after{content:'';position:absolute;left:16px;right:16px;bottom:-7px;height:7px;border-radius:50%;background:radial-gradient(closest-side,rgba(74,48,39,.18),transparent)}
.mc-dlg .acts .sl{translate:0 -4px}
.mc-dlg .acts button:active .sl{translate:0 0;scale:.94}
.mc-dlg .acts button.inked .sl{translate:0 0;mix-blend-mode:multiply;animation:mcink .3s cubic-bezier(.2,1.2,.4,1) both}
@keyframes mcink{0%{scale:1.25;opacity:.5}60%{scale:.94}100%{scale:1;opacity:.85}}
@media (prefers-reduced-motion:reduce){.mc-bell,.mc-dlg,.mc-mask{transition:none}.mc-bell.on svg{animation:none}.mc-dlg .acts .sl{transition:none;animation:none}}
`;
const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
const BELL='<svg viewBox="0 0 24 24" fill="none" stroke="#5b3a2c" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.2v1.6"/><circle cx="12" cy="2.6" r="1" fill="#5b3a2c" stroke="none"/><path d="M5 17.5c0-6 3-9.2 7-9.2s7 3.2 7 9.2Z" fill="#a6d9c4"/><path d="M3.5 17.5h17" stroke-width="1.8"/><path d="M8.5 12.3c.4-1.2 1.1-2 2-2.4" stroke="#fbf6ea" stroke-width="1.3"/></svg>';
const WARN='<svg class="ic" viewBox="0 0 44 44" fill="none" stroke="#8a5c46" stroke-width="1.4" stroke-linejoin="round"><path d="M22 6 39 36H5Z" fill="#f6d7cb"/><path d="M22 17v9" stroke="#b8573c" stroke-width="2.6" stroke-linecap="round"/><circle cx="22" cy="31" r="1.7" fill="#b8573c" stroke="none"/></svg>';
let bell,tm;
function toast(text,o={}){
 if(!bell){bell=document.createElement('div');bell.className='mc-bell';bell.setAttribute('role','status');document.body.appendChild(bell)}
 clearTimeout(tm);bell.classList.remove('on');void bell.offsetWidth;
 bell.innerHTML=BELL+'<span class="t"></span>'+(o.undo?'<button>撤销</button>':'');bell.querySelector('.t').textContent=text;
 if(o.undo)bell.querySelector('button').onclick=()=>{clearTimeout(tm);bell.classList.remove('on');o.undo()};
 requestAnimationFrame(()=>bell.classList.add('on'));tm=setTimeout(()=>bell.classList.remove('on'),o.ms||3200)}
let sid=0;
function seal(w,en,cls,label){const id='mcs'+(++sid);return `<button class="${cls}" aria-label="${label}"><i class="sl"><svg viewBox="0 0 100 100" aria-hidden="true"><defs><path id="${id}" d="M50 50 m-37 0 a37 37 0 1 1 74 0 a37 37 0 1 1 -74 0"/></defs><circle cx="50" cy="50" r="47" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="50" cy="50" r="43" fill="none" stroke="currentColor" stroke-width=".9"/><circle cx="50" cy="50" r="27" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="1.2 2.6"/><text font-family="Baloo,sans-serif" font-size="8.2" font-weight="700" fill="currentColor"><textPath href="#${id}" textLength="226" lengthAdjust="spacing">MINT CHOCO ◆ ${en} ◆ TEA ATELIER ◆</textPath></text></svg><b>${w}</b></i></button>`}
function confirm(o){return new Promise(res=>{
 const m=document.createElement('div');m.className='mc-mask';
 const okT=o.ok||'确定',noT=o.cancel||'再想想';
 m.innerHTML=`<div class="mc-dlg" role="alertdialog" aria-modal="true">${WARN}<h4></h4><p></p><div class="acts">${seal(o.noSeal||'留','KEEP IT','no',noT)}${seal(o.seal||okT.slice(0,1),o.en||'TEAR OFF','ok',okT)}</div></div>`;
 m.querySelector('h4').textContent=o.title||'确定吗？';m.querySelector('p').innerHTML=o.body||'';
 document.body.appendChild(m);requestAnimationFrame(()=>m.classList.add('on'));
 const done=v=>{m.classList.remove('on');setTimeout(()=>m.remove(),280);res(v)};
 const pick=(c,v)=>{const b=m.querySelector(c);b.onclick=()=>{b.classList.add('inked');setTimeout(()=>done(v),260)}};pick('.ok',true);pick('.no',false);
 m.onclick=e=>{if(e.target===m)done(false)}})}
window.MC={toast,confirm};
})();
