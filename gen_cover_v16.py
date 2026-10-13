# -*- coding: utf-8 -*-
"""Generate cover v16: 酒红 theme, 900x383 JPG."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 900, 383
BG = (58, 16, 22)        # 酒红 #3a1016
ACCENT = (240, 160, 168) # 玫粉 #f0a0a8
TEXT = (255, 255, 255)
SUB = (217, 179, 184)    # 浅玫瑰 #d9b3b8
MUTED = (168, 120, 126)

FONT_DIR = "/usr/share/fonts/google-noto-cjk"
f_large = ImageFont.truetype(os.path.join(FONT_DIR, "NotoSansCJK-Black.ttc"), 44)
f_tag   = ImageFont.truetype(os.path.join(FONT_DIR, "NotoSansCJK-Medium.ttc"), 22)
f_sub   = ImageFont.truetype(os.path.join(FONT_DIR, "NotoSansCJK-Medium.ttc"), 18)
f_note  = ImageFont.truetype(os.path.join(FONT_DIR, "NotoSansCJK-Regular.ttc"), 16)
f_foot  = ImageFont.truetype(os.path.join(FONT_DIR, "NotoSansCJK-Medium.ttc"), 15)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle top accent line
d.rectangle([0, 0, W, 6], fill=ACCENT)

def center_text(y, text, font, fill, spacing=0):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) / 2
    d.text((x, y), text, font=font, fill=fill)

# 分类标签
center_text(36, "干货引流 · 宽带分销佣金", f_tag, ACCENT)
# 主标题
center_text(88, "宽带分销佣金一般多少？", f_large, TEXT)
# 副标题
center_text(190, "结算规则 + 后台对账实操", f_sub, SUB)
# 补充说明
center_text(248, "分小号分销商必看 · 佣金账单一目了然", f_note, MUTED)
# 底部平台名
d.line([330, 306, 570, 306], fill=(90, 40, 48), width=1)
center_text(318, "fenxiaohao.com", f_foot, ACCENT)

out = "/root/.openclaw/workspace/wechat_cover_v16.jpg"
img.save(out, "JPEG", quality=92)
print("saved", out, img.size)
