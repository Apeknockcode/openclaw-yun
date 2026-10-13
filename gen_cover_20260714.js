const sharp = require('sharp');
const path = require('path');

const W = 1200;
const H = 675;
const OUTPUT = path.join(__dirname, 'juejin_cover_20260714.png');

async function main() {
  const TITLE = '佣金计算引擎实战';
  const SUBTITLE = '多级分佣 · 阶梯返利 · 结算设计';
  const TAG_TEXT = '后端 · 系统设计';

  const svg = `
    <svg width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#0a1628"/>
          <stop offset="50%" stop-color="#0f2440"/>
          <stop offset="100%" stop-color="#1a365d"/>
        </linearGradient>
        <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#3b82f6"/>
          <stop offset="100%" stop-color="#06b6d4"/>
        </linearGradient>
        <filter id="glow">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>
      <!-- 背景 -->
      <rect width="${W}" height="${H}" fill="url(#bg)"/>
      <!-- 网格线 -->
      <g stroke="#1e3a5f" stroke-width="0.5" opacity="0.4">
        ${Array.from({length: 13}, (_, i) => `<line x1="${i*100}" y1="0" x2="${i*100}" y2="${H}"/>`).join('')}
        ${Array.from({length: 8}, (_, i) => `<line x1="0" y1="${i*100}" x2="${W}" y2="${i*100}"/>`).join('')}
      </g>
      <!-- 连接点装饰 -->
      <g fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.3">
        <circle cx="200" cy="150" r="4"/><circle cx="350" cy="200" r="3"/>
        <circle cx="500" cy="120" r="5"/><circle cx="650" cy="250" r="3"/>
        <circle cx="800" cy="160" r="4"/><circle cx="950" cy="220" r="3"/>
        <line x1="200" y1="150" x2="350" y2="200"/><line x1="350" y1="200" x2="500" y2="120"/>
        <line x1="500" y1="120" x2="650" y2="250"/><line x1="650" y1="250" x2="800" y2="160"/>
        <line x1="800" y1="160" x2="950" y2="220"/>
      </g>
      <!-- 装饰圆环 -->
      <circle cx="1000" cy="100" r="120" fill="none" stroke="#3b82f6" stroke-width="0.5" opacity="0.15"/>
      <circle cx="200" cy="550" r="100" fill="none" stroke="#06b6d4" stroke-width="0.5" opacity="0.12"/>
      <!-- 底部强调线 -->
      <rect x="0" y="${H-4}" width="${W}" height="4" fill="url(#accent)" opacity="0.8"/>
      <rect x="0" y="0" width="6" height="${H}" fill="url(#accent)" opacity="0.6"/>
      <!-- 主标题 -->
      <text x="600" y="290" text-anchor="middle"
        font-family="'PingFang SC','Microsoft YaHei','Noto Sans SC',sans-serif"
        font-size="64" font-weight="bold" fill="#ffffff" filter="url(#glow)">
        ${TITLE}
      </text>
      <!-- 副标题 -->
      <text x="600" y="355" text-anchor="middle"
        font-family="'PingFang SC','Microsoft YaHei','Noto Sans SC',sans-serif"
        font-size="28" fill="#94a3b8" letter-spacing="4">
        ${SUBTITLE}
      </text>
      <!-- 标签 -->
      <rect x="470" y="400" width="260" height="36" rx="18"
        fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1" stroke-opacity="0.4"/>
      <text x="600" y="425" text-anchor="middle"
        font-family="'PingFang SC','Microsoft YaHei','Noto Sans SC',sans-serif"
        font-size="16" fill="#93c5fd">
        ${TAG_TEXT}
      </text>
    </svg>
  `;
  const buf = Buffer.from(svg);
  await sharp(buf).png().toFile(OUTPUT);
  console.log(`Cover generated: ${OUTPUT}`);
}
main().catch(err => { console.error('Failed:', err.message); process.exit(1); });
