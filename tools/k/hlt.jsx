// 健康页 · 基础版：结构照抄 antd-mobile 官方 List / CapsuleTabs / NoticeBar 示例（MIT），不加装饰。
// 后端：GET /api/health/summary（steps_today、sleep_last_night、last_sync_at、stale）、
//       GET /api/health/records（kind = steps / heart_rate / resting_heart_rate / sleep；按 kind 过滤待确认）、POST /api/health/webhook。
import React, { useState } from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, NavBar, List, CapsuleTabs, NoticeBar, Button, Tag } from 'antd-mobile'

const SUM = { steps: '6,284', hr: 72, rest: 58, sleep: '7 小时 40 分', sleepRange: '23:10 – 06:50', sync: '10:52' }
const HOOK = 'https://example.local/api/health/webhook?role_id=r_demo'
const K = { steps: '步数', hr: '心率', sleep: '睡眠' }
const R = [
  { d: '今天', t: '10:52', k: 'steps', v: '+1,860 步', s: '09:00 – 10:52' },
  { d: '今天', t: '09:00', k: 'steps', v: '+2,410 步', s: '07:00 – 09:00' },
  { d: '今天', t: '08:10', k: 'hr', v: '58 bpm', s: '静息心率' },
  { d: '今天', t: '06:55', k: 'steps', v: '+2,014 步', s: '00:00 – 06:55' },
  { d: '今天', t: '06:50', k: 'sleep', v: '7 小时 40 分', s: '23:10 – 06:50' },
  { d: '昨天', t: '20:40', k: 'steps', v: '+3,102 步', s: '12:52 – 20:40' },
  { d: '昨天', t: '18:20', k: 'hr', v: '91 bpm', s: '活动时' },
  { d: '昨天', t: '12:52', k: 'steps', v: '+640 步', s: '12:30 – 12:52' },
  { d: '昨天', t: '12:30', k: 'steps', v: '+1,488 步', s: '09:00 – 12:30' },
  { d: '昨天', t: '08:05', k: 'hr', v: '57 bpm', s: '静息心率' },
]

function App() {
  const [tab, setTab] = useState('all'), [rest, setRest] = useState(false), [stale, setStale] = useState(false)
  const rows = R.filter(r => tab === 'all' || r.k === tab)
  const days = [...new Set(rows.map(r => r.d))]
  const copy = () => { navigator.clipboard?.writeText(HOOK).catch(() => {}); MC.toast('地址已复制') }
  return <>
    <NavBar onBack={() => { location.href = 'set.html' }}>健康</NavBar>
    {stale && <NoticeBar content="3 小时没同步了，下面是那时候的数" color="alert" wrap />}
    <List mode="card" header="今天">
      <List.Item description="今天累计" onClick={() => setTab('steps')} extra={<span className="k-big">{SUM.steps}</span>}>步数</List.Item>
      <List.Item description={rest ? '静息心率 · 点一下看实时' : '实时 · 点一下看静息'} onClick={() => setRest(!rest)}
        extra={<span className="k-big">{rest ? SUM.rest : SUM.hr}<small> bpm</small></span>}>心率</List.Item>
      <List.Item description={SUM.sleepRange} onClick={() => setTab('sleep')} extra={<span className="k-big">{SUM.sleep}</span>}>昨晚睡眠</List.Item>
      <List.Item description={stale ? '超过 3 小时，演示：点一下恢复' : '演示：点一下看过期的样子'} onClick={() => setStale(!stale)}
        extra={<Tag color={stale ? 'warning' : 'success'} fill="outline">{stale ? '过期' : '正常'}</Tag>}>同步于 {SUM.sync}</List.Item>
    </List>
    <CapsuleTabs activeKey={tab} onChange={setTab}>
      <CapsuleTabs.Tab title="全部" key="all" />
      <CapsuleTabs.Tab title="步数" key="steps" />
      <CapsuleTabs.Tab title="心率" key="hr" />
      <CapsuleTabs.Tab title="睡眠" key="sleep" />
    </CapsuleTabs>
    {days.map(d => <List mode="card" header={d} key={d}>
      {rows.filter(r => r.d === d).map((r, i) => <List.Item key={i} prefix={<span className="k-mute k-time">{r.t}</span>} description={r.s} extra={r.v}>{K[r.k]}</List.Item>)}
    </List>)}
    {!rows.length && <List mode="card"><List.Item>这一类还没有记录</List.Item></List>}
    <List mode="card" header="接手环">
      <List.Item description="手环或快捷指令把数据发到这个地址，要带签名" extra={<Button size="mini" onClick={copy}>复制</Button>}>
        <span className="k-url">{HOOK}</span></List.Item>
    </List>
    <div style={{ height: 24 }} />
  </>
}

createRoot(document.getElementById('root')).render(<ConfigProvider locale={window.MCK.zhCN}><App /></ConfigProvider>)
