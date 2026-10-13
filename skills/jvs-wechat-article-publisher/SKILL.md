---
name: "jvs-wechat-article-publisher"
description: "带排版模板的发布工具，支持多种微信公众号文章排版风格一键切换"
---

# jvs-wechat-article-publisher - 带排版模板的发布工具

提供多种微信公众号文章排版模板，通过浏览器自动化实现一键排版+发布。

## 功能特性

### 1. 排版模板库

内置多种排版风格：

| 模板名 | 风格 | 适用场景 |
|--------|------|----------|
| `简约白` | 干净清爽，无多余装饰 | 技术文章、教程 |
| `文艺清新` | 柔和色彩，圆角卡片 | 情感、生活类 |
| `商务专业` | 严谨排版，蓝色调 | 行业分析、报告 |
| `科技感` | 深色背景，亮色高亮 | 科技资讯、产品发布 |
| `小红书风` | 图文并茂，大标题 | 生活方式、种草 |

### 2. 模板自定义

通过 YAML 配置文件自定义模板：

```yaml
# templates/my-template.yaml
name: "自定义模板"
css:
  body:
    font_family: "微软雅黑"
    font_size: "15px"
    color: "#333"
    line_height: 1.75
  title:
    font_size: "20px"
    font_weight: bold
    color: "#1a1a1a"
    margin: "20px 0 10px"
  subtitle:
    font_size: "14px"
    color: "#888"
  quote:
    border_left: "4px solid #4A90D9"
    background: "#f8f9fa"
    padding: "12px 16px"
  code:
    background: "#f4f4f4"
    border_radius: "4px"
    padding: "2px 6px"
  image:
    border_radius: "8px"
    margin: "10px 0"
```

### 3. 工作流程

```python
def apply_template_and_publish(
    content_path: str,
    template: str = "简约白",
    custom_css: str = None,
    preview: bool = False,
) -> dict:
    \"\"\"
    应用模板后发布到公众号草稿箱。
    preview=True 则生成预览 HTML 到本地。
    \"\"\"
```

### 4. 实现机制

1. 读取 Markdown 内容
2. 根据模板生成带样式的 HTML
3. 通过浏览器操作（粘贴 HTML 到微信编辑器）
4. 调整格式细节（通过浏览器元素操作）
5. 保存草稿

### 5. 预览模式

在本地生成预览 HTML 文件，可在浏览器中查看排版效果后再发布。

## 注意

- 微信编辑器对部分 CSS 支持有限，模板需经过测试
- 复杂排版建议先预览再发布
- 模板中的图片链接需为可访问的 URL 或使用微信素材库
