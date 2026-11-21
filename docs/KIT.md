# 组件库说明书（p/mc）

2026-11-21 起：新页、改版页一律用共用组件库，不再每页复制样式。改 `p/mc/mc.css` / `p/mc/mc.js` 一次，全站一起变。

- 图鉴（所有组件 × 所有状态，可点）：`p/mc/index.html`
- 新页模板：`p/mc/_page.html`（复制到 `p/<页>/index.html` 起步）
- 第一张用上的页：`p/chn/vc.html`（渠道页样稿）

## 文件
| 文件 | 内容 |
|---|---|
| `p/mc/mc.css` | 设计变量（颜色、状态色、线、4 倍数间距、玻璃）＋全部组件样式 |
| `p/mc/mc.js` | 组件函数（见下）。先引 `../ui.js`（出餐铃/警告窗）再引它 |
| `p/mc/zk.ttf` `wk.ttf` | 共用字体子集，`python3 tools/mkfonts.py` 扫全站重切 |
| `p/mc/img/` | 状态小杯 cup-*.png、珍珠、淋酱 |

## 组件
| 组件 | 用法 | 备注 |
|---|---|---|
| 六态 | `MC.STATES` ok/making/fail/warn/empty | 签条、小票、普通行共用；换色只改这里 |
| 状态小杯 | `MC.cup('ok')` 或 `MC.cup('leaf')` | |
| 记号 | `MC.mark(k)` / `MC.markSVG(k)` | 勾、叉、转圈 |
| 签条 | `MC.tag({name,state,count,unit,sel})`、`MC.tag({add:1,name})` | 竖版，挂轨用 |
| 普通行 | `MC.row({cup,k,sub,v,vs})` | 不加底，文字＋小杯 |
| 模型小签 | `MC.chips([[名,开,新]])` | |
| 小票纸卷 | `MC.roll(el,[{st,t,c,m,tm,tip,nw}])` | 撕线＋半圆缺口，tip 自动带 info |
| 店章 | `MC.stamp('存'|'开')` | `.mute` 淡着 → 去掉抬起 → `.inked` 盖下 |
| info 提示 | `MC.info()` ＋ `.tip`（放同一个 `[data-tipbox]` 里） | 少文案：补充说明只放这里 |
| 页顶 | `MC.head({title,en,back,right:[{icon,label,id}]})` | icon: back/search/plus |
| 底栏 | `MC.nav('设置',{dots:['记忆']})` | 自带渐隐、切页 |
| 出餐铃/警告 | `MC.toast(t,{undo})`、`MC.confirm({title,body,ok})` | 来自 ui.js |
| CSS 类 | `.glass` `.soft` `.go` `.tx(.danger)` `.f` `.seg-pick` `.q` `.pr` `.ld` `.err` `.sep` `.more` | |

**还没收进库**（旧页里有，下次用到时收）：一级巧克力牌、三级圆形小甜点、饮品卡、小选单、波峰圆点。

## 规矩
1. 页面 `<style>` 只写场景和布局；组件长得不对就改库，不在页面里覆盖。
2. 新组件先在图鉴里做出全部状态，再拿去页面用。
3. 改了库 → `mc.css?v=` / `mc.js?v=` +1。加了新字 → `python3 tools/mkfonts.py`。

## 交付流程（每次给茶茶看之前）
1. `python3 -m http.server 8811`（仓库根）
2. `python3 tools/check.py p/<页>/index.html p/mc/index.html` → 必须「全过 ✓」
   查：报错、横向溢出、文字被裁、缺字、点击区太小、坏图；两尺寸截图拼在 /tmp/check/*_sheet.png
3. 自己看截图：焦点是否只有一个、主角够不够大、有没有空洞
4. 改了库就把用到它的页全跑一遍 check
5. 一批做完再给茶茶看，一次给全部对照图
