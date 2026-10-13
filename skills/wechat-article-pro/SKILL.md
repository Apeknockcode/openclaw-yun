---
name: "wechat-article-pro"
description: "专业版 AI 写作助手，浏览网页搜热点、AI 生成 3000-5000 字深度文、自动生成封面图"
---

# wechat-article-pro - 专业版 AI 写作助手

专业级公众号文章创作工具，基于浏览器自动化 + 本地 AI 能力，无需任何 API 调用。

## 核心功能

### 1. 热点搜索

使用浏览器自动搜索微信、微博、知乎等平台的热点话题：

```python
def search_hot_topics(
    keywords: list,
    platforms: list = ["weixin", "weibo", "zhihu"],
    time_range: str = "today",
) -> list:
    \"\"\"
    通过浏览器搜索各平台热点。
    返回 [ { "title", "url", "summary", "hot_score", "source" } ]
    \"\"\"
```

实现方式：
- 打开微信搜一搜（浏览器操作）
- 打开微博热搜榜
- 打开知乎热榜
- 聚合结果，按热度排序

### 2. AI 深度写作

利用本地 Ollama 或其他本地 LLM 生成 3000-5000 字深度文章：

```python
def generate_article(
    topic: str,
    references: list,
    tone: str = "专业",
    word_count: int = 4000,
    sections: list = None,
) -> dict:
    \"\"\"
    生成深度文章。
    返回: { "title", "content_md", "summary", "keywords", "cover_suggestion" }
    \"\"\"
```

写作流程：
1. 收集参考资料（浏览器搜索并抓取）
2. 生成文章大纲
3. 逐章节生成内容
4. 整体润色优化
5. 生成摘要和标签

### 3. 智能配图

- 根据文章段落语义匹配图片
- 浏览器搜索版权友好的图片
- 自动裁剪和压缩

### 4. 封面图生成

使用浏览器 Canvas API 生成专业封面图：
- 标题大字 + 背景渐变
- 可添加作者名、日期
- 多种模板可选

### 5. 一键发布

直接发布到微信公众号草稿箱（依赖 wechat-publisher 的发布能力）。

## 工作流示例

```bash
# 1. 搜热点
$ python search_hot.py --topic "AI" --output hot.json

# 2. 写文章
$ python generate_article.py --topic "2026年AI趋势" --refs hot.json --output article.md

# 3. 发布
$ python publish.py --md article.md --title "2026年AI趋势深度解析"
```

## 注意事项

- 所有联网操作通过浏览器完成，无外部 API 依赖
- 本地 LLM 需要提前安装 Ollama
- 建议使用至少 7B 以上模型以保证文章质量
