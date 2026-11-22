// 基础版公用小件（只用 antd 组件拼，不加装饰）
import React, { useState } from 'react'
import { Popover, Form, Input } from 'antd-mobile'
export const Ico = ({ d }) => <svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: d }} />
export const DOWN = '<path d="m6 8 4 4 4-4"/>', MORE = '<circle cx="5" cy="10" r=".7"/><circle cx="10" cy="10" r=".7"/><circle cx="15" cy="10" r=".7"/>'
export const EYE = '<path d="M2 10s3-5.5 8-5.5S18 10 18 10s-3 5.5-8 5.5S2 10 2 10Z"/><circle cx="10" cy="10" r="2.4"/>'
// 下拉：Popover.Menu，选中项打勾
export function Pick({ value, options, onChange, ph }) {
  return <Popover.Menu trigger="click" placement="bottom-end" actions={options.map(v => ({ key: v, text: v + (v === value ? '  ✓' : '') }))} onAction={a => onChange(a.key)}>
    <span className="k-pick">{value || ph}<Ico d={DOWN} /></span>
  </Popover.Menu>
}
// 密钥：密码框 + 眼睛
export function KeyItem({ label, value, onChange, required, ph = '粘贴密钥' }) {
  const [eye, setEye] = useState(false)
  return <Form.Item label={label} required={required} extra={<span className="k-eye" onClick={() => setEye(!eye)}><Ico d={EYE + (eye ? '' : '<path d="M3.5 3.5l13 13"/>')} /></span>}>
    <Input type={eye ? 'text' : 'password'} value={value} onChange={onChange} placeholder={ph} autoComplete="off" /></Form.Item>
}
export const pack = d => JSON.stringify(d)
