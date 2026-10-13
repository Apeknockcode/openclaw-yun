# -*- coding: utf-8 -*-
"""Debug: capture demo env state"""
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.set_default_timeout(15000)
    try:
        page.goto("https://app.fenxiaohao.com/#/login", wait_until="networkidle", timeout=30000)
        time.sleep(3)
        print("URL:", page.url)
        body = page.inner_text("body")[:500].replace("\n", " | ")
        print("BODY:", body)
        for kw in ["快速体验", "一键开始体验", "立即体验"]:
            try:
                el = page.get_by_text(kw, exact=False).first
                print(kw, "visible:", el.is_visible(timeout=2000))
            except Exception as e:
                print(kw, "not visible:", type(e).__name__)
    except Exception as e:
        print("FATAL:", e)
    finally:
        browser.close()
print("DONE")
