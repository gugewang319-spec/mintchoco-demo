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
/*V=53 弹窗主按钮：位图巧克力大牌换成代码画的细巧克力条（矮一半、两端各一道分格槽、可可描边）*/.mc-dlg .ok{position:relative;display:grid;place-items:center;margin:20px auto 0;width:min(168px,60%);height:44px;border:1.2px solid #8a5c46;border-radius:10px;cursor:pointer;transition:scale .16s;background:linear-gradient(90deg,transparent calc(17% - 1px),rgba(38,20,13,.4) calc(17% - 1px) 17%,rgba(255,232,210,.16) 17% calc(17% + 1px),transparent calc(17% + 1px) calc(83% - 1px),rgba(38,20,13,.4) calc(83% - 1px) 83%,rgba(255,232,210,.16) 83% calc(83% + 1px),transparent calc(83% + 1px)),linear-gradient(#7d503c,#5f3b2c);box-shadow:inset 0 1px 0 rgba(255,232,210,.3),inset 0 -2px 0 rgba(38,20,13,.28),0 8px 14px -10px rgba(74,48,39,.5)}
.mc-dlg .ok:active{scale:.95}

.mc-dlg .ok span{position:relative;font:17px/1 ZK,WK,sans-serif;color:#fdf6e8;letter-spacing:.12em;text-shadow:0 1px 0 rgba(38,20,13,.35)}
.mc-dlg .no{display:block;margin:8px auto 0;min-height:40px;padding:0 14px;border:0;background:none;font:14px/1 WK,ZK,sans-serif;color:#8a5c46;text-decoration:underline dashed 1.1px;text-underline-offset:4px;cursor:pointer}
@media (prefers-reduced-motion:reduce){.mc-bell,.mc-dlg,.mc-mask{transition:none}.mc-bell.on svg{animation:none}}
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
function confirm(o){return new Promise(res=>{
 const m=document.createElement('div');m.className='mc-mask';
 m.innerHTML=`<div class="mc-dlg" role="alertdialog" aria-modal="true">${WARN}<h4></h4><p></p><button class="ok"><span></span></button><button class="no"></button></div>`;
 m.querySelector('h4').textContent=o.title||'确定吗？';m.querySelector('p').innerHTML=o.body||'';
 m.querySelector('.ok span').textContent=o.ok||'确定';m.querySelector('.no').textContent=o.cancel||'再想想';
 document.body.appendChild(m);requestAnimationFrame(()=>m.classList.add('on'));
 const done=v=>{m.classList.remove('on');setTimeout(()=>m.remove(),280);res(v)};
 m.querySelector('.ok').onclick=()=>done(true);m.querySelector('.no').onclick=()=>done(false);
 m.onclick=e=>{if(e.target===m)done(false)}})}
window.MC={toast,confirm};
})();
