#!/usr/bin/env python3
"""小红书配图生成 v3 - 哒守哒纪 专用版 (Linux Noto字体)"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = os.path.expanduser("~/.openclaw/workspace/assets/xiaohongshu/dashoudaji")
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1080, 1440  # 小红书 3:4 竖屏

# Linux Noto Sans CJK 字体
FONT_CANDIDATES = [
    "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc",
    "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/google-noto-cjk/NotoSansCJK-DemiLight.ttc",
    "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Light.ttc",
]

FONT_BOLD = None
FONT_MEDIUM = None
FONT_REGULAR = None
FONT_DEMI = None
FONT_LIGHT = None

for fp in FONT_CANDIDATES:
    if os.path.exists(fp):
        if "Bold" in fp:
            FONT_BOLD = fp
        elif "Medium" in fp:
            FONT_MEDIUM = fp
        elif "Regular" in fp:
            FONT_REGULAR = fp
        elif "DemiLight" in fp:
            FONT_DEMI = fp
        elif "Light" in fp:
            FONT_LIGHT = fp

# Fallbacks
if not FONT_BOLD:
    FONT_BOLD = FONT_MEDIUM or FONT_REGULAR
if not FONT_MEDIUM:
    FONT_MEDIUM = FONT_REGULAR or FONT_BOLD
if not FONT_REGULAR:
    FONT_REGULAR = FONT_BOLD
if not FONT_DEMI:
    FONT_DEMI = FONT_LIGHT or FONT_REGULAR
if not FONT_LIGHT:
    FONT_LIGHT = FONT_DEMI or FONT_REGULAR

if not FONT_BOLD:
    raise RuntimeError("No Noto Sans CJK font found! Install: dnf install google-noto-cjk-fonts")

print(f"Bold: {os.path.basename(FONT_BOLD)}")
print(f"Medium: {os.path.basename(FONT_MEDIUM)}")
print(f"Regular: {os.path.basename(FONT_REGULAR)}")


def load_font(style, size):
    path = {"bold": FONT_BOLD, "medium": FONT_MEDIUM, "regular": FONT_REGULAR,
            "demi": FONT_DEMI, "light": FONT_LIGHT}.get(style, FONT_REGULAR)
    return ImageFont.truetype(path, size)


def draw_rounded_rect(draw, xy, radius, fill, outline=None, outline_width=2):
    """绘制圆角矩形"""
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=outline_width)


def draw_centered_text(draw, text, font, y, color, x_center=WIDTH//2):
    """居中绘制文本"""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = x_center - tw // 2
    draw.text((x, y), text, fill=color, font=font)
    return bbox[3] - bbox[1]


# ============ 图1：封面 ============
def generate_cover():
    img = Image.new('RGB', (WIDTH, HEIGHT), (255, 248, 235))
    draw = ImageDraw.Draw(img)

    import random as rnd
    rnd.seed(42)
    for _ in range(25):
        x = rnd.randint(0, WIDTH)
        y = rnd.randint(0, HEIGHT)
        r = rnd.randint(3, 10)
        colors = [(236, 111, 35, 50), (255, 200, 100, 30), (212, 91, 76, 40)]
        col = rnd.choice(colors)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=col[:3])

    # 主标题
    font_title = load_font("bold", 68)
    draw_centered_text(draw, "月租199 → 19块", font_title, 280, (60, 60, 60))

    font_sub = load_font("medium", 40)
    draw_centered_text(draw, "运营商不会告诉你的", font_sub, 380, (140, 140, 140))
    draw_centered_text(draw, "流量卡秘密", font_sub, 430, (140, 140, 140))

    # 中间大号价格
    font_price = load_font("bold", 120)
    price_text = "19元/月"
    bbox = draw.textbbox((0, 0), price_text, font=font_price)
    tw = bbox[2] - bbox[0]
    x = (WIDTH - tw) // 2
    draw.text((x+3, 558), price_text, fill=(200, 160, 120), font=font_price)
    draw.text((x, 555), price_text, fill=(236, 111, 35), font=font_price)

    # 流量信息
    font_desc = load_font("medium", 44)
    draw_centered_text(draw, "219G全国通用流量", font_desc, 700, (80, 80, 80))
    font_small = load_font("regular", 32)
    draw_centered_text(draw, "平均每天只要6毛钱", font_small, 780, (180, 120, 80))

    # 对比卡
    card_y = 900
    card_w = 420
    card_h = 130
    gap = 30
    total_w = card_w * 2 + gap
    start_x = (WIDTH - total_w) // 2

    # 旧套餐
    draw_rounded_rect(draw, (start_x, card_y, start_x+card_w, card_y+card_h), 16, (200, 200, 200))
    font_card = load_font("medium", 36)
    bbox = draw.textbbox((0, 0), "199元/月", font=font_card)
    tw = bbox[2] - bbox[0]
    draw.text((start_x + (card_w - tw)//2, card_y + 20), "199元/月", fill=(120, 120, 120), font=font_card)
    bbox = draw.textbbox((0, 0), "30G流量", font=font_card)
    tw = bbox[2] - bbox[0]
    draw.text((start_x + (card_w - tw)//2, card_y + 75), "30G流量", fill=(160, 160, 160), font=font_card)

    # 新套餐
    x2 = start_x + card_w + gap
    draw_rounded_rect(draw, (x2, card_y, x2+card_w, card_y+card_h), 16, (236, 111, 35))
    bbox = draw.textbbox((0, 0), "19元/月", font=font_card)
    tw = bbox[2] - bbox[0]
    draw.text((x2 + (card_w - tw)//2, card_y + 20), "19元/月", fill=(255, 255, 255), font=font_card)
    bbox = draw.textbbox((0, 0), "219G流量", font=font_card)
    tw = bbox[2] - bbox[0]
    draw.text((x2 + (card_w - tw)//2, card_y + 75), "219G流量", fill=(255, 255, 255), font=font_card)

    # 引导
    draw_centered_text(draw, "--- 往下滑查看详情 ---", font_small, 1150, (180, 180, 180))
    draw_centered_text(draw, "#流量卡推荐 #话费省钱", load_font("regular", 24), 1350, (180, 180, 180))

    path = os.path.join(OUTPUT_DIR, "xhs_cover_final.png")
    img.save(path, "PNG")
    print(f"封面 -> {path}")


# ============ 图2-4：套餐详情卡片 ============
CARDS = [
    {
        "name": "联通海藻卡",
        "rank": "TOP 1 - 性价比之王",
        "price": "19元/月",
        "traffic": "219G全国通用",
        "call": "100分钟通话",
        "speed": "5G不限速",
        "per_day": "日均仅0.6元，两颗糖的钱",
        "fit": "适合：学生党 / 年轻人 / 刷剧党",
        "bg_color": (255, 248, 224),
        "accent": (236, 111, 35),
    },
    {
        "name": "电信西沙卡",
        "rank": "TOP 2 - 均衡之选",
        "price": "29元/月",
        "traffic": "220G通用 + 30G定向",
        "call": "300分钟通话",
        "speed": "电信5G - 信号稳定",
        "per_day": "一包零食钱 = 一个月流量自由",
        "fit": "适合：上班族 / 需要稳定通话",
        "bg_color": (232, 246, 233),
        "accent": (76, 175, 80),
    },
    {
        "name": "移动沐雪卡",
        "rank": "TOP 3 - 追剧党福音",
        "price": "20元/月",
        "traffic": "160G通用 + 30G定向",
        "call": "400分钟通话",
        "speed": "移动5G - 覆盖最广",
        "per_day": "400分钟，跟家人聊到饱",
        "fit": "适合：常打电话 / 偏远地区用户",
        "bg_color": (228, 242, 253),
        "accent": (33, 150, 243),
    },
]


def generate_detail_card(card, index):
    img = Image.new('RGB', (WIDTH, HEIGHT), card["bg_color"])
    draw = ImageDraw.Draw(img)

    import random as rnd
    rnd.seed(index * 100)
    for _ in range(18):
        x = rnd.randint(0, WIDTH)
        y = rnd.randint(0, HEIGHT)
        r = rnd.randint(2, 7)
        col = card["accent"][:3] + (30,)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=col[:3])

    y = 180
    font_large = load_font("bold", 54)

    # Rank
    draw_centered_text(draw, card["rank"], font_large, y, card["accent"])
    y += 90

    # 名称
    draw_centered_text(draw, card["name"], load_font("bold", 66), y, (50, 50, 50))
    y += 100

    # 价格
    price_font = load_font("bold", 110)
    bbox = draw.textbbox((0, 0), card["price"], font=price_font)
    tw = bbox[2] - bbox[0]
    x = (WIDTH - tw) // 2
    draw.text((x+3, y+3), card["price"], fill=(180, 180, 180), font=price_font)
    draw.text((x, y), card["price"], fill=card["accent"], font=price_font)
    y += 130

    # 分割线
    line_y = y + 10
    draw.line([(200, line_y), (WIDTH-200, line_y)], fill=card["accent"]+(160,), width=2)
    y += 40

    # 信息卡片
    info_items = [
        f"流量：{card['traffic']}",
        f"通话：{card['call']}",
        f"网速：{card['speed']}",
    ]

    card_margin = 120
    info_card_y1 = y - 20
    info_card_y2 = info_card_y1 + len(info_items) * 75 + 60
    draw_rounded_rect(draw, (card_margin, info_card_y1, WIDTH-card_margin, info_card_y2), 20,
                       fill=(255, 255, 255, 200),
                       outline=card["accent"]+(100,))

    font_small = load_font("regular", 36)
    for item in info_items:
        draw_centered_text(draw, item, font_small, y+10, (80, 80, 80))
        y += 75

    y = info_card_y2 + 50

    # 亮点
    draw_centered_text(draw, card["per_day"], font_small, y, card["accent"])
    y += 70

    # 适合人群
    draw_centered_text(draw, card["fit"], load_font("regular", 30), y, (120, 120, 120))

    # 底部
    draw_centered_text(draw, "留言城市+流量需求，帮你推荐", load_font("light", 28), HEIGHT-120, (160, 160, 160))

    path = os.path.join(OUTPUT_DIR, f"xhs_img{index+2}.jpg")
    img.save(path, "JPEG", quality=92)
    print(f"{card['rank']} -> {path}")


# ============ 图5：选卡3步法 ============
def generate_step_guide():
    img = Image.new('RGB', (WIDTH, HEIGHT), (243, 229, 246))
    draw = ImageDraw.Draw(img)

    font_title = load_font("bold", 56)
    font_step = load_font("medium", 40)
    font_body = load_font("regular", 32)
    font_tiny = load_font("regular", 28)

    draw_centered_text(draw, "选卡3步法", font_title, 150, (80, 50, 100))

    steps = [
        ("Step 1", "看月租预算", [
            "19元 → 入门首选，日常刷剧够用",
            "29元 → 一步到位，流量通话全包",
        ]),
        ("Step 2", "看流量需求", [
            "少于150G/月 → 选便宜的够用",
            "大于等于150G/月 → 选中高档套餐",
        ]),
        ("Step 3", "看号码归属地", [
            "确认运营商在你所在地区有信号",
            "偏远地区优先选移动或电信",
        ]),
    ]

    y = 260
    for step_title, step_sub, details in steps:
        draw_centered_text(draw, step_title, font_step, y, (120, 80, 150))
        y += 50
        draw_centered_text(draw, step_sub, load_font("bold", 46), y, (60, 40, 80))
        y += 65

        margin = (WIDTH - 620) // 2
        for detail in details:
            draw.text((margin, y), f"* {detail}", fill=(100, 90, 110), font=font_body)
            y += 50
        y += 30

    # 底部提示
    y += 20
    tips = [
        "免费申请 | 无预存话费 | 无隐形消费",
        "正规手机卡，能打电话能发短信",
    ]
    for tip in tips:
        draw_centered_text(draw, tip, font_tiny, y, (140, 120, 150))
        y += 40

    draw_centered_text(draw, "--- 评论区留言帮你推荐 ---", load_font("light", 30), HEIGHT-100, (150, 130, 160))

    path = os.path.join(OUTPUT_DIR, "xhs_img5.jpg")
    img.save(path, "JPEG", quality=92)
    print(f"选卡3步法 -> {path}")


# ============ 图6：互动引导图 ============
def generate_cta_card():
    img = Image.new('RGB', (WIDTH, HEIGHT), (255, 242, 223))
    draw = ImageDraw.Draw(img)

    draw_rounded_rect(draw, (60, 200, WIDTH-60, HEIGHT-200), 30, fill=(255, 255, 255, 230))

    font_title = load_font("bold", 52)
    font_body = load_font("regular", 36)
    font_tiny = load_font("regular", 30)

    draw_centered_text(draw, "评论区留下你的信息", font_title, 300, (60, 50, 40))

    y = 420
    lines = [
        "格式：【城市】+【每月需要多少流量】",
        "",
        "示例：",
        "  上海 + 每月150G够不够？",
        "  北京 + 想要多打电话的卡",
        "",
        "我会一对一帮你推荐",
        "最合适的流量卡！",
    ]

    for line in lines:
        if not line.strip():
            y += 20
            continue
        draw_centered_text(draw, line, font_body, y, (100, 90, 80))
        y += 55

    y += 40
    promises = [
        "* 免费咨询 不推销",
        "* 纯经验分享 帮你避坑",
        "* 只推荐适合你的，不推贵的",
    ]
    for p in promises:
        draw_centered_text(draw, p, font_tiny, y, (180, 140, 100))
        y += 45

    y += 20
    draw_centered_text(draw, "--- 觉得有用的话点个赞收藏吧 ---", font_tiny, y, (180, 180, 180))

    path = os.path.join(OUTPUT_DIR, "xhs_img6.jpg")
    img.save(path, "JPEG", quality=92)
    print(f"互动引导图 -> {path}")


if __name__ == "__main__":
    print("="*50)
    print("生成小红书配图 v3 - 哒守哒纪 专用版")
    print("="*50)
    generate_cover()
    for i, card in enumerate(CARDS):
        generate_detail_card(card, i)
    generate_step_guide()
    generate_cta_card()
    print("="*50)
    print("全部完成！输出目录:", OUTPUT_DIR)
    print("="*50)
