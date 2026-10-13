# -*- coding: utf-8 -*-
"""8/26: 上传截图到微信CDN + 生成封面 v39 紫色"""
import requests, json, os, sys

APPID = "wx09afa091cac18c86"
APPSECRET = ""  # 已抹除：改用环境变量 WX_APPSECRET

def get_token():
    r = requests.get("https://api.weixin.qq.com/cgi-bin/token",
                     params={"grant_type": "client_credential", "appid": APPID, "secret": APPSECRET}, timeout=15)
    return r.json()["access_token"]

tok = get_token()
print("token ok")

# 1) 上传截图到 CDN
shots = ["tmp_shots_0826/wb_top.jpg", "tmp_shots_0826/wb_mid.jpg", "tmp_shots_0826/wb_low.jpg",
         "tmp_shots_0826/an_left.jpg", "tmp_shots_0826/an_left2.jpg"]
names = ["wb_top", "wb_mid", "wb_low", "an_left", "an_left2"]
urls = {}
for path, name in zip(shots, names):
    with open(path, "rb") as f:
        r = requests.post("https://api.weixin.qq.com/cgi-bin/media/uploadimg",
                          params={"access_token": tok},
                          files={"media": (name + ".jpg", f, "image/jpeg")}, timeout=30)
    d = r.json()
    if "url" in d:
        urls[name] = d["url"]
        print(name, "->", d["url"][:80])
    else:
        print(name, "FAIL", d)
        sys.exit(1)

with open("tmp_shots_0826/cdn_urls.json", "w") as f:
    json.dump(urls, f, ensure_ascii=False, indent=2)
print("CDN urls saved")
