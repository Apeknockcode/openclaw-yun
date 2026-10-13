const sharp = require('sharp');
const fs = require('path');

const FONT = '/usr/share/fonts/google-noto-vf/NotoSans-VF.ttf';
const W = 1080, H = 1440;
const OUT = '/root/.openclaw/workspace/assets/xiaohongshu/20260714';

function svg(w, h, content) {
  return Buffer.from(
    `<svg width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg">
      <style>
        @font-face { font-family: 'Noto'; src: url('file://${FONT}'); }
        * { font-family: 'Noto', sans-serif; }
      </style>
      ${content}
    </svg>`
  );
}

// ============ 图1: 封面 ============
async function genCover() {
  const s = svg(W, H, `
    <rect width="1080" height="1440" fill="#f0f7ff"/>
    <rect x="0" y="0" width="1080" height="1440" fill="url(#bg)" fill-opacity="0.05"/>
    <defs>
      <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#4A90D9"/>
        <stop offset="100%" stop-color="#2B5EA7"/>
      </linearGradient>
    </defs>
    <!-- Top banner -->
    <rect x="60" y="60" width="960" height="200" rx="20" fill="#2B5EA7"/>
    <text x="540" y="150" text-anchor="middle" fill="white" font-size="58" font-weight="700">租房党办卡避坑</text>
    <text x="540" y="220" text-anchor="middle" fill="#B8D4FF" font-size="38">实测3个月的真实体验</text>
    
    <!-- Phone mockup -->
    <rect x="340" y="320" width="400" height="580" rx="40" fill="white" stroke="#ddd" stroke-width="4"/>
    <rect x="340" y="320" width="400" height="60" rx="40" fill="#f5f5f5"/>
    <rect x="340" y="360" width="400" height="20" fill="#f5f5f5"/>
    <rect x="500" y="340" width="80" height="12" rx="6" fill="#333"/>
    <text x="540" y="420" text-anchor="middle" fill="#333" font-size="28">📱 流量卡</text>
    <text x="540" y="480" text-anchor="middle" fill="#666" font-size="24">月租低至19元</text>
    <text x="540" y="530" text-anchor="middle" fill="#666" font-size="24">100G大流量</text>
    <rect x="440" y="580" width="200" height="50" rx="25" fill="#4A90D9"/>
    <text x="540" y="613" text-anchor="middle" fill="white" font-size="26">已办卡 3 张</text>
    <text x="540" y="750" text-anchor="middle" fill="#999" font-size="20">对比实测 · 干货分享</text>
    <text x="540" y="790" text-anchor="middle" fill="#999" font-size="20">无广 · 放心食用</text>

    <!-- Bottom bar -->
    <rect x="60" y="1220" width="960" height="120" rx="60" fill="#4A90D9" opacity="0.15"/>
    <text x="540" y="1295" text-anchor="middle" fill="#2B5EA7" font-size="32">👆 收藏备用 · 办卡前看一遍</text>
    
    <!-- Decorative elements -->
    <circle cx="150" cy="1100" r="40" fill="#4A90D9" opacity="0.1"/>
    <circle cx="930" cy="400" r="30" fill="#4A90D9" opacity="0.08"/>
    <circle cx="100" cy="300" r="20" fill="#4A90D9" opacity="0.12"/>
  `);
  await sharp(s).png().toFile(`${OUT}/cover.png`);
  console.log('✅ 图1 cover.png');
}

// ============ 图2: 月租对比 ============
async function genImg2() {
  const plans = [
    { name: 'A套餐', p1: '0元', p2: '19元', p3: '39元', color: '#E8F4FD' },
    { name: 'B套餐', p1: '29元', p2: '29元', p3: '59元', color: '#F0F7E8' },
    { name: 'C套餐', p1: '免费', p2: '19元', p3: '29元', color: '#FFF3E0' },
    { name: 'D套餐', p1: '9元', p2: '29元', p3: '49元', color: '#FCE4EC' },
  ];
  let rows = plans.map((p, i) => {
    const y = 340 + i * 220;
    return `
      <rect x="140" y="${y}" width="800" height="200" rx="16" fill="${p.color}"/>
      <text x="220" y="${y+75}" text-anchor="middle" fill="#333" font-size="32" font-weight="700">${p.name}</text>
      <text x="420" y="${y+75}" text-anchor="middle" fill="#666" font-size="28">${p.p1}</text>
      <text x="620" y="${y+75}" text-anchor="middle" fill="#E74C3C" font-size="32" font-weight="700">${p.p2}</text>
      <text x="820" y="${y+75}" text-anchor="middle" fill="#999" font-size="28" text-decoration="line-through">${p.p3}</text>
      <!-- column labels -->
      ${i === 0 ? `
        <text x="220" y="${y-20}" text-anchor="middle" fill="#999" font-size="22">套餐名</text>
        <text x="420" y="${y-20}" text-anchor="middle" fill="#999" font-size="22">首月</text>
        <text x="620" y="${y-20}" text-anchor="middle" fill="#999" font-size="22">优惠期</text>
        <text x="820" y="${y-20}" text-anchor="middle" fill="#999" font-size="22">原价</text>
      ` : ''}
      <!-- highlight cheapest -->
      ${p.name === 'C套餐' ? `
        <rect x="580" y="${y+85}" width="90" height="36" rx="18" fill="#4CAF50"/>
        <text x="625" y="${y+110}" text-anchor="middle" fill="white" font-size="20">超值</text>
      ` : ''}
    `;
  }).join('');

  const s = svg(W, H, `
    <rect width="1080" height="1440" fill="#FAFAFA"/>
    <text x="540" y="120" text-anchor="middle" fill="#333" font-size="50" font-weight="700">📊 月租对比</text>
    <text x="540" y="180" text-anchor="middle" fill="#999" font-size="26">各套餐不同时期价格一览</text>
    ${rows}
    <rect x="140" y="1220" width="800" height="100" rx="16" fill="#FFF8E1"/>
    <text x="540" y="1275" text-anchor="middle" fill="#E65100" font-size="26">⚠️ 注意优惠期结束后的价格！办卡前问清楚</text>
    <text x="540" y="1400" text-anchor="middle" fill="#999" font-size="22">💡 收藏对比 · 办卡不被坑</text>
  `);
  await sharp(s).png().toFile(`${OUT}/img2.png`);
  console.log('✅ 图2 img2.png');
}

// ============ 图3: 网速对比 ============
async function genImg3() {
  const s = svg(W, H, `
    <rect width="1080" height="1440" fill="#FAFAFA"/>
    <text x="540" y="120" text-anchor="middle" fill="#333" font-size="48" font-weight="700">🌐 高峰期 vs 凌晨网速</text>
    <text x="540" y="180" text-anchor="middle" fill="#999" font-size="26">实测数据对比</text>
    
    <!-- Left: peak -->
    <rect x="80" y="260" width="440" height="500" rx="24" fill="#FFF0F0"/>
    <rect x="80" y="260" width="440" height="80" rx="24" fill="#FF6B6B"/>
    <rect x="80" y="300" width="440" height="40" fill="#FF6B6B"/>
    <text x="300" y="315" text-anchor="middle" fill="white" font-size="32" font-weight="700">🌆 晚上8点</text>
    
    <!-- Speed gauge -->
    <circle cx="300" cy="420" r="80" fill="none" stroke="#FFCDD2" stroke-width="12"/>
    <path d="M 300 420 L 300 355" stroke="#FF6B6B" stroke-width="8" stroke-linecap="round"/>
    <text x="300" y="430" text-anchor="middle" fill="#FF6B6B" font-size="48" font-weight="700">12</text>
    <text x="300" y="465" text-anchor="middle" fill="#FF6B6B" font-size="22">Mbps</text>
    
    <text x="300" y="540" text-anchor="middle" fill="#666" font-size="24">刷视频卡顿 ❌</text>
    <text x="300" y="580" text-anchor="middle" fill="#666" font-size="24">加载缓慢 😫</text>
    <text x="300" y="620" text-anchor="middle" fill="#666" font-size="24">网页转圈 ⏳</text>
    <rect x="180" y="660" width="240" height="50" rx="25" fill="#FF6B6B" opacity="0.15"/>
    <text x="300" y="693" text-anchor="middle" fill="#FF6B6B" font-size="24">差</text>
    
    <!-- Right: off-peak -->
    <rect x="560" y="260" width="440" height="500" rx="24" fill="#F0FFF0"/>
    <rect x="560" y="260" width="440" height="80" rx="24" fill="#4CAF50"/>
    <rect x="560" y="300" width="440" height="40" fill="#4CAF50"/>
    <text x="780" y="315" text-anchor="middle" fill="white" font-size="32" font-weight="700">🌙 凌晨2点</text>
    
    <circle cx="780" cy="420" r="80" fill="none" stroke="#C8E6C9" stroke-width="12"/>
    <path d="M 780 420 L 780 355" stroke="#4CAF50" stroke-width="12" stroke-linecap="round"/>
    <text x="780" y="430" text-anchor="middle" fill="#4CAF50" font-size="48" font-weight="700">85</text>
    <text x="780" y="465" text-anchor="middle" fill="#4CAF50" font-size="22">Mbps</text>
    
    <text x="780" y="540" text-anchor="middle" fill="#666" font-size="24">视频秒开 ✅</text>
    <text x="780" y="580" text-anchor="middle" fill="#666" font-size="24">下载飞快 🚀</text>
    <text x="780" y="620" text-anchor="middle" fill="#666" font-size="24">体验流畅 ✨</text>
    <rect x="660" y="660" width="240" height="50" rx="25" fill="#4CAF50" opacity="0.15"/>
    <text x="780" y="693" text-anchor="middle" fill="#4CAF50" font-size="24">优</text>
    
    <!-- Difference arrow -->
    <rect x="470" y="440" width="140" height="60" rx="10" fill="#FFF3E0"/>
    <text x="540" y="478" text-anchor="middle" fill="#E65100" font-size="24">差 7 倍</text>
    
    <rect x="80" y="880" width="920" height="100" rx="16" fill="#FFF8E1"/>
    <text x="540" y="930" text-anchor="middle" fill="#E65100" font-size="26">💡 流量卡高峰期拥堵是普遍现象，选卡时看看评价</text>
    
    <text x="540" y="1100" text-anchor="middle" fill="#999" font-size="22">📌 办卡前搜一下"XX卡 网速"看真实反馈</text>
  `);
  await sharp(s).png().toFile(`${OUT}/img3.png`);
  console.log('✅ 图3 img3.png');
}

// ============ 图4: 主副卡搭配 ============
async function genImg4() {
  const s = svg(W, H, `
    <rect width="1080" height="1440" fill="#F0FFF4"/>
    <text x="540" y="120" text-anchor="middle" fill="#333" font-size="50" font-weight="700">💳 主卡 + 副卡最佳搭配</text>
    <text x="540" y="180" text-anchor="middle" fill="#999" font-size="26">一个月话费不到 40 元</text>
    
    <!-- Left: 主卡 -->
    <rect x="80" y="280" width="400" height="520" rx="24" fill="white" stroke="#4A90D9" stroke-width="3"/>
    <rect x="80" y="280" width="400" height="90" rx="24" fill="#4A90D9"/>
    <rect x="80" y="330" width="400" height="40" fill="#4A90D9"/>
    <text x="280" y="340" text-anchor="middle" fill="white" font-size="34" font-weight="700">主卡</text>
    
    <text x="280" y="430" text-anchor="middle" fill="#666" font-size="26">保号套餐</text>
    <text x="280" y="490" text-anchor="middle" fill="#4A90D9" font-size="64" font-weight="700">8<text font-size="32">元/月</text></text>
    
    <text x="280" y="580" text-anchor="middle" fill="#999" font-size="22">接打电话 ✅</text>
    <text x="280" y="620" text-anchor="middle" fill="#999" font-size="22">收验证码 ✅</text>
    <text x="280" y="660" text-anchor="middle" fill="#999" font-size="22">少量流量</text>
    
    <!-- Center: + -->
    <text x="540" y="540" text-anchor="middle" fill="#4A90D9" font-size="72" font-weight="700">+</text>
    
    <!-- Right: 副卡 -->
    <rect x="600" y="280" width="400" height="520" rx="24" fill="white" stroke="#4CAF50" stroke-width="3"/>
    <rect x="600" y="280" width="400" height="90" rx="24" fill="#4CAF50"/>
    <rect x="600" y="330" width="400" height="40" fill="#4CAF50"/>
    <text x="800" y="340" text-anchor="middle" fill="white" font-size="34" font-weight="700">副卡</text>
    
    <text x="800" y="430" text-anchor="middle" fill="#666" font-size="26">流量卡</text>
    <text x="800" y="490" text-anchor="middle" fill="#4CAF50" font-size="54" font-weight="700">19~29<text font-size="32">元/月</text></text>
    <text x="800" y="550" text-anchor="middle" fill="#4CAF50" font-size="28">100G 大流量</text>
    
    <text x="800" y="620" text-anchor="middle" fill="#999" font-size="22">刷视频 ✅</text>
    <text x="800" y="660" text-anchor="middle" fill="#999" font-size="22">上网冲浪 ✅</text>
    <text x="800" y="700" text-anchor="middle" fill="#999" font-size="22">热点分享 ✅</text>
    
    <!-- Bottom: total -->
    <rect x="140" y="900" width="800" height="120" rx="60" fill="url(#g_total)"/>
    <defs>
      <linearGradient id="g_total" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#4A90D9"/>
        <stop offset="100%" stop-color="#4CAF50"/>
      </linearGradient>
    </defs>
    <text x="540" y="965" text-anchor="middle" fill="white" font-size="40" font-weight="700">每月总花费 ≈ 8 + 19~29</text>
    <text x="540" y="1010" text-anchor="middle" fill="#E8F5E9" font-size="36">不到 40 元 💰</text>
    
    <!-- Tips -->
    <rect x="80" y="1100" width="920" height="200" rx="20" fill="#FFF8E1"/>
    <text x="540" y="1155" text-anchor="middle" fill="#E65100" font-size="28">💡 搭配秘籍</text>
    <text x="540" y="1205" text-anchor="middle" fill="#666" font-size="24">1. 主卡选运营商最低保号套餐</text>
    <text x="540" y="1245" text-anchor="middle" fill="#666" font-size="24">2. 副卡选纯流量卡，用完可注销更换</text>
  `);
  await sharp(s).png().toFile(`${OUT}/img4.png`);
  console.log('✅ 图4 img4.png');
}

// ============ 图5: 自测清单 ============
async function genImg5() {
  const items = [
    { q: '优惠期多久？到期后恢复多少钱？', check: false },
    { q: '流量是通用还是定向？超出怎么收费？', check: false },
    { q: '能不能线上注销？用不用去归属地？', check: false },
    { q: '高峰期网速怎么样？（搜搜评价）', check: false },
    { q: '售后渠道方便吗？客服响应快吗？', check: false },
  ];
  let list = items.map((item, i) => {
    const y = 340 + i * 180;
    return `
      <rect x="100" y="${y}" width="880" height="150" rx="16" fill="${i % 2 === 0 ? '#F5F9FF' : 'white'}" stroke="#E0E0E0" stroke-width="1"/>
      <rect x="130" y="${y+45}" width="40" height="40" rx="6" fill="none" stroke="#4A90D9" stroke-width="3"/>
      <text x="200" y="${y+73}" fill="#333" font-size="26">第${i+1}问</text>
      <text x="200" y="${y+110}" fill="#666" font-size="26">${item.q}</text>
    `;
  }).join('');

  const s = svg(W, H, `
    <rect width="1080" height="1440" fill="#FAFAFA"/>
    <text x="540" y="120" text-anchor="middle" fill="#333" font-size="48" font-weight="700">📋 办卡前问自己这 5 个问题</text>
    <text x="540" y="180" text-anchor="middle" fill="#999" font-size="26">全部确认后再下单👇</text>
    ${list}
    
    <rect x="100" y="1260" width="880" height="100" rx="16" fill="#E8F5E9"/>
    <text x="540" y="1310" text-anchor="middle" fill="#2E7D32" font-size="26">✅ 5个问题都确认了？可以放心办卡了</text>
    <text x="540" y="1350" text-anchor="middle" fill="#666" font-size="22">📌 收藏本文 · 办卡时对照</text>
  `);
  await sharp(s).png().toFile(`${OUT}/img5.png`);
  console.log('✅ 图5 img5.png');
}

// ============ 图6: 互动引导 ============
async function genImg6() {
  const s = svg(W, H, `
    <rect width="1080" height="1440" fill="#FFF5F5"/>
    
    <!-- Decorative circles -->
    <circle cx="540" cy="200" r="300" fill="#FFE0E0" opacity="0.3"/>
    
    <text x="540" y="350" text-anchor="middle" fill="#E91E63" font-size="64" font-weight="700">💬</text>
    <text x="540" y="460" text-anchor="middle" fill="#333" font-size="56" font-weight="700">你一个月话费多少？</text>
    <text x="540" y="540" text-anchor="middle" fill="#999" font-size="30">被套餐坑过吗？评论区聊聊吧 👇</text>
    
    <!-- Chat bubble -->
    <rect x="200" y="620" width="680" height="90" rx="45" fill="white" stroke="#E0E0E0" stroke-width="2"/>
    <text x="540" y="677" text-anchor="middle" fill="#666" font-size="26">我一个月要交 128 元 😭</text>
    
    <rect x="260" y="740" width="560" height="90" rx="45" fill="white" stroke="#E0E0E0" stroke-width="2"/>
    <text x="540" y="797" text-anchor="middle" fill="#666" font-size="26">办了保号套餐只要 8 块！</text>
    
    <rect x="300" y="860" width="480" height="90" rx="45" fill="white" stroke="#E0E0E0" stroke-width="2"/>
    <text x="540" y="917" text-anchor="middle" fill="#666" font-size="26">求推荐好用的流量卡 🙋</text>
    
    <!-- Comment input area -->
    <rect x="140" y="1050" width="800" height="100" rx="20" fill="white" stroke="#E0E0E0" stroke-width="2"/>
    <text x="220" y="1115" fill="#CCC" font-size="28">来说两句...</text>
    <rect x="780" y="1070" width="120" height="60" rx="30" fill="#E91E63"/>
    <text x="840" y="1110" text-anchor="middle" fill="white" font-size="26">发布</text>
    
    <!-- Collection button -->
    <rect x="340" y="1260" width="400" height="80" rx="40" fill="#E91E63"/>
    <text x="540" y="1315" text-anchor="middle" fill="white" font-size="32">📌 收藏备用</text>
    
    <text x="540" y="1420" text-anchor="middle" fill="#999" font-size="22">👍 点赞 💬 评论 🔄 转发</text>
  `);
  await sharp(s).png().toFile(`${OUT}/img6.png`);
  console.log('✅ 图6 img6.png');
}

// Run all
async function main() {
  // Ensure output dir exists
  const fs2 = require('fs');
  if (!fs2.existsSync(OUT)) fs2.mkdirSync(OUT, { recursive: true });
  
  await genCover();
  await genImg2();
  await genImg3();
  await genImg4();
  await genImg5();
  await genImg6();
  console.log('\n🎉 全部6张图生成完毕！');
}

main().catch(e => console.error('Error:', e.message, e.stack));
