const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { test } = require('node:test');
const vm = require('node:vm');
const source = readFileSync('assets/js/site-analytics.js', 'utf8');

function run(origin = 'https://www.lidaxiang.cn', snapshotDate = '2026-11-07') {
  const pageListeners = {};
  const browserListeners = {};
  const documentListeners = {};
  const numbers = [{ textContent: '1000' }, { textContent: '30' }, { textContent: '7' }];
  const stats = { dataset: { statsDate: snapshotDate }, querySelectorAll: () => numbers.slice(1) };
  const scripts = [];
  let tick;
  const window = {
    location: { origin, pathname: '/' },
    addEventListener: (type, callback) => { browserListeners[type] = callback; },
    setInterval: (callback) => { tick = callback; },
  };
  const document = {
    currentScript: { dataset: { baiduTrackingId: 'a'.repeat(32), siteOrigin: 'https://www.lidaxiang.cn' } },
    head: { appendChild: (node) => scripts.push(node) },
    createElement: () => ({}),
    getElementById: () => ({ addEventListener: (type, callback) => { pageListeners[type] = callback; } }),
    querySelectorAll: (selector) => selector === '[data-stats-date]' ? [stats] : numbers,
    addEventListener: (type, callback) => { documentListeners[type] = callback; },
  };
  let instant = '2026-11-07T03:00:00Z';
  class Clock extends Date { constructor(...args) { super(...(args.length ? args : [instant])); } }
  vm.runInNewContext(source, { document, window, Date: Clock, Intl });
  return { window, document, scripts, numbers, pageListeners, browserListeners, documentListeners,
    advance: (value) => { instant = value; tick(); } };
}

test('one initial PV, one PV per article navigation, none for duplicate load or fragment', () => {
  const env = run();
  assert.equal(env.scripts.length, 1);
  const pv = () => env.window._hmt.filter((item) => item[0] === '_trackPageview').map((item) => item[1]);
  const load = env.pageListeners['hy-push-state-load'];
  load();
  assert.deepEqual(Array.from(pv()), ['/']);
  env.window.location.pathname = '/ai/article'; load(); load();
  env.window.location.hash = '#heading'; load();
  env.window.location.pathname = '/'; load();
  assert.deepEqual(Array.from(pv()), ['/', '/ai/article', '/']);
  assert.equal(env.window._hmt[0][0], '_setAutoPageview');
  assert.equal(env.window._hmt[0][1], false);
});

test('local previews render counts without sending production PV', () => {
  const env = run('http://127.0.0.1:4000');
  assert.equal(env.scripts.length, 0);
  assert.equal(env.window._hmt, undefined);
  assert.equal(env.numbers[0].textContent, '1,000');
});

test('Shanghai midnight clears only daily counts while the tab stays open', () => {
  const env = run();
  env.advance('2026-11-07T16:00:01Z');
  assert.deepEqual(env.numbers.map((item) => item.textContent), ['1,000', '—', '—']);
  assert.equal(env.numbers[1].title, '今日统计尚未更新');
});

test('stale HTML never calls yesterday counts today on page load', () => {
  const env = run('https://www.lidaxiang.cn', '2026-11-06');
  assert.deepEqual(env.numbers.map((item) => item.textContent), ['1,000', '—', '—']);
  env.browserListeners.pageshow();
  env.documentListeners.visibilitychange();
});
