// 渠道页 · 纯组件版（不带场景和装饰，装饰以后再加）。
// 构建：sh tools/kit/adm/build.sh tools/k/chn.jsx p/k/chn.js ；页面 python3 tools/k/mk.py
import React, { useState, useMemo, useRef } from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, NavBar, Form, Input, Button, List, Popover, SearchBar, Checkbox, CheckList, Dialog, CapsuleTabs, ErrorBlock } from 'antd-mobile'
import { Leaf, Star, I, PLUS, EYE, Grp, Pick } from 'mck-kit'
import { CH as CH0, UP, WO, OO, EP, FM, RT, worst } from './chn-data.js'

const MORE = '<circle cx="5" cy="10" r=".6"/><circle cx="10" cy="10" r=".6"/><circle cx="15" cy="10" r=".6"/>'
const SEND = '<path d="M3 10h12M11 5l5 5-5 5"/>'
const kv = x => parseInt(x) * (/M/.test(x) ? 1024 : 1)
const guessW = u => /gemini/.test(u) ? '1M' : /claude|o3|o4|glm/.test(u) ? '200K' : /qwen|kimi|grok/.test(u) ? '256K' : '128K'
const ST = { '': '正常', cool: '冷却中', bad: '有钥匙超时', off: '停用' }
const pack = d => JSON.stringify(d)
const hl = (t, q) => { if (!q) return t; const i = t.toLowerCase().indexOf(q.toLowerCase()); return i < 0 ? t : <>{t.slice(0, i)}<mark>{t.slice(i, i + q.length)}</mark>{t.slice(i + q.length)}</> }

function KeyField({ label, value, onChange, placeholder }) {
  const [eye, setEye] = useState(false)
  return <Form.Item label={label} extra={<button type="button" className="eye" aria-label="显示或隐藏" onClick={() => setEye(!eye)}><I d={EYE + (eye ? '' : '<path d="M3.5 3.5l13 13"/>')} /></button>}>
    <Input type={eye ? 'text' : 'password'} value={value} onChange={onChange} placeholder={placeholder} autoComplete="off" />
  </Form.Item>
}

// 尝一口：就地展开的小对话（演示）
function Taste({ model, ch }) {
  const [log, setLog] = useState([])
  const [v, setV] = useState('')
  const send = () => {
    const t = v.trim() || '你好'; setV('')
    const txt = `你好，我是 ${model}，在「${ch}」这条渠道上回答你。`, t0 = performance.now()
    setLog(l => [...l, { u: t }, { a: '' }])
    setTimeout(() => { let k = 0; const ft = ((performance.now() - t0) / 1000).toFixed(1)
      const tick = () => { k++; setLog(l => { const n = [...l]; n[n.length - 1] = { a: txt.slice(0, k), done: k >= txt.length ? `首字 ${ft} 秒 · ${txt.length} 字` : '' }; return n }); if (k < txt.length) setTimeout(tick, 30) }; tick() }, 600)
  }
  return <div className="taste">
    {log.length > 0 && <div className="tlog">{log.map((x, i) => x.u ? <p key={i} className="tu">{x.u}</p> : <p key={i} className="ta">{x.a || '···'}{x.done && <small>{x.done}</small>}</p>)}</div>}
    <div className="trow"><Input value={v} onChange={setV} placeholder="说点什么" onEnterPress={send} /><Button shape="rounded" className="b3" aria-label="送出" onClick={send}><I d={SEND} /></Button></div>
  </div>
}

function Detail({ c, isNew, no, onBack, onSave, onHang, onRip }) {
  const base = useMemo(() => isNew ? { n: '', h: '', f: 'OpenAI', r: 2, p: EP.OpenAI, k: [], m: [] }
    : { n: c.n, h: c.h, f: c.f, r: c.r, p: c.p || EP[c.f], k: c.k.map(x => [...x]), m: c.m.map(x => ({ ...x })) }, [c, isNew])
  const [D, setD] = useState(base)
  const [nk, setNk] = useState('')
  const [open, setOpen] = useState(-1)
  const [taste, setTaste] = useState(-1)
  const [q, setQ] = useState('')
  const [pull, setPull] = useState(false)
  const [pq, setPq] = useState('')
  const [sel, setSel] = useState([])
  const [miss, setMiss] = useState(false)
  const set = k => v => setD(d => ({ ...d, [k]: v }))
  const dirty = pack(D) !== pack(base) || !!nk.trim()
  const ready = isNew ? D.n.trim() && D.h.trim() && nk.trim() : dirty
  const setFmt = f => setD(d => ({ ...d, f, p: (!d.p.trim() || Object.values(EP).includes(d.p.trim())) ? EP[f] : d.p }))
  const setM = (j, patch) => setD(d => ({ ...d, m: d.m.map((x, i) => i === j ? { ...x, ...patch } : x) }))

  const back = async () => {
    if (dirty && !await Dialog.confirm({ title: '改的还没存', content: <>现在回去，<b>这次的改动就不要了</b>。</>, confirmText: '不存了', cancelText: '回去存' })) return
    onBack()
  }
  const save = () => {
    if (!D.n.trim()) { setMiss(true); return }
    if (isNew) return onHang({ ...D, n: D.n.trim(), h: D.h.trim(), k: [[nk.trim().slice(-4), '', '正常']] })
    onSave(D, nk.trim()); setNk('')
  }
  const delKey = async j => {
    const tail = '···' + D.k[j][0]
    if (!await Dialog.confirm({ title: '删掉这把钥匙？', content: <>{tail} 会从「{D.n}」拿掉，<b>删了就得重新粘贴</b>，正在用它的请求会换下一把。</>, confirmText: '删掉', cancelText: '再想想' })) return
    const old = D.k; setD(d => ({ ...d, k: d.k.filter((_, i) => i !== j) }))
    MC.toast(`删掉了 ${tail}，记得保存`, { undo: () => setD(d => ({ ...d, k: old })) })
  }
  const upKey = j => setD(d => { const k = [...d.k]; const [x] = k.splice(j, 1); k.unshift(x); return { ...d, k } })
  const delM = j => {
    const old = D.m, nm = D.m[j].n; setOpen(-1); setD(d => ({ ...d, m: d.m.filter((_, i) => i !== j) }))
    MC.toast(`拿掉了 ${nm}，记得保存`, { undo: () => setD(d => ({ ...d, m: old })) })
  }
  const addPulled = () => {
    setD(d => ({ ...d, m: [...d.m, ...sel.map(u => ({ n: u, w: guessW(u), o: '16K', v: /gpt|claude|gemini|o3|o4|grok/.test(u) ? 1 : 0, s: 1, nw: 1 }))] }))
    MC.toast(`拉进来 ${sel.length} 个，记得保存`); setSel([]); setPull(false); setPq('')
  }
  const rip = async () => {
    if (!await Dialog.confirm({ title: `删掉「${c.n}」？`, content: <>这条渠道和它的 {c.k.length} 把钥匙、{c.m.length} 个模型会一起拿掉，<b>正在用它的入口会断</b>。</>, confirmText: '删掉', cancelText: '再想想' })) return
    onRip()
  }
  const has = new Set(D.m.map(x => x.n))
  const ups = UP.filter(u => !pq || u.toLowerCase().includes(pq.toLowerCase()))
  const ms = D.m.map((m, j) => [m, j]).filter(([m]) => !q || m.n.toLowerCase().includes(q.toLowerCase()))

  return <div className="view">
    <NavBar className="hd" onBack={back} right={<span className="tno">NO.{String(no).padStart(4, '0')}</span>}><span className="ttl"><b>{isNew ? '新渠道' : (D.n || '未命名')}</b></span></NavBar>

    <Grp no="01" name="基本" />
    <Form layout="vertical" className="fm">
      <Form.Item label="名字" className={miss ? 'miss' : ''}><Input value={D.n} maxLength={6} placeholder="给它起个名字" onChange={v => { setMiss(false); set('n')(v) }} clearable /></Form.Item>
      <Form.Item label="地址"><Input value={D.h} placeholder="api.example.com" inputMode="url" onChange={set('h')} clearable /></Form.Item>
      <Form.Item label="API 路径"><Input value={D.p} onChange={set('p')} /></Form.Item>
      <div className="two">
        <Form.Item label="格式"><Pick value={D.f} onChange={setFmt} options={FM.map(f => ({ v: f }))} /></Form.Item>
        <Form.Item label="失败重试"><Pick value={'×' + D.r} onChange={v => set('r')(+v.slice(1))} options={RT.map(r => ({ v: '×' + r }))} /></Form.Item>
      </div>
    </Form>

    <Grp no="02" name="钥匙" ct={(D.k.length + (isNew ? 1 : 0)) + ' 把'} />
    {!isNew && D.k.length > 0 && <List className="rows">{D.k.map(([s, cl, tx], j) =>
      <List.Item key={s + j} arrowIcon={false} className={cl ? 'k-' + cl : ''} description={<span className="kst"><i className={'dot ' + cl} />{tx}{j === 0 ? ' · 先用这把' : ''}</span>}
        extra={<Popover.Menu trigger="click" placement="bottom-end" mode="light"
          actions={[...(j ? [{ key: 'up', text: <span className="opt"><span>往前挪</span></span> }] : []), { key: 'del', text: <span className="opt dg"><span>删掉</span></span> }]}
          onAction={a => a.key === 'up' ? upKey(j) : delKey(j)}>
          <Button shape="rounded" className="b3 mt sm" aria-label="更多"><I d={MORE} /></Button></Popover.Menu>}>
        <span className="nm">···{s}</span></List.Item>)}</List>}
    <Form layout="vertical" className="fm">
      <KeyField label={isNew ? '第一把钥匙' : '再加一把'} value={nk} onChange={setNk} placeholder="粘贴密钥" />
    </Form>

    {!isNew && <>
      <Grp no="03" name="模型" ct={D.m.length + ' 个'} end={<Button fill="none" size="small" className="b4" onClick={() => { setPull(!pull); setSel([]); setPq('') }}>{pull ? '收起' : '拉新的'}</Button>} />
      {pull && <div className="pullbox">
        <SearchBar className="sb" placeholder="在上游里找" value={pq} onChange={setPq} />
        <CheckList multiple className="cl" value={sel} onChange={setSel}>{ups.map(u =>
          <CheckList.Item key={u} value={u} disabled={has.has(u)} description={has.has(u) ? '已经有了' : null}>{hl(u, pq)}</CheckList.Item>)}</CheckList>
        {!ups.length && <p className="nil">上游没有这个</p>}
        <div className="b2s"><Button className="b2" onClick={() => setPull(false)}>算了</Button><Button className="b2" disabled={!sel.length} onClick={addPulled}><I d={PLUS} />加 {sel.length} 个</Button></div>
      </div>}
      {D.m.length > 5 && <SearchBar className="sb" placeholder="搜模型名" value={q} onChange={setQ} />}
      <List className="rows">{ms.map(([m, j]) => [
        <List.Item key={m.n + j} arrowIcon={false} className={open === j ? 'on' : ''} onClick={() => { setOpen(open === j ? -1 : j); setTaste(-1) }}
          description={`窗口 ${m.w} · 输出 ${m.o}`} extra={<span className="caps">{m.v ? <Leaf /> : null}{m.s ? <Star /> : null}</span>}>
          <span className="nm">{hl(m.n, q)}{m.nw ? <i className="xin">新</i> : null}</span></List.Item>,
        open === j && <div key={'ed' + j} className="ed">
          <div className="two">
            <label className="fl"><span>窗口</span><Pick value={m.w} onChange={w => setM(j, { w })} options={WO.map(v => ({ v }))} /></label>
            <label className="fl"><span>输出</span><Pick value={m.o} onChange={o => setM(j, { o })} options={OO.map(v => ({ v }))} /></label>
          </div>
          <div className="cks"><Checkbox checked={!!m.v} onChange={v => setM(j, { v: v ? 1 : 0 })}>能看图</Checkbox><Checkbox checked={!!m.s} onChange={v => setM(j, { s: v ? 1 : 0 })}>流式</Checkbox></div>
          {kv(m.o) >= kv(m.w) && <p className="warn">输出比窗口还大，杯子要溢了</p>}
          <div className="b2s"><Button className="b2" onClick={() => setTaste(taste === j ? -1 : j)}>{taste === j ? '不尝了' : '尝一口'}</Button><Button className="b2" color="danger" fill="outline" onClick={() => delM(j)}>拿掉</Button></div>
          {taste === j && <Taste model={m.n} ch={D.n} />}
        </div>])}</List>
      {!ms.length && <p className="nil">没有叫这个的</p>}
    </>}

    <Button block color="primary" size="large" className="b1" disabled={!ready} onClick={save}>{isNew ? '开单' : '保存'}</Button>
    {!isNew && <div className="ripr"><Button fill="none" size="small" color="danger" className="b4 dg" onClick={rip}>删掉这条渠道</Button></div>}
  </div>
}

function Home({ CH, onOpen, onNew }) {
  const [q, setQ] = useState('')
  const [tab, setTab] = useState('all')
  const n = { all: CH.length, bad: CH.filter(c => ['bad', 'cool'].includes(worst(c))).length, off: CH.filter(c => c.off).length }
  const rows = CH.map((c, i) => [c, i]).filter(([c]) => (tab === 'all' || (tab === 'bad' ? ['bad', 'cool'].includes(worst(c)) : c.off)) && (!q || (c.n + c.h).toLowerCase().includes(q.toLowerCase())))
  return <div className="view">
    <NavBar className="hd" backIcon={true} onBack={() => {}} right={<span className="plate"><b>{CH.length}</b>条</span>}><span className="ttl"><b>渠道</b><i>Channel</i></span></NavBar>
    <div className="stat"><div><b>1,284</b><span>今日出单</span></div><div><b>1.8<small>秒</small></b><span>平均出单</span></div><div className="bad"><b>3</b><span>没出成</span></div></div>
    <SearchBar className="sb" placeholder="站名或地址" value={q} onChange={setQ} />
    <CapsuleTabs className="ct2" activeKey={tab} onChange={setTab}>
      <CapsuleTabs.Tab title={'全部 ' + n.all} key="all" /><CapsuleTabs.Tab title={'有问题 ' + n.bad} key="bad" /><CapsuleTabs.Tab title={'停用 ' + n.off} key="off" />
    </CapsuleTabs>
    {rows.length ? <List className="rows">{rows.map(([c, i]) => { const w = worst(c); return <List.Item key={c.n + i} arrowIcon={false} className={(w ? 'k-' + w : '') + (c.now ? ' now' : '')} onClick={() => onOpen(i)}
      description={`${c.h} · ${c.f} · 重试 ×${c.r}`} extra={<span className="num">{c.k.length}<small>把钥匙</small></span>}>
      <span className="nm">{hl(c.n, q)}{c.now ? <i className="xin">在用</i> : null}{w ? <span className="kst"><i className={'dot ' + w} />{ST[w]}</span> : null}</span></List.Item> })}</List>
      : <ErrorBlock className="st" status="empty" title="没有这个站" description="换个字试试，或者接一条新的" />}
    <Button block color="primary" size="large" className="b1" onClick={onNew}><I d={PLUS} /> 新渠道</Button>
  </div>
}

function App() {
  const [CH, setCH] = useState(CH0)
  const [view, setView] = useState(null) // null | {i} | 'new'
  const top = () => window.scrollTo(0, 0)
  const go = v => { setView(v); top() }
  if (view === 'new') return <Detail key="new" isNew no={CH.length + 1} onBack={() => go(null)}
    onHang={nc => { let at = CH.findIndex(c => c.off); if (at < 0) at = CH.length; const n = [...CH]; n.splice(at, 0, nc); setCH(n); go(null)
      MC.toast(`「${nc.n}」接上了`, { undo: () => setCH(CH) }) }} />
  if (view) { const c = CH[view.i]; return <Detail key={'d' + view.i + view.v} c={c} no={view.i + 1} onBack={() => go(null)}
    onSave={(D, nk) => { const nc = { ...c, n: D.n.trim(), h: D.h.trim(), f: D.f, r: D.r, p: D.p, k: [...D.k.map(x => [...x]), ...(nk ? [[nk.slice(-4), '', '正常']] : [])], m: D.m.map(({ n, w, o, v, s }) => ({ n, w, o, v, s })) }
      const n = [...CH]; n[view.i] = nc; setCH(n); setView({ i: view.i, v: (view.v || 0) + 1 }); MC.toast(`「${nc.n}」存好了`) }}
    onRip={() => { const old = CH; setCH(CH.filter((_, i) => i !== view.i)); go(null); MC.toast(`删掉了「${c.n}」`, { undo: () => setCH(old) }) }} /> }
  return <Home CH={CH} onOpen={i => go({ i })} onNew={() => go('new')} />
}

createRoot(document.getElementById('root')).render(<ConfigProvider locale={window.MCK.zhCN}><main className="app"><App /></main></ConfigProvider>)
