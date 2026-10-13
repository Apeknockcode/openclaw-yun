---
name: "wechat-toolkit"
description: "一站式公众号工具箱：搜索文章 + 下载内容 + AI 改写 + 自动发布，全部浏览器自动化实现"
---

# wechat-toolkit - 一站式公众号工具箱

整合搜索、下载、改写、发布全流程的公众号工具集。所有操作通过浏览器自动化实现，零 API 依赖。

## 功能模块

### 1. 🔍 搜索（Search）

集成 jisu-wechat-article 的搜索能力：

```python
toolkit.search(keyword="AI", sources=["sogou", "baidu"], limit=50)
```

### 2. 📥 下载（Download）

集成 hermione-wechat-article 的内容抓取能力：

```python
toolkit.download(urls=["https://mp.weixin.qq.com/s/..."], output_dir="downloads/")
```

### 3. ✏️ 改写（Rewrite）

利用本地 Ollama 模型对文章进行改写：

```python
toolkit.rewrite(
    input_path="downloads/article.md",
    style="deep_analysis",  # deep_analysis | concise | storytelling | listicle
    tone="专业",
    word_count=3000,
    add_intro=True,
    add_conclusion=True,
)
```

改写策略：
- **深度分析型**：保持原文事实，增加分析和见解
- **简洁型**：压缩为要点，适合快速阅读
- **故事叙述型**：用故事线重新组织
- **清单体**：转为列表/要点格式

### 4. 📤 发布（Publish）

集成 wechat-publisher 的发布能力：

```python
toolkit.publish(
    md_path="rewrites/article_final.md",
    title="改写后标题",
    cover="auto",
    draft_only=True,      # True=仅保存草稿, False=直接发布
    schedule_time=None,   # 定时发布
)
```

### 5. 🔄 完整流水线（Pipeline）

一键执行搜索→下载→改写→发布：

```python
toolkit.pipeline(
    keyword="AI趋势2026",
    download_count=10,
    rewrite_style="deep_analysis",
    publish_draft=True,
)
```

## 配置文件

```yaml
# wechat-toolkit.yaml
search:
  sources: ["sogou", "baidu"]
  max_count: 50
  dedup: true
download:
  output_dir: "./downloads"
  format: "markdown"
  include_images: true
rewrite:
  model: "qwen2.5:7b"  # Ollama 模型
  default_style: "deep_analysis"
  temperature: 0.7
publish:
  draft_only: true
  default_author: ""
  cover_auto: true
```

## 工作流示例

```bash
# 一键完成：搜索"AI创业"相关文章，下载、改写后保存为草稿
$ python toolkit.py --pipeline --keyword "AI创业" --style deep_analysis --count 5
```

## 注意事项

- 需要本地安装 Ollama 用于改写功能
- 发布功能需要首次扫码登录微信公众号后台
- 批量操作注意控制频率
