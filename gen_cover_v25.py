# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
bg_top = (13, 27, 51)      # 深蓝第三轮首色
bg_bottom = (26, 42, 74)
accent = (240, 192, 128)   # 亮金点缀
title_c = (255, 255, 255)
sub_c = (168, 200, 232)
label_c = (240, 192, 128)
foot_c = (140, 168, 200)

img = Image.new("RGB", (W, H), bg_top)
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    r = int(bg_top[0] + (bg_bottom[0] - bg_top[0]) * t)
    g = int(bg_top[1] + (bg_bottom[1] - bg_top[1]) * t)
    b = int(bg_top[2] + (bg_bottom[2] - bg_top[2]) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

d.rectangle([0, 0, W, 6], fill=accent)

F = "/usr/share/fonts/google-noto-cjk/"
f_label = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 22)
f_title = ImageFont.truetype(F + "NotoSansCJK-Black.ttc", 44)
f_sub = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 19)
f_foot = ImageFont.truetype(F + "NotoSansCJK-Regular.ttc", 16)

def center(text, font, fill, y):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

center("实操教程 · 转化率专题", f_label, label_c, 34)
center("落地页转化率这样提", f_title, title_c, 92)
center("店铺装修 + 协议模板 + 素材库", f_sub, sub_c, 178)
center("宽带分销推广三件套实操指南", f_sub, sub_c, 226)
d.line([(W/2 - 160, 284), (W/2 + 160, 284)], fill=accent, width=2)
center("fenxiaohao.com", f_foot, foot_c, 302)

img.save("/root/.openclaw/workspace/wechat_cover_v25.jpg", "JPEG", quality=92)
print("cover v25 saved")
