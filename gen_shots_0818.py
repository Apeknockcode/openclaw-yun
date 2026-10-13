# -*- coding: utf-8 -*-
"""8/18 shots attempt 2: handle modal + new tab"""
import time, os
from playwright.sync_api import sync_playwright

OUT = "/root/.openclaw/workspace/tmp_shots_0818"
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
        print("pages:", len(ctx.pages), "url:", page.url)
        # 可能是新 tab
        if len(ctx.pages) > 1:
            page = ctx.pages[-1]
            page.wait_for_load_state("networkidle", timeout=20000)
            time.sleep(4)
        # 尝试模态框按钮（选择业务场景）
        for kw in ["宽带演示", "号卡演示"]:
            try:
                el = page.get_by_text(kw, exact=False).first
                if el.is_visible(timeout=2500):
                    el.click(timeout=4000)
                    print("clicked scene:", kw)
                    time.sleep(8)
                    break
            except Exception:
                pass
        for kw in ["一键开始体验", "开始体验", "进入体验", "确定"]:
            try:
                el = page.get_by_text(kw, exact=False).first
                if el.is_visible(timeout=2500):
                    el.click(timeout=4000)
                    print("clicked modal:", kw)
                    time.sleep(5)
                    break
            except Exception:
                pass
        print("final url:", page.url)
        body = page.inner_text("body")[:300].replace("\n", " | ")
        print("BODY:", body)
        time.sleep(2)
        page.screenshot(path=f"{OUT}/state.jpg", quality=70, type="jpeg")
        # 菜单（演示环境为短标签：关系/组织/资金）
        for menu_kw, tag in [("关系", "guanxi"), ("组织", "zuzhi"), ("资金", "zijin")]:
            try:
                item = page.locator(f"text={menu_kw}").first
                item.click(timeout=6000)
                time.sleep(3)
                page.screenshot(path=f"{OUT}/{tag}.jpg", quality=70, type="jpeg")
                print(f"saved {tag}.jpg")
            except Exception as e:
                print(f"menu {menu_kw} failed: {type(e).__name__}")
    except Exception as e:
        print("FATAL:", e)
    finally:
        browser.close()
print("DONE")
