# -*- coding: utf-8 -*-
"""8/26 shots: 工作台 dashboard + 分析页 (data ops article)"""
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
        # 关闭引导浮层（下一步 x7）
        for i in range(8):
            try:
                btn = page.get_by_text("下一步", exact=False).first
                if btn.is_visible(timeout=2000):
                    btn.click(timeout=3000)
                    time.sleep(1)
                else:
                    break
            except Exception:
                break
        # 直接 goto dashboard
        page.goto("https://app.fenxiaohao.com/#/dashboard", wait_until="networkidle", timeout=20000)
        time.sleep(5)
        print("dashboard url:", page.url)
        page.screenshot(path=f"{OUT}/workbench_top.jpg", quality=72, type="jpeg")
        time.sleep(1)
        # scroll down for full dashboard (订单趋势 etc)
        for i in range(3):
            page.mouse.wheel(0, 600)
            time.sleep(1.2)
            page.screenshot(path=f"{OUT}/workbench_scroll{i}.jpg", quality=72, type="jpeg")
        # 回到顶部
        page.mouse.wheel(0, -4000)
        time.sleep(2)
        # 尝试分析页：先看侧栏菜单文字
        try:
            menu_text = page.locator(".el-menu, aside, .sidebar, nav").first.inner_text(timeout=5000)
            print("SIDEBAR MENU:", menu_text[:500].replace("\n", " | "))
        except Exception as e:
            print("menu read fail:", type(e).__name__)
        # 尝试常见分析页路由
        for route, tag in [("#/analysis", "analysis"), ("#/data/analysis", "analysis2")]:
            try:
                page.goto("https://app.fenxiaohao.com" + route, wait_until="networkidle", timeout=15000)
                time.sleep(4)
                print(f"{route} -> {page.url}")
                page.screenshot(path=f"{OUT}/{tag}.jpg", quality=72, type="jpeg")
            except Exception as e:
                print(f"route {route} fail:", type(e).__name__)
    except Exception as e:
        print("FATAL:", e)
    finally:
        browser.close()
print("DONE")
