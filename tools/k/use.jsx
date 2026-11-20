// 用量页 · 基础版：antd-mobile List / CapsuleTabs 示例 + AntV F2 柱状图（MIT），不加装饰。
// 后端：GET /api/usage/summary?from&to（chat、memory、context、index、unknown_calls），按天或按周各查一次。
import React, { useState, useEffect, useRef } from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, NavBar, List, CapsuleTabs } from 'antd-mobile'
import { drawBars } from './chart.js'

const DAY = ['周一', '周二', '周三', '周四', '今天'], CHAT = [22.4, 18.0, 25.6, 17.3, 12.8], MEM = [6.1, 8.4, 5.2, 7.9, 4.7]
const WEEK = [['第 43 周', 151.2], ['第 44 周', 176.5], ['第 45 周', 205.8], ['本周', 128.4]]
const dayData = DAY.flatMap((x, i) => [{ x, y: CHAT[i], type: '聊天' }, { x, y: MEM[i], type: '记忆整理' }])
const weekData = WEEK.map(([x, y]) => ({ x, y, type: '合计' }))

function Bars({ tab }) {
  const ref = useRef()
  useEffect(() => { const c = drawBars(ref.current, tab === 'day' ? dayData : weekData); return () => c.destroy() }, [tab])
  return <canvas ref={ref} className="k-chart" />
}

function App() {
  const [tab, setTab] = useState('day')
  return <>
    <NavBar onBack={() => { location.href = 'set.html' }}>用量</NavBar>
    <List mode="card" header="本周 · 第 46 周">
      <List.Item description="上周同一时候 183.4 万，到了七成" extra={<span className="k-big">128.4<small> 万</small></span>}>tokens</List.Item>
    </List>
    <CapsuleTabs activeKey={tab} onChange={setTab}>
      <CapsuleTabs.Tab title="本周每天" key="day" />
      <CapsuleTabs.Tab title="最近四周" key="week" />
    </CapsuleTabs>
    <List mode="card" header={tab === 'day' ? '单位：万 tokens' : '单位：万 tokens，本周到今天'}>
      <List.Item><Bars tab={tab} /></List.Item>
    </List>
    <List mode="card" header="本周分类">
      <List.Item description="和角色聊天" extra="96.1 万">聊天</List.Item>
      <List.Item description="后台整理记忆" extra="32.3 万">记忆整理</List.Item>
      <List.Item description="这些调用没报用量，没算进上面的数" extra="12 次">没报用量的调用</List.Item>
    </List>
    <div style={{ height: 24 }} />
  </>
}
createRoot(document.getElementById('root')).render(<ConfigProvider locale={window.MCK.zhCN}><App /></ConfigProvider>)
