# -*- coding: utf-8 -*-
"""8/27: 上传截图到微信CDN"""
import requests, json, os, sys

APPID = "wx09afa091cac18c86"
APPSECRET = ""  # 已抹除：改用环境变量 WX_APPSECRET

def get_token():
    r = requests.get("https://api.weixin.qq.com/cgi-bin/token",
                     params={"grant_type": "client_credential", "appid": APPID, "secret": APPSECRET}, timeout=15)
    return r.json()["access_token"]

tok = get_token()
print("token ok")

shots = ["od_list_top.jpg", "od_list_mid.jpg", "od_detail.jpg",
         "rel_top.jpg", "shop_top.jpg", "agr_top.jpg"]
names = ["od_list_top", "od_list_mid", "od_detail", "rel_top", "shop_top", "agr_top"]
urls = {}
for path, name in zip(shots, names):
    with open("tmp_shots_0827/" + path, "rb") as f:
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

with open("tmp_shots_0827/cdn_urls.json", "w") as f:
    json.dump(urls, f, ensure_ascii=False, indent=2)
print("CDN urls saved")
