# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 900, 383
img = Image.new('RGB', (W, H), color='#0f2a43')
draw = ImageDraw.Draw(img)

# 装饰线条
draw.rectangle([0, 0, W, 8], fill='#2563eb')
draw.rectangle([0, H-8, W, H], fill='#2563eb')

font_large = ImageFont.truetype('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Black.ttc', 42)
font_medium = ImageFont.truetype('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc', 22)
font_regular = ImageFont.truetype('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc', 16)

def center_text(draw, y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((W - w) // 2, y), text, font=font, fill=fill)

center_text(draw, 40, '热点引流 · 宽带分销', font_medium, '#7fb4e6')
center_text(draw, 85, '装宽带返佣是真的吗？', font_large, '#ffffff')
center_text(draw, 160, '返佣机制 + 防坑要点一次说清', font_medium, '#b8d4ef')
center_text(draw, 215, '宽带代理怎么做 · 佣金怎么结 · 对账实操', font_regular, '#7fb4e6')
center_text(draw, 300, 'fenxiaohao.com 复制到浏览器打开', font_regular, '#5a8fc0')

img.save('/tmp/wechat_cover_v19_20260805.jpg', 'JPEG', quality=90)
print('cover saved:', os.path.getsize('/tmp/wechat_cover_v19_20260805.jpg'), 'bytes')
