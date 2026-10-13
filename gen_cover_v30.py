# -*- coding: utf-8 -*-
"""生成 v30 酒红封面 900x383 —— 六色轮换：v29紫 → v30酒红"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
# 酒红主题：深酒红渐变底 + 浅玫红点缀
TOP = (112, 24, 43)      # #70182b
BOTTOM = (43, 10, 18)    # #2b0a12
ACCENT = (253, 164, 175) # #fda4af
WHITE = (255, 255, 255)
LIGHT = (245, 194, 204)  # #f5c2cc

img = Image.new("RGB", (W, H), TOP)
draw = ImageDraw.Draw(img)

# 垂直渐变
for y in range(H):
    t = y / (H - 1)
    r = int(TOP[0] + (BOTTOM[0] - TOP[0]) * t)
    g = int(TOP[1] + (BOTTOM[1] - TOP[1]) * t)
    b = int(TOP[2] + (BOTTOM[2] - TOP[2]) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# 装饰：右下角大圆环（纯色）
draw.ellipse([W - 280, H - 210, W - 40, H + 30], outline=(159, 18, 57), width=2)
draw.ellipse([W - 240, H - 170, W - 80, H - 10], outline=(190, 24, 60), width=2)

F = "/usr/share/fonts/google-noto-cjk/"
f_label = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 22)
f_title = ImageFont.truetype(F + "NotoSansCJK-Black.ttc", 44)
f_sub = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 18)
f_note = ImageFont.truetype(F + "NotoSansCJK-Regular.ttc", 16)
f_domain = ImageFont.truetype(F + "NotoSansCJK-Bold.ttc", 15)

x = 52
y = 46
draw.text((x, y), "实操教程 · 进阶技巧", font=f_label, fill=ACCENT)
y += 30 + 8

draw.text((x, y), "宽带分销团队怎么带？", font=f_title, fill=WHITE)
y += 44 + 30

draw.text((x, y), "招募下级分销商 + 等级佣金 + 团队奖励", font=f_sub, fill=LIGHT)
y += 18 + 15

draw.text((x, y), "关系管理 × 组织架构，组合拳一次跑通", font=f_note, fill=ACCENT)
y += 16 + 30

draw.text((x, y), "fenxiaohao.com", font=f_domain, fill=ACCENT)

img.save("/root/.openclaw/workspace/wechat_cover_v30_20260818.jpg", "JPEG", quality=92)
print("saved wechat_cover_v30_20260818.jpg")
