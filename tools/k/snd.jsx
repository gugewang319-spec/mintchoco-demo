// 声音页 · 基础版：结构照抄 antd-mobile 官方 List / Form 示例（MIT），不加装饰。
// 后端：GET/POST /api/voices、POST /api/voices/{id}/default、POST /api/voices/{id}/preview、DELETE /api/voices/{id}；
//       GET/POST /api/tts/providers、DELETE /api/tts/providers/{id}（provider ∈ minimax / elevenlabs / fish）。
// 试听用浏览器朗读代替（演示）。
import React, { useState, useMemo } from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, NavBar, List, Form, Input, TextArea, Button, Tag, Dialog, Space } from 'antd-mobile'
import { Pick, KeyItem, pack } from './ui.jsx'

const PROV = ['MiniMax', 'ElevenLabs', 'Fish Audio']
const V0 = [
  { n: '晚风', c: 'c1', m: 'speech-02-hd', vid: 'male-qn-jingying', def: 1, pitch: .75, rate: .95 },
  { n: '薄荷', c: 'c1', m: 'speech-02-turbo', vid: 'male-qn-qingse', pitch: 1.15, rate: 1.1 },
  { n: '奶油', c: 'c2', m: '', vid: '7f2a-whisper', pitch: .9, rate: .8 },
]
const C0 = [{ id: 'c1', n: '海螺', t: 'MiniMax', h: 'tts.mint.example', k: 'a3f2' }, { id: 'c2', n: '小鱼', t: 'Fish Audio', h: 'fish.cocoa.example', k: '9c01' }]
const LINE = '今天也辛苦啦，过来喝口奶茶。'

function say(v, text) {
  const s = window.speechSynthesis; if (!s) return MC.toast('这台手机不能朗读')
  s.cancel(); const u = new SpeechSynthesisUtterance(text); u.lang = 'zh-CN'; u.pitch = v.pitch || 1; u.rate = v.rate || 1; s.speak(u)
}
const leave = async dirty => !dirty || await Dialog.confirm({ title: '改动还没保存', content: '现在返回，这次的改动就不要了。', confirmText: '不保存', cancelText: '继续编辑' })

function VoiceDetail({ v, isNew, C, onBack, onSave, onDel, onDef }) {
  const base = useMemo(() => isNew ? { n: '', c: C[0]?.id || '', vid: '', m: '' } : { n: v.n, c: v.c, vid: v.vid, m: v.m }, [v, isNew])
  const [D, setD] = useState(base), [line, setLine] = useState(LINE)
  const set = k => x => setD(d => ({ ...d, [k]: x }))
  const dirty = pack(D) !== pack(base)
  const cn = id => C.find(c => c.id === id)?.n
  const ready = D.n.trim() && D.c && D.vid.trim() && (isNew || dirty)
  const del = async () => {
    if (!await Dialog.confirm({ title: `删除「${v.n}」？`, content: v.def ? '它是默认音色，删除后 Telegram 语音会改用剩下的第一种。' : '删除后不能恢复。', confirmText: '删除', cancelText: '取消' })) return
    onDel()
  }
  return <>
    <NavBar onBack={async () => await leave(dirty) && onBack()}>{isNew ? '新音色' : v.n}</NavBar>
    <Form layout="horizontal" mode="card">
      <Form.Header>音色</Form.Header>
      <Form.Item label="名字" required><Input value={D.n} maxLength={6} placeholder="请输入名字" onChange={set('n')} clearable /></Form.Item>
      <Form.Item label="渠道" required childElementPosition="right"><Pick value={cn(D.c)} ph="请选择" options={C.map(c => c.n)} onChange={n => set('c')(C.find(c => c.n === n).id)} /></Form.Item>
      <Form.Item label="音色 ID" required><Input value={D.vid} placeholder="服务商给的音色 ID" onChange={set('vid')} clearable /></Form.Item>
      <Form.Item label="模型"><Input value={D.m} placeholder="可不填" onChange={set('m')} clearable /></Form.Item>
      {!isNew && <>
        <Form.Header>试听</Form.Header>
        <Form.Item label="试听句"><TextArea value={line} onChange={setLine} rows={2} maxLength={60} showCount /></Form.Item>
        <Form.Item><Space><Button size="small" onClick={() => say(v, line || LINE)}>试听</Button>
          {v.def ? <Tag color="success" fill="outline">默认音色</Tag> : <Button size="small" onClick={onDef}>设为默认</Button>}</Space></Form.Item>
      </>}
    </Form>
    <div className="k-foot">
      <Button block color="primary" size="large" disabled={!ready} onClick={() => onSave({ ...D, n: D.n.trim(), vid: D.vid.trim(), m: D.m.trim() })}>{isNew ? '创建' : '保存'}</Button>
      {!isNew && <Button block fill="none" color="danger" onClick={del} style={{ marginTop: 8 }}>删除音色</Button>}
    </div>
  </>
}

function ProvDetail({ c, isNew, uses, onBack, onSave, onDel }) {
  const base = useMemo(() => isNew ? { n: '', t: 'MiniMax', h: '' } : { n: c.n, t: c.t, h: c.h }, [c, isNew])
  const [D, setD] = useState(base), [nk, setNk] = useState('')
  const set = k => x => setD(d => ({ ...d, [k]: x }))
  const dirty = pack(D) !== pack(base) || !!nk.trim()
  const ready = D.n.trim() && D.h.trim() && (isNew ? nk.trim() : dirty)
  const del = async () => {
    if (!await Dialog.confirm({ title: `删除「${c.n}」？`, content: uses.length ? `用它的 ${uses.length} 种音色（${uses.join('、')}）会一起不能用。` : '没有音色在用它。', confirmText: '删除', cancelText: '取消' })) return
    onDel()
  }
  return <>
    <NavBar onBack={async () => await leave(dirty) && onBack()}>{isNew ? '新渠道' : c.n}</NavBar>
    <Form layout="horizontal" mode="card">
      <Form.Header>语音渠道</Form.Header>
      <Form.Item label="名字" required><Input value={D.n} maxLength={6} placeholder="请输入名字" onChange={set('n')} clearable /></Form.Item>
      <Form.Item label="服务商" required childElementPosition="right"><Pick value={D.t} options={PROV} onChange={set('t')} /></Form.Item>
      <Form.Item label="地址" required><Input value={D.h} placeholder="api.example.com" onChange={set('h')} clearable /></Form.Item>
      {!isNew && <Form.Item label="当前钥匙"><span className="k-mute">···{c.k}</span></Form.Item>}
      <KeyItem label={isNew ? '钥匙' : '换钥匙'} required={isNew} value={nk} onChange={setNk} ph={isNew ? '粘贴密钥' : '不换就不填'} />
    </Form>
    <div className="k-foot">
      <Button block color="primary" size="large" disabled={!ready} onClick={() => onSave({ ...D, n: D.n.trim(), h: D.h.trim(), k: nk.trim() ? nk.trim().slice(-4) : c?.k })}>{isNew ? '创建' : '保存'}</Button>
      {!isNew && <Button block fill="none" color="danger" onClick={del} style={{ marginTop: 8 }}>删除渠道</Button>}
    </div>
  </>
}

function App() {
  const [V, setV] = useState(V0), [C, setC] = useState(C0), [view, setView] = useState(null)
  const go = x => { setView(x); window.scrollTo(0, 0) }
  const cn = id => C.find(c => c.id === id)?.n || '渠道已删除'

  if (view?.k === 'v') { const v = V[view.i]; return <VoiceDetail key={'v' + view.i} v={v} isNew={view.i < 0} C={C} onBack={() => go(null)}
    onSave={d => { if (view.i < 0) { setV([...V, { ...d, pitch: 1, rate: 1 }]); MC.toast(`已创建「${d.n}」`) } else { const n = [...V]; n[view.i] = { ...v, ...d }; setV(n); MC.toast('已保存') } go(null) }}
    onDef={() => { setV(V.map((x, i) => ({ ...x, def: i === view.i ? 1 : 0 }))); MC.toast(`「${v.n}」设为默认`) }}
    onDel={() => { const old = V; let n = V.filter((_, i) => i !== view.i); if (v.def && n.length) n = n.map((x, i) => ({ ...x, def: i === 0 ? 1 : 0 })); setV(n); go(null); MC.toast(`已删除「${v.n}」`, { undo: () => setV(old) }) }} /> }

  if (view?.k === 'c') { const c = C[view.i]; return <ProvDetail key={'c' + view.i} c={c} isNew={view.i < 0} uses={c ? V.filter(v => v.c === c.id).map(v => v.n) : []} onBack={() => go(null)}
    onSave={d => { if (view.i < 0) { setC([...C, { ...d, id: 'c' + Date.now() }]); MC.toast(`已创建「${d.n}」`) } else { const n = [...C]; n[view.i] = { ...c, ...d }; setC(n); MC.toast('已保存') } go(null) }}
    onDel={() => { const old = C; setC(C.filter((_, i) => i !== view.i)); go(null); MC.toast(`已删除「${c.n}」`, { undo: () => setC(old) }) }} /> }

  return <>
    <NavBar onBack={() => { location.href = 'set.html' }}>声音</NavBar>
    <List mode="card" header={`音色 ${V.length}`}>
      {V.map((v, i) => <List.Item key={v.n + i} onClick={() => go({ k: 'v', i })} description={`${cn(v.c)}${v.m ? ' · ' + v.m : ''}`}
        extra={<Space style={{ '--gap': '8px' }} align="center">{v.def ? <Tag color="success" fill="outline">默认</Tag> : null}
          <Button size="mini" onClick={e => { e.stopPropagation(); say(v, LINE) }}>试听</Button></Space>}>{v.n}</List.Item>)}
      <List.Item onClick={() => go({ k: 'v', i: -1 })} className="k-add">新建音色</List.Item>
    </List>
    <List mode="card" header={`语音渠道 ${C.length}`}>
      {C.map((c, i) => <List.Item key={c.id} onClick={() => go({ k: 'c', i })} description={`${c.t} · ···${c.k}`} extra={`${V.filter(v => v.c === c.id).length} 种音色`}>{c.n}</List.Item>)}
      <List.Item onClick={() => go({ k: 'c', i: -1 })} className="k-add">新建渠道</List.Item>
    </List>
  </>
}

createRoot(document.getElementById('root')).render(<ConfigProvider locale={window.MCK.zhCN}><App /></ConfigProvider>)
