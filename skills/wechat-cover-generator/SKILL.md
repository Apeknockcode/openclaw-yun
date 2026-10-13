---
name: "wechat-cover-generator"
description: "在浏览器中通过 Canvas API 生成专业公众号封面图，支持模板、渐变、中文排版"
---

# wechat-cover-generator - 公众号封面图生成器

在浏览器中通过 Canvas API 生成专业封面图，然后上传到微信素材库。

## 封面图规范

| 项目 | 要求 |
|------|------|
| 尺寸 | 900×383（1:0.426，首页卡片）或 900×500（1.8:1，详情页） |
| 格式 | JPEG |
| 大小 | ≤ 10MB |
| 文字 | ≤ 64字，大标题清晰 |

## 核心能力

### 1. 浏览器 Canvas 模板

```python
class CoverTemplate:
    BLUE_MODERN = {
        "bg_gradient": ["#1a73e8", "#0d47a1"],
        "title_color": "#ffffff",
        "subtitle_color": "#bbdefb",
        "accent_color": "#ff6f00",
        "title_font": "bold 48px 'PingFang SC', 'Microsoft YaHei'",
        "subtitle_font": "24px 'PingFang SC', 'Microsoft YaHei'",
    }
    ORANGE_HOT = {
        "bg_gradient": ["#ff6f00", "#e65100"],
        "title_color": "#ffffff",
        "subtitle_color": "#ffe0b2",
    }
    GREEN_TECH = {
        "bg_gradient": ["#00c853", "#1b5e20"],
        "title_color": "#ffffff",
        "subtitle_color": "#c8e6c9",
    }
    DARK_TECH = {
        "bg_gradient": ["#1a1a2e", "#16213e"],
        "title_color": "#e0e0e0",
        "subtitle_color": "#64b5f6",
    }
```

### 2. 工作流程

通过 browser evaluate 执行 Canvas 渲染：

```python
def generate_cover(
    title: str,
    subtitle: str = "",
    template: str = "BLUE_MODERN",
    output_path: str = "/tmp/cover.jpg",
):
    \"\"\"
    在浏览器中生成封面图，保存到本地。
    步骤：
    1. 打开一个空白页面
    2. 用 Canvas 绘制封面
    3. 通过 toDataURL 导出为 JPEG
    4. 写入本地文件
    \"\"\"
```

### 3. Canvas JS 渲染脚本

```javascript
function renderCover(title, subtitle, template) {
  const canvas = document.createElement('canvas');
  canvas.width = 900;
  canvas.height = 383;
  const ctx = canvas.getContext('2d');
  
  // 绘制渐变背景
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, template.bg[0]);
  grad.addColorStop(1, template.bg[1]);
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  
  // 绘制装饰元素（形状、线条等）
  // ...
  
  // 绘制标题
  ctx.fillStyle = template.titleColor;
  ctx.font = template.titleFont;
  ctx.textAlign = 'center';
  wrapText(ctx, title, canvas.width/2, 180, 700, 60);
  
  // 绘制副标题
  if (subtitle) {
    ctx.fillStyle = template.subtitleColor;
    ctx.font = template.subtitleFont;
    ctx.fillText(subtitle, canvas.width/2, 270);
  }
  
  return canvas.toDataURL('image/jpeg', 0.92);
}
```

### 4. 上传到微信

生成封面后，通过 WeChat API 上传为永久素材：

```python
def upload_cover_to_wechat(image_path: str, access_token: str) -> str:
    \"\"\"上传封面图到微信素材库，返回 media_id\"\"\"
```

## 模板示例

| 模板 | 适用场景 | 配色 |
|------|---------|------|
| BLUE_MODERN | 科技、教程、干货 | 蓝白 |
| ORANGE_HOT | 热点、促销、活动 | 橙白 |
| GREEN_TECH | 省钱、理财、生活 | 绿白 |
| DARK_TECH | 深度、分析、行业 | 深蓝+金色 |
