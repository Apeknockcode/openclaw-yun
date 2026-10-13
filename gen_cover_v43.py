# -*- coding: utf-8 -*-
"""生成公众号封面 v43：深蓝渐变，2026-08-30（六色轮换 v42暗金 → v43深蓝）"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
TOP = (0x1E, 0x40, 0xAF)      # #1e40af 深蓝
BOTTOM = (0x0C, 0x1A, 0x3A)   # #0c1a3a 深藏青

img = Image.new("RGB", (W, H), TOP)
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / (H - 1)
    color = tuple(int(TOP[i] + (BOTTOM[i] - TOP[i]) * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=color)

FONT = "/usr/share/fonts/google-noto-cjk/"
f_label   = ImageFont.truetype(FONT + "NotoSansCJK-Medium.ttc", 22)
f_title   = ImageFont.truetype(FONT + "NotoSansCJK-Black.ttc", 44)
f_sub     = ImageFont.truetype(FONT + "NotoSansCJK-Medium.ttc", 18)
f_note    = ImageFont.truetype(FONT + "NotoSansCJK-Regular.ttc", 16)
f_bottom  = ImageFont.truetype(FONT + "NotoSansCJK-Medium.ttc", 14)

WHITE = (255, 255, 255)
LIGHT = (0x93, 0xC5, 0xFD)    # 浅蓝 #93c5fd
SKY = (0xDB, 0xEA, 0xFE)      # 极浅蓝 #dbeafe

def center_text(d, y, text, font, fill):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) / 2
    d.text((x, y), text, font=font, fill=fill)

# 第一行：分类标签
center_text(d, 34, "实操教程 · 素材管理模块", f_label, LIGHT)
# 第二行：主标题
center_text(d, 92, "宽带分销营销素材怎么找？", f_title, WHITE)
# 第三行：副标题
center_text(d, 186, "308张内置素材：主图、详情图、海报直接用", f_sub, SKY)
# 第四行：补充说明
center_text(d, 232, "素材库 + 主图设计 + 店铺装修，三步搞定落地页素材", f_note, LIGHT)
# 底部：平台名称
center_text(d, 330, "fenxiaohao.com", f_bottom, SKY)

img.save("/root/.openclaw/workspace/wechat_cover_v43_20260830.jpg", "JPEG", quality=92)
print("saved wechat_cover_v43_20260830.jpg")
