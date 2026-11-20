// 设置页 · 基础版：结构和间距照抄 antd-mobile 官方 List 示例（MIT），不加装饰。
// 数据是演示数字（与正式页 p/set 一致）；后端对应见 DESIGN §3.2「设置」。
import React from 'react'
import { createRoot } from 'react-dom/client'
import { ConfigProvider, NavBar, List, Tag, ProgressBar, Space } from 'antd-mobile'

const go = p => () => { location.href = p }
const soon = t => () => MC.toast(t + '的基础版下一步做')

function App() {
  return <>
    <NavBar backArrow={false}>设置</NavBar>

    <List mode="card" header="本周用量 · 第 46 周">
      <List.Item description="比上周同一时候，到了七成" extra={<span className="k-big">128.4<small> 万</small></span>} onClick={soon('用量')}>tokens</List.Item>
      <List.Item extra="96.1 万">聊天</List.Item>
      <List.Item extra="32.3 万">记忆整理</List.Item>
      <List.Item><ProgressBar percent={70} text="70%" /></List.Item>
    </List>

    <List mode="card" header="服务">
      <List.Item onClick={go('chn.html')} description="13 个模型" extra={<Space style={{ '--gap': '6px' }}><Tag color="danger" fill="outline">备用超时</Tag><span>3 条</span></Space>}>渠道和模型</List.Item>
      <List.Item onClick={go('snd.html')} description="默认：晚风" extra="3 种">声音</List.Item>
      <List.Item onClick={go('hlt.html')} description="10:52 同步" extra="6,284 步">健康</List.Item>
    </List>

    <List mode="card" header="网关工具">
      <List.Item extra="3 个" description="记忆提议、健康查询、网页搜索">工具</List.Item>
      <List.Item extra={<Tag color="success" fill="outline">正常</Tag>}>网页搜索</List.Item>
      <List.Item extra={<Tag fill="outline">未连接</Tag>}>MCP</List.Item>
    </List>

    <List mode="card" header="连接">
      <List.Item onClick={soon('连接')} description="网关地址和管理密钥，只存在这次打开">重新连接</List.Item>
    </List>
  </>
}

createRoot(document.getElementById('root')).render(<ConfigProvider locale={window.MCK.zhCN}><App /></ConfigProvider>)
