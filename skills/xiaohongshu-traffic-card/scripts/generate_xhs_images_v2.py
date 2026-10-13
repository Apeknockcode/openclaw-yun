#!/usr/bin/env python3
"""
小红书配图生成 v2 - 哒守哒纪
主题：号卡知识科普 - 流量卡避坑指南
角度：个人经验分享，偏生活+知识科普风格
"""

from PIL import Image, ImageDraw, ImageFont
import os, random as rnd

OUTPUT_DIR = os.path.expanduser("~/.openclaw/workspace/assets/xiaohongshu/dashoudaji-v2")
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1080, 1440

# 字体
FONT_CANDIDATES = {
    "bold": "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Bold.ttc",
    "medium": "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Medium.ttc",
    "regular": "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc",
    "demi": "/usr/share/fonts/google-noto-cjk/NotoSansCJK-DemiLight.ttc",
    "light": "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Light.ttc",
}
FONTS = {}
for style, path in FONT_CANDIDATES.items():
    if os.path.exists(path):
        FONTS[style] = path
if not FONTS:
    raise RuntimeError("No Chinese font found!")


def font(style, size):
    p = FONTS.get(style, list(FONTS.values())[0])
    return ImageFont.truetype(p, size)


def center(draw, text, font, y, color, x_center=WIDTH//2):
    bbox = draw.textbbox((0,0), text, font=font)
    x = x_center - (bbox[2]-bbox[0])//2
    draw.text((x,y), text, fill=color, font=font)


def rrect(draw, xy, r, fill, outline=None, w=2):
    draw.rounded_rectangle(xy, r, fill=fill, outline=outline, width=w)


# ============ 图1：封面 ============
def cover():
    img = Image.new('RGB', (WIDTH, HEIGHT), (235, 245, 255))
    draw = ImageDraw.Draw(img)
    rnd.seed(99)
    for _ in range(20):
        x, y = rnd.randint(0,WIDTH), rnd.randint(0,HEIGHT)
        s = rnd.randint(3,12)
        c = [(52,119,237,30),(100,180,255,20),(200,220,255,40)]
        col = rnd.choice(c)
        draw.ellipse([x-s,y-s,x+s,y+s], fill=col[:3])

    center(draw, '办了3张流量卡之后', font("bold",60), 240, (30,60,100))
    center(draw, '我才知道这些坑', font("bold",60), 320, (30,60,100))

    center(draw, '运营商店大欺客的真相', font("medium",36), 450, (80,120,160))
    center(draw, '选卡小白必看的避坑指南', font("medium",36), 500, (80,120,160))

    # 卡片列表
    items = ['「流量虚标」', '「优惠期陷阱」', '「注销套路」']
    y = 620
    for item in items:
        rrect(draw, (180,y, 900,y+70), 12, fill=(255,255,255,200))
        center(draw, item, font("medium",36), y+15, (60,60,60))
        y += 90

    center(draw, '看完这篇帮你省下大几百', font("regular",32), 1050, (100,140,180))
    center(draw, '--- 往下滑看全文 ---', font("light",28), 1200, (160,180,200))
    center(draw, '#流量卡避坑 #话费省钱 #经验分享', font("light",22), 1360, (160,180,200))

    path = os.path.join(OUTPUT_DIR,"cover.png")
    img.save(path,"PNG")
    print(f'封面 -> {path}')


# ============ 图2-4：避坑详情 ============
PITFALLS = [
    {'icon': '1', 'title': '流量虚标',
     'sub': '300G 到手可能就 150G',
     'color': (229,57,53), 'bg': (255,235,235),
     'points': [
        '运营商标的都是理论最高值',
        '通用流量不等于定向流量',
        '很多100G里一半是定向',
        '问清楚：通用多少？定向给谁用？',
     ],
     'tip': '选卡时问清楚通用流量有多少',
    },
    {'icon': '2', 'title': '优惠期陷阱',
     'sub': '前6个月19块，后面变回39',
     'color': (255,160,0), 'bg': (255,248,225),
     'points': [
        '第7个月开始默默恢复原价',
        '自动续费，不提醒也不通知',
        '想注销？先确认优惠期写在哪',
        '合约期内注销要赔违约金',
     ],
     'tip': '选长期有效的套餐，别被短期低价迷惑',
    },
    {'icon': '3', 'title': '注销有多难',
     'sub': '线上办卡，线下注销，故意卡你',
     'color': (56,142,60), 'bg': (232,245,233),
     'points': [
        '异地卡注销要本人去归属地营业厅',
        '客服来回踢皮球不给办',
        '告诉你有合约期不能注销',
        '工信部投诉后才给处理',
     ],
     'tip': '办卡前先问：能线上注销吗？',
    },
]

def gen_detail(p, idx):
    img = Image.new('RGB', (WIDTH, HEIGHT), p["bg"])
    draw = ImageDraw.Draw(img)

    rnd.seed(idx*50)
    for _ in range(15):
        x,y = rnd.randint(0,WIDTH), rnd.randint(0,HEIGHT)
        s = rnd.randint(2,8)
        c = p["color"][:3]+(25,)
        draw.ellipse([x-s,y-s,x+s,y+s], fill=c[:3])

    y = 200
    center(draw, f'{p["icon"]} {p["title"]}', font("bold",64), y, p["color"])
    y += 90
    center(draw, p["sub"], font("medium",38), y, (80,80,80))
    y += 90

    rrect(draw, (100,y-20, 980,y+len(p["points"])*70+40), 18, fill=(255,255,255,220))
    for pt in p["points"]:
        draw.text((140,y+5), f'* {pt}', fill=(60,60,60), font=font("regular",32))
        y += 70

    y += 50
    rrect(draw, (120,y, 960,y+70), 12, fill=p["color"][:3]+(30,))
    center(draw, f'Tip: {p["tip"]}', font("medium",30), y+18, p["color"])

    center(draw, '--- 留言你的踩坑经历 ---', font("light",28), HEIGHT-120, (160,160,160))

    path = os.path.join(OUTPUT_DIR,f'img{idx+2}.jpg')
    img.save(path,"JPEG",quality=92)
    print(f'{p["title"]} -> {path}')


# ============ 图5：选卡对照表 ============
def checklist():
    img = Image.new('RGB', (WIDTH, HEIGHT), (245,240,255))
    draw = ImageDraw.Draw(img)

    center(draw, '办卡前先问这5个问题', font("bold",52), 140, (60,40,100))

    questions = [
        ('通用流量有多少G？', '别被总流量骗了，通用才是真流量'),
        ('优惠期多久？到期后多少钱？', '前半年20块？半年后可能变40'),
        ('能线上注销吗？', '异地卡一定要问清楚注销流程'),
        ('有合约期吗？违约金多少？', '有些卡绑12个月，提前退要赔钱'),
        ('归属地是哪？信号咋样？', '偏远地区先确认运营商信号'),
    ]

    y = 240
    for q,a in questions:
        rrect(draw, (80,y, 1000,y+105), 14, fill=(255,255,255,230))
        draw.text((120,y+12), q, fill=(40,40,80), font=font("medium",30))
        draw.text((120,y+55), a, fill=(120,120,140), font=font("regular",26))
        y += 120

    center(draw, '把这5个问题截图保存', font("regular",30), 1300, (120,100,150))
    center(draw, '办卡的时候一个一个问清楚', font("regular",30), 1350, (120,100,150))

    path = os.path.join(OUTPUT_DIR,"img5.jpg")
    img.save(path,"JPEG",quality=92)
    print(f'选卡对照表 -> {path}')


# ============ 图6：互动 ============
def cta():
    img = Image.new('RGB', (WIDTH, HEIGHT), (240,248,235))
    draw = ImageDraw.Draw(img)

    rrect(draw, (60,200, WIDTH-60, HEIGHT-200), 30, fill=(255,255,255,230))

    center(draw, '你踩过流量卡的坑吗？', font("bold",48), 280, (50,80,50))

    y = 380
    lines = [
        '我办了3张卡才总结出这些经验',
        '如果你也遇到过这些问题：',
        '',
        '- 办的流量卡网速特别慢',
        '- 优惠期到了才发现变贵了',
        '- 想注销发现要违约金',
        '- 流量虚标严重不够用',
        '',
        '评论区说说你的经历！',
        '帮更多人避坑',
    ]
    for l in lines:
        if not l.strip():
            y += 15
            continue
        center(draw, l, font("regular",34), y, (80,90,80))
        y += 55

    y += 20
    for p in ['* 纯个人经验分享', '* 不推销不广告', '* 有问题评论区问']:
        center(draw, p, font("regular",26), y, (140,160,120))
        y += 40

    center(draw, '--- 点个赞让更多人看到吧 ---', font("light",26), y+40, (160,180,160))

    path = os.path.join(OUTPUT_DIR,"img6.jpg")
    img.save(path,"JPEG",quality=92)
    print(f'互动引导 -> {path}')


if __name__ == "__main__":
    print("="*50)
    print("哒守哒纪 - 小红书配图 v2（避坑指南）")
    print("="*50)
    cover()
    for i,p in enumerate(PITFALLS):
        gen_detail(p,i)
    checklist()
    cta()
    print("="*50)
    print("输出:", OUTPUT_DIR)
