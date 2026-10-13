# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
# v33 紫色：顶部 #7c3aed -> 底部 #4c1d95 垂直渐变
top, bottom = (124, 58, 237), (76, 29, 149)
img = Image.new('RGB', (W, H))
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / (H - 1)
    c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

F = '/usr/share/fonts/google-noto-cjk/'
f_tag = ImageFont.truetype(F + 'NotoSansCJK-Bold.ttc', 22)
f_title = ImageFont.truetype(F + 'NotoSansCJK-Black.ttc', 44)
f_sub = ImageFont.truetype(F + 'NotoSansCJK-Medium.ttc', 19)
f_note = ImageFont.truetype(F + 'NotoSansCJK-Regular.ttc', 16)
f_plat = ImageFont.truetype(F + 'NotoSansCJK-Medium.ttc', 17)

white = (255, 255, 255)
cream = (233, 213, 255)

def center(text, font, y, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

# 装饰横条
d.rectangle([40, 34, 52, 74], fill=cream)

center('热点引流 · 开学季', f_tag, 40, cream)
center('开学季校园宽带订单暴涨', f_title, 88, white)
center('供应商一站式管理：上架 · 接单 · 结算', f_sub, 168, cream)
center('分小号后台实操，忙季不混乱', f_note, 220, cream)
d.line([(300, 268), (600, 268)], fill=cream)
center('fenxiaohao.com', f_plat, 292, white)

out = '/root/.openclaw/workspace/wechat_cover_v33_20260820.jpg'
img.save(out, 'JPEG', quality=92)
print('saved', out)
