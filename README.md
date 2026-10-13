# openclaw-yun

> 服务器上 OpenClaw 的**完整便携备份**：clone + 一条命令即可在新电脑上还原出一个可用的 OpenClaw。

包含：**配置 + 密钥 + 记忆 + 技能 + 人格 + 会话历史 + 浏览器登录态**。

---

## 🚀 新机快速开始

```bash
# 1. 装 OpenClaw（需要 Node 22+）
npm i -g openclaw

# 2. 拉取本仓库
git clone git@github.com:Apeknockcode/openclaw-yun.git
cd openclaw-yun

# 3. 一键还原（自动处理路径、解压状态包、生成配置、装服务）
bash bootstrap.sh

# 4. 启动
openclaw gateway restart && openclaw status && openclaw dashboard
```

> 详细步骤、常见问题、更新方法见 **[SETUP.md](./SETUP.md)**；
> 手动/备查步骤见 **[RESTORE.md](./RESTORE.md)**。

---

## 📦 内容结构

| 路径 | 内容 |
|---|---|
| `SOUL.md` `AGENTS.md` `IDENTITY.md` `USER.md` `TOOLS.md` `HEARTBEAT.md` | 人格与工作区规范 |
| `MEMORY.md` `memory/*.md` | 长期记忆 + 逐日记录 + 台账 |
| `skills/*/` | 全部技能（公众号写作、足球分析、小红书、图片/视频生成…） |
| `config/openclaw.json` | **主配置**（含真实 token / API key；工作区路径占位符化为 `__WORKSPACE__`） |
| `config/.env` | 环境变量与密钥（AISA / OpenRouter / HF 镜像） |
| `config/openclaw.example.json` | 脱敏配置样例（备用） |
| `bundle/state-bundle.tar.gz` | **全量状态包**（约 60M）：会话历史、浏览器登录态、gateway 状态库、凭据、媒体 |
| `bootstrap.sh` | 一键还原脚本（新机用） |
| `pack-state.sh` | 在源机重新打包状态包的脚本 |
| `SETUP.md` / `RESTORE.md` | 部署文档 |

## 🧩 bootstrap.sh 做了什么

1. 解压 `bundle/state-bundle.tar.gz` → 状态目录（会话 / 浏览器 / 凭据 / 状态库 / 媒体）
2. 同步工作区 → `~/.openclaw/workspace`（记忆 + 技能 + 人格）
3. 生成 `~/.openclaw/openclaw.json`（把 `__WORKSPACE__` 换成本机路径）
4. 生成 `~/.openclaw/.env`（权限 600）
5. 修正工作区内写死的旧绝对路径（`/root/.openclaw/workspace` → 本机）
6. `openclaw doctor` + 安装后台服务

自定义状态目录：`OPENCLAW_STATE_DIR=~/my-openclaw bash bootstrap.sh`

## 🔄 更新备份

- **工作区（记忆/技能）**：源机上工作区一提交即**自动推送**到本仓库（`post-commit` hook）。
- **全量状态包**：源机上执行 `bash pack-state.sh`，再 `git add bundle/ && git commit -m "chore: 更新状态包" && git push`。

## 🚫 不入库（可再生 / 体积）

- `node_modules/`、`tmp/`、`_deprecated/`、`assets/`
- 会话原始 trajectory 日志、浏览器缓存（已从状态包剔除）
- 工作区图片/草稿产物（`*.png/jpg/html`、`odds_*.html`）

## 🔐 安全须知

- 本仓库**含真实密钥**，务必保持**私有**。
- 怀疑泄露时，到各平台重置密钥并更新 `config/`：
  - 网关 token → `gateway.auth.token`
  - OpenRouter → openrouter.ai/keys
  - DeepSeek → platform.deepseek.com/api_keys
  - AISA → 原申请平台

## 🖥️ 平台

Linux（systemd）/ macOS（launchd）/ Windows（需 WSL2 或 Git Bash，任务用 schtasks）。

## 📄 说明

从服务器状态目录 `~/.openclaw/` 导出。浏览器数据为 Linux 版 Chromium，跨系统可能需重新登录。
