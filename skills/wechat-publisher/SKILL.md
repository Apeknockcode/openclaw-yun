---
name: "wechat-publisher"
description: "轻量级 Markdown 发布助手，通过浏览器自动化将 Markdown 文章发布到微信公众号草稿箱"
---

# wechat-publisher - 轻量级 Markdown 发布助手

基于浏览器自动化（Playwright），将本地 Markdown 文件发布到微信公众号后台草稿箱。

## 前置条件

- 本地有 Playwright 浏览器环境（`browser-automation` skill 可用）
- 微信公众平台账号（可手动扫码登录）

## 工作流程

### 1. 登录微信公众号后台

使用 `profile="user"` 打开 https://mp.weixin.qq.com，提示用户扫码登录。

### 2. 导航到草稿箱

登录后，通过浏览器操作进入「草稿箱」→「新建图文」。

### 3. 填充内容

从本地 Markdown 文件读取内容：

```python
import re

def markdown_to_wechat_html(md_text):
    \"\"\"简单的 Markdown → 微信编辑器兼容 HTML\"\"\"
    # 处理标题
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    # 处理加粗、斜体等
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # 处理段落
    paragraphs = []
    for line in text.split('\n'):
        line = line.strip()
        if line and not line.startswith('<h'):
            paragraphs.append(f'<p>{line}</p>')
        elif line:
            paragraphs.append(line)
    return '\n'.join(paragraphs)
```

### 4. 上传封面图（可选）

如果提供了封面图片路径，通过浏览器文件上传控件上传。

### 5. 保存草稿

点击「保存」按钮，记录草稿 ID。

## 接口

```python
def publish_to_draft(
    md_path: str,
    title: str = None,
    cover_image: str = None,
    author: str = None,
) -> dict:
    \"\"\"
    将 Markdown 文件发布为公众号草稿。
    返回: { "success": bool, "draft_id": str, "error": str }
    \"\"\"
```

## 注意

- 所有操作通过浏览器元素定位完成，不使用任何微信 API
- 首次使用需要用户扫码登录
- cookie/session 可持久化到本地，避免每次重新登录
