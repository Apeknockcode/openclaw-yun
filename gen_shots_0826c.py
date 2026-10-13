# -*- coding: utf-8 -*-
"""8/26 shots v3: dismiss guide fully, dashboard tabs, find 分析"""
import time, os
from playwright.sync_api import sync_playwright

OUT = "/root/.openclaw/workspace/tmp_shots_0826"
os.makedirs(OUT, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
    page = ctx.new_page()
    page.set_default_timeout(12000)
    try:
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
        # 关引导：下一步×N，出现「结束导览」就点
        for i in range(12):
            try:
                end = page.get_by_text("结束导览", exact=False).first
                if end.is_visible(timeout=1200):
                    end.click(timeout=3000)
                    print("guide ended")
                    break
            except Exception:
                pass
            try:
                btn = page.get_by_text("下一步", exact=False).first
                if btn.is_visible(timeout=1200):
                    btn.click(timeout=3000)
                    time.sleep(1)
                else:
                    break
            except Exception:
                break
        time.sleep(3)
        # 回到 dashboard
        page.goto("https://app.fenxiaohao.com/#/dashboard", wait_until="networkidle", timeout=20000)
        time.sleep(6)
        body = page.inner_text("body")
        print("DASHBOARD BODY:", body[:2000].replace("\n", " | "))
        page.screenshot(path=f"{OUT}/dashboard_top.jpg", quality=72, type="jpeg")
        # 找「分析」可点元素
        for txt in ["分析", "工作台", "数据看板"]:
            els = page.get_by_text(txt, exact=False).all()
            print(f"text '{txt}' matches:", len(els))
            for e in els[:5]:
                try:
                    print("   ->", e.inner_text()[:50])
                except Exception:
                    pass
        # 滚动截图
        for i in range(4):
            page.mouse.wheel(0, 700)
            time.sleep(1.5)
            page.screenshot(path=f"{OUT}/dash_s{i}.jpg", quality=72, type="jpeg")
    except Exception as e:
        print("FATAL:", e)
    finally:
        browser.close()
print("DONE")
