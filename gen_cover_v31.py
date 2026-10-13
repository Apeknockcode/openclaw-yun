# -*- coding: utf-8 -*-
"""生成 v31 深蓝封面 900x383 —— 六色轮换：v30酒红 → v31深蓝"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
# 深蓝主题：深藏蓝渐变底 + 亮蓝点缀
TOP = (23, 37, 84)       # #172554
BOTTOM = (10, 15, 40)    # #0a0f28
ACCENT = (147, 197, 253) # #93c5fd
WHITE = (255, 255, 255)
LIGHT = (191, 219, 254)  # #bfdbfe

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
draw.ellipse([W - 280, H - 210, W - 40, H + 30], outline=(30, 58, 138), width=2)
draw.ellipse([W - 240, H - 170, W - 80, H - 10], outline=(37, 99, 235), width=2)

F = "/usr/share/fonts/google-noto-cjk/"
f_label = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 22)
f_title = ImageFont.truetype(F + "NotoSansCJK-Black.ttc", 44)
f_sub = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 18)
f_note = ImageFont.truetype(F + "NotoSansCJK-Regular.ttc", 16)
f_domain = ImageFont.truetype(F + "NotoSansCJK-Bold.ttc", 15)

x = 52
y = 46
draw.text((x, y), "干货指南 · 新手入门", font=f_label, fill=ACCENT)
y += 30 + 8

draw.text((x, y), "政企宽带分销怎么做？", font=f_title, fill=WHITE)
y += 44 + 30

draw.text((x, y), "小微企业通信市场入门：获客、报价、结算", font=f_sub, fill=LIGHT)
y += 18 + 15

draw.text((x, y), "第一单怎么跑通，全流程拆解", font=f_note, fill=ACCENT)
y += 16 + 30

draw.text((x, y), "fenxiaohao.com", font=f_domain, fill=ACCENT)

img.save("/root/.openclaw/workspace/wechat_cover_v31_20260819.jpg", "JPEG", quality=92)
print("saved wechat_cover_v31_20260819.jpg")
