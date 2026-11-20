// 图表：AntV F2（MIT）。只用官方 Interval / Axis / Tooltip / Legend，不加装饰；颜色读 --adm-* 变量。
import { jsx, Canvas, Chart, Interval, Axis, Legend } from '@antv/f2'
const cv = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim()
export function drawBars(el, data, { stack = true, colors } = {}) {
  const w = el.clientWidth, h = el.clientHeight, ctx = el.getContext('2d'), pr = window.devicePixelRatio || 2
  const font = getComputedStyle(document.body).fontFamily, tx = cv('--adm-color-text-secondary'), bd = cv('--adm-color-border')
  const c = new Canvas({ context: ctx, pixelRatio: pr, width: w, height: h, theme: { fontFamily: font },
    children: jsx(Chart, { data, children: [
      jsx(Axis, { field: 'x', style: { label: { fill: tx, fontSize: '22px' }, line: null } }),
      jsx(Axis, { field: 'y', tickCount: 4, style: { label: { fill: tx, fontSize: '20px' }, grid: { stroke: bd, lineDash: null } } }),
      jsx(Interval, { x: 'x', y: 'y', color: { field: 'type', range: colors || [cv('--adm-color-primary'), cv('--adm-color-success')] }, adjust: stack ? 'stack' : undefined }),
      jsx(Legend, { position: 'top', style: { justifyContent: 'flex-start' }, itemFormatter: v => v, nameStyle: { fill: tx, fontSize: '22px' } }),
    ] }) })
  c.render(); return c
}
