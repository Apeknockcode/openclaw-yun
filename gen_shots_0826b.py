# -*- coding: utf-8 -*-
"""8/26 shots v2: dismiss guide, explore dashboard + find 分析 page"""
import time, os
from playwright.sync_api import sync_playwright

OUT = "/root/.openclaw/workspace/tmp_shots_0826"
os.makedirs(OUT, exist_ok=True)

def login(p, ctx):
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
    return page

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
    page = login(p, ctx)
    try:
        page.goto("https://app.fenxiaohao.com/#/dashboard", wait_until="networkidle", timeout=20000)
        time.sleep(5)
        # 关闭引导浮层：最多 10 次点「下一步」
        for i in range(10):
            try:
                btn = page.get_by_text("下一步", exact=False).first
                if btn.is_visible(timeout=1500):
                    btn.click(timeout=3000)
                    time.sleep(1.2)
                    print(f"guide step {i+1} dismissed")
                else:
                    print(f"guide btn not visible at step {i+1}, break")
                    break
            except Exception:
                print(f"guide exception at step {i+1}")
                break
        time.sleep(3)
        body = page.inner_text("body")
        print("BODY after guide:", body[:1500].replace("\n", " | "))
        # 找含「分析」的元素
        els = page.locator("text=分析").all()
        print("分析 matches:", len(els))
        for e in els[:10]:
            try:
                print("  ->", e.inner_text()[:60], "| href:", e.get_attribute("href"))
            except Exception:
                pass
        # 找所有带 href 的导航链接
        links = page.locator("a[href]").all()
        hrefs = set()
        for l in links:
            try:
                h = l.get_attribute("href")
                if h and h.startswith("#/"):
                    hrefs.add(h)
            except Exception:
                pass
        print("ALL HASH LINKS:", sorted(hrefs))
        page.screenshot(path=f"{OUT}/dashboard_clean.jpg", quality=72, type="jpeg")
        # 滚动截取 dashboard 各段
        for i in range(4):
            page.mouse.wheel(0, 700)
            time.sleep(1.5)
            page.screenshot(path=f"{OUT}/dashboard_s{i}.jpg", quality=72, type="jpeg")
    except Exception as e:
        print("FATAL:", e)
    finally:
        browser.close()
print("DONE")
