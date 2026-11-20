#!/bin/sh
# 需要 /workspace/work/adm 下 npm i antd-mobile@5 react@18 react-dom@18 esbuild
set -e
H=$(cd "$(dirname "$0")/../../.." && pwd)
cd /workspace/work/adm
NODE_PATH=/workspace/work/adm/node_modules npx esbuild "$H/tools/kit/adm/app.jsx" --bundle --minify --jsx=automatic --loader:.js=jsx --define:process.env.NODE_ENV='"production"' --outfile="$H/p/kit/adm.js"
