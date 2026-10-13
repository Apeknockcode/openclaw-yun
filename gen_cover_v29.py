# -*- coding: utf-8 -*-
"""生成 v29 紫色封面 900x383 —— 六色轮换：v28暗金 → v29紫"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
# 紫色主题：深紫渐变底 + 亮紫点缀
TOP = (76, 29, 149)      # #4c1d95
BOTTOM = (46, 16, 101)   # #2e1065
ACCENT = (192, 132, 252) # #c084fc
WHITE = (255, 255, 255)
LIGHT = (216, 200, 236)  # 副文字

img = Image.new("RGB", (W, H), TOP)
draw = ImageDraw.Draw(img)

# 垂直渐变
for y in range(H):
    t = y / (H - 1)
    r = int(TOP[0] + (BOTTOM[0] - TOP[0]) * t)
    g = int(TOP[1] + (BOTTOM[1] - TOP[1]) * t)
    b = int(TOP[2] + (BOTTOM[2] - TOP[2]) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# 装饰：右下角大圆环（纯色，无渐变无圆角限制问题）
draw.ellipse([W - 280, H - 210, W - 40, H + 30], outline=(139, 92, 246), width=2)
draw.ellipse([W - 240, H - 170, W - 80, H - 10], outline=(168, 85, 247), width=2)

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

draw.text((x, y), "宽带分销开户流程怎么走？", font=f_title, fill=WHITE)
y += 44 + 30

draw.text((x, y), "材料清单 + 装维 + 结算节点，代理从0跑通第一单", font=f_sub, fill=LIGHT)
y += 18 + 15

draw.text((x, y), "五步实操：备料 → 上架 → 签约 → 装维 → 结算", font=f_note, fill=(168, 85, 247))
y += 16 + 30

draw.text((x, y), "fenxiaohao.com", font=f_domain, fill=ACCENT)

img.save("/root/.openclaw/workspace/wechat_cover_v29_20260817.jpg", "JPEG", quality=92)
print("saved wechat_cover_v29_20260817.jpg")
