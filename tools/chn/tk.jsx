// 渠道页 · 打开的那张单（样板件试点）。场景（挂单轨、夹子、小票纸）不动，单子里的控件全换成样板组件。
// 构建：sh tools/kit/adm/build.sh tools/chn/tk.jsx p/chn/tk.js
import React, { useState, useMemo } from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, Form, Input, Button, List, Popover, SearchBar, Checkbox, CheckList, Dialog } from 'antd-mobile'
import { Leaf, Star, I, PLUS, EYE, Grp, Pick } from 'mck-kit'

const SRCH = '<circle cx="8.8" cy="8.8" r="5"/><path d="m12.6 12.6 3.6 3.6"/>'
const MORE = '<circle cx="5" cy="10" r=".6"/><circle cx="10" cy="10" r=".6"/><circle cx="15" cy="10" r=".6"/>'
const kv = x => parseInt(x) * (/M/.test(x) ? 1024 : 1)
const guessW = u => /gemini/.test(u) ? '1M' : /claude|o3|o4|glm/.test(u) ? '200K' : /qwen|kimi|grok/.test(u) ? '256K' : '128K'
const ST = { '': '正常', cool: '冷却', bad: '超时', off: '停用' }
const pack = d => JSON.stringify(d)

function KeyField({ label, value, onChange, placeholder }) {
  const [eye, setEye] = useState(false)
  return <Form.Item label={label} extra={<button type="button" className="eye" aria-label="显示或隐藏" onClick={() => setEye(!eye)}><I d={EYE + (eye ? '' : '<path d="M3.5 3.5l13 13"/>')} /></button>}>
    <Input type={eye ? 'text' : 'password'} value={value} onChange={onChange} placeholder={placeholder} autoComplete="off" />
  </Form.Item>
}

function Ticket(p) {
  const isNew = p.mode === 'new', c = p.c || {}
  const base = useMemo(() => isNew ? { n: '', h: '', f: 'OpenAI', r: 2, p: p.EP.OpenAI, k: [], m: [] }
    : { n: c.n, h: c.h, f: c.f, r: c.r, p: c.p || p.EP[c.f], k: c.k.map(x => [...x]), m: c.m.map(x => ({ ...x })) }, [p.c, p.mode])
  const [D, setD] = useState(base)
  const [nk, setNk] = useState('')
  const [open, setOpen] = useState(-1)
  const [q, setQ] = useState('')
  const [pull, setPull] = useState(false)
  const [pq, setPq] = useState('')
  const [sel, setSel] = useState([])
  const [miss, setMiss] = useState(false)
  const set = k => v => setD(d => ({ ...d, [k]: v }))
  const dirty = pack(D) !== pack(base) || !!nk.trim()
  const ready = isNew ? D.n.trim() && D.h.trim() && nk.trim() : dirty
  const setFmt = f => setD(d => ({ ...d, f, p: (!d.p.trim() || Object.values(p.EP).includes(d.p.trim())) ? p.EP[f] : d.p }))
  const setM = (j, patch) => setD(d => ({ ...d, m: d.m.map((x, i) => i === j ? { ...x, ...patch } : x) }))

  const lift = async () => {
    if (dirty && !await Dialog.confirm({ title: '改的还没存', content: <>现在挂回去，<b>这次的改动就不要了</b>。</>, confirmText: '不存了', cancelText: '回去存' })) return
    p.onLift()
  }
  const save = () => {
    if (!D.n.trim()) { setMiss(true); return }
    if (isNew) return p.onHang({ ...D, n: D.n.trim(), h: D.h.trim(), k: [[nk.trim().slice(-4), '', '正常']] })
    p.onSave(D, nk.trim()); setNk('')
  }
  const delKey = async j => {
    const tail = '···' + D.k[j][0]
    if (!await Dialog.confirm({ title: '删掉这把钥匙？', content: <>{tail} 会从「{D.n || c.n}」拿掉，<b>删了就得重新粘贴</b>，正在用它的请求会换下一把。</>, confirmText: '删掉', cancelText: '再想想' })) return
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
    if (!await Dialog.confirm({ title: `撕掉「${c.n}」？`, content: <>这条渠道和它的 {c.k.length} 把钥匙、{c.m.length} 个模型会一起拿掉，<b>正在用它的入口会断</b>。</>, confirmText: '撕掉', cancelText: '再想想' })) return
    p.onRip()
  }

  const has = new Set(D.m.map(x => x.n))
  const ups = p.UP.filter(u => !pq || u.toLowerCase().includes(pq.toLowerCase()))
  const ms = D.m.map((m, j) => [m, j]).filter(([m]) => !q || m.n.toLowerCase().includes(q.toLowerCase()))

  return <ConfigProvider locale={window.MCK.zhCN}><div className="shade"><div className={'rc mck' + (isNew ? ' nw' : '')}>
    <div className="tkh"><span className="tno">NO.{String(p.no).padStart(4, '0')}{isNew ? ' · 空白单' : ''}</span>
      <Button fill="none" size="small" className="b4" onClick={lift}>{isNew ? '不开了' : '挂回去'}</Button></div>

    <Form layout="vertical" className="fm">
      <Form.Item label="名字" className={miss ? 'miss' : ''}><Input value={D.n} maxLength={6} placeholder="给它起个名字" onChange={v => { setMiss(false); set('n')(v) }} clearable /></Form.Item>
      <Form.Item label="地址"><Input value={D.h} placeholder="api.example.com" inputMode="url" onChange={set('h')} clearable /></Form.Item>
      <Form.Item label="API 路径"><Input value={D.p} onChange={set('p')} /></Form.Item>
      <div className="two">
        <Form.Item label="格式"><Pick value={D.f} onChange={setFmt} options={p.FM.map(f => ({ v: f }))} /></Form.Item>
        <Form.Item label="失败重试"><Pick value={'×' + D.r} onChange={v => set('r')(+v.slice(1))} options={p.RT.map(r => ({ v: '×' + r }))} /></Form.Item>
      </div>
    </Form>

    <Grp no="01" name="钥匙" ct={(D.k.length + (isNew ? 1 : 0)) + ' 把'} />
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
      <Grp no="02" name="模型" ct={D.m.length + ' 个'} end={<Button fill="none" size="small" className="b4" onClick={() => { setPull(!pull); setSel([]); setPq('') }}>{pull ? '收起' : '拉新的'}</Button>} />
      {pull && <div className="pullbox">
        <SearchBar className="sb" placeholder="在上游里找" value={pq} onChange={setPq} />
        <CheckList multiple className="cl" value={sel} onChange={setSel}>{ups.map(u =>
          <CheckList.Item key={u} value={u} disabled={has.has(u)} description={has.has(u) ? '已经有了' : null}>{u}</CheckList.Item>)}</CheckList>
        {!ups.length && <p className="nil">上游没有这个</p>}
        <div className="b2s"><Button className="b2" onClick={() => setPull(false)}>算了</Button><Button className="b2" disabled={!sel.length} onClick={addPulled}><I d={PLUS} />加 {sel.length} 个</Button></div>
      </div>}
      {D.m.length > 5 && <SearchBar className="sb" placeholder="搜模型名" value={q} onChange={setQ} />}
      <List className="rows">{ms.map(([m, j]) => [
        <List.Item key={m.n + j} arrowIcon={false} className={open === j ? 'on' : ''} onClick={() => setOpen(open === j ? -1 : j)}
          description={`窗口 ${m.w} · 输出 ${m.o}`} extra={<span className="caps">{m.v ? <Leaf /> : null}{m.s ? <Star /> : null}</span>}>
          <span className="nm">{m.n}{m.nw ? <i className="xin">新</i> : null}</span></List.Item>,
        open === j && <div key={'ed' + j} className="ed">
          <div className="two">
            <label className="fl"><span>窗口</span><Pick value={m.w} onChange={w => setM(j, { w })} options={p.WO.map(v => ({ v }))} /></label>
            <label className="fl"><span>输出</span><Pick value={m.o} onChange={o => setM(j, { o })} options={p.OO.map(v => ({ v }))} /></label>
          </div>
          <div className="cks"><Checkbox checked={!!m.v} onChange={v => setM(j, { v: v ? 1 : 0 })}>能看图</Checkbox><Checkbox checked={!!m.s} onChange={v => setM(j, { s: v ? 1 : 0 })}>流式</Checkbox></div>
          {kv(m.o) >= kv(m.w) && <p className="warn">输出比窗口还大，杯子要溢了</p>}
          <div className="b2s"><Button className="b2" onClick={() => p.onTaste(m.n)}>尝一口</Button><Button className="b2" color="danger" fill="outline" onClick={() => delM(j)}>拿掉</Button></div>
        </div>])}</List>
      {!ms.length && <p className="nil">没有叫这个的</p>}
    </>}

    <Button block color="primary" size="large" className="b1" disabled={!ready} onClick={save}>{isNew ? '开单' : '保存'}</Button>
    {!isNew && <div className="ripr"><Button fill="none" size="small" color="danger" className="b4 dg" onClick={rip}>撕掉这张单</Button></div>}
    <div className="foot">2026-11-12 20:40<br />NO.{String(p.no).padStart(4, '0')}</div><div className="bar"></div>
  </div></div></ConfigProvider>
}

const roots = new WeakMap()
let seq = 0
window.TK = {
  show(el, props) { let r = roots.get(el); if (!r) { r = createRoot(el); roots.set(el, r) } r.render(<Ticket key={++seq} {...props} />) },
  hide(el) { const r = roots.get(el); if (r) r.render(null) }
}
