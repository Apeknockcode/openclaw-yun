# 新机部署指南（SETUP）

把本仓库的 OpenClaw 完整部署到一台**新电脑**上的操作手册。
含：配置、密钥、记忆、技能、会话历史、浏览器登录态。

---

## 0. 准备

| 需要 | 说明 |
|---|---|
| Node.js | 22 或 24（`node -v` 确认） |
| npm | 随 Node 自带 |
| git | 有即可 |
| 网络 | 能访问 github.com（国内建议用 SSH + 已配 deploy key） |
| 系统 | macOS / Linux / **Windows 需在 WSL2 或 Git Bash 中操作** |

## 1. 安装 OpenClaw

```bash
node -v                       # 确保 >= 22
npm i -g openclaw
openclaw --version            # 期望 2026.7.1 或兼容版本
```

> 用 nvm 的话先 `nvm install 24 && nvm use 24`。

## 2. 拉取仓库

```bash
# SSH（推荐）
git clone git@github.com:Apeknockcode/openclaw-yun.git
cd openclaw-yun

# 或用 HTTPS（私有仓库需 GitHub 账号 / PAT）
git clone https://github.com/Apeknockcode/openclaw-yun.git
```

## 3. 一键还原

```bash
bash bootstrap.sh
```

脚本会自动完成：

1. 解压 `bundle/state-bundle.tar.gz` → 状态目录（会话历史 / 浏览器 / 凭据 / 状态库 / 媒体）
2. 同步工作区 → `~/.openclaw/workspace`（记忆 + 技能 + 人格）
3. 生成 `~/.openclaw/openclaw.json`（用仓库里的真实配置，并把工作区路径适配成本机）
4. 生成 `~/.openclaw/.env`（真实密钥，权限 600）
5. 修正工作区内写死的旧绝对路径（`/root/.openclaw/workspace` → 本机路径）
6. 运行 `openclaw doctor` 并安装后台服务

自定义状态目录（可选）：

```bash
OPENCLAW_STATE_DIR=~/my-openclaw bash bootstrap.sh
```

## 4. 启动并验证

```bash
openclaw gateway restart
openclaw status
openclaw dashboard            # 打开控制台
```

`openclaw status` 里应看到 gateway running、sessions 已恢复。

## 5. 首次使用必做

- [ ] **批准设备**：Control UI → Devices / 或 `openclaw devices list`，批准新机的设备（原机器 token 不通用）
- [ ] **密钥轮换后同步**：若你换了 key，更新 `config/.env` 和 `config/openclaw.json` 后重新跑 `bootstrap.sh`（或直接改 `~/.openclaw/`）
- [ ] **国内镜像**：确认 `HF_ENDPOINT=https://hf-mirror.com`（本地记忆模型下载用，已含在 `.env`）
- [ ] **检查定时任务**：`openclaw cron list`，确认符合预期

## 6. 平台差异

| 系统 | 后台服务 | 备注 |
|---|---|---|
| Linux | systemd 用户服务 | `openclaw gateway install` 自动装 |
| macOS | launchd | 首次可能需在「系统设置 → 通用 → 登录项」放行 |
| Windows | schtasks | 必须在 WSL2 / Git Bash 内运行脚本 |

## 7. 常见问题

**`dubious ownership` 报错**
```bash
git config --global --add safe.directory "$(pwd)"
```

**路径不对 / 工作区找不到**：检查并修正
```bash
openclaw config set agents.defaults.workspace "$HOME/.openclaw/workspace"
```

**插件依赖缺失**（`node_modules` 未入库）：
```bash
openclaw plugins update
# 或按需重装：openclaw plugins install <spec>
```

**端口被占用**：改 `gateway.port`（默认 18789）后 `openclaw gateway restart`。

**浏览器登录态在新系统失效**：浏览器数据是 Linux 版 Chromium，mac/win 上可能需重新登录一次。

**密钥安全**：本仓库含真实密钥，务必保持**私有**；如怀疑泄露立即在各平台轮换。

## 8. 以后如何更新这份备份

**工作区（记忆/技能）**：服务器上工作区一有提交就**自动推送**到本仓库（post-commit hook），无需手动操作。

**全量状态包（会话/浏览器等）**：在**源机**上重打并推送：

```bash
cd ~/openclaw-yun          # 或服务器上的工作区仓库
bash pack-state.sh         # 重新生成 bundle/state-bundle.tar.gz
git add bundle/ && git commit -m "chore: 更新状态包" && git push
```

> 状态包约 60M+，GitHub 会提示 >50MB（正常）。别频繁重打，以免仓库膨胀。

## 9. 目录速查

| 路径 | 内容 |
|---|---|
| `~/.openclaw/openclaw.json` | 主配置（含密钥） |
| `~/.openclaw/.env` | 环境变量 / 密钥 |
| `~/.openclaw/workspace/` | 工作区（记忆、技能、人格） |
| `~/.openclaw/agents/` | 会话历史 |
| `~/.openclaw/browser/` | 浏览器登录态 |
| `~/.openclaw/state/` | gateway 状态库 |
