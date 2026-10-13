---
name: "wechat-publisher-pro"
description: "增强版自动发布，Markdown/HTML 转草稿箱，支持自动配图、排版优化、多图上传"
---

# wechat-publisher-pro - 增强版自动发布

基于 wechat-publisher 的增强版本，额外支持自动配图、智能排版、批量发布。

## 增强功能

### 1. Markdown/HTML 双格式支持

- Markdown → 微信 HTML（带样式映射）
- 直接 HTML 输入（保留原始样式）
- 自动检测输入格式

### 2. 自动配图

- 根据文章内容关键词，从本地图片库或网络搜索匹配图片
- 自动上传到微信公众号素材库
- 智能插入到文章合适位置（每 300-500 字插入一张）
- 支持自定义配图策略

### 3. 排版优化

- 自动设置字体、字号、行间距
- 代码块美化（带背景色和边框）
- 引用块样式优化
- 列表样式统一
- 表格格式转换（微信表格兼容）

### 4. 封面图智能生成

- 从文章内容提取标题和摘要
- 通过浏览器操作（Canvas/截图）生成封面图
- 上传设置为文章封面

### 5. 批量发布

支持目录批量处理：

```python
def batch_publish(
    md_dir: str,
    pattern: str = "*.md",
    cover_strategy: str = "auto",
    dry_run: bool = False,
) -> list:
    \"\"\"
    批量发布目录下的所有 Markdown 文件。
    dry_run=True 只检查不发布。
    \"\"\"
```

### 6. 定时发布

通过浏览器操作设置定时发布时间。

## 配置

```yaml
# wechat-publisher-pro.yaml
layout:
  font_size: 16
  line_height: 1.8
  code_bg_color: "#f5f5f5"
cover:
  auto_generate: true
  template: "default"
  fallback: "path/to/default-cover.png"
image:
  source: "local"  # local | web_search
  local_dir: "images/"
  max_per_article: 5
batch:
  concurrent: false
  interval_seconds: 30
```

## 注意

- 封面图生成使用浏览器内 Canvas/截图方式，不依赖外部 API
- 批量发布时注意间隔，避免触发微信风控
