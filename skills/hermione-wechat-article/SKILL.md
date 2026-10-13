---
name: "hermione-wechat-article"
description: "通过浏览器自动化抓取公众号文章列表和完整内容，支持批量下载和历史归档"
---

# hermione-wechat-article - 公众号文章抓取

基于浏览器自动化从微信公众号抓取文章列表和完整内容。不使用任何微信 API。

## 抓取方式

### 方式一：搜狗微信搜索（无需扫码）

通过浏览器访问 https://weixin.sogou.com，搜索公众号或文章：

```python
def search_articles_by_keyword(
    keyword: str,
    pages: int = 5,
    sort: str = "relevance",  # relevance | time
) -> list:
    \"\"\"
    通过搜狗微信搜索文章。
    返回 [ { "title", "url", "pub_date", "source_account", "summary" } ]
    \"\"\"
```

### 方式二：公众号主页抓取

先通过搜狗搜索找到公众号主页链接，然后打开公众号主页获取历史文章列表：

```python
def get_account_articles(
    account_name: str,
    max_count: int = 100,
    include_content: bool = False,
) -> list:
    \"\"\"
    获取公众号的历史文章列表。
    通过浏览器操作公众号主页的"全部消息"功能。
    \"\"\"
```

### 方式三：文章详情抓取

```python
def fetch_article_detail(url: str) -> dict:
    \"\"\"
    抓取单篇文章的完整内容。
    返回: {
        "title", "author", "pub_date",
        "content_html", "content_md",
        "cover_url", "digest"
    }
    \"\"\"
```

### 方式四：批量归档

```python
def archive_account(
    account_name: str,
    output_dir: str = "archive/",
    format: str = "markdown",  # markdown | html | json
    max_articles: int = 200,
) -> dict:
    \"\"\"
    批量归档某个公众号的所有可获取文章。
    保存到本地，支持 Markdown / HTML / JSON 格式。
    \"\"\"
```

## 注意事项

- 搜狗微信搜索可能遇到验证码，需手动处理
- 单个公众号的历史文章有数量限制（约最新 10 篇可直接获取）
- 可通过"全部消息"页面滚动加载获取更多
- 抓取频率建议控制，避免被封
- 仅用于学习和研究，请遵守相关法律法规
