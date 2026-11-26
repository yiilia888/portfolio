// Render bìa dự án Vinamilk (tools/cover-vinamilk.html) thành ảnh PNG 1600x900.
// Chạy từ thư mục gốc repo: node tools/render_cover.js
// Sau đó nén thành images/projects/vinamilk.jpg (rộng 1200px, chất lượng ~86).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(__dirname, 'cover-vinamilk.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  await p.screenshot({ path: path.resolve(__dirname, '..', 'images', 'projects', 'vinamilk.png') });
  await b.close();
  console.log('Đã render images/projects/vinamilk.png');
})();
