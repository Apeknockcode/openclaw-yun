# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
bg_top = (63, 51, 23)      # 暗金深底
bg_bottom = (46, 37, 16)
accent = (224, 182, 79)    # 暗金主色
title_c = (245, 215, 142)  # 标题亮金
sub_c = (233, 197, 106)
label_c = (201, 162, 75)
foot_c = (176, 145, 80)

img = Image.new("RGB", (W, H), bg_top)
# 简单纵向渐变（无圆角/无透明，纯色块叠加，微信安全）
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    r = int(bg_top[0] + (bg_bottom[0] - bg_top[0]) * t)
    g = int(bg_top[1] + (bg_bottom[1] - bg_top[1]) * t)
    b = int(bg_top[2] + (bg_bottom[2] - bg_top[2]) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

# 顶部装饰线
d.rectangle([0, 0, W, 6], fill=accent)

F = "/usr/share/fonts/google-noto-cjk/"
f_label = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 22)
f_title = ImageFont.truetype(F + "NotoSansCJK-Black.ttc", 44)
f_sub = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 18)
f_foot = ImageFont.truetype(F + "NotoSansCJK-Regular.ttc", 16)

def center(text, font, fill, y):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

center("进阶技巧 · 税务实务", f_label, label_c, 34)
center("佣金提现要交税吗？", f_title, title_c, 92)
center("通信分销佣金税务 + 发票处理实操指南", f_sub, sub_c, 176)
center("分小号后台留痕，报税有底账", f_sub, sub_c, 224)
# 分隔线
d.line([(W/2 - 160, 282), (W/2 + 160, 282)], fill=accent, width=2)
center("fenxiaohao.com", f_foot, foot_c, 300)

img.save("/root/.openclaw/workspace/wechat_cover_v24.jpg", "JPEG", quality=92)
print("cover saved")
