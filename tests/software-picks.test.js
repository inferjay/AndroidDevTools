const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const root = path.resolve(__dirname, '..');
const read = (file) => fs.readFileSync(path.join(root, file), 'utf8');
const { BATCH_SIZE, formatPrice, filterProducts, validateCatalog } = require('../static/js/software-picks.js');
const catalog = JSON.parse(read('static/data/software-picks.json'));

test('catalog contains the complete current promotion snapshot without duplicate products', () => {
  assert.equal(validateCatalog(catalog), true);
  assert.equal(catalog.total, 365);
  assert.equal(catalog.products.length, catalog.total);
  assert.equal(new Set(catalog.products.map((product) => product.id)).size, catalog.total);
  assert.equal(catalog.source, 'https://union.lizhi.shop/dashboard/promotion/products');
  assert.match(catalog.updatedAt, /^\d{4}-\d{2}-\d{2}$/);
  for (const product of catalog.products) {
    assert.ok(product.name && product.fullName && product.description, product.id);
    assert.ok(Number.isInteger(product.price) && product.price >= 0, product.id);
    const link = new URL(product.url);
    assert.equal(link.origin, 'https://lizhi.shop');
    assert.ok(link.pathname.startsWith('/products/') || link.pathname.startsWith('/site/products/id/'), product.id);
    assert.deepEqual(link.searchParams.getAll('cid'), ['rmzbxelm'], product.id);
    assert.ok(product.icon.startsWith('https://shop-cdn.lizhi.shop/'), product.id);
    if (product.promotionImage) {
      assert.ok(product.promotionImage.startsWith('https://union.lizhi.shop/uploads/images/'), product.id);
    }
    assert.ok(Array.isArray(product.platforms), product.id);
  }
  assert.equal(catalog.products.filter((product) => product.promotionImage).length, 62);
  assert.equal(catalog.products.filter((product) => !product.promotionImage).length, 303);
});

test('search and platform filters work together across the whole catalog', () => {
  assert.equal(filterProducts(catalog.products, '', 'all').length, catalog.total);
  const target = catalog.products.find((product) => product.id === 'typora');
  assert.ok(target);
  assert.ok(filterProducts(catalog.products, 'TYPORA', 'all').includes(target));
  assert.ok(filterProducts(catalog.products, '  typora  ', 'all').includes(target));
  assert.ok(filterProducts(catalog.products, 'typora', 'Windows').includes(target));
  assert.equal(filterProducts(catalog.products, '软件不存在-xyz987', 'all').length, 0);
  const macProducts = filterProducts(catalog.products, '', 'macOS');
  assert.ok(macProducts.length > BATCH_SIZE);
  assert.ok(macProducts.every((product) => product.platforms.includes('macOS')));
  const last = catalog.products.at(-1);
  assert.ok(filterProducts(catalog.products, last.name, 'all').includes(last));
});

test('recommended software can be filtered together with platform and search', () => {
  const recommended = filterProducts(catalog.products, '', 'all', true);
  assert.equal(recommended.length, 17);
  assert.ok(recommended.every((product) => product.isRecommended));
  const typora = catalog.products.find((product) => product.id === 'typora');
  assert.ok(recommended.includes(typora));
  assert.deepEqual(filterProducts(catalog.products, 'typora', 'Windows', true), [typora]);
  assert.equal(filterProducts(catalog.products, 'downie', 'Windows', true).length, 0);
  assert.equal(filterProducts(catalog.products, 'fences', 'Windows', true).length, 0);
  assert.equal(filterProducts(catalog.products, '', 'all', false).length, catalog.total);
});

test('prices are rendered from integer cents without rounding fractional yuan', () => {
  assert.equal(formatPrice(4900), '49');
  assert.equal(formatPrice(1299), '12.99');
  assert.equal(formatPrice(0), '0');
});

test('all site navigation menus include the new standalone page', () => {
  const pages = ['index.html', 'android-studio.html', 'android-emulator.html',
    'android-emulator-install-guide.html', 'welfare-pi.html', 'friends.html',
    'donate.html', '404.html', 'software-picks.html'];
  for (const page of pages) {
    const header = read(page).match(/<header[\s\S]*?<\/header>/)[0];
    assert.match(header, /href="software-picks\.html"[^>]*>✨ 精选软件/, page);
  }
});

test('welfare courses and books remain intact while software becomes a page link', () => {
  const html = read('welfare-pi.html');
  assert.equal((html.match(/href="software-picks\.html">精选软件<\/a>/g) || []).length, 2);
  assert.doesNotMatch(html, /var softwares\s*=|data-type="2"|item\.type == 2|loadGoodsList\(type, softwares\)/);
  assert.match(html, /\.goods-type-navbar \.nav-item a\[data-type\]/);
  const dataScript = html.match(/<script>\s*Date\.prototype\.Format[\s\S]*?<\/script>/)[0];
  const context = {};
  vm.runInNewContext(dataScript.replace(/^<script>|<\/script>$/g, ''), context);
  assert.equal(context.courses.length, 39);
  assert.equal(context.books.length, 63);
  assert.equal(context.discounts.length, 6);
});

test('the extracted welfare inline scripts remain valid JavaScript', () => {
  const html = read('welfare-pi.html');
  for (const match of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)) {
    if (/src=|text\/x-jquery-tmpl/.test(match[1]) || !match[2].trim()) continue;
    assert.doesNotThrow(() => new vm.Script(match[2]));
  }
});
