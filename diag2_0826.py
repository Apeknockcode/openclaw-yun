# -*- coding: utf-8 -*-
"""8/26 diag2: full DOM of dashboard, look for metric cards / iframes"""
import time, re
from playwright.sync_api import sync_playwright

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
        page.goto("https://app.fenxiaohao.com/#/dashboard", wait_until="networkidle", timeout=20000)
        time.sleep(6)
        html = page.content()
        print("HTML len:", len(html))
        print("iframes:", page.locator("iframe").count())
        for kw in ["落地页", "访问量", "订单趋势", "分销商排名", "发货", "激活", "首充", "分析", "订单数"]:
            print(f"  '{kw}' in html:", kw in html, "| in bodytext:", kw in page.inner_text("body"))
        # 点击「首页」导航（可能菜单是折叠的，先hover/click）
        try:
            page.locator("text=首页").first.click(timeout=4000)
            time.sleep(4)
            print("clicked 首页, url:", page.url)
            print("BODY:", page.inner_text("body")[:800].replace("\n", " | "))
        except Exception as e:
            print("首页 click fail:", type(e).__name__)
        # 检查 el-main 区域的实际 HTML 结构
        mains = page.locator("main, .el-main, .app-main, .main-container").all()
        print("main containers:", len(mains))
        for m in mains[:3]:
            try:
                h = m.inner_html()
                print("MAIN HTML head:", h[:500])
            except Exception:
                pass
    except Exception as e:
        print("FATAL:", e)
    finally:
        browser.close()
print("DONE")
