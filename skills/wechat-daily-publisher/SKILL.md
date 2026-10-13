---
name: "wechat-daily-publisher"
description: "每日微信公众号推文助手：自动搜热点→AI写文→生成封面→配图→排版→存入草稿箱"
---

# wechat-daily-publisher - 每日公众号推文助手

自动完成 热点搜索 → AI 写作 → 封面生成 → 配图搜索 → 排版发布 全流程。

## 前置条件

- 已激活的微信 skill 全家桶 + multi-search-engine
- 微信 AppID + AppSecret（已配置）
- 公众号定位已确定（当前：号卡/流量卡）

## 每日工作流程

### 步骤 1：多引擎热点调研 🚀

使用 `multi-search-engine` 替代纯浏览器搜索，更快更全面：

```python
def search_hotspots(keywords: list):
    \"\"\"
    使用 multi-search-engine 的 web_fetch 策略，
    同时搜索多个中文引擎获取当日热点。

    关键词池：流量卡推荐、号卡套餐、5G资费、运营商新政、流量卡避坑
    引擎选择：百度、搜狗微信、360、Bing CN

    优势：
    - 无需开浏览器（快10倍）
    - 多引擎交叉验证（结果更全面）
    - 自动处理 Cookie（不会遇到验证码）
    - 支持时间过滤（只看当周内容）
    \"\"\"
```

**多引擎搜索示例：**
```python
# 同时搜索多个引擎
queries = [
    "https://www.baidu.com/s?wd=流量卡推荐+2026",
    "https://wx.sogou.com/weixin?type=2&query=流量卡推荐",
    "https://cn.bing.com/search?q=流量卡推荐+2026",
]
# 用 web_fetch 批量请求，引擎间加 1-2 秒延迟
```

### 步骤 2：AI 写作

使用本地 Ollama 或内置 LLM 生成文章。

### 步骤 3：封面生成（Canvas 浏览器）

浏览器 Canvas 生成封面图，上传微信素材库。

### 步骤 4：配图插入（Pixabay 搜索）

Pixabay 搜图 → 下载 → 上传微信 → 插入正文。

### 步骤 5：排版与发布

格式化 HTML → 微信 draft API 存入草稿箱。

## 配置

```yaml
account:
  name: "启源符号"
  appid: "wx09afa091cac18c86"
publish:
  frequency: "daily"
  draft_only: true
content:
  niche: "号卡/流量卡"
  tone: "通俗易懂"
  avg_word_count: 2000
search:
  engines: ["baidu", "sogou", "sogou_weixin", "bing_cn"]
  max_results_per_engine: 5
  time_filter: "week"
cover:
  template: "BLUE_MODERN"
images:
  sources: ["pixabay"]
  per_article: 2
```
