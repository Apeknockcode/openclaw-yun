---
name: "jisu-wechat-article"
description: "按关键词搜索公众号文章，聚合多平台搜索结果，支持批量导出"
---

# jisu-wechat-article - 关键词搜索公众号文章

通过浏览器自动化在多个平台搜索微信公众号文章，聚合结果。

## 搜索源

支持多个搜索渠道：

### 1. 搜狗微信搜索

https://weixin.sogou.com - 最全的微信文章搜索引擎

```python
def search_sogou(keyword: str, pages: int = 10) -> list:
    \"\"\"
    在搜狗微信搜索文章。
    支持按时间排序。
    \"\"\"
```

### 2. 微信"搜一搜"

通过浏览器模拟打开微信网页版或 WeChat 内置浏览器进行搜索。

### 3. 百度搜索（site 限定）

通过浏览器在百度搜索 `site:mp.weixin.qq.com <keyword>`。

### 4. 今日头条搜索

通过浏览器在头条搜索微信文章。

## 核心功能

```python
def search_wechat_articles(
    keyword: str,
    sources: list = ["sogou", "baidu"],
    max_results: int = 100,
    date_from: str = None,
    date_to: str = None,
    dedup: bool = True,
    export: str = None,  # csv | json | markdown
) -> list:
    \"\"\"
    多平台搜索微信公众号文章，支持去重、时间过滤、导出。
    返回聚合后的文章列表。
    \"\"\"
```

## 导出格式

### CSV（适合 Excel 分析）
```csv
title,account,pub_date,url,summary,source
```

### JSON（适合程序处理）
```json
[
  {
    "title": "...",
    "account": "公众号名称",
    "pub_date": "2026-07-12",
    "url": "https://mp.weixin.qq.com/s/...",
    "summary": "...",
    "cover_url": "...",
    "source": "sogou"
  }
]
```

### Markdown（适合阅读）
```markdown
# 搜索结果：关键词
- [标题1](url1) - 公众号1 - 2026-07-12
- [标题2](url2) - 公众号2 - 2026-07-11
```

## 限速控制

```python
rate_limit = {
    "sogou": {"delay": 3, "max_per_minute": 10},
    "baidu": {"delay": 2, "max_per_minute": 15},
}
```

## 注意

- 各搜索源可能有反爬机制，需要合理控制频率
- 搜狗搜索可能弹出验证码
- 建议使用 `profile="user"` 利用已有登录态
