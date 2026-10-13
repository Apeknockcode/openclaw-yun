# -*- coding: utf-8 -*-
"""Generate cover v18 - 暗金配色 (900x383 JPG)"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
BG_TOP = (43, 36, 23)      # 深暗金底 #2b2417
BG_BOT = (24, 20, 14)      # 更深的底 #18140e
ACCENT = (212, 175, 55)    # 金色 #d4af37
ACCENT2 = (240, 210, 130)  # 亮金 #f0d282
TEXT_W = (250, 245, 235)   # 暖白
TEXT_S = (200, 190, 168)   # 浅灰金
LINE = (212, 175, 55)

img = Image.new("RGB", (W, H), BG_TOP)
d = ImageDraw.Draw(img)
# vertical gradient
for y in range(H):
    t = y / H
    r = int(BG_TOP[0] * (1 - t) + BG_BOT[0] * t)
    g = int(BG_TOP[1] * (1 - t) + BG_BOT[1] * t)
    bl = int(BG_TOP[2] * (1 - t) + BG_BOT[2] * t)
    d.line([(0, y), (W, y)], fill=(r, g, bl))

# left gold accent bar
d.rectangle([0, 0, 8, H], fill=ACCENT)

# subtle diamond pattern on right
for i in range(8):
    x = 700 + i * 30
    d.line([(x, 60), (x + 14, 60 + 14)], fill=(212, 175, 55, ), width=2)
    d.line([(x + 14, 60 + 14), (x, 60 + 28)], fill=(212, 175, 55), width=2)
    d.line([(x, 60 + 28), (x - 14, 60 + 14)], fill=(212, 175, 55), width=2)
    d.line([(x - 14, 60 + 14), (x, 60)], fill=(212, 175, 55), width=2)

# fonts
f_big = ImageFont.truetype('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Bold.ttc', 46)
f_tag = ImageFont.truetype('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc', 22)
f_sub = ImageFont.truetype('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc', 19)
f_note = ImageFont.truetype('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc', 16)

# tag
d.text((48, 40), "实操教程", font=f_tag, fill=ACCENT2)
# title (two lines)
d.text((48, 92), "分销订单转化率上不去？", font=f_big, fill=TEXT_W)
d.text((48, 152), "协议模板设置+落地页挂载", font=f_big, fill=TEXT_W)
# divider
d.rectangle([48, 232, 180, 234], fill=LINE)
# subtitle
d.text((48, 258), "3步配置协议模板，下单前多一道信任保障", font=f_sub, fill=TEXT_S)
# bottom platform
d.text((48, 330), "fenxiaohao.com", font=f_note, fill=ACCENT)

img.save("/root/.openclaw/workspace/wechat_cover_v18.jpg", "JPEG", quality=92)
print("saved wechat_cover_v18.jpg")
