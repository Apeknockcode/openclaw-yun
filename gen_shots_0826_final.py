# -*- coding: utf-8 -*-
"""8/26 final shots: 工作台 + 分析页（避开含'开卡'状态词的订单状态分布区域）"""
import time, os
from playwright.sync_api import sync_playwright

OUT = "/root/.openclaw/workspace/tmp_shots_0826"
os.makedirs(OUT, exist_ok=True)

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
    # 工作台（#/dashboard/desk）
    page.goto("https://app.fenxiaohao.com/#/dashboard/desk", wait_until="networkidle", timeout=20000)
    time.sleep(6)
    print("workbench url:", page.url)
    page.screenshot(path=f"{OUT}/wb_top.jpg", quality=72, type="jpeg")
    page.mouse.wheel(0, 520); time.sleep(1.5)
    page.screenshot(path=f"{OUT}/wb_mid.jpg", quality=72, type="jpeg")
    page.mouse.wheel(0, 520); time.sleep(1.5)
    page.screenshot(path=f"{OUT}/wb_low.jpg", quality=72, type="jpeg")
    # 分析页 tab（顶部区域，维度筛选+核心指标对比，不滚动到订单状态分布）
    try:
        tab = page.get_by_text("分析页", exact=True).first
        tab.click(timeout=4000)
        time.sleep(6)
        print("analysis url:", page.url)
        page.screenshot(path=f"{OUT}/an_top.jpg", quality=72, type="jpeg")
        page.mouse.wheel(0, 450); time.sleep(1.5)
        page.screenshot(path=f"{OUT}/an_mid.jpg", quality=72, type="jpeg")
        # 检查当前视口文本是否含'开卡'
        body = page.inner_text("body")
        print("viewport contains 开卡:", "开卡" in body[:2000])
    except Exception as e:
        print("analysis fail:", type(e).__name__, e)
    browser.close()
print("DONE")
