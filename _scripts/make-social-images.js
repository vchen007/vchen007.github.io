// Renders the 1200x630 link-preview images in images/og/ from each project's
// front matter (title, kicker, excerpt, teaser, og_image) plus a site card.
// Usage, from the repo root:  node _scripts/make-social-images.js
// Needs Playwright with Chromium (npm i -D playwright && npx playwright install chromium).
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const esc = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function frontMatter(file) {
  const m = fs.readFileSync(file, 'utf8').match(/^---\n([\s\S]*?)\n---/);
  const out = {};
  if (!m) return out;
  for (const line of m[1].split('\n')) {
    const kv = line.match(/^([a-z_]+):\s*(.*)$/); // top-level scalar keys only
    if (kv && kv[2] !== '') out[kv[1]] = kv[2].replace(/^"(.*)"$/, '$1').replace(/^'(.*)'$/, '$1');
  }
  return out;
}

function imageUrl(name) {
  if (!name || name.includes('://')) return null; // remote teasers (Tableau) are skipped
  const file = path.join(ROOT, 'images', name);
  return fs.existsSync(file) ? 'file://' + file : null;
}

function card({ kicker, title, excerpt, image, avatar }) {
  const media = image ? `<div class="media"><img src="${image}"></div>` : '';
  const face = avatar ? `<img class="avatar" src="${avatar}">` : '';
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{box-sizing:border-box} body{margin:0;width:1200px;height:630px;font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:#fff;color:#14181c}
  .wrap{position:absolute;inset:0;display:flex;gap:44px;padding:56px 60px 92px;border-top:12px solid #0b6f8c}
  .text{flex:1;display:flex;flex-direction:column;justify-content:center;min-width:0}
  .kicker{color:#0b6f8c;font-size:24px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin:0 0 14px}
  h1{font-size:${image ? 50 : 60}px;line-height:1.12;margin:0 0 20px}
  p{color:#4a535b;font-size:26px;line-height:1.4;margin:0;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
  .media{width:470px;flex:none;display:flex;align-items:center}
  .media img{width:100%;max-height:440px;object-fit:contain;border:1px solid #e3e7eb;border-radius:14px;background:#fff;padding:10px}
  .avatar{width:300px;height:326px;flex:none;align-self:center;object-fit:contain}
  .foot{position:absolute;left:60px;right:60px;bottom:30px;display:flex;align-items:center;gap:14px;color:#5b646c;font-size:23px}
  .mono{width:40px;height:40px} .foot b{color:#14181c}
  </style></head><body><div class="wrap"><div class="text">
  <p class="kicker">${esc(kicker)}</p><h1>${esc(title)}</h1><p>${esc(excerpt)}</p></div>${media}${face}</div>
  <div class="foot"><img class="mono" src="file://${path.join(ROOT, 'images/favicon.svg')}"><b>Victor Chen</b> · vchen007.github.io</div>
  </body></html>`;
}

(async () => {
  const jobs = [{
    out: 'og/site.png',
    html: card({ kicker: 'Sports & business analytics', title: 'Victor Chen',
      excerpt: 'Dashboards, data pipelines and models with SQL, Python, R and Tableau. MS Business Analytics, UW–Madison.',
      avatar: imageUrl('victor-chen.webp') }),
  }];
  for (const f of fs.readdirSync(path.join(ROOT, '_portfolio')).sort()) {
    const fm = frontMatter(path.join(ROOT, '_portfolio', f));
    if (!fm.og_image) continue;
    jobs.push({ out: fm.og_image, html: card({ kicker: fm.kicker || 'Project', title: fm.title, excerpt: fm.excerpt, image: imageUrl(fm.teaser) }) });
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  for (const job of jobs) {
    const out = path.join(ROOT, 'images', job.out);
    fs.mkdirSync(path.dirname(out), { recursive: true });
    const tmp = path.join(require('os').tmpdir(), 'og-card.html');
    fs.writeFileSync(tmp, job.html);
    await page.goto('file://' + tmp);
    await page.waitForTimeout(150);
    await page.screenshot({ path: out });
    console.log('wrote images/' + job.out);
  }
  await browser.close();
})();
