#!/usr/bin/env python3
"""Generate cover image v14 - 暖橙配色"""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/usr/share/fonts/google-noto-cjk"
OUTPUT = "/root/.openclaw/workspace/wechat_cover_v14.jpg"

# 暖橙配色
BG_COLOR = (60, 30, 10)  # deep brown-orange
ACCENT_COLOR = (255, 140, 0)  # orange
TEXT_COLOR = (255, 255, 255)
SUB_COLOR = (255, 200, 150)

img = Image.new("RGB", (900, 383), BG_COLOR)
draw = ImageDraw.Draw(img)

# Draw accent bar on left
draw.rectangle([(0, 0), (8, 383)], fill=ACCENT_COLOR)

# Subtle strip on right side
for i in range(0, 383, 3):
    alpha = int(30 + 20 * (i / 383))
    draw.rectangle([(892, i), (899, i + 1)], fill=(ACCENT_COLOR[0], ACCENT_COLOR[1]-20, 0))

# Draw decorative circles (subtle)
draw.ellipse([(700, 40), (850, 190)], outline=(100, 60, 20), width=2)
draw.ellipse([(720, 50), (830, 180)], outline=(80, 50, 15), width=1)

# Load fonts
font_tag = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Medium.ttc", 22, encoding='unic')
font_title = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Black.ttc", 42, encoding='unic')
font_sub = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Medium.ttc", 18, encoding='unic')
font_bottom = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Regular.ttc", 16, encoding='unic')

# Draw tag label (rounded rect simulated with rectangle)
tag_w, tag_h = 130, 32
draw.rectangle([(28, 24), (28 + tag_w, 24 + tag_h)], fill=ACCENT_COLOR)
draw.text((28 + 8, 26), "新手入门", font=font_tag, fill=BG_COLOR)

# Main title
draw.text((28, 80), "号卡分销商后台配置指南", font=font_title, fill=TEXT_COLOR)

# Subtitle
draw.text((28, 135), "实名认证 · API接入 · 团队权限管理", font=font_sub, fill=SUB_COLOR)

# Separator line
draw.rectangle([(28, 180), (580, 181)], fill=(255, 180, 80, 128))

# Bottom text
draw.text((28, 200), "分小号账户中心+组织架构全攻略", font=font_sub, fill=SUB_COLOR)

# Platform tag bottom right
draw.text((700, 340), "fenxiaohao.com", font=font_bottom, fill=(180, 120, 60))

img.save(OUTPUT, quality=92)
print(f"Cover saved: {OUTPUT}")
