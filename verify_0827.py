# -*- coding: utf-8 -*-
"""8/27 verify: dump visible text at each route to confirm screenshot content + sensitive words"""
import time
from playwright.sync_api import sync_playwright

def close_guides(page, max_steps=10):
    for i in range(max_steps):
        try:
            end = page.get_by_text("结束导览", exact=False).first
            if end.is_visible(timeout=800):
                end.click(timeout=2500); return
        except Exception:
            pass
        try:
            btn = page.get_by_text("下一步", exact=False).first
            if btn.is_visible(timeout=800):
                btn.click(timeout=2500); time.sleep(0.6)
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
                el.click(timeout=4000); time.sleep(8); break
        except Exception:
            pass
    for kw in ["一键开始体验", "开始体验", "进入体验", "确定"]:
        try:
            el = page.get_by_text(kw, exact=False).first
            if el.is_visible(timeout=2500):
                el.click(timeout=4000); time.sleep(5); break
        except Exception:
            pass
    page.goto("https://app.fenxiaohao.com/#/dashboard", wait_until="networkidle", timeout=20000)
    time.sleep(5)
    close_guides(page)

    page.goto("https://app.fenxiaohao.com/#/order/orderList", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    print("=== ORDER LIST ===")
    print(page.inner_text("body")[:1200].replace("\n", " | "))

    # click 日志 tab if any
    try:
        t = page.get_by_text("流转日志", exact=False).first
        if t.is_visible(timeout=1500):
            t.click(timeout=3000); time.sleep(3)
            print("=== AFTER 流转日志 CLICK ===")
            print(page.inner_text("body")[:1000].replace("\n", " | "))
    except Exception:
        pass

    page.goto("https://app.fenxiaohao.com/#/enterprise/relationship", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    print("=== RELATIONSHIP ===")
    print(page.inner_text("body")[:800].replace("\n", " | "))

    page.goto("https://app.fenxiaohao.com/#/shop/list", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    print("=== SHOP LIST ===")
    print(page.inner_text("body")[:800].replace("\n", " | "))

    browser.close()
print("DONE")
