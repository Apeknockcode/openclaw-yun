# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw

W, H = 900, 383
BG = "#7c2d12"        # 深暖橙棕
ACCENT = "#fdba74"    # 亮橙
TITLE_C = "#ffffff"
SUB_C = "#fed7aa"
META_C = "#c9a27e"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

font_tag = "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Bold.ttc"
font_title = "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Black.ttc"
font_sub = "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc"
font_meta = "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc"

from PIL import ImageFont
f_tag = ImageFont.truetype(font_tag, 22)
f_title = ImageFont.truetype(font_title, 44)
f_sub = ImageFont.truetype(font_sub, 20)
f_meta = ImageFont.truetype(font_meta, 16)

def draw_center(text, font, fill, y):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

# 顶部装饰条
d.rectangle([0, 0, W, 8], fill="#ea580c")

# 分类标签
draw_center("转型指南 · 企业通信分销", f_tag, ACCENT, 36)

# 主标题（两行）
draw_center("企业专线多少钱？", f_title, TITLE_C, 96)
draw_center("通信代理转行，从0跑通第一单", f_title, TITLE_C, 160)

# 分隔线
d.rectangle([330, 240, 570, 242], fill=ACCENT)

# 副标题
draw_center("宽带 · 专线 · 云总机，企业客户才是金矿", f_sub, SUB_C, 262)

# 补充说明
draw_center("政策解读 + 转型实操 · 分小号后台全流程", f_meta, META_C, 310)

# 底部平台名
draw_center("fenxiaohao.com", f_meta, ACCENT, 348)

img.save("/root/.openclaw/workspace/wechat_cover_v20.jpg", quality=92)
print("saved wechat_cover_v20.jpg", img.size)
