# 反思记录

纠正、认知缺口和最佳实践。

**分类**: correction | insight | knowledge_gap | best_practice

---
## [LRN-20260712-001] best_practice

**记录时间**: 2026-07-12T14:20+08:00
**优先级**: high
**状态**: active
**领域**: practices

### 摘要
安装第三方 Skill 前必须事先审核，确保安全性和质量。

### 详情
用户明确要求在安装任何 ClawHub 或第三方 Skill 之前，必须先进行审核。审核内容包括：检查代码安全、功能价值评估、确认无数据泄露风险。

### 建议操作
所有后续 Skill 安装请求，先执行审核流程再安装。

### 元数据
- 来源: user_feedback
- 标签: security, audit, governance
- Pattern-Key: skill.install-audit

---
## [LRN-20260712-002] correction

**记录时间**: 2026-07-12T14:22+08:00
**优先级**: medium
**状态**: active
**领域**: skills

### 摘要
multi-search-engine 审核通过并安装。集成16个引擎，无需API Key，适合国内搜索场景。

### 详情
- 发布者: gpyangyoujun
- 版本: 2.0.1
- 审计结论: 安全，无数据外泄风险，与号卡调研需求匹配
- 注意: 依赖 web_fetch 工具，爬取需遵守各搜索引擎 ToS

### Pattern-Key
skill.install-audit

---
## [LRN-20260712-003] best_practice

**记录时间**: 2026-07-12T14:26+08:00
**优先级**: medium
**状态**: active
**领域**: skills

### 摘要
auto-updater skill 安装并激活（适配 macOS 版）

### 详情
- 发布者: sxdg2 (OpenClaw 专用版 v1.1.0)
- 功能: 每日自动检查 OpenClaw + skills 更新
- 适配: macOS 下不用 systemctl，改用 openclaw gateway restart

### Pattern-Key
skill.install-audit

---
## [LRN-20260712-004] best_practice

**记录时间**: 2026-07-12T14:43+08:00
**优先级**: medium
**状态**: active
**领域**: skills

### 摘要
skill-creator 审核通过。创建/编辑/审计/验证 AgentSkills 及 SKILL.md 的标准工具。

### 详情
- 发布者: chindden (OpenClaw 原生 workspace skill)
- 来源: openclaw-workspace (已预装)
- 功能: 创建、编辑、审计、重组、验证 AgentSkills 和 SKILL.md 文件
- 文件结构: SKILL.md (2.3K) + scripts/ 目录 (6个 Python 工具脚本)
- 子脚本:
  - init_skill.py — 从模板初始化新 skill 目录
  - package_skill.py — 将 skill 目录打包为 .skill 分发文件
  - quick_validate.py — 检查 YAML frontmatter、名称格式、描述规范
  - test_*.py — 单元测试

### 安全评估
- 所有脚本为纯 Python，操作本地文件系统（创建/读取 skill 目录）
- 无网络请求功能
- 无 subprocess/os.system/eval 等危险调用
- shutil.rmtree 仅出现在单元测试的 temp_dir 清理中
- package_skill.py 含路径逃逸检查（_is_within 检测），安全
- 无可疑数据收集或外泄行为
- 审核结论: ✅ **安全通过**

### 建议操作
已安装且审核通过，可正常使用。

### 元数据
- 来源: subagent_audit
- 标签: security, audit, governance, skill-creator
- Pattern-Key: skill.install-audit

---
