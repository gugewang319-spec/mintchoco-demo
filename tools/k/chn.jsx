// 渠道页 · 基础版：页面结构和间距照抄 antd-mobile 官方示例（List / Form demo，MIT），
// 只换颜色字体变量（p/k/k-base.css），不加任何装饰。装饰以后作为单独一层加。
// 构建：sh tools/kit/adm/build.sh tools/k/chn.jsx p/k/chn.js ；页面 python3 tools/k/mk.py
import React, { useState, useMemo } from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, NavBar, Form, Input, Button, List, Popover, SearchBar, Checkbox, CheckList, Dialog, CapsuleTabs, ErrorBlock, Tag, Space } from 'antd-mobile'
import { CH as CH0, UP, WO, OO, EP, FM, RT, worst } from './chn-data.js'

const kv = x => parseInt(x) * (/M/.test(x) ? 1024 : 1)
const guessW = u => /gemini/.test(u) ? '1M' : /claude|o3|o4|glm/.test(u) ? '200K' : /qwen|kimi|grok/.test(u) ? '256K' : '128K'
const ST = { cool: ['冷却中', 'warning'], bad: ['有钥匙超时', 'danger'], off: ['停用', 'default'] }
const pack = d => JSON.stringify(d)
const Ico = ({ d }) => <svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: d }} />
const DOWN = '<path d="m6 8 4 4 4-4"/>', MORE = '<circle cx="5" cy="10" r=".7"/><circle cx="10" cy="10" r=".7"/><circle cx="15" cy="10" r=".7"/>'
const EYE = '<path d="M2 10s3-5.5 8-5.5S18 10 18 10s-3 5.5-8 5.5S2 10 2 10Z"/><circle cx="10" cy="10" r="2.4"/>'

// 下拉：Popover.Menu，选中项打勾
function Pick({ value, options, onChange }) {
  return <Popover.Menu trigger="click" placement="bottom-end" actions={options.map(v => ({ key: v, text: v + (v === value ? '  ✓' : '') }))} onAction={a => onChange(a.key)}>
    <span className="k-pick">{value}<Ico d={DOWN} /></span>
  </Popover.Menu>
}

function Taste({ model, ch }) {
  const [log, setLog] = useState([]), [v, setV] = useState('')
  const send = () => {
    const t = v.trim() || '你好'; setV('')
    const txt = `你好，我是 ${model}，在「${ch}」这条渠道上回答你。`, t0 = performance.now()
    setLog(l => [...l, { u: t }, { a: '' }])
    setTimeout(() => { let k = 0; const ft = ((performance.now() - t0) / 1000).toFixed(1)
      const tick = () => { k++; setLog(l => { const n = [...l]; n[n.length - 1] = { a: txt.slice(0, k), done: k >= txt.length ? `首字 ${ft} 秒 · ${txt.length} 字` : '' }; return n }); if (k < txt.length) setTimeout(tick, 30) }; tick() }, 600)
  }
  return <>
    {log.map((x, i) => <List.Item key={i} description={x.done || null}>{x.u ? '你：' + x.u : (x.a || '…')}</List.Item>)}
    <List.Item extra={<Button size="small" color="primary" fill="outline" onClick={send}>发送</Button>}><Input value={v} onChange={setV} placeholder="说点什么" onEnterPress={send} /></List.Item>
  </>
}

function Detail({ c, isNew, onBack, onSave, onHang, onRip }) {
  const base = useMemo(() => isNew ? { n: '', h: '', f: 'OpenAI', r: 2, p: EP.OpenAI, k: [], m: [] }
    : { n: c.n, h: c.h, f: c.f, r: c.r, p: c.p || EP[c.f], k: c.k.map(x => [...x]), m: c.m.map(x => ({ ...x })) }, [c, isNew])
  const [D, setD] = useState(base)
  const [nk, setNk] = useState(''), [eye, setEye] = useState(false)
  const [open, setOpen] = useState(-1), [taste, setTaste] = useState(-1)
  const [q, setQ] = useState(''), [pull, setPull] = useState(false), [pq, setPq] = useState(''), [sel, setSel] = useState([])
  const set = k => v => setD(d => ({ ...d, [k]: v }))
  const dirty = pack(D) !== pack(base) || !!nk.trim()
  const ready = isNew ? D.n.trim() && D.h.trim() && nk.trim() : dirty
  const setFmt = f => setD(d => ({ ...d, f, p: (!d.p.trim() || Object.values(EP).includes(d.p.trim())) ? EP[f] : d.p }))
  const setM = (j, patch) => setD(d => ({ ...d, m: d.m.map((x, i) => i === j ? { ...x, ...patch } : x) }))
  const back = async () => {
    if (dirty && !await Dialog.confirm({ title: '改动还没保存', content: '现在返回，这次的改动就不要了。', confirmText: '不保存', cancelText: '继续编辑' })) return
    onBack()
  }
  const save = () => { if (isNew) return onHang({ ...D, n: D.n.trim(), h: D.h.trim(), k: [[nk.trim().slice(-4), '', '正常']] }); onSave(D, nk.trim()); setNk('') }
  const delKey = async j => {
    const tail = '···' + D.k[j][0]
    if (!await Dialog.confirm({ title: '删除这把钥匙？', content: `${tail} 删除后需要重新粘贴。`, confirmText: '删除', cancelText: '取消' })) return
    const old = D.k; setD(d => ({ ...d, k: d.k.filter((_, i) => i !== j) })); MC.toast(`已删除 ${tail}，记得保存`, { undo: () => setD(d => ({ ...d, k: old })) })
  }
  const upKey = j => setD(d => { const k = [...d.k]; const [x] = k.splice(j, 1); k.unshift(x); return { ...d, k } })
  const delM = j => { const old = D.m, nm = D.m[j].n; setOpen(-1); setD(d => ({ ...d, m: d.m.filter((_, i) => i !== j) })); MC.toast(`已移除 ${nm}，记得保存`, { undo: () => setD(d => ({ ...d, m: old })) }) }
  const addPulled = () => { setD(d => ({ ...d, m: [...d.m, ...sel.map(u => ({ n: u, w: guessW(u), o: '16K', v: /gpt|claude|gemini|o3|o4|grok/.test(u) ? 1 : 0, s: 1, nw: 1 }))] })); MC.toast(`已添加 ${sel.length} 个，记得保存`); setSel([]); setPull(false); setPq('') }
  const rip = async () => { if (await Dialog.confirm({ title: `删除「${c.n}」？`, content: `它的 ${c.k.length} 把钥匙和 ${c.m.length} 个模型会一起删除，正在用它的入口会断开。`, confirmText: '删除', cancelText: '取消' })) onRip() }
  const has = new Set(D.m.map(x => x.n))
  const ups = UP.filter(u => !pq || u.toLowerCase().includes(pq.toLowerCase()))
  const ms = D.m.map((m, j) => [m, j]).filter(([m]) => !q || m.n.toLowerCase().includes(q.toLowerCase()))

  return <>
    <NavBar onBack={back}>{isNew ? '新渠道' : (D.n || '未命名')}</NavBar>
    <Form layout="horizontal" mode="card">
      <Form.Header>基本信息</Form.Header>
      <Form.Item label="名字" required><Input value={D.n} maxLength={6} placeholder="请输入名字" onChange={set('n')} clearable /></Form.Item>
      <Form.Item label="地址" required><Input value={D.h} placeholder="api.example.com" onChange={set('h')} clearable /></Form.Item>
      <Form.Item label="API 路径"><Input value={D.p} onChange={set('p')} /></Form.Item>
      <Form.Item label="格式" childElementPosition="right"><Pick value={D.f} onChange={setFmt} options={FM} /></Form.Item>
      <Form.Item label="失败重试" childElementPosition="right"><Pick value={'×' + D.r} onChange={v => set('r')(+v.slice(1))} options={RT.map(r => '×' + r)} /></Form.Item>
      <Form.Header>钥匙</Form.Header>
      {!isNew && D.k.map(([s, cl, tx], j) => <Form.Item key={s + j} label={'···' + s} help={null} childElementPosition="right">
        <Space align="center">{j === 0 && <Tag color="primary" fill="outline">先用</Tag>}<span className={'k-st ' + cl}>{tx}</span>
          <Popover.Menu trigger="click" placement="bottom-end" actions={[...(j ? [{ key: 'up', text: '移到最前' }] : []), { key: 'del', text: '删除' }]} onAction={a => a.key === 'up' ? upKey(j) : delKey(j)}>
            <span className="k-more" aria-label="更多"><Ico d={MORE} /></span></Popover.Menu></Space></Form.Item>)}
      <Form.Item label={isNew ? '钥匙' : '新增钥匙'} required={isNew} extra={<span className="k-eye" onClick={() => setEye(!eye)}><Ico d={EYE + (eye ? '' : '<path d="M3.5 3.5l13 13"/>')} /></span>}>
        <Input type={eye ? 'text' : 'password'} value={nk} onChange={setNk} placeholder="粘贴密钥" autoComplete="off" /></Form.Item>
    </Form>

    {!isNew && <>
      <List mode="card" header={<div className="k-hd"><span>模型 {D.m.length}</span><Button size="mini" fill="none" color="primary" onClick={() => { setPull(!pull); setSel([]); setPq('') }}>{pull ? '收起' : '从上游拉取'}</Button></div>}>
        {pull && <>
          <List.Item><SearchBar placeholder="搜索上游模型" value={pq} onChange={setPq} /></List.Item>
          <List.Item><CheckList multiple value={sel} onChange={setSel}>{ups.map(u => <CheckList.Item key={u} value={u} disabled={has.has(u)} description={has.has(u) ? '已添加' : null}>{u}</CheckList.Item>)}</CheckList></List.Item>
          <List.Item><Button block color="primary" fill="outline" disabled={!sel.length} onClick={addPulled}>添加 {sel.length} 个</Button></List.Item>
        </>}
        {D.m.length > 5 && <List.Item><SearchBar placeholder="搜索模型" value={q} onChange={setQ} /></List.Item>}
        {ms.map(([m, j]) => [
          <List.Item key={m.n + j} onClick={() => { setOpen(open === j ? -1 : j); setTaste(-1) }} arrowIcon={<Ico d={DOWN} />} className={open === j ? 'k-on' : ''}
            description={`窗口 ${m.w} · 输出 ${m.o}${m.v ? ' · 看图' : ''}${m.s ? ' · 流式' : ''}`}>{m.n}{m.nw ? <Tag color="success" fill="outline" style={{ marginLeft: 6 }}>新</Tag> : null}</List.Item>,
          open === j && <React.Fragment key={'ed' + j}>
            <List.Item extra={<Pick value={m.w} onChange={w => setM(j, { w })} options={WO} />}>上下文窗口</List.Item>
            <List.Item extra={<Pick value={m.o} onChange={o => setM(j, { o })} options={OO} />} description={kv(m.o) >= kv(m.w) ? '输出不能大于窗口' : null}>最大输出</List.Item>
            <List.Item><Space><Checkbox checked={!!m.v} onChange={v => setM(j, { v: v ? 1 : 0 })}>能看图</Checkbox><Checkbox checked={!!m.s} onChange={v => setM(j, { s: v ? 1 : 0 })}>流式</Checkbox></Space></List.Item>
            <List.Item><Space><Button size="small" onClick={() => setTaste(taste === j ? -1 : j)}>{taste === j ? '结束测试' : '测试'}</Button><Button size="small" color="danger" fill="outline" onClick={() => delM(j)}>移除</Button></Space></List.Item>
            {taste === j && <Taste model={m.n} ch={D.n} />}
          </React.Fragment>])}
        {!ms.length && <List.Item>没有匹配的模型</List.Item>}
      </List>
    </>}
    <div className="k-foot">
      <Button block color="primary" size="large" disabled={!ready} onClick={save}>{isNew ? '创建' : '保存'}</Button>
      {!isNew && <Button block fill="none" color="danger" onClick={rip} style={{ marginTop: 8 }}>删除渠道</Button>}
    </div>
  </>
}

function Home({ CH, onOpen, onNew }) {
  const [q, setQ] = useState(''), [tab, setTab] = useState('all')
  const isBad = c => ['bad', 'cool'].includes(worst(c))
  const n = { all: CH.length, bad: CH.filter(isBad).length, off: CH.filter(c => c.off).length }
  const rows = CH.map((c, i) => [c, i]).filter(([c]) => (tab === 'all' || (tab === 'bad' ? isBad(c) : c.off)) && (!q || (c.n + c.h).toLowerCase().includes(q.toLowerCase())))
  return <>
    <NavBar onBack={() => {}}>渠道</NavBar>
    <List mode="card" header="今日">
      <List.Item extra="1,284">出单</List.Item>
      <List.Item extra="1.8 秒">平均耗时</List.Item>
      <List.Item extra={<span className="k-st bad">3</span>}>失败</List.Item>
    </List>
    <div className="k-pad"><SearchBar placeholder="搜索站名或地址" value={q} onChange={setQ} /></div>
    <CapsuleTabs activeKey={tab} onChange={setTab}>
      <CapsuleTabs.Tab title={'全部 ' + n.all} key="all" /><CapsuleTabs.Tab title={'异常 ' + n.bad} key="bad" /><CapsuleTabs.Tab title={'停用 ' + n.off} key="off" />
    </CapsuleTabs>
    {rows.length ? <List mode="card" header={`渠道 ${rows.length}`}>{rows.map(([c, i]) => { const w = worst(c)
      return <List.Item key={c.n + i} onClick={() => onOpen(i)} extra={`${c.k.length} 把钥匙`} description={`${c.h} · ${c.f}`}>
        <Space align="center" style={{ '--gap': '6px' }}>{c.n}{c.now ? <Tag color="success">在用</Tag> : null}{w ? <Tag color={ST[w][1]} fill="outline">{ST[w][0]}</Tag> : null}</Space></List.Item> })}</List>
      : <ErrorBlock status="empty" title="没有找到" description="换个关键词试试" />}
    <div className="k-foot"><Button block color="primary" size="large" onClick={onNew}>新建渠道</Button></div>
  </>
}

function App() {
  const [CH, setCH] = useState(CH0), [view, setView] = useState(null)
  const go = v => { setView(v); window.scrollTo(0, 0) }
  if (view === 'new') return <Detail key="new" isNew onBack={() => go(null)}
    onHang={nc => { let at = CH.findIndex(c => c.off); if (at < 0) at = CH.length; const n = [...CH]; n.splice(at, 0, nc); setCH(n); go(null); MC.toast(`已创建「${nc.n}」`, { undo: () => setCH(CH) }) }} />
  if (view) { const c = CH[view.i]; return <Detail key={'d' + view.i + (view.v || 0)} c={c} onBack={() => go(null)}
    onSave={(D, nk) => { const nc = { ...c, n: D.n.trim(), h: D.h.trim(), f: D.f, r: D.r, p: D.p, k: [...D.k.map(x => [...x]), ...(nk ? [[nk.slice(-4), '', '正常']] : [])], m: D.m.map(({ n, w, o, v, s }) => ({ n, w, o, v, s })) }
      const n = [...CH]; n[view.i] = nc; setCH(n); setView({ i: view.i, v: (view.v || 0) + 1 }); MC.toast('已保存') }}
    onRip={() => { const old = CH; setCH(CH.filter((_, i) => i !== view.i)); go(null); MC.toast(`已删除「${c.n}」`, { undo: () => setCH(old) }) }} /> }
  return <Home CH={CH} onOpen={i => go({ i })} onNew={() => go('new')} />
}

createRoot(document.getElementById('root')).render(<ConfigProvider locale={window.MCK.zhCN}><App /></ConfigProvider>)
