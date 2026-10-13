#!/usr/bin/env python3
"""Generate cover image v15 - 紫色配色 (流量卡避坑/热点资讯)"""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/usr/share/fonts/google-noto-cjk"
OUTPUT = "/root/.openclaw/workspace/wechat_cover_v15.jpg"

# 紫色配色
BG_COLOR = (45, 27, 61)      # deep purple
ACCENT_COLOR = (168, 85, 247)  # a855f7 purple
TEXT_COLOR = (255, 255, 255)
SUB_COLOR = (200, 170, 215)   # light lavender

img = Image.new("RGB", (900, 383), BG_COLOR)
draw = ImageDraw.Draw(img)

# Accent bar on left
draw.rectangle([(0, 0), (8, 383)], fill=ACCENT_COLOR)

# Right decorative side strip
for i in range(0, 383, 3):
    draw.rectangle([(892, i), (899, i + 1)], fill=(120, 70, 170))

# Subtle circles decoration
draw.ellipse([(700, 30), (860, 190)], outline=(120, 70, 170), width=2)
draw.ellipse([(720, 45), (840, 175)], outline=(100, 60, 150), width=1)

# Load fonts
font_tag = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Medium.ttc", 22, encoding='unic')
font_title = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Black.ttc", 44, encoding='unic')
font_sub = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Medium.ttc", 18, encoding='unic')
font_bottom = ImageFont.truetype(f"{FONT_DIR}/NotoSansCJK-Regular.ttc", 16, encoding='unic')

# Tag label
tag_w, tag_h = 130, 32
draw.rectangle([(28, 24), (28 + tag_w, 24 + tag_h)], fill=ACCENT_COLOR)
draw.text((28 + 8, 27), "热点资讯", font=font_tag, fill=BG_COLOR)

# Main title
draw.text((28, 78), "办流量卡避坑指南", font=font_title, fill=TEXT_COLOR)

# Subtitle
draw.text((28, 140), "5个常见坑一次说清", font=font_sub, fill=SUB_COLOR)

# Separator line
draw.rectangle([(28, 182), (560, 183)], fill=(168, 85, 247, 128))

# Bottom note
draw.text((28, 202), "附号卡分销商自查方法", font=font_sub, fill=SUB_COLOR)

# Platform tag bottom right
draw.text((700, 340), "fenxiaohao.com", font=font_bottom, fill=(150, 110, 180))

img.save(OUTPUT, quality=92)
print(f"Cover saved: {OUTPUT}")
