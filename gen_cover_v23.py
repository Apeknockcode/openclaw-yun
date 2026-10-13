# -*- coding: utf-8 -*-
"""生成 2026-08-11 封面 v23：墨绿配色（六色轮换第二轮：v21紫→v22酒红→v23墨绿）"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 383
BG = "#0e3b2e"          # 深墨绿
ACCENT = "#34d399"      # 亮绿
SUB = "#a7d7c5"         # 浅薄荷
TEXT = "#ffffff"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 顶部细条装饰
d.rectangle([0, 0, W, 6], fill=ACCENT)
# 左侧竖条
d.rectangle([0, 0, 10, H], fill=ACCENT)

def font(path, size):
    return ImageFont.truetype(path, size)

F_BLACK = "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Black.ttc"
F_MED = "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc"
F_REG = "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc"

# 第一行：分类标签
d.text((46, 42), "热点解读 · 新政 Q&A", font=font(F_MED, 24), fill=ACCENT)

# 第二行：主标题（可能两行）
d.text((46, 100), "新政落地第11天", font=font(F_BLACK, 46), fill=TEXT)
d.text((46, 166), "通信分销商还能做什么？", font=font(F_BLACK, 46), fill=TEXT)

# 第三行：副标题
d.text((46, 250), "5个高频问题一次说清", font=font(F_MED, 24), fill=SUB)

# 分隔线
d.rectangle([46, 310, 320, 312], fill=ACCENT)

# 第四行：底部平台名
d.text((46, 330), "fenxiaohao.com", font=font(F_REG, 20), fill=SUB)

img.save("/root/.openclaw/workspace/wechat_cover_v23.jpg", quality=92)
print("saved wechat_cover_v23.jpg")
