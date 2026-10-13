---
name: "context-economy"
description: "OpenClaw 上下文管理策略，通过轻量上下文、子代理隔离、内存剪枝等手段减少 Token 消耗"
---

# context-economy - OpenClaw 上下文节能策略

减少 Token 消耗的上下文管理技能。通过合理使用 OpenClaw 的上下文控制机制，在保持能力的同时大幅降低每次会话的 Token 用量。

## 核心策略

### 1. 轻量上下文（lightContext）

在子代理或 cron 任务中使用 `lightContext: true` 可大幅减少启动时加载的上下文量。

```json
// 子代理 - lightContext
{
  "task": "执行简单任务",
  "lightContext": true
}

// Cron 任务 - lightContext
{
  "kind": "agentTurn",
  "message": "每日检查",
  "lightContext": true
}
```

**适用场景：** 简单明确的任务、定时检查、数据采集、不需要完整上下文的工作。

### 2. 子代理隔离（sessions_spawn）

将独立任务委托给子代理，避免主会话上下文膨胀：

```javascript
// ❌ 差：在主会话中执行大量操作，上下文持续膨胀
// ✅ 好：用子代理隔离，完成后只带回结果
sessions_spawn({
  task: "搜索并整理资料...",
  context: "isolated",  // 关键：不继承主会话上下文
  mode: "run"
})
```

**隔离级别：**
- `context: "isolated"` — 完全隔离，不继承上下文（最省 Token）
- `context: "fork"` — 继承当前上下文（仅当需要历史时才用）

### 3. 基于 cron 的独立任务

不要在主会话中长时间运行复杂任务：

```javascript
// ✅ 好：用 cron 在独立 session 中执行
cron.add({
  name: "复杂报表",
  schedule: { kind: "at", at: "..." },
  payload: {
    kind: "agentTurn",
    message: "生成报表",
    lightContext: true
  },
  sessionTarget: "isolated"  // 独立 session，不消耗主会话 Token
})
```

### 4. MEMORY.md 瘦身

定期清理 MEMORY.md，只保留真正重要的信息：

```markdown
## ✅ 好 - 精确简洁
- 用户偏好：简洁回复，不用敬语
- 项目：三个活跃项目（A、B、C）
- 学习：Python 自动化

## ❌ 差 - 冗长
- 用户在上次会话中提到他喜欢...（3段废话）
- 项目A的...项目B的...项目C的...（详细到每行代码）
```

### 5. 会话生命周期管理

```python
# 策略矩阵
STRATEGY = {
    "短问答": {
        "action": "main会话直接回复",
        "token_cost": "低 ~200",
    },
    "多步骤操作": {
        "action": "子代理 isolated",
        "token_cost": "中 ~500-2000",
    },
    "定时任务": {
        "action": "cron isolated + lightContext",
        "token_cost": "低 ~100-300",
    },
    "批量数据": {
        "action": "子代理 + 结果写入文件",
        "token_cost": "低（只回传摘要）",
    },
    "需要历史": {
        "action": "fork 上下文",
        "token_cost": "高 ~5000+",
    },
}
```

### 6. 返回值最小化

子代理或工具调用只返回必要结果：

```javascript
// ❌ 差：返回完整数据
return "完整文章内容 5000字..."

// ✅ 好：只返回摘要 + 写入文件
write("output/article.md", content)
return "已保存到 output/article.md，摘要：..."
```

### 7. HEARTBEAT.md 管理

- HEARTBEAT.md 中只放真正需要定期检查的任务
- 保持文件简短，注释内容不消耗 Token
- 定期清理已完成的任务

## 决策树

```
任务来了
├─ 简单回答？ → 主会话直接回复
├─ 需要搜索/计算？ → 子代理 isolated + lightContext
├─ 定时/周期任务？ → cron isolated
├─ 需要历史上下文？ → 判断是否真的需要，尽量用摘要替代
└─ 批量数据处理？ → 子代理写文件，只回状态
```

## Token 节省预估

| 策略 | 单次节省 | 说明 |
|------|---------|------|
| lightContext | 30-50% | 减少启动上下文 |
| 子代理 isolated | 50-70% | 完全隔离上下文 |
| MEMORY 瘦身 | 10-30% | 减少每轮系统提示 |
| cron isolated | 80-90% | 不占主会话 Token |
| 返回值最小化 | 10-20% | 减少历史积累 |

## 注意

- lightContext 更适合简单任务，复杂任务可能需要完整上下文
- 子代理结果通过文件传递比通过返回值更省 Token
- 定期（每周）检查 MEMORY.md 和 HEARTBEAT.md 是否需要瘦身
