const CACHE_NAME = 'meu-patrimonio-pwa-v4';
const CORE_ASSETS = [
  './',
  './index.html',
  './install.html',
  './manifest.webmanifest',
  './icon.svg?v=3'
];

const CONTRIBUTION_STYLE = `
<style id="contribution-placement-fix">
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
</style>`;

function enhanceAppHtml(html) {
  if (!html.includes('mobile-contribution-slot')) return html;

  let updated = html.replace(
    'homeContent.after(contributionWrap)',
    'mobileContributionSlot.append(contributionWrap)'
  );

  if (!updated.includes('id="contribution-placement-fix"')) {
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
