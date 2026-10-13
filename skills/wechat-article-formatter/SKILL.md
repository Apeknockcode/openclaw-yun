---
name: "wechat-article-formatter"
description: "将 Markdown 格式化为微信编辑器兼容的 HTML，含字体、间距、代码块、引用等样式优化"
---

# wechat-article-formatter - 微信文章排版格式化工具

将 Markdown 内容转换为微信编辑器兼容的优质 HTML，确保手机端阅读体验。

## 格式化规则

### 1. 字体与排版

```yaml
wechat_styles:
  body:
    font_size: 15px
    line_height: 1.8
    color: "#333333"
    font_family: "-apple-system, 'PingFang SC', 'Microsoft YaHei'"
  title:
    font_size: 18px
    font_weight: bold
    color: "#1a1a1a"
    margin_top: 24px
    margin_bottom: 12px
  subtitle:
    font_size: 16px
    font_weight: bold
    color: "#2c3e50"
    margin: "20px 0 10px"
  paragraph:
    margin_bottom: 16px
    line_height: 1.8
  quote:
    border_left: "4px solid #1a73e8"
    background: "#f0f4ff"
    padding: "12px 16px"
    color: "#555"
    font_size: 14px
  code_inline:
    background: "#f4f4f4"
    padding: "2px 6px"
    border_radius: "3px"
    font_size: 13px
    color: "#d63384"
  code_block:
    background: "#1e1e1e"
    color: "#d4d4d4"
    padding: "16px"
    border_radius: "6px"
    font_size: 13px
    overflow_x: auto
  image:
    max_width: "100%"
    border_radius: "6px"
    margin: "12px 0"
  strong:
    color: "#1a1a1a"
```

### 2. Markdown → WeChat HTML 转换

```python
def format_article(md_text: str, template: str = "default") -> str:
    \"\"\"
    将 Markdown 转换为微信兼容 HTML。
    支持：标题、粗体、斜体、列表、引用、代码块、表格、图片
    \"\"\"

def add_section_divider(style: str = "line") -> str:
    \"\"\"在段落之间添加分隔线或装饰元素\"\"\"

def add_callout(text: str, style: str = "tip") -> str:
    \"\"\"添加提示框（tip/warning/info）\"\"\"
```

### 3. 微信兼容性处理

- 移除不支持的 HTML 标签（script, iframe, object 等）
- 转换 CSS 为内联样式（微信编辑器会过滤 style 标签）
- 代码块用微信兼容方式展示（背景色+边框）
- 表格转为可读格式

### 4. 预览功能

```python
def generate_preview(html_content: str) -> str:
    \"\"\"生成手机端预览 HTML 文件\"\"\"
```

### 5. 使用示例

```python
# 从文件读取 Markdown，格式化后输出
formatted = format_article(open("article.md").read())
print(formatted)  # 可直接粘贴到微信编辑器
```
