# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
BG = "#3a1016"          # 酒红深底
ACCENT = "#f0a0a8"      # 玫粉
ACCENT2 = "#e8c0c6"
TEXT_MAIN = "#ffffff"
TEXT_SUB = "#f5c8cd"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 底部装饰条
d.rectangle([0, H-8, W, H], fill="#c2413c")

def font(path, size):
    return ImageFont.truetype(path, size)

f_tag   = font("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Bold.ttc", 22)
f_main  = font("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Black.ttc", 44)
f_sub   = font("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc", 18)
f_note  = font("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc", 16)
f_foot  = font("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc", 17)

def center_text(y, text, fnt, fill):
    w = d.textlength(text, font=fnt)
    d.text(((W-w)/2, y), text, font=fnt, fill=fill)

# 第一行：分类标签
center_text(26, "热点解读 · 合规自查", f_tag, ACCENT)

# 第二行：主标题
center_text(72, "新政下合规经营自查清单", f_main, TEXT_MAIN)

# 分隔线
d.line([(W/2-180, 138), (W/2+180, 138)], fill="#5a2028", width=2)

# 第三行：副标题
center_text(158, "5条清单避开审核红线，安心做宽带分销", f_sub, ACCENT2)

# 第四行：补充说明
center_text(205, "业务 · 内容 · 税务 · 客户信息 · 留痕", f_note, "#c98a92")

# 底部平台名
center_text(300, "fenxiaohao.com", f_foot, "#e8c0c6")

img.save("/root/.openclaw/workspace/wechat_cover_v22.jpg", "JPEG", quality=92)
print("cover saved: wechat_cover_v22.jpg")
