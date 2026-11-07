/* Public counts are rendered by Jekyll; API credentials stay in GitHub Secrets. */
(() => {
  'use strict';
  const config = document.currentScript;
  const trackingId = config?.dataset.baiduTrackingId || '';
  const siteOrigin = config?.dataset.siteOrigin || '';
  let lastPath;

  function updateCounts(now = new Date()) {
    const dateParts = new Intl.DateTimeFormat('en-CA', {
      timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit',
    }).formatToParts(now);
    const part = (type) => dateParts.find((item) => item.type === type).value;
    const today = `${part('year')}-${part('month')}-${part('day')}`;
    document.querySelectorAll('[data-stats-date]').forEach((stats) => {
      if (stats.dataset.statsDate !== today) {
        stats.querySelectorAll('[data-stat-today]').forEach((value) => {
          value.textContent = '—';
          value.title = '今日统计尚未更新';
        });
      }
    });
    document.querySelectorAll('[data-stat-number]').forEach((value) => {
      const raw = value.textContent.trim();
      if (/^\d+$/.test(raw)) value.textContent = Number(raw).toLocaleString('zh-CN');
    });
  }

  const canTrack = /^[a-f0-9]{32}$/i.test(trackingId)
    && siteOrigin && window.location.origin === siteOrigin;
  if (canTrack) {
    window._hmt = window._hmt || [];
    window._hmt.push(['_setAutoPageview', false]);
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://hm.baidu.com/hm.js?${trackingId}`;
    document.head.appendChild(script);
  }

  function onPageLoad() {
    updateCounts();
    const path = window.location.pathname;
    // Hydejack emits an initial load event too; fragments are not new articles.
    if (canTrack && path !== lastPath) {
      window._hmt.push(['_trackPageview', path]);
      lastPath = path;
    }
  }

  document.getElementById('_pushState')?.addEventListener('hy-push-state-load', onPageLoad);
  window.addEventListener('pageshow', () => updateCounts());
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) updateCounts();
  });
  // Open tabs should stop calling yesterday's snapshot "today" after midnight.
  window.setInterval(updateCounts, 60_000);
  onPageLoad();
})();
