---
name: "wechat-image-finder"
description: "通过浏览器搜索免费商用图片，适配公众号文章内容，支持多搜索引擎自动筛选"
---

# wechat-image-finder - 公众号文章配图搜索

通过浏览器自动化搜索免费商用图片，为公众号文章配图。

## 支持的图片来源

| 源 | URL | 特点 |
|----|-----|------|
| Unsplash | https://unsplash.com | 高质量免费图，无需版权标记 |
| Pixabay | https://pixabay.com | 大量免费素材 |
| Pexels | https://www.pexels.com | 精品免费图库 |
| 百度图片 | https://image.baidu.com | 中文关键词搜索（需筛选版权） |

## 核心功能

### 1. 按内容语义搜图

```python
def search_images(
    keywords: list,
    sources: list = ["unsplash", "pixabay", "pexels"],
    max_per_keyword: int = 3,
    min_width: int = 800,
    aspect_ratio: str = "16:9",
) -> list:
    \"\"\"
    根据关键词搜索图片，返回图片 URL 列表。
    自动过滤过小、不适合的图片。
    \"\"\"
```

### 2. 文章智能配图

```python
def match_images_to_content(
    article_text: str,
    images_per_section: int = 1,
    style: str = "modern",
) -> list:
    \"\"\"
    分析文章分段，为每个段落匹配最合适的图片。
    返回: [ { "section_idx": 0, "section_topic": "...", "image_url": "...", "source": "unsplash" } ]
    \"\"\"
```

### 3. 图片处理

```python
def optimize_for_wechat(image_url: str) -> str:
    \"\"\"
    下载图片，处理为微信友好格式：
    - 压缩大小（≤ 2MB）
    - 转为 JPEG
    - 可选添加水印
    \"\"\"
```

### 4. 上传到微信素材库

```python
def upload_to_wechat(image_path: str, access_token: str) -> str:
    \"\"\"
    上传图片到微信公众号素材库。
    返回 media_id 和 URL。
    \"\"\"
```

## 工作流

1. 输入文章主题或关键词
2. 自动搜索多源图片
3. 按文章段落分配图片
4. 下载+优化+上传到微信素材库
5. 返回可直接插入内容的图片 HTML

## 注意事项

- 优先使用 Unsplash/Pixabay 等明确免费商用的图库
- 使用百度图片时需注意版权标注
- 使用时尺寸≥800px，避免模糊
- 图片不超过微信限制（2MB）
