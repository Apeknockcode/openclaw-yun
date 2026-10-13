#!/usr/bin/env bash
# ============================================================
# 在【源机】上重新打包全量状态包 -> bundle/state-bundle.tar.gz
# 用法（在仓库根目录）：
#   bash pack-state.sh
# 说明：会剔除会话 trajectory 原始日志与浏览器缓存以控制体积。
# ============================================================
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "==> 源状态目录: $STATE"

for d in agents state media credentials identity devices browser; do
  [ -e "$STATE/$d" ] || { echo "   跳过（不存在）: $d"; continue; }
  rsync -a --relative \
    --exclude='agents/main/sessions/*.trajectory.jsonl' \
    --exclude='agents/main/sessions/*.trajectory-path.json' \
    --exclude='agents/main/sessions/*.deleted.*' \
    --exclude='agents/main/sessions/*.reset.*' \
    --exclude='browser/openclaw/user-data/Default/Cache' \
    --exclude='browser/openclaw/user-data/Default/Code Cache' \
    --exclude='browser/openclaw/user-data/Default/GPUCache' \
    --exclude='browser/openclaw/user-data/Default/DawnGraphiteCache' \
    --exclude='browser/openclaw/user-data/Default/DawnWebGPUCache' \
    --exclude='browser/openclaw/user-data/Default/Service Worker/CacheStorage' \
    --exclude='browser/openclaw/user-data/Default/Service Worker/ScriptCache' \
    --exclude='browser/openclaw/user-data/GraphiteDawnCache' \
    --exclude='browser/openclaw/user-data/BrowserMetrics*' \
    --exclude='browser/openclaw/user-data/Crashpad' \
    --exclude='browser/openclaw/user-data/ShaderCache' \
    --exclude='browser/openclaw/user-data/GrShaderCache' \
    "$STATE/./$d" "$TMP/"
done

mkdir -p "$REPO/bundle"
if command -v pigz >/dev/null 2>&1; then
  tar -C "$TMP" -cf - . | pigz -p 4 -6 > "$REPO/bundle/state-bundle.tar.gz"
else
  tar -C "$TMP" -cf - . | gzip -6 > "$REPO/bundle/state-bundle.tar.gz"
fi

echo "==> 完成:"; ls -lh "$REPO/bundle/state-bundle.tar.gz"
echo "==> 提交并推送:"
echo "    git add bundle/ && git commit -m 'chore: 更新状态包' && git push"
