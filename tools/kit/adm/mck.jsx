// 全站公用底子：React 18 + antd-mobile v5 + 样板组件，挂到 window.MCK。各页的 jsx 通过 shim 用它，不再各打一份。
import * as React from 'react'
import * as jsxRuntime from 'react/jsx-runtime'
import * as ReactDOMClient from 'react-dom/client'
import * as antd from 'antd-mobile'
import zhCN from 'antd-mobile/es/locales/zh-CN'
import * as kit from './kit.jsx'
window.MCK = { React, jsxRuntime, ReactDOMClient, antd, kit, zhCN }
