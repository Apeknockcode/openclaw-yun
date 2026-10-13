---
name: "wechat-browser-automation"
description: "微信公众号专用浏览器操作基础层，封装公众号后台元素定位、登录态管理、防检测策略"
---

# wechat-browser-automation - 微信公众号浏览器自动化核心

微信公众号操作的浏览器自动化基础层。所有其他微信 skill 的底层依赖。纯本地浏览器控制，零 API 调用。

## 设计目标

为所有微信相关 skill 提供统一的浏览器操作基础能力，封装微信公众号后台的复杂元素定位和交互逻辑。

## 核心能力

### 1. 登录态管理

```python
class WeChatSession:
    def __init__(self, profile_dir: str = "./wc-profiles"):
        \"\"\"管理微信公众号登录状态\"\"\"

    def login(self, force: bool = False) -> bool:
        \"\"\"
        扫码登录 mp.weixin.qq.com。
        force=True 强制重新登录。
        自动保存/恢复 session cookie。
        \"\"\"

    def ensure_logged_in(self) -> bool:
        \"\"\"检查登录状态，未登录则引导扫码\"\"\"

    def logout(self):
        \"\"\"清除本地保存的 session\"\"\"
```

### 2. 页面路由

```python
class WeChatNavigator:
    DRAFT_URL = "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2"
    MATERIAL_URL = "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/list&action=list"

    def go_to_draft_editor(self) -> str:
        \"\"\"导航到新建图文编辑器，返回页面 targetId\"\"\"

    def go_to_material_library(self) -> str:
        \"\"\"导航到素材库\"\"\"

    def go_to_published_list(self) -> str:
        \"\"\"导航到已发布列表\"\"\"

    def go_to_statistics(self) -> str:
        \"\"\"导航到数据统计\"\"\"
```

### 3. 编辑器交互

```python
class WeChatEditor:
    def set_title(self, title: str):
        \"\"\"设置文章标题\"\"\"

    def set_author(self, author: str):
        \"\"\"设置作者\"\"\"

    def set_body_html(self, html: str):
        \"\"\"使用 HTML 填充正文（通过剪贴板+快捷键）\"\"\"

    def upload_cover(self, image_path: str):
        \"\"\"上传封面图\"\"\"

    def set_summary(self, summary: str):
        \"\"\"设置摘要\"\"\"

    def save_draft(self) -> str:
        \"\"\"保存草稿，返回草稿 ID\"\"\"

    def publish(self, schedule_time: str = None):
        \"\"\"发布（或定时发布）\"\"\"
```

### 4. 防检测策略

```python
class AntiDetection:
    @staticmethod
    def random_delay(min_s: float = 0.5, max_s: float = 2.0):
        \"\"\"随机延迟，模拟人类操作节奏\"\"\"

    @staticmethod
    def human_like_typing(element, text: str):
        \"\"\"模拟人打字：随机间隔、偶尔停顿\"\"\"

    @staticmethod
    def random_scroll(target_id: str):
        \"\"\"随机滚动页面\"\"\"

    @staticmethod
    def get_fingerprint_script() -> str:
        \"\"\"返回反指纹检测的 JS（覆盖 navigator.webdriver 等）\"\"\"
```

### 5. 元素定位

```python
class WeChatSelectors:
    # 微信公众号后台的元素选择器集合
    # 需根据微信后台实际 DOM 结构更新
    LOGIN_QR = ".login__qr"
    TITLE_INPUT = "#title"
    BODY_EDITOR = ".rich_media_content"
    SAVE_BTN = ".btn_save_draft"
    PUBLISH_BTN = ".btn_publish"
    COVER_UPLOAD = ".cover_upload_btn"
    SUMMARY_INPUT = "#digest"
```

### 6. 错误处理

```python
class WeChatError(Exception):
    \"\"\"微信操作基础异常\"\"\"

class LoginRequired(WeChatError):
    \"\"\"需要重新登录\"\"\"

class RateLimited(WeChatError):
    \"\"\"操作频繁，需要等待\"\"\"

class ElementNotFound(WeChatError):
    \"\"\"页面元素未找到（可能页面结构更新了）\"\"\"
```

## 与其他 skill 的关系

```
wechat-browser-automation (基础层)
├── wechat-publisher (轻量发布)
├── wechat-publisher-pro (增强发布)
├── wechat-article-pro (专业写作)
├── jvs-wechat-article-publisher (模板发布)
├── hermione-wechat-article (文章抓取)
├── jisu-wechat-article (关键词搜索)
├── wechat-toolkit (一站式工具箱)
└── wechat-account-audit (账号诊断)
```

## 注意

- 微信后台的 DOM 结构可能更新，需要定期维护选择器
- 建议使用 `profile="user"` 模式的 Playwright 登录已有浏览器
- 登录态持久化到本地 profile 目录
- 所有 skill 共享同一套登录态管理
