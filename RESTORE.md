# RESTORE.md — 从本仓库恢复 / 迁移 OpenClaw

目标：在新机器上把 OpenClaw 跑起来，并还原这台服务器的工作区（记忆 + 技能 + 人格）。

## 0. 前置

- 安装 Node（建议 22+，与源机一致的话用 Node 24）
- 安装 OpenClaw CLI：`npm i -g openclaw`（版本尽量与源机对齐，源机为 **2026.7.1**）

## 1. 拉取工作区

```bash
git clone git@github.com:Apeknockcode/openclaw-yun.git
```

把内容放进状态目录的工作区位置（默认 `~/.openclaw/workspace`）：

```bash
# 若 ~/.openclaw 还不存在，先让 OpenClaw 生成一次：openclaw onboard（或 openclaw gateway run 一次）
mkdir -p ~/.openclaw/workspace
rsync -a --exclude=.git/ openclaw-yun/ ~/.openclaw/workspace/
```

## 2. 恢复配置

本仓库**不含密钥**。用脱敏样例重建 `~/.openclaw/openclaw.json`：

```bash
cp openclaw-yun/config/openclaw.example.json ~/.openclaw/openclaw.json
```

然后填入真实值（`REPLACE_ME` 处）：

- `gateway.auth.token` —— 自定义一个长随机串
- `models.providers.openrouter.apiKey`
- 相应 provider 的 `auth.profiles`

并创建 `~/.openclaw/.env`（权限 600）：

```bash
cat > ~/.openclaw/.env <<'EOF'
AISA_API_KEY=<你的值>
OPENROUTER_API_KEY=<你的值>
HF_ENDPOINT=https://hf-mirror.com
EOF
chmod 600 ~/.openclaw/.env ~/.openclaw/openclaw.json
```

## 3. 修正工作区绝对路径（关键）

`openclaw.json` 里的 `agents.defaults.workspace` 需指向本机路径：

```bash
openclaw config set agents.defaults.workspace "$HOME/.openclaw/workspace"
```

工作区内有约 39 个文件**硬编码**了源机的 `/root/.openclaw/workspace`，
迁移到非 root 用户时需批量替换：

```bash
grep -rl '/root/.openclaw/workspace' ~/.openclaw/workspace \
  | xargs sed -i.bak "s#/root/.openclaw/workspace#$HOME/.openclaw/workspace#g"
```

## 4. 重建服务并自检

```bash
openclaw doctor
openclaw gateway install     # 按系统生成 launchd(mac)/systemd(linux)/schtasks(win) 服务
openclaw gateway restart
openclaw status
```

## 5. 运行期注意

- **设备/配对**：新主机上原设备 token 失效，需在 Control UI 重新批准。
- **本地记忆搜索**：会重新下载 embedding 模型；国内需 `HF_ENDPOINT=https://hf-mirror.com`。
- **插件依赖**：`~/.openclaw/npm` 未入库；如需重建 `openclaw plugins update` / 重装。
- **浏览器登录态**：`browser/` 是 Linux 版 Chromium 数据，跨系统不可直接复用，需重新登录。

## 未包含的内容（如需完整还原，请另行保管）

| 内容 | 源机路径 | 大小 | 处理方式 |
|---|---|---|---|
| 会话/对话历史 | `~/.openclaw/agents/main/` | ~395M | 加密打包单独保管 |
| 浏览器登录态 | `~/.openclaw/browser/` | ~187M | 通常可放弃，重新登录 |
| 真实配置与密钥 | `~/.openclaw/openclaw.json`、`.env` | 小 | 密码管理器 / 加密包 |
