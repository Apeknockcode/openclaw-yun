# -*- coding: utf-8 -*-
"""Generate cover for 2026-08-16: 暗金 theme (v28), 900x383 JPG"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
# 暗金 gradient (deeper than v24)
top = (92, 74, 30)      # #5c4a1e
bottom = (44, 33, 10)   # #2c210a
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
    r = int(bottom[0] * (1 - 0.30 * t))
    g = int(bottom[1] * (1 - 0.30 * t))
    b = int(bottom[2] * (1 - 0.30 * t))
    d.line([(0, y), (W, y)], fill=(r, g, b))

F = "/usr/share/fonts/google-noto-cjk/"
f_label = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 22)
f_title = ImageFont.truetype(F + "NotoSansCJK-Black.ttc", 46)
f_sub = ImageFont.truetype(F + "NotoSansCJK-Medium.ttc", 20)
f_note = ImageFont.truetype(F + "NotoSansCJK-Regular.ttc", 16)
f_footer = ImageFont.truetype(F + "NotoSansCJK-Bold.ttc", 17)

GOLD = (245, 215, 142)      # #f5d78e
GOLD_LIGHT = (255, 240, 200)
GOLD_DIM = (226, 196, 128)


def center_text(draw, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)


# 分类标签
center_text(d, 32, "热点解读 · 新政满半月", f_label, GOLD)
# 主标题
center_text(d, 88, "新政满半月，转型到哪一步了？", f_title, (255, 255, 255))
# 副标题
center_text(d, 166, "4个自查维度 + 分小号后台实操清单", f_sub, GOLD_LIGHT)
# 补充说明
center_text(d, 208, "通信分销商转型进度自查，宽带/企业业务对照表", f_note, GOLD_DIM)
# 底部平台名
center_text(d, 330, "fenxiaohao.com", f_footer, GOLD_LIGHT)

out = "/root/.openclaw/workspace/wechat_cover_v28_20260816.jpg"
img.save(out, "JPEG", quality=92)
print("saved", out)
