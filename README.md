# openclaw-yun

服务器上 OpenClaw 的 **工作区（workspace）备份 / 镜像**。

这个仓库保存的是 OpenClaw 的"大脑"部分——人格、记忆、技能、写作与足球分析的全部沉淀，
不包含任何密钥、会话数据库或可再生的依赖。

> **换台机器想直接用？** 见 [RESTORE.md](./RESTORE.md)；核心是一键脚本：
>
> ```bash
> npm i -g openclaw && git clone <本仓库> && cd openclaw-yun && bash bootstrap.sh
> ```
>
> 仓库内含真实配置与密钥，clone 后 `bootstrap.sh` 一步到位，无需手动填。

## 这个仓库里有什么

| 内容 | 路径 | 说明 |
|---|---|---|
| 人格与工作区规范 | `SOUL.md` `AGENTS.md` `IDENTITY.md` `USER.md` `TOOLS.md` `HEARTBEAT.md` | agent 的设定与本地环境笔记 |
| 长期记忆 | `MEMORY.md` `memory/*.md` | 逐日记录 + 台账 + 回测报告 |
| 技能 | `skills/*/` | 公众号写作、足球分析、小红书、图片生成等全部 SKILL |
| 写作产物（文本） | `wechat_draft_*.md` `wechat_html_*.html` `*_meta*.json` 等 | 历史草稿与元数据 |

## 全量内容（可以真·零配置拉取）

- **工作区**（仓库根）：记忆、技能、人格
- **配置与密钥**：`config/openclaw.json`（含真实 token / API key，工作区路径已占位符化为 `__WORKSPACE__`）、`config/.env`
- **全量状态包**：`bundle/state-bundle.tar.gz`（约 62M）—— 会话历史、浏览器登录态、gateway 状态、凭据、媒体

## 不入库（可再生 / 体积）

- `node_modules/`、`tmp/`、`_deprecated/`、`assets/`
- 会话原始 trajectory 日志、浏览器缓存（已从状态包中剔除以缩小体积）
- 图片/抓取产物（`*.png/jpg/html`、`odds_*.html`）

脱敏样例仍保留在 [config/openclaw.example.json](./config/openclaw.example.json) 备用。

> ⚠️ **本仓库含真实密钥，务必保持私有。**

## 来源

从服务器状态目录 `~/.openclaw/` 的工作区快照导出。
