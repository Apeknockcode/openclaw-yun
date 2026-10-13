# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
FONT_DIR = "/usr/share/fonts/google-noto-cjk/"
f_label = ImageFont.truetype(FONT_DIR + "NotoSansCJK-Medium.ttc", 22)
f_title = ImageFont.truetype(FONT_DIR + "NotoSansCJK-Black.ttc", 44)
f_sub = ImageFont.truetype(FONT_DIR + "NotoSansCJK-Medium.ttc", 20)
f_note = ImageFont.truetype(FONT_DIR + "NotoSansCJK-Regular.ttc", 16)
f_bottom = ImageFont.truetype(FONT_DIR + "NotoSansCJK-Medium.ttc", 18)

# 紫色主题（六色轮换剩余色）
BG1 = (60, 24, 110)     # 深紫 #3c186e
BG2 = (94, 43, 165)     # 紫 #5e2ba5
ACCENT = (196, 132, 252)  # 亮紫 #c484fc
WHITE = (255, 255, 255)
LIGHT = (216, 190, 245)   # 浅紫 #d8bef5

img = Image.new("RGB", (W, H), BG1)
d = ImageDraw.Draw(img)

# 右侧装饰色块（简单几何，不用图标/emoji）
for i, (x0, x1, c) in enumerate([(700, 900, BG2), (760, 900, (124, 58, 237)), (820, 900, (168, 85, 247))]):
    d.rectangle([x0, 0, x1, H], fill=c)

# 左侧竖条
d.rectangle([0, 0, 10, H], fill=ACCENT)

x = 40
y = 34
d.text((x, y), "实操教程", font=f_label, fill=ACCENT)
y += 30 + 30

d.text((x, y), "通信分销商对账总出错？", font=f_title, fill=WHITE)
y += 44 + 26

d.text((x, y), "资金管理实操：佣金账单 + 充值记录 + 余额明细", font=f_sub, fill=LIGHT)
y += 20 + 20

d.text((x, y), "3步理清账目 · 月底不再糊涂账", font=f_note, fill=ACCENT)
y += 16 + 34

d.text((x, H - 40), "fenxiaohao.com", font=f_bottom, fill=LIGHT)

out = "/root/.openclaw/workspace/wechat_cover_v21.jpg"
img.save(out, "JPEG", quality=92)
print("saved", out)
