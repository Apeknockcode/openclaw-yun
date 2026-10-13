# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Related

- [Agent workspace](/concepts/agent-workspace)

## 足球数据源补充（2026-09-10 实测 · 已固化进 SKILL.md 数据源清单）
- ✅ **官方竞彩 API** `webapi.sporttery.cn` getMatchCalculatorV1：HAD/HHAD/TTG/CRS 全赔率（含总进球/比分），最可靠
- ✅ **titan007（球探）**：`bf.titan007.com/football/Next_YYYYMMDD.htm`（赛程+sId）→ `zq.titan007.com/analysis/{sId}cn.htm` —— **必须带 Referer: bf.titan007.com**（否则连接被拒）；含伤停/停赛/资格限制+上轮首发+天气+大小球初盘+盘路
- ✅ **okooo**：竞彩页 + `/jingcai/shuju/pankou/`（亚盘 15 家走势，静态）+ history 页——**history 必须 gb18030 解码**（iconv gb2312 会中途截断→误判「数据缺失」）

## 足球数据源可用性（2026-08-17 实测）
- ✅ okooo.com：积分榜/竞彩赔率/H2H+365亚盘终指（history 页）全静态可用；/qingbao/ 和 /team/ 被 WAF 405
- ✅ 500.com odds：shuju/yazhi/daxiao(大小球盘口)/touzhu(必发交易量)/youliao(专家标题) 可用（部分 -L 跟随 302）；shuju_zhanji.php 近况接口需 session 拿不到
- ❌ 雷速 leisu.com：**服务器 IP 被 WAF 拉黑**（403 denied by IP ACL=blacklist），所有域名含 api/img/static 全封，无法使用
- ❌ 腾讯 matchweb.sports.qq.com：API 通但返回空 data（无比赛数据）
- ❌ 直播吧：页面可访问但数据站 data.zhibo8.cc 是闭源 SPA
- ❌ 懂球帝：API 需 app token
- ⚠️ web_search(Perplexity)：402 额度耗尽（经常性）

## 分小号演示环境截图（2026-08-20 实测）

- 登录：app.fenxiaohao.com/#/login → 快速体验 → 宽带演示 → 一键开始体验（引导浮层点「下一步」×7 可关）
- ⚠️ **侧栏菜单 JS 点击在演示环境被遮挡/失效，截图一律用 hash 路由 goto 直达**：
  - 工作台/首页：`#/dashboard`
  - 产品-销售中心：`#/products/onsale`（采购市场/下架/新增：`#/products/productsList`、`#/products/offsale`、`#/products/ProAdd`）
  - 店铺列表：`#/shop/list`（装修：`#/shop/decoration`）
  - 订单：`#/order/orderList`
  - 资金：`#/fund/commission`、`#/payment/record`、`#/balance/transaction`
  - 关系：`#/enterprise/relationship`、`#/enterprise/custom-supplier`
  - 协议：`#/agreement/agreemantList`
  - 组织：`#/org/roles`、`#/org/sub-accounts`、`#/org/sales-staff`
  - 素材：`#/file/fileManage`、`#/file/materialLibrary`；工具：`#/operation/operation-tools`；日志：`#/logs/loginLog`

## 足球数据源补充（2026-09-19 实测新增）
- ✅ **titan 亚盘页（新发现，免登录）**：`vip.titan007.com/AsianOdds_n.aspx?id={sId}&l=0` —— 15 家指数公司「初盘→即时」水位/盘口 + **升盘/降盘计数 + 高水/低水计数**（判定「市场否定让球方」的硬信号）；同一页给出 `OverDown_n.aspx?id={sId}&l=0`（进球数/大小球同结构）与 `Corner.aspx`（角球）、`1x2.asp`（欧赔，实测 404）
- ✅ titan 分析页 `zq.titan007.com/analysis/{sId}cn.htm`（**Referer: bf.titan007.com**，页面为 UTF-8）：积分/主客/近6 进失球、盘路赢盘率+大球率、**阵容情况（伤停+原因）**、上一场首发、球员评分、赛前简报（含 H2H 文字）；**对赛往绩/近期战绩字段为空**（H2H 只能取简报文字）
- ✅ 竞彩官方 API 只开 HAD+HHAD 时（TTG/CRS/HAFU 空）→ 进球区间腿无法定价，主串只能用让球宽格腿

- ⚠️ **竞彩 API 按 poolCode 过滤**（2026-09-19 教训）：`getMatchCalculatorV1.qry` 只返回请求里列出的玩法；查询必须写 `poolCode=had,hhad,ttg,crs,hafu`，否则 TTG/CRS/HAFU 字段为空 → **误判「未开售总进球/比分/半全场」**（首查仅 had,hhad 即踩坑）

## 足球数据源补充（2026-09-20 实测）
- ✅ **竞彩官方 API** `webapi.sporttery.cn/gateway/jc/football/getMatchCalculatorV1.qry?poolCode=had,hhad,ttg,crs,hafu&channel=c`：**必须带 `Referer: https://www.sporttery.cn/`**；返回**当前在售**全部场次（businessDate / matchNumStr / HAD+HHAD 让球线 / TTG / CRS / HAFU）。
- ❌ `getMatchListV1.qry` → **「禁止访问」（403）不可用**（备选用 getMatchCalculatorV1 取赛程）。
- ⚠️ titan `bf.titan007.com/football/Next_YYYYMMDD.htm`：静态 HTML 只见联赛筛选项，**逐场赛程行为 JS 装载**（本次未直接从该页拿到编号→sId 映射，赛程改用竞彩 API）。
