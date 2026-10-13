# -*- coding: utf-8 -*-
# v34 墨绿：顶部 #065f46 -> 底部 #022c22 垂直渐变（六色轮换：v33紫色 → v34墨绿）
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
top, bottom = (6, 95, 70), (2, 44, 34)
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
cream = (167, 243, 208)  # 浅薄荷绿

def center(text, font, y, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

# 装饰横条
d.rectangle([40, 34, 52, 74], fill=cream)

center('干货/转型 · 存量客户盘活', f_tag, 40, cream)
center('手里客户名单怎么盘活？', f_title, 88, white)
center('老客户转宽带/企业通信，3步实操', f_sub, 168, cream)
center('通信分销商转型：名单变订单', f_note, 220, cream)
d.line([(300, 268), (600, 268)], fill=cream)
center('fenxiaohao.com', f_plat, 292, white)

out = '/root/.openclaw/workspace/wechat_cover_v34_20260821.jpg'
img.save(out, 'JPEG', quality=92)
print('saved', out)
