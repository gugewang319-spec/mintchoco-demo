// 样板间 v2：底子用 antd-mobile v5（成熟组件，间距/交互现成），我们只换主题变量 + 加装饰。
// 构建：tools/kit/adm/build.sh → p/kit/adm.js + adm.css；皮肤 p/kit/adm-skin-*.css。
import React, { useState, useRef } from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, NavBar, List, Button, Form, Input, TextArea, Popover, CapsuleTabs, SearchBar, Dialog, ErrorBlock, DotLoading } from 'antd-mobile'
import zhCN from 'antd-mobile/es/locales/zh-CN'

const Leaf = () => <svg className="ico" viewBox="0 0 16 16" fill="#a6d9c4" stroke="#5b8a74" strokeWidth="1"><path d="M2.5 13.5C2.5 6 7 2.5 13.5 2.5 13.5 9 10 13.5 2.5 13.5Z"/><path d="M3 13 10 6" fill="none"/></svg>
const Star = () => <svg className="ico" viewBox="0 0 16 16" fill="#f6e3b8" stroke="#a9825f" strokeWidth="1" strokeLinejoin="round"><path d="M8 1.8 9.8 6l4.4.4-3.3 2.9 1 4.4L8 11.4l-3.9 2.3 1-4.4L1.8 6.4 6.2 6Z"/></svg>
const I = ({ d }) => <svg className="bi" viewBox="0 0 20 20" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: d }} />
const PLUS = '<path d="M10 4v12M4 10h12"/>', SRCH = '<circle cx="8.8" cy="8.8" r="5"/><path d="m12.6 12.6 3.6 3.6"/>', PEN = '<path d="m4 16 1-4 8-8 3 3-8 8Z"/>', BIN = '<path d="M4.5 6h11M8 6V4h4v2M6 6l1 10h6l1-10"/>'
const EYE = '<path d="M2 10s3-5.5 8-5.5S18 10 18 10s-3 5.5-8 5.5S2 10 2 10Z"/><circle cx="10" cy="10" r="2.4"/>'
const Chev = () => <svg className="chev" viewBox="0 0 10 10" fill="none" strokeWidth="1.6" strokeLinecap="round"><path d="m2 3.5 3 3 3-3"/></svg>
const Dec = ({ src, s, cls = 'sway', o = '50% 90%', a = '4deg' }) => <img className={'dec ' + cls} src={src} alt="" style={{ ...s, '--o': o, '--a': a }} />
const Grp = ({ no, name, ct, end }) => <div className="grp"><span className="no">{no}</span><span className="rib"><h2>{name}</h2>{ct && <span className="ct">{ct}</span>}</span><span className="end">{end}</span></div>

// 就地小选单：antd-mobile Popover.Menu，贴着字段下沿浮出
function Pick({ value, options, onChange }) {
  const [open, setOpen] = useState(false)
  return <Popover.Menu visible={open} onVisibleChange={setOpen} trigger="click" placement="bottom-start" mode="light"
    actions={options.map(o => ({ key: o.v, text: <span className={'opt' + (o.v === value ? ' on' : '')}><span>{o.v}</span>{o.sub && <small>{o.sub}</small>}<svg className="ck" viewBox="0 0 14 14" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="m2.5 7.5 3 3 6-7"/></svg></span> }))}
    onAction={a => { onChange(a.key); setOpen(false) }}>
    <button type="button" className={'pickf' + (open ? ' open' : '')}><span>{value}</span><Chev /></button>
  </Popover.Menu>
}

function App() {
  const [skin, setSkin] = useState('薄荷巧克力')
  const [sel, setSel] = useState('gpt-4o')
  const init = { name: '小鲸鱼中转', url: 'https://example.local/v1', key: 'demo-key-123', fmt: 'OpenAI', note: '' }
  const [saved, setSaved] = useState(init)
  const [v, setV] = useState(init)
  const [eye, setEye] = useState(false)
  const dirty = Object.keys(v).some(k => v[k] !== saved[k])
  const set = k => x => setV(p => ({ ...p, [k]: x }))
  const changeSkin = s => { setSkin(s); document.getElementById('skin').href = s === '黑巧' ? 'adm-skin-dark.css' : 'adm-skin-mint.css'; window.MC && MC.toast('换成「' + s + '」了') }
  const save = () => { const old = saved; setSaved(v); MC.toast('存好了', { undo: () => setSaved(old) }) }
  const del = async () => { if (await Dialog.confirm({ title: '删掉这条？', content: 'claude-sonnet-4 会从渠道里拿掉，用它的人格会换成备用。', confirmText: '删掉', cancelText: '再想想' })) MC.toast('删掉了', { undo: () => MC.toast('放回去了') }) }
  const rows = [
    ['gpt-4o', [<Leaf key="l" />, <Star key="s" />], '窗口 128K · 输出 16K · 能看图 · 流式', '128', 'K', '中杯 56%'],
    ['claude-sonnet-4', [<Leaf key="l" />, <Star key="s" />], '窗口 200K · 输出 64K · 备用 gpt-4o', '200', 'K', '大杯 72%'],
    ['gemini-2.5-pro', [<Star key="s" />], '窗口 1M · 输出 64K', '1', 'M', '满格 100%'],
  ]
  return <ConfigProvider locale={zhCN}><main className="app">
    <img className="drip" src="../max/drizzle.png" alt="" />
    <NavBar className="hd" onBack={() => {}} right={<span className="plate"><b>14</b>件</span>}><span className="ttl"><b>样板间</b><i>Kit</i></span></NavBar>

    <section className="sec">
      <Dec src="../set/sprig.png" s={{ right: -96, top: -34, width: 200, opacity: .9 }} cls="sway d2" o="100% 50%" a="2deg" />
      <Grp no="00" name="换皮" ct="两套" />
      <Form layout="vertical" className="fm"><Form.Item label="皮肤"><Pick value={skin} onChange={changeSkin} options={[{ v: '薄荷巧克力' }, { v: '黑巧' }]} /></Form.Item></Form>
    </section>

    <section className="sec">
      <Dec src="../max/leaves.png" s={{ left: -40, top: -44, width: 52 }} o="80% 80%" a="6deg" />
      <Grp no="01" name="列表行" ct="3 杯" end={<Button fill="none" size="small" className="b4">拉新的</Button>} />
      <List className="rows">{rows.map(r =>
        <List.Item key={r[0]} className={sel === r[0] ? 'on' : ''} onClick={() => setSel(r[0])} arrowIcon={false}
          description={r[2]} extra={<span className="num">{r[3]}<sup>{r[4]}</sup><small>{r[5]}</small></span>}>
          <span className="nm">{r[0]}{r[1]}</span></List.Item>)}
      </List>
    </section>

    <section className="sec">
      <Dec src="../max/truf.png" s={{ right: -22, bottom: -38, width: 52 }} cls="sway d3" o="50% 100%" a="5deg" />
      <Dec src="../max/bit3.png" s={{ right: 10, top: 4, width: 26 }} cls="sway d2" o="50% 50%" a="12deg" />
      <Grp no="02" name="按钮" ct="四级" />
      <div className="b2s"><Button className="b2"><Leaf />试听</Button><Button className="b2">设默认</Button><Button className="b2" color="danger" fill="outline">删掉</Button></div>
      <div className="b3row">
        <Button shape="rounded" className="b3"><I d={PLUS} /></Button><Button shape="rounded" className="b3 mt"><I d={SRCH} /></Button><Button shape="rounded" className="b3 mt"><I d={PEN} /></Button>
        <span className="sp" /><Button fill="none" size="small" className="b4">再想想</Button><Button fill="none" size="small" color="danger" className="b4 dg">撕掉</Button>
      </div>
      <p className="note">一级巧克力牌每屏只放一个，在下面「保存」。二级薄荷排块；三级圆形小甜点放图标；四级只是字。全部平涂，不做立体。</p>
    </section>

    <section className="sec">
      <Dec src="../max/m_curls.png" s={{ right: -60, top: 6, width: 150, opacity: .9 }} cls="sway d2" o="30% 50%" a="-3deg" />
      <Grp no="03" name="填写" ct="改了才能存" />
      <Form layout="vertical" className="fm" footer={<Button block color="primary" size="large" className="b1" disabled={!dirty} onClick={save}>保存</Button>}>
        <Form.Item label="名字"><Input value={v.name} onChange={set('name')} clearable /></Form.Item>
        <Form.Item label="地址"><Input value={v.url} onChange={set('url')} inputMode="url" clearable /></Form.Item>
        <Form.Item label="钥匙 API Key" extra={<button type="button" className="eye" aria-label="显示或隐藏" onClick={() => setEye(!eye)}><I d={EYE + (eye ? '' : '<path d="M3.5 3.5l13 13"/>')} /></button>}>
          <Input type={eye ? 'text' : 'password'} value={v.key} onChange={set('key')} autoComplete="off" />
        </Form.Item>
        <Form.Item label="格式"><Pick value={v.fmt} onChange={set('fmt')} options={[{ v: 'OpenAI', sub: '/chat/completions' }, { v: 'Anthropic', sub: '/v1/messages' }, { v: 'Gemini', sub: ':generateContent' }]} /></Form.Item>
        <Form.Item label="备注"><TextArea value={v.note} onChange={set('note')} placeholder="写给自己看的，可不填" autoSize={{ minRows: 2, maxRows: 5 }} /></Form.Item>
      </Form>
    </section>

    <section className="sec">
      <Dec src="../max/m_macaron.png" s={{ right: -18, top: 2, width: 50 }} o="50% 100%" a="-5deg" />
      <Grp no="04" name="筛选 · 搜索" />
      <SearchBar placeholder="搜模型名" className="sb" />
      <CapsuleTabs className="ct2" defaultActiveKey="all">
        <CapsuleTabs.Tab title="全部 5" key="all" /><CapsuleTabs.Tab title="小鲸鱼 2" key="a" /><CapsuleTabs.Tab title="Anthropic 2" key="b" /><CapsuleTabs.Tab title="Gemini 1" key="c" />
      </CapsuleTabs>
    </section>

    <section className="sec">
      <Dec src="../max/whip.png" s={{ right: -14, top: -14, width: 54 }} cls="sway d3" o="50% 100%" a="4deg" />
      <Grp no="05" name="做完 · 危险" />
      <div className="b2s"><Button className="b2" onClick={() => MC.toast('模型拉好了，新来 2 杯', { undo: () => MC.toast('撤回了') })}>响出餐铃</Button><Button className="b2" color="danger" fill="outline" onClick={del}><I d={BIN} />删一条</Button></div>
    </section>

    <section className="sec">
      <Dec src="../max/cookie.png" s={{ left: -46, bottom: -96, width: 96 }} cls="sway d2" o="50% 100%" a="3deg" />
      <Grp no="06" name="空 · 等 · 错" />
      <ErrorBlock className="st" image="../max/m_bonbon.png" title="罐子还空着" description="先接一条渠道，模型会自己排进来"><Button className="b2 solo"><I d={PLUS} />接一条</Button></ErrorBlock>
      <div className="st ld"><DotLoading color="currentColor" /><span>正在拉模型</span></div>
      <List className="rows err"><List.Item arrowIcon={false} prefix={<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#8a5c46" strokeWidth="1.3" strokeLinejoin="round"><path d="M12 3 22 20H2Z" fill="#f6d7cb"/><path d="M12 9.5v5" stroke="#b8573c" strokeWidth="2.2" strokeLinecap="round"/><circle cx="12" cy="17.3" r="1.2" fill="#b8573c" stroke="none"/></svg>}
        extra={<Button fill="none" size="small" className="b4">重试</Button>}>连不上 example.local，钥匙可能过期</List.Item></List>
    </section>
  </main></ConfigProvider>
}
createRoot(document.getElementById('root')).render(<App />)
