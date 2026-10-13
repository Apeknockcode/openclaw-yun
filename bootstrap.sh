#!/usr/bin/env bash
# ============================================================
# OpenClaw 便携引导脚本
# 把本仓库还原成一个可用的 OpenClaw：状态目录 + 工作区 + 配置 + 服务
# 用法：
#   git clone <repo> && cd <repo> && bash bootstrap.sh
# 兼容 macOS / Linux / WSL / Git Bash（Windows 需在 WSL 或 Git Bash 中运行）
# ============================================================
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
WS="$STATE/workspace"

echo "==> 仓库目录 : $REPO"
echo "==> 状态目录 : $STATE"

# 0) 依赖检查
if ! command -v openclaw >/dev/null 2>&1; then
  echo "!! 未检测到 openclaw CLI。请先安装："
  echo "   npm i -g openclaw"
  exit 1
fi

mkdir -p "$STATE"

# 1) 同步工作区（排除仓库自身的 git 与引导文件）
if command -v rsync >/dev/null 2>&1; then
  rsync -a \
    --exclude='.git/' --exclude='config/' --exclude='bootstrap.sh' \
    --exclude='README.md' --exclude='RESTORE.md' \
    "$REPO/" "$WS/"
else
  mkdir -p "$WS"
  cp -a "$REPO/." "$WS/"
  rm -rf "$WS/.git" "$WS/config" "$WS/bootstrap.sh" "$WS/README.md" "$WS/RESTORE.md"
fi

# 2) 配置：优先真实配置 config/openclaw.json，否则用脱敏样例
if [ -f "$REPO/config/openclaw.json" ]; then
  SRC="$REPO/config/openclaw.json"
  echo "==> 使用真实配置 config/openclaw.json"
else
  SRC="$REPO/config/openclaw.example.json"
  echo "!! 未找到 config/openclaw.json，使用脱敏样例（需手动填 REPLACE_ME）"
fi
sed "s#__WORKSPACE__#$WS#g" "$SRC" > "$STATE/openclaw.json"
chmod 600 "$STATE/openclaw.json"

# 3) 环境变量文件
if [ -f "$REPO/config/.env" ]; then
  cp "$REPO/config/.env" "$STATE/.env"; chmod 600 "$STATE/.env"
  echo "==> 已恢复 .env"
elif [ -f "$REPO/config/.env.example" ]; then
  cp "$REPO/config/.env.example" "$STATE/.env"; chmod 600 "$STATE/.env"
  echo "!! 已生成 $STATE/.env（来自 .env.example），请填入真实密钥"
fi

# 4) 修正工作区内写死的旧绝对路径（源机：/root/.openclaw/workspace）
OLD="/root/.openclaw/workspace"
if [ "$WS" != "$OLD" ]; then
  grep -rl -- "$OLD" "$WS" 2>/dev/null | while IFS= read -r f; do
    sed -i.bak "s#$OLD#$WS#g" "$f" && rm -f "$f.bak"
  done
  echo "==> 已修正工作区内的绝对路径 -> $WS"
fi

# 5) 健康检查 + 安装后台服务
echo "==> openclaw doctor"
openclaw doctor || true
echo "==> openclaw gateway install"
openclaw gateway install || true

cat <<EOF

==> 完成。下一步：
    openclaw gateway restart
    openclaw status
    openclaw dashboard        # 打开控制台

提示：
 - 国内环境请确保已设置 HF_ENDPOINT=https://hf-mirror.com（本地记忆模型下载用）
 - 新机器首次需在 Control UI 里重新批准设备
EOF
