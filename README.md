# openclaw-yun

服务器上 OpenClaw 的 **工作区（workspace）备份 / 镜像**。

这个仓库保存的是 OpenClaw 的"大脑"部分——人格、记忆、技能、写作与足球分析的全部沉淀，
不包含任何密钥、会话数据库或可再生的依赖。

> 恢复/迁移步骤见 [RESTORE.md](./RESTORE.md)。

## 这个仓库里有什么

| 内容 | 路径 | 说明 |
|---|---|---|
| 人格与工作区规范 | `SOUL.md` `AGENTS.md` `IDENTITY.md` `USER.md` `TOOLS.md` `HEARTBEAT.md` | agent 的设定与本地环境笔记 |
| 长期记忆 | `MEMORY.md` `memory/*.md` | 逐日记录 + 台账 + 回测报告 |
| 技能 | `skills/*/` | 公众号写作、足球分析、小红书、图片生成等全部 SKILL |
| 写作产物（文本） | `wechat_draft_*.md` `wechat_html_*.html` `*_meta*.json` 等 | 历史草稿与元数据 |

## 明确**不**会入库的东西（见 `.gitignore`）

- **密钥/凭据**：`openclaw.json`、`.env`、`wc-profiles/`、`*token*`、`*secret*`、`*.key`
- **会话与运行时状态**：`agents/`（SQLite + 对话历史）、`browser/`（浏览器登录态）
- **可再生产物**：`node_modules/`、`tmp/`、`_deprecated/`、`assets/`
- **图片/抓取产物**：`*.png/jpg/html`、`odds_*.html`

脱敏后的配置样例放在 [config/openclaw.example.json](./config/openclaw.example.json)。

## 来源

从服务器状态目录 `~/.openclaw/` 的工作区快照导出。
