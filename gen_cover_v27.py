# -*- coding: utf-8 -*-
"""Generate cover for 2026-08-15: 暖橙 theme, 900x383 JPG"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 900, 383
# 暖橙 gradient
top = (255, 138, 76)    # #ff8a4c
bottom = (217, 74, 10)  # #d94a0a
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / (H - 1)
    r = int(top[0] + (bottom[0] - top[0]) * t)
    g = int(top[1] + (bottom[1] - top[1]) * t)
    b = int(top[2] + (bottom[2] - top[2]) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

# subtle darker bottom band
for y in range(H - 56, H):
    t = (y - (H - 56)) / 56
    r = int(bottom[0] * (1 - 0.35 * t))
    g = int(bottom[1] * (1 - 0.35 * t))
    b = int(bottom[2] * (1 - 0.35 * t))
    d.line([(0, y), (W, y)], fill=(r, g, b))

F = "/usr/share/fonts/google-noto-cjk/"
f_label = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 22)
f_title = ImageFont.truetype(F + "NotoSansCJK-Black.ttc", 46)
f_sub = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 20)
f_note = ImageFont.truetype(F + "NotoSansCJK-Regular.ttc", 16)
f_footer = ImageFont.truetype(F + "NotoSansCJK-Bold.ttc", 17)

def center_text(draw, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)

# 分类标签
center_text(d, 34, "实操教程 · 产品管理", f_label, (255, 243, 230))
# 主标题
center_text(d, 92, "宽带分销产品怎么管？", f_title, (255, 255, 255))
# 副标题
center_text(d, 170, "采购市场 vs 自建产品，佣金配置+上架下架", f_sub, (255, 235, 214))
# 补充说明
center_text(d, 210, "分小号后台产品管理实操，宽带+企业通信一起管", f_note, (255, 224, 200))
# 底部平台名
center_text(d, 330, "fenxiaohao.com", f_footer, (255, 255, 255))

out = "/root/.openclaw/workspace/wechat_cover_v27_20260815.jpg"
img.save(out, "JPEG", quality=92)
print("saved", out)
