#!/usr/bin/env python3
"""
小红书配图生成 v5 - 小红书风格排版
暖色调 + 圆润卡片 + 装饰元素 + 大字标题
"""

import cairosvg
import os

OUTPUT_DIR = os.path.expanduser("~/.openclaw/workspace/assets/xiaohongshu/2026-07-15-liuliangka-how-to-choose")
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H = 1080, 1440
FF = "'Noto Sans CJK SC', 'Noto Sans CJK', sans-serif"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def r(x, y, w, h, rv=0, fill="none", stroke="none", sw=0, op=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rv}" ry="{rv}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>\n'

def cxy(x, y, rv, fill, op=1):
    return f'<circle cx="{x}" cy="{y}" r="{rv}" fill="{fill}" opacity="{op}"/>\n'

def t(x, y, s, sz, c="#1a1a2e", w=400, a="start"):
    return f'<text x="{x}" y="{y}" font-size="{sz}" fill="{c}" font-weight="{w}" font-family="{FF}" text-anchor="{a}" xml:space="preserve">{esc(s)}</text>\n'

def tc(y, s, sz, c="#1a1a2e", w=400):
    return t(540, y, s, sz, c, w, "middle")

def shadow(rx, ry, rw, rh, rr):
    """简单阴影效果"""
    return f'<rect x="{rx+4}" y="{ry+4}" width="{rw}" height="{rh}" rx="{rr}" ry="{rr}" fill="#000" opacity="0.04"/>\n'

# 颜色
PINK = "#ff4d6d"
CORAL = "#ff6b6b"
PEACH = "#ff8fa3"
WARM = "#ffb3c1"
LIGHT_PINK = "#fff0f3"
LIGHT_CORAL = "#fff5f5"
BG = "#fef9fb"
CARD = "#ffffff"
SOFT_BLACK = "#2b2d42"
MID_GRAY = "#6c757d"
SOFT_GRAY = "#adb5bd"
GREEN_SPOT = "#06d6a0"
BLUE_SPOT = "#118ab2"
YELLOW_SPOT = "#ffd166"

# ======== 封面 ========
def cover():
    body = r(0, 0, W, H, 0, BG)
    
    # 装饰元素
    body += cxy(120, 180, 25, PINK, 0.06)
    body += cxy(960, 300, 35, CORAL, 0.05)
    body += cxy(180, 1000, 20, GREEN_SPOT, 0.04)
    body += cxy(900, 1100, 28, BLUE_SPOT, 0.04)
    
    # 标签
    body += r(80, 120, 160, 38, 19, PINK)
    body += t(160, 147, "选卡指南", 18, "#fff", 600, "middle")
    
    # 主标题
    body += t(90, 260, "流量卡到底怎么选？", 56, SOFT_BLACK, 800)
    body += t(90, 330, "3步搞定，不踩坑", 44, PINK, 700)
    
    # 分隔线
    body += r(90, 375, 60, 4, 2, PINK, "", 0, 0.3)
    
    body += t(90, 430, "看完上一篇踩坑经历", 26, MID_GRAY, 400)
    body += t(90, 470, "很多姐妹问我到底该怎么选", 26, MID_GRAY, 400)
    body += t(90, 510, "今天手把手教你", 26, MID_GRAY, 400)
    
    # 三个步骤卡片
    steps = [
        ("Step 1  看需求", "你要多少流量？通话要不要？", PINK),
        ("Step 2  看价格", "优惠期多久？到期多少钱？", "#ff8c42"),
        ("Step 3  看售后", "能线上注销吗？客服靠谱吗？", "#5e60ce"),
    ]
    
    sy = 580
    card_h = 100
    for title, desc, color in steps:
        body += shadow(80, sy, 920, card_h, 16)
        body += r(80, sy, 920, card_h, 16, "#fff")
        body += r(80, sy, 6, card_h, 3, color)  # 左侧色条
        body += t(120, sy + 38, title, 30, SOFT_BLACK, 700)
        body += t(120, sy + 76, desc, 22, MID_GRAY, 400)
        sy += card_h + 25
    
    body += tc(1200, "往下滑看完整攻略", 22, SOFT_GRAY, 400)
    body += tc(1350, "#流量卡 #话费省钱 #怎么选流量卡", 20, SOFT_GRAY, 400)
    
    return svg(body)


# ======== 步骤详情 ========
STEP_DATA = [
    {
        "color": PINK, "bg": LIGHT_PINK,
        "title": "看需求",
        "sub": "先搞清楚自己要什么",
        "items": [
            ("每个月大概用多少流量？", True),
            ("50G以下  普通套餐够用", False),
            ("50-100G  中档流量卡", False),
            ("100G以上  大流量卡", False),
            ("需不需要通话分钟？", True),
            ("纯上网  纯流量卡就够了", False),
            ("要打电话  选带通话的套餐", False),
            ("在哪个城市用？哪家信号强？", True),
        ],
        "tip": "先明确需求再选卡，别被低价冲昏头"
    },
    {
        "color": "#ff8c42", "bg": "#fff8f0",
        "title": "看价格",
        "sub": "别只看第一月的价格",
        "items": [
            ("优惠期多久？", True),
            ("前6个月19  第7个月变39", False),
            ("有些卡优惠12个月", False),
            ("到期后恢复多少钱？", True),
            ("39 / 59 / 99  差很多", False),
            ("有没有隐形收费？", True),
            ("月租之外还有来电显示费？", False),
            ("提前注销要违约金吗？", True),
        ],
        "tip": "看年均月费，别看首月低价"
    },
    {
        "color": "#5e60ce", "bg": "#f5f3ff",
        "title": "看售后",
        "sub": "办卡容易注销难",
        "items": [
            ("能不能线上注销？", True),
            ("很多卡要本人去归属地营业厅", False),
            ("客服电话打得通吗？", True),
            ("有些小众卡售后等于没有", False),
            ("异地卡怎么办理业务？", True),
            ("补卡换卡销户都要回原地？", False),
            ("有没有官方客服渠道？", True),
            ("选运营商的官方卡最稳", False),
        ],
        "tip": "办卡前问清楚售后，不然注销欲哭无泪"
    },
]


def gen_step(data):
    color = data["color"]
    step_idx = STEP_DATA.index(data) + 1
    
    body = r(0, 0, W, H, 0, data["bg"])
    
    # 装饰
    body += cxy(960, 200, 30, color, 0.05)
    body += cxy(120, 1100, 20, color, 0.04)
    
    # 标题区
    body += r(80, 100, 200, 50, 25, color)
    body += t(180, 133, f'Step {step_idx}', 22, "#fff", 700, "middle")
    
    body += t(90, 210, data["title"], 44, SOFT_BLACK, 800)
    body += t(90, 255, data["sub"], 24, MID_GRAY, 400)
    
    # 计算内容区域
    items_svg = ""
    iy = 355
    for text_item, is_header in data["items"]:
        if is_header:
            items_svg += r(110, iy - 2, 8, 8, 4, color)
            items_svg += t(135, iy + 8, text_item, 28, SOFT_BLACK, 600)
            iy += 52
        else:
            items_svg += t(135, iy + 8, text_item, 22, MID_GRAY, 400)
            iy += 48
    
    # 计算实际内容高度，让卡片刚好包住文字
    content_end = iy
    padding = 80
    card_y = 285
    card_h = content_end - card_y + padding
    
    body += shadow(80, card_y, 920, card_h, 16)
    body += r(80, card_y, 920, card_h, 16, "#fff")
    body += items_svg
    
    # Tip
    ty = card_y + card_h + 30
    body += r(100, ty, 880, 60, 14, color, "", 0, 0.08)
    body += t(120, ty + 36, data["tip"], 24, color, 600)
    
    body += tc(1380, "留言你的城市+需求，帮你推荐", 20, SOFT_GRAY, 400)
    
    return svg(body)


# ======== 自测清单 ========
def checklist():
    questions = [
        ("每月需要多少G流量？", "50G以下 / 50-100G / 100G以上"),
        ("优惠期多久  到期多少钱？", "别只看首月，看第7个月后多少钱"),
        ("流量通用还是定向？", "定向流量只能用在特定APP"),
        ("能不能线上注销？", "异地卡注销难，先确认流程"),
        ("有合约期吗  违约金多少？", "有些卡绑12个月，提前退要赔钱"),
        ("归属地信号怎么样？", "先确认运营商在你那的信号"),
    ]
    
    body = r(0, 0, W, H, 0, "#fef9f0")
    
    # 装饰
    body += cxy(900, 120, 25, YELLOW_SPOT, 0.08)
    body += cxy(150, 1200, 30, CORAL, 0.05)
    
    body += t(80, 130, "办卡前自测清单", 44, SOFT_BLACK, 800)
    body += r(80, 155, 50, 4, 2, CORAL, "", 0, 0.3)
    body += t(80, 195, "问清楚这6个问题再下单", 24, MID_GRAY, 400)
    
    cy = 250
    icons = ["1", "2", "3", "4", "5", "6"]
    for (q, a), icon in zip(questions, icons):
        body += shadow(60, cy, 960, 100, 14)
        body += r(60, cy, 960, 100, 14, "#fff")
        body += cxy(108, cy + 50, 18, CORAL)
        body += t(108, cy + 56, icon, 18, "#fff", 700, "middle")
        body += t(145, cy + 36, q, 26, SOFT_BLACK, 600)
        body += t(145, cy + 72, a, 22, MID_GRAY, 400)
        cy += 120
    
    body += tc(1370, "截图保存  办卡前对照检查", 22, SOFT_GRAY, 400)
    
    return svg(body)


# ======== 互动引导 ========
def cta():
    body = r(0, 0, W, H, 0, "#fef5f7")
    
    # 装饰
    body += cxy(960, 200, 40, PINK, 0.04)
    body += cxy(120, 800, 30, CORAL, 0.04)
    body += cxy(800, 1200, 25, YELLOW_SPOT, 0.05)
    
    # 大卡片
    body += shadow(60, 160, 960, 1100, 28)
    body += r(60, 160, 960, 1100, 28, "#fff")
    
    body += tc(280, "你选流量卡踩过坑吗？", 40, SOFT_BLACK, 700)
    
    # 分割装饰
    body += r(470, 310, 140, 3, 1.5, CORAL, "", 0, 0.3)
    
    content = [
        ("t", "上一篇我分享了自己踩的坑", 380),
        ("t", "这一篇教你怎么选卡", 430),
        ("s", "", 470),
        ("t", "如果你还在纠结：", 520),
        ("s", "", 560),
        ("t", "不知道自己该选多少流量的", 610),
        ("t", "被低价套餐迷惑过的", 660),
        ("t", "怕选错了又要换卡的", 710),
        ("s", "", 760),
        ("t", "评论区留下你的情况", 820),
        ("s", "", 860),
        ("hl", "【城市】+【每月用多少G】", 920),
        ("t", "我帮你看看该选哪种", 980),
        ("s", "", 1030),
        ("m", "纯经验分享  不推销  看情况回复", 1080),
    ]
    
    for typ, text_item, cy in content:
        if typ == "t":
            body += tc(cy, text_item, 26, MID_GRAY, 400)
        elif typ == "hl":
            body += r(320, cy-38, 440, 48, 24, PINK, "", 0, 0.08)
            body += tc(cy, text_item, 26, PINK, 600)
        elif typ == "m":
            body += tc(cy, text_item, 20, SOFT_GRAY, 400)
    
    return svg(body)


def svg(body):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  * {{ font-family: {FF}; }}
</style>
{body}
</svg>'''


if __name__ == "__main__":
    configs = [
        ("cover.png", cover()),
        ("img2.jpg", gen_step(STEP_DATA[0])),
        ("img3.jpg", gen_step(STEP_DATA[1])),
        ("img4.jpg", gen_step(STEP_DATA[2])),
        ("img5.jpg", checklist()),
        ("img6.jpg", cta()),
    ]
    
    for fname, svg_content in configs:
        fpath = os.path.join(OUTPUT_DIR, fname)
        try:
            cairosvg.svg2png(bytestring=svg_content.encode('utf-8'), write_to=fpath, output_width=W, output_height=H)
            sz = os.path.getsize(fpath) / 1024
            print(f'  {fname}: {sz:.0f}KB')
        except Exception as e:
            print(f'  {fname}: ERROR - {e}')
    
    print(f'\n输出: {OUTPUT_DIR}')
