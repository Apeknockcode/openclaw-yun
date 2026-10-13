# RESTORE.md — 从本仓库恢复 / 迁移 OpenClaw

目标：在新机器上把 OpenClaw 跑起来，并还原这台服务器的工作区（记忆 + 技能 + 人格）。

## 一键（推荐）

```bash
npm i -g openclaw          # 1. 装 OpenClaw（需 Node 22+/24）
git clone git@github.com:Apeknockcode/openclaw-yun.git
cd openclaw-yun
bash bootstrap.sh          # 2. 自动还原工作区+配置+服务
```

`bootstrap.sh` 会自动：同步工作区到 `~/.openclaw/workspace`、生成 `openclaw.json`（路径已适配本机）、
修正工作区内写死的旧绝对路径、跑 `openclaw doctor` 并安装后台服务。

> 若仓库里没有真实 `config/openclaw.json`，脚本会退回脱敏样例，这时需要手动填 `REPLACE_ME`（见下）。

## 手动步骤（备查）

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
- **浏览器登录态**：`browser/` 是 Linux 版 Chromium 数据，跨系统（mac/win）可能需重新登录。

## 全量状态包

`bundle/state-bundle.tar.gz`（约 62M）包含：

| 内容 | 说明 |
|---|---|
| `agents/` | 会话历史（已剔除 trajectory 原始日志与已删除/重置的碎片） |
| `state/` | gateway 状态库 `openclaw.sqlite` |
| `browser/` | 浏览器登录态（已剔除各类缓存；Linux 版 Chromium 数据，跨系统可能需重新登录） |
| `credentials/` `identity/` `devices/` | 凭据与设备标识 |
| `media/` | 历史媒体文件 |

`bootstrap.sh` 若发现该包会自动解压到状态目录，因此 clone + 运行即可还原全部内容。

> 不含：`node_modules/`（依赖，可再生）、会话 trajectory 原始日志、浏览器缓存、工作区图片/草稿产物。
