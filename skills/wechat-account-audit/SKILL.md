---
name: "wechat-account-audit"
description: "公众号账号诊断、对标分析、用户画像分析，通过浏览器采集公开数据生成分析报告"
---

# wechat-account-audit - 公众号账号诊断工具

通过浏览器自动化采集公众号的公开数据，进行账号诊断、对标分析和用户画像分析。

## 功能介绍

### 1. 账号诊断（Account Audit）

分析指定公众号的整体表现：

```python
def audit_account(account_name: str) -> dict:
    \"\"\"
    生成账号诊断报告。
    返回: {
        "basic_info": { "name", "id", "description", "avatar", "qr_code" },
        "content_analysis": { "total_articles", "avg_read_count", "publish_frequency", "top_articles" },
        "style_analysis": { "writing_style", "avg_word_count", "common_topics", "cover_style" },
        "score": { "overall", "content", "engagement", "consistency" }
    }
    \"\"\"
```

采集数据来源：
- 公众号主页公开信息
- 历史文章列表（通过"全部消息"）
- 文章阅读量、点赞数（公众号文章底部公开数据）
- 文章发布时间规律

### 2. 对标分析（Competitive Analysis）

对比多个同领域公众号：

```python
def competitive_analysis(
    accounts: list,
    metrics: list = ["publish_freq", "avg_word_count", "topic_distribution", "engagement"],
) -> dict:
    \"\"\"
    对标分析报告。
    返回对比表格和雷达图数据。
    \"\"\"
```

分析维度：
- 发布频率对比
- 文章平均字长
- 主题分布对比
- 标题风格分析
- 发布时间偏好
- 互动数据对比

### 3. 用户画像（User Profiling）

通过分析文章内容和互动数据，描绘读者画像：

```python
def user_profile(account_name: str) -> dict:
    \"\"\"
    生成用户画像报告。
    返回: {
        "demographics": { "estimated_age_group", "gender_ratio", "region_focus" },
        "interests": { "top_topics", "reading_time", "preferred_content_type" },
        "behavior": { "peak_reading_time", "share_rate", "save_rate" }
    }
    \"\"\"
```

### 4. 报告生成

支持多种报告格式：

```python
def generate_report(
    account: str,
    report_type: str = "full",  # full | audit | competitive | profile
    output_format: str = "html",  # html | markdown | pdf
    output_path: str = "report.html",
) -> str:
    \"\"\"
    生成分析报告。
    报告包含：数据可视化图表（通过 Canvas 截图）、分析结论、建议。
    \"\"\"
```

## 数据采集说明

所有数据通过浏览器自动化从公开页面采集：
- 公众号主页（基本信息）
- 历史文章列表页
- 单篇文章阅读数据
- 搜狗微信搜索页

## 注意

- 仅分析公众号公开数据
- 阅读量等数据仅为文章页公开显示的数值
- 用户画像基于文章内容和互动特征推断
- 请遵守相关法律法规，不采集隐私数据
