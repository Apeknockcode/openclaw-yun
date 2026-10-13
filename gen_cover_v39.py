# -*- coding: utf-8 -*-
# v39 紫色：顶部 #6d28d9 -> 底部 #2e1065 垂直渐变（六色轮换：v38暖橙 → v39紫色）
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
top, bottom = (109, 40, 217), (46, 16, 101)
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
lav = (216, 180, 254)  # 浅紫

def center(text, font, y, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

# 装饰横条
d.rectangle([40, 34, 52, 74], fill=lav)

center('实操教程 · 数据运营', f_tag, 40, lav)
center('宽带分销运营数据怎么看？', f_title, 88, white)
center('工作台+分析页：4组数据定位转化断点', f_sub, 168, lav)
center('推广不靠猜，决策有依据', f_note, 220, lav)
d.line([(300, 268), (600, 268)], fill=lav)
center('fenxiaohao.com', f_plat, 292, white)

out = '/root/.openclaw/workspace/wechat_cover_v39_20260826.jpg'
img.save(out, 'JPEG', quality=92)
print('saved', out)
