# -*- coding: utf-8 -*-
"""生成公众号封面 v41：酒红渐变，2026-08-28（六色轮换 v40墨绿 → v41酒红）"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
TOP = (0x7F, 0x1D, 0x1D)      # #7f1d1d 酒红
BOTTOM = (0x45, 0x0A, 0x0A)   # #450a0a 深酒红

img = Image.new("RGB", (W, H), TOP)
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / (H - 1)
    color = tuple(int(TOP[i] + (BOTTOM[i] - TOP[i]) * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=color)

FONT = "/usr/share/fonts/google-noto-cjk/"
f_label   = ImageFont.truetype(FONT + "NotoSansCJK-Medium.ttc", 22)
f_title   = ImageFont.truetype(FONT + "NotoSansCJK-Black.ttc", 44)
f_sub     = ImageFont.truetype(FONT + "NotoSansCJK-Medium.ttc", 18)
f_note    = ImageFont.truetype(FONT + "NotoSansCJK-Regular.ttc", 16)
f_bottom  = ImageFont.truetype(FONT + "NotoSansCJK-Medium.ttc", 14)

WHITE = (255, 255, 255)
LIGHT = (0xFD, 0xA4, 0xAF)   # 浅粉红 #fda4af
PINK_LIGHT = (0xFE, 0xCD, 0xD3)  # 浅粉 #fecdd3

def center_text(d, y, text, font, fill):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) / 2
    d.text((x, y), text, font=font, fill=fill)

# 第一行：分类标签
center_text(d, 34, "热点解读 · 政策月报", f_label, LIGHT)
# 第二行：主标题
center_text(d, 92, "8月通信政策月报", f_title, WHITE)
# 第三行：副标题
center_text(d, 186, "新政首月落地盘点，9月分销商行动清单", f_sub, PINK_LIGHT)
# 第四行：补充说明
center_text(d, 232, "什么停了什么没停，佣金结算正不正常，一次盘清", f_note, LIGHT)
# 底部：平台名称
center_text(d, 330, "fenxiaohao.com", f_bottom, PINK_LIGHT)

img.save("/root/.openclaw/workspace/wechat_cover_v41_20260828.jpg", "JPEG", quality=92)
print("saved wechat_cover_v41_20260828.jpg")
