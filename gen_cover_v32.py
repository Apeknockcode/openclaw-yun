# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
# v32 暖橙：顶部 #f97316 -> 底部 #9a3412 垂直渐变（与 v27 暖橙 #ff8a4c/#d94a0a 区分）
top, bottom = (249, 115, 22), (154, 52, 18)
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
cream = (255, 237, 213)

def center(text, font, y, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

# 装饰横条
d.rectangle([40, 34, 52, 74], fill=cream)

center('实操教程 · 资金管理', f_tag, 40, cream)
center('宽带分销佣金结算实操', f_title, 88, white)
center('对账 · 提现 · 税务 三步走', f_sub, 168, cream)
center('资金管理模块，月底对账三分钟搞定', f_note, 220, cream)
d.line([(300, 268), (600, 268)], fill=cream)
center('fenxiaohao.com', f_plat, 292, white)

out = '/root/.openclaw/workspace/wechat_cover_v32_20260820.jpg'
img.save(out, 'JPEG', quality=92)
print('saved', out)
