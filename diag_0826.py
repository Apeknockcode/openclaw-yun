# -*- coding: utf-8 -*-
"""Diagnose dashboard/analysis page content"""
import time
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
        print("URL after login flow:", page.url)
        time.sleep(3)
        for route in ["#/dashboard", "#/analysis", "#/dashboard"]:
            page.goto("https://app.fenxiaohao.com" + route, wait_until="networkidle", timeout=20000)
            time.sleep(5)
            print(f"===== {route} =====")
            print("URL:", page.url)
            body = page.inner_text("body")
            print("BODY TEXT (first 1200):", body[:1200].replace("\n", " | "))
            print("canvases:", page.locator("canvas").count())
            page.screenshot(path=f"/root/.openclaw/workspace/tmp_shots_0826/diag_{route[2:]}.jpg", quality=70, type="jpeg")
    except Exception as e:
        print("FATAL:", e)
    finally:
        browser.close()
print("DONE")
