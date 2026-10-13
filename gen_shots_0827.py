# -*- coding: utf-8 -*-
"""8/27 shots v2: clip 右侧内容区（避开左侧菜单'靓号'字样）+ 订单详情弹窗 + 协议管理"""
import time, os
from playwright.sync_api import sync_playwright

OUT = "/root/.openclaw/workspace/tmp_shots_0827"
os.makedirs(OUT, exist_ok=True)
CLIP = {"x": 280, "y": 0, "width": 1160, "height": 900}  # 裁掉左侧菜单栏

def close_guides(page, max_steps=12):
    for i in range(max_steps):
        try:
            end = page.get_by_text("结束导览", exact=False).first
            if end.is_visible(timeout=1000):
                end.click(timeout=3000)
                print("guide ended")
                return
        except Exception:
            pass
        try:
            btn = page.get_by_text("下一步", exact=False).first
            if btn.is_visible(timeout=1000):
                btn.click(timeout=3000)
                time.sleep(0.8)
            else:
                return
        except Exception:
            return
    time.sleep(2)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
    page = ctx.new_page()
    page.set_default_timeout(12000)
    page.goto("https://app.fenxiaohao.com/#/login", wait_until="networkidle", timeout=30000)
    time.sleep(3)
    page.get_by_text("快速体验", exact=False).first.click(timeout=8000)
    time.sleep(4)
    if len(ctx.pages) > 1:
        page = ctx.pages[-1]
        page.wait_for_load_state("networkidle", timeout=20000)
        time.sleep(4)
    for kw in ["宽带演示", "号卡演示"]:
        try:
            el = page.get_by_text(kw, exact=False).first
            if el.is_visible(timeout=2500):
                el.click(timeout=4000)
                time.sleep(8)
                break
        except Exception:
            pass
    for kw in ["一键开始体验", "开始体验", "进入体验", "确定"]:
        try:
            el = page.get_by_text(kw, exact=False).first
            if el.is_visible(timeout=2500):
                el.click(timeout=4000)
                time.sleep(5)
                break
        except Exception:
            pass
    page.goto("https://app.fenxiaohao.com/#/dashboard", wait_until="networkidle", timeout=20000)
    time.sleep(5)
    close_guides(page)

    # 1) 订单管理列表（clip 右侧）
    page.goto("https://app.fenxiaohao.com/#/order/orderList", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    page.screenshot(path=f"{OUT}/od_list_top.jpg", quality=75, type="jpeg", clip=CLIP)
    page.mouse.wheel(0, 450); time.sleep(1.5)
    page.screenshot(path=f"{OUT}/od_list_mid.jpg", quality=75, type="jpeg", clip=CLIP)

    # 2) 订单详情弹窗（点第一行「详情」）
    try:
        det = page.get_by_text("详情", exact=True).first
        if det.is_visible(timeout=3000):
            det.click(timeout=4000)
            time.sleep(3)
            page.screenshot(path=f"{OUT}/od_detail.jpg", quality=75, type="jpeg", clip=CLIP)
            # 找「日志」tab 或「流转日志」
            for kw in ["流转日志", "日志"]:
                try:
                    t = page.get_by_text(kw, exact=False).first
                    if t.is_visible(timeout=1500):
                        t.click(timeout=3000)
                        time.sleep(3)
                        page.screenshot(path=f"{OUT}/od_log.jpg", quality=75, type="jpeg", clip=CLIP)
                        print("log view captured:", kw)
                        break
                except Exception:
                    pass
            page.keyboard.press("Escape"); time.sleep(1.5)
    except Exception as e:
        print("order detail fail:", type(e).__name__, e)

    # 3) 关系管理（我的分销商）
    page.goto("https://app.fenxiaohao.com/#/enterprise/relationship", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    page.screenshot(path=f"{OUT}/rel_top.jpg", quality=75, type="jpeg", clip=CLIP)

    # 4) 店铺列表
    page.goto("https://app.fenxiaohao.com/#/shop/list", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    page.screenshot(path=f"{OUT}/shop_top.jpg", quality=75, type="jpeg", clip=CLIP)

    # 5) 协议管理
    page.goto("https://app.fenxiaohao.com/#/agreement/agreemantList", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    page.screenshot(path=f"{OUT}/agr_top.jpg", quality=75, type="jpeg", clip=CLIP)

    browser.close()
print("DONE")
