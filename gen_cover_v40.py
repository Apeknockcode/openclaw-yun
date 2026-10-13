# -*- coding: utf-8 -*-
"""生成公众号封面 v40：墨绿渐变，2026-08-27（六色轮换 v39紫 → v40墨绿）"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
TOP = (0x16, 0x5A, 0x3A)      # #165a3a 墨绿
BOTTOM = (0x06, 0x2B, 0x1A)   # #062b1a 深墨绿

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
LIGHT = (0xCD, 0xE8, 0xD8)   # 浅绿白
GREEN_LIGHT = (0x9F, 0xD8, 0xB8)  # 浅绿

def center_text(d, y, text, font, fill):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) / 2
    d.text((x, y), text, font=font, fill=fill)

# 第一行：分类标签
center_text(d, 42, "实操教程 · 转型计划连载 第2期", f_label, GREEN_LIGHT)
# 第二行：主标题
center_text(d, 92, "通信分销商转型30天计划", f_title, WHITE)
# 第三行：副标题
center_text(d, 165, "第2周：客户名单怎么变成订单", f_sub, LIGHT)
# 第四行：补充说明
center_text(d, 215, "7天跟进节奏 + 三类话术 + 首单落地", f_note, LIGHT)
# 底部：平台名称
center_text(d, 330, "fenxiaohao.com", f_bottom, GREEN_LIGHT)

out = "/root/.openclaw/workspace/wechat_cover_v40_20260827.jpg"
img.save(out, "JPEG", quality=92)
print("saved", out)
