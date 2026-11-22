// 样板组件（全站公用）：图标、分组标题、装饰、就地小选单
import React, { useState } from 'react'
import { Popover } from 'antd-mobile'
export const Leaf = () => <svg className="ico" viewBox="0 0 16 16" fill="#a6d9c4" stroke="#5b8a74" strokeWidth="1"><path d="M2.5 13.5C2.5 6 7 2.5 13.5 2.5 13.5 9 10 13.5 2.5 13.5Z"/><path d="M3 13 10 6" fill="none"/></svg>
export const Star = () => <svg className="ico" viewBox="0 0 16 16" fill="#f6e3b8" stroke="#a9825f" strokeWidth="1" strokeLinejoin="round"><path d="M8 1.8 9.8 6l4.4.4-3.3 2.9 1 4.4L8 11.4l-3.9 2.3 1-4.4L1.8 6.4 6.2 6Z"/></svg>
export const I = ({ d }) => <svg className="bi" viewBox="0 0 20 20" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: d }} />
export const PLUS = '<path d="M10 4v12M4 10h12"/>', SRCH = '<circle cx="8.8" cy="8.8" r="5"/><path d="m12.6 12.6 3.6 3.6"/>', PEN = '<path d="m4 16 1-4 8-8 3 3-8 8Z"/>', BIN = '<path d="M4.5 6h11M8 6V4h4v2M6 6l1 10h6l1-10"/>'
export const EYE = '<path d="M2 10s3-5.5 8-5.5S18 10 18 10s-3 5.5-8 5.5S2 10 2 10Z"/><circle cx="10" cy="10" r="2.4"/>'
export const Chev = () => <svg className="chev" viewBox="0 0 10 10" fill="none" strokeWidth="1.6" strokeLinecap="round"><path d="m2 3.5 3 3 3-3"/></svg>
export const Dec = ({ src, s, cls = 'sway', o = '50% 90%', a = '4deg' }) => <img className={'dec ' + cls} src={src} alt="" style={{ ...s, '--o': o, '--a': a }} />
export const Grp = ({ no, name, ct, end }) => <div className="grp"><span className="no">{no}</span><span className="rib"><h2>{name}</h2>{ct && <span className="ct">{ct}</span>}</span><span className="end">{end}</span></div>

// 就地小选单：antd-mobile Popover.Menu，贴着字段下沿浮出
export function Pick({ value, options, onChange }) {
  const [open, setOpen] = useState(false)
  return <Popover.Menu visible={open} onVisibleChange={setOpen} trigger="click" placement="bottom-start" mode="light"
    actions={options.map(o => ({ key: o.v, text: <span className={'opt' + (o.v === value ? ' on' : '')}><span>{o.v}</span>{o.sub && <small>{o.sub}</small>}<svg className="tick" viewBox="0 0 14 14" fill="none" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="m2.5 7.5 3 3 6-7"/></svg></span> }))}
    onAction={a => { onChange(a.key); setOpen(false) }}>
    <button type="button" className={'pickf' + (open ? ' is-open' : '')}><span>{value}</span><Chev /></button>
  </Popover.Menu>
}

