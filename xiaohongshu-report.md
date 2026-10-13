# 小红书营销技能报告

## 搜索结果

### ClawHub 搜索
通过 5 组关键词搜索（xiaohongshu、小红书、social media marketing image、video generation marketing、content creation），在 ClawHub 上找到大量小红书及相关营销技能。

### 已安装的技能（共 10 个）

| # | 技能名称 | 版本 | 功能说明 | 安装路径 |
|---|---------|------|---------|---------|
| 1 | **xiaohongshu** | 1.0.0 | 小红书笔记创作与运营方法论（双引擎逻辑、数据诊断、合规红线） | `skills/xiaohongshu/` |
| 2 | **xiaohongshu-content-automation** | 1.0.0 | 小红书内容创作自动化工作流（选题→文案→标题→话题→排版） | `skills/xiaohongshu-content-automation/` |
| 3 | **red-book-content-creation** | 1.0.2 | 小红书风格 HTML 内容+封面生成（热情风/科技风两张模板） | `skills/red-book-content-creation/` |
| 4 | **xiaohongshu-hot-trend** | 0.1.0 | 小红书热门趋势搜索与分析 | `skills/xiaohongshu-hot-trend/` |
| 5 | **xiaohongshu-browser** | 1.2.1 | Playwright 自动化浏览小红书，搜索关键词+截图帖子弹窗 | `skills/xiaohongshu-browser/` |
| 6 | **xiaohongshucreator** | 1.0.0 | 小红书内容创作助手（标题优化、话题标签、emoji优化） | `skills/xiaohongshucreator/` |
| 7 | **redbook-image-generator** | 1.0.0 | 小红书配图生成器（用 PIL 生成文字配图） | `skills/redbook-image-generator/` |
| 8 | **content-creation-pro** | 1.0.1 | 多平台内容创作超级助手（小红书/知乎/抖音/公众号） | `skills/content-creation-pro/` |
| 9 | **content-creation-helper** | 1.0.0 | 金融/交易内容小红书/知乎/公众号适配 | `skills/content-creation-helper/` |
| 10 | **pomelli-marketing-skill** | - | 品牌营销助手（campaign brief、brand book、AI image/video prompts） | `skills/pomelli-marketing-skill/` |

### 关键分析
- ✅ **笔记创作方法论** → `xiaohongshu` 技能覆盖全面
- ✅ **内容自动化** → `xiaohongshu-content-automation` 提供完整工作流
- ✅ **图片/配图生成** → 有 PIL 方案，但无 AI 图片生成（nano-banana-pro 集成）
- ✅ **热点趋势分析** → `xiaohongshu-hot-trend` 覆盖
- ✅ **浏览器自动化** → `xiaohongshu-browser` 覆盖
- ❌ **nano-banana-pro 集成配图** → 无现成技能
- ❌ **综合营销策略 + 内容生成** → 无现成技能

## 自定义技能创建

### 已创建：xiaohongshu-marketing (proposal)
通过 `skill_workshop` 创建了一个自定义技能提案（pending 状态），路径将位于：
`~/.openclaw/workspace/skills/xiaohongshu-marketing/`

**功能覆盖：**
1. **图文笔记生成** - 整合 nano-banana-pro 生成小红书风格配图 + 爆款文案模板
2. **视频内容处理** - 小红书视频文案、封面生成流程
3. **热点话题搜索** - 利用 multi-search-engine 搜索百度/Google 小红书热门话题
4. **爆款文案模板库** - 5 套模板（清单干货型、真实测评型、经验分享型、情绪共鸣型、教程步骤型）
5. **配图风格指南** - 4 种风格（清新生活风、ins 简约风、手绘插画风、知识信息图风）
6. **营销策略建议** - 账号定位、内容矩阵、发布时间、互动运营、SEO、数据监测

**依赖技能：** nano-banana-pro、multi-search-engine、xiaohongshu、xiaohongshu-hot-trend、xiaohongshu-content-automation

## 使用指南

### 方式一：直接使用已安装的 ClawHub 技能
1. **生成内容** → 调用 `xiaohongshu-content-automation` 或 `content-creation-pro`
2. **运营方法** → 调用 `xiaohongshu` 技能获得方法论指导
3. **分析热点** → 调用 `xiaohongshu-hot-trend` 分析热门趋势
4. **搜索内容** → 调用 `xiaohongshu-browser`（需先手动登录小红书）
5. **生成配图** → 调用 `redbook-image-generator`（PIL）或 `nano-banana-pro`（AI）

### 方式二：结合自定义技能 xiaohongshu-marketing
当自定义技能被正式批准启用后，输入如以下指令即可触发：
- "帮写一篇小红书种草文案"
- "生成小红书风格的图文笔记"
- "搜一下小红书最近的热门话题"
- "做一个小红书营销方案"
- "生成一篇咖啡入门的小红书笔记，包含配图"

### 方式三：手动操作流程
```
1. 热点搜索 → multi-search-engine 搜索"小红书+{主题}+热门"
2. 文案创作 → 使用爆款文案模板生成
3. 配图生成 → nano-banana-pro 生成（使用指南中的 prompt 模板）
4. 排版发布 → 手动或通过 xiaohongshu-publish 技能发布
```

---

报告生成时间: 2026-07-12 15:16 GMT+8
