#!/bin/sh
# 依赖装在 /workspace/work/adm：npm i antd-mobile@5 react@18 react-dom@18 esbuild
# 1) 公用底子 p/kit/mck.js + mck-adm.css（antd 自带样式）
# 2) 各页 jsx：用 shim 引 window.MCK，体积很小。用法：build.sh [页面jsx 输出js]...
set -e
H=$(cd "$(dirname "$0")/../../.." && pwd);S=$H/tools/kit/adm/shim
export NODE_PATH=/workspace/work/adm/node_modules
cd /workspace/work/adm
npx esbuild "$H/tools/kit/adm/mck.jsx" --bundle --minify --jsx=automatic --define:process.env.NODE_ENV='"production"' --outfile="$H/p/kit/mck.js"
mv "$H/p/kit/mck.css" "$H/p/kit/mck-adm.css"
page(){ npx esbuild "$1" --bundle --minify --jsx=automatic --define:process.env.NODE_ENV='"production"' \
  --alias:react/jsx-runtime=$S/jsx-runtime.js --alias:react-dom/client=$S/react-dom-client.js --alias:react=$S/react.js --alias:antd-mobile=$S/antd.js --alias:mck-kit=$S/kit.js --outfile="$2"; }
page "$H/tools/kit/adm/app.jsx" "$H/p/kit/adm.js"
while [ $# -ge 2 ]; do page "$H/$1" "$H/$2"; shift 2; done
