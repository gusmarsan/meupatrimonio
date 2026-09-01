const CACHE_NAME = 'meu-patrimonio-pwa-v7';
const CORE_ASSETS = [
  './',
  './index.html',
  './install.html',
  './manifest.webmanifest',
  './icon.svg?v=3'
];

const CONTRIBUTION_STYLE = `
<style id="contribution-placement-fix-v7">
@media (min-width: 761px) {
  #home .home-dashboard {
    grid-template-areas:
      "balance metrics"
      "contribution contribution"
      "allocation contributors"
      "positions positions"
      "history history";
  }
  #home .mobile-contribution-slot {
    grid-area: contribution;
    display: block;
    padding: 28px 0 34px;
    border-bottom: 1px solid var(--home-rule, rgba(23,32,27,.12));
  }
  #home .mobile-contribution-slot .contribution-wrap {
    max-width: none;
    margin: 0;
    padding: 0;
    border: 0;
  }
  #home .mobile-contribution-slot .contribution-toggle {
    min-height: 44px;
    padding: 0 16px;
    border: 1px solid #17201b2b;
    border-radius: 9px;
    background: #fff;
    color: #365d4b;
    font-size: .78rem;
    font-weight: 700;
    cursor: pointer;
  }
  #home .mobile-contribution-slot .contribution-panel {
    width: 100%;
    max-width: 980px;
    margin-top: 10px;
  }
}
@media (max-width: 1100px) and (min-width: 761px) {
  #home .home-dashboard {
    grid-template-areas:
      "balance"
      "metrics"
      "contribution"
      "allocation"
      "contributors"
      "positions"
      "history";
  }
}
@media (max-width: 760px) {
  body.contribution-open {
    overflow: hidden !important;
    overscroll-behavior: none;
  }
  body.contribution-open::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 2147483000;
    background: rgba(11,20,16,.48);
  }
  body.contribution-open nav {
    visibility: hidden;
    pointer-events: none;
  }
  body.contribution-open > #contributionPanel:not(.hidden) {
    position: fixed !important;
    z-index: 2147483001 !important;
    top: calc(12px + env(safe-area-inset-top, 0px)) !important;
    right: 12px !important;
    bottom: calc(12px + env(safe-area-inset-bottom, 0px)) !important;
    left: 12px !important;
    width: auto !important;
    max-width: none !important;
    max-height: none !important;
    margin: 0 !important;
    padding: 18px 16px calc(22px + env(safe-area-inset-bottom, 0px)) !important;
    overflow-x: hidden !important;
    overflow-y: auto !important;
    overscroll-behavior: contain;
    -webkit-overflow-scrolling: touch;
    border-radius: 18px;
    background: #fff !important;
    box-shadow: 0 24px 70px rgba(16,29,22,.24);
  }
  body.contribution-open > #contributionPanel .contribution-head {
    position: sticky;
    top: -18px;
    z-index: 2;
    margin: -18px -16px 14px;
    padding: 18px 16px 12px;
    background: #fff;
    border-bottom: 1px solid rgba(23,32,27,.08);
  }
  body.contribution-open > #contributionPanel .contribution-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  body.contribution-open > #contributionPanel .field {
    min-width: 0;
  }
  body.contribution-open > #contributionPanel input,
  body.contribution-open > #contributionPanel select {
    min-height: 50px;
    font-size: 16px;
  }
  body.contribution-open > #contributionPanel .contribution-save {
    width: 100%;
    min-height: 50px;
    margin-top: 2px;
    font-size: .88rem;
  }
  body.contribution-open > #contributionPanel .contribution-note {
    margin-top: 14px;
  }
}
</style>`;

function enhanceAppHtml(html) {
  if (!html.includes('mobile-contribution-slot')) return html;

  let updated = html.replace(
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,interactive-widget=resizes-content">'
  );

  updated = updated.replace(
    'homeContent.after(contributionWrap)',
    'mobileContributionSlot.append(contributionWrap)'
  );

  updated = updated.replace(
    "placeUserControl();addEventListener('resize',placeUserControl);",
    "placeUserControl();const layoutMedia=matchMedia('(max-width:760px)');if(layoutMedia.addEventListener)layoutMedia.addEventListener('change',placeUserControl);else if(layoutMedia.addListener)layoutMedia.addListener(placeUserControl);"
  );

  updated = updated.replace(
    'function setContributionPanel(open){el.contributionPanel.classList.toggle("hidden",!open);if(open){renderContributionControls();setTimeout(()=>el.contributionValue.focus(),30)}}',
    'function setContributionPanel(open){const mobile=matchMedia("(max-width:760px)").matches;if(open&&mobile&&el.contributionPanel.parentElement!==document.body)document.body.append(el.contributionPanel);if(!open&&el.contributionPanel.parentElement!==el.contributionWrap)el.contributionWrap.append(el.contributionPanel);el.contributionPanel.classList.toggle("hidden",!open);document.body.classList.toggle("contribution-open",open&&mobile);if(open){renderContributionControls();if(!mobile)setTimeout(()=>el.contributionValue.focus(),30)}}'
  );

  if (!updated.includes('id="contribution-placement-fix-v7"')) {
    updated = updated.replace('</head>', `${CONTRIBUTION_STYLE}\n</head>`);
  }

  return updated;
}

function htmlResponse(response, html) {
  const headers = new Headers(response.headers);
  headers.delete('content-length');
  headers.delete('content-encoding');
  headers.set('content-type', 'text/html; charset=utf-8');
  return new Response(html, {
    status: response.status,
    statusText: response.statusText,
    headers
  });
}

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(CORE_ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
    ))
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  if (event.request.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const response = await fetch(event.request, { cache: 'no-store' });
        const contentType = response.headers.get('content-type') || '';
        if (!contentType.includes('text/html')) return response;

        const html = enhanceAppHtml(await response.text());
        const transformed = htmlResponse(response, html);
        const cache = await caches.open(CACHE_NAME);
        cache.put(event.request, transformed.clone());
        return transformed;
      } catch (error) {
        const cached = await caches.match(event.request) || await caches.match('./index.html');
        if (!cached) throw error;
        const contentType = cached.headers.get('content-type') || '';
        if (!contentType.includes('text/html')) return cached;
        return htmlResponse(cached, enhanceAppHtml(await cached.text()));
      }
    })());
    return;
  }

  event.respondWith(
    caches.match(event.request).then(cached => cached || fetch(event.request).then(response => {
      const copy = response.clone();
      caches.open(CACHE_NAME).then(cache => cache.put(event.request, copy));
      return response;
    }))
  );
});
