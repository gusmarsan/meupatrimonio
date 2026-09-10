const CACHE_NAME = 'meu-patrimonio-pwa-v8';
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

const LETRAO_STYLE = `
<style id="letrao-mode-v8">
.letrao-toggle{display:none}
@media (min-width:761px){
  .letrao-toggle{display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:0 14px;border:1px solid rgba(23,32,27,.16);border-radius:10px;background:rgba(255,255,255,.72);color:#344139;font-size:.78rem;font-weight:700;cursor:pointer;white-space:nowrap}
  .letrao-toggle:hover{border-color:rgba(23,32,27,.34);background:#fff}
  .letrao-toggle[aria-pressed="true"]{border-color:#137a5266;background:#137a5212;color:#116743}
  body.letrao-mode{--mut:#46514b}
  body.letrao-mode .eyebrow{font-size:.82rem;color:#46514b}
  body.letrao-mode .label{font-size:.92rem;color:#46514b}
  body.letrao-mode .delta{font-size:.96rem}
  body.letrao-mode .small{font-size:.88rem;color:#46514b}
  body.letrao-mode label{font-size:.86rem;color:#46514b}
  body.letrao-mode .note{font-size:.84rem;color:#46514b}
  body.letrao-mode .cat b{font-size:1rem}
  body.letrao-mode .cat .tap{font-size:.8rem;color:#4b5851}
  body.letrao-mode .cat .s{font-size:.82rem;color:#4b5851}
  body.letrao-mode .meta{font-size:.84rem;color:#4b5851}
  body.letrao-mode .mini{font-size:.8rem;color:#4b5851}
  body.letrao-mode .nav small{font-size:.82rem}
  body.letrao-mode #home .home-balance .label{font-size:.84rem;color:#344239}
  body.letrao-mode #home .home-updated{font-size:.82rem;color:#46514b}
  body.letrao-mode #home .home-return-badge{font-size:.82rem}
  body.letrao-mode #home .metric-block>span{font-size:.82rem;color:#3f4c44}
  body.letrao-mode #home .metric-block small{font-size:.8rem;color:#536057}
  body.letrao-mode #home .section-heading .small{font-size:.84rem;color:#4a574f}
  body.letrao-mode .projection-current span{font-size:.86rem;color:#46514b}
  body.letrao-mode .projection-case h3{font-size:.88rem}
  body.letrao-mode .projection-rate{font-size:.8rem;color:#4b5851}
  body.letrao-mode .projection-case small{font-size:.78rem;color:#4b5851}
  body.letrao-mode .projection-date{font-size:1rem}
  body.letrao-mode .projection-previous{font-size:.78rem;color:#4b5851}
  body.letrao-mode .projection-previous b{font-size:.84rem}
  body.letrao-mode .projection-note{font-size:.82rem;color:#4b5851}
  body.letrao-mode .wealth-card .wealth-label{font-size:.84rem;color:#46514b}
  body.letrao-mode .wealth-detail{font-size:.8rem;color:#4b5851}
  body.letrao-mode .wealth-cta{font-size:.8rem}
  body.letrao-mode .wealth-check{font-size:.8rem;color:#46514b}
  body.letrao-mode .wealth-warning{font-size:.8rem}
  body.letrao-mode .settings-copy{font-size:.92rem;color:#46514b}
  body.letrao-mode .settings-note,
  body.letrao-mode .csv-status,
  body.letrao-mode .backup-status,
  body.letrao-mode .cdb-help{font-size:.82rem;color:#4b5851}
  body.letrao-mode .backup-stat span{font-size:.8rem;color:#4b5851}
  body.letrao-mode .milestone-meta{font-size:.84rem;color:#4b5851}
  body.letrao-mode .milestone-date{font-size:.9rem;color:#344039}
  body.letrao-mode .retirement-simulation-index{font-size:.76rem;color:#46514b}
  body.letrao-mode .retirement-simulation-capital-main>span,
  body.letrao-mode .retirement-simulation-years>span:first-child{font-size:.92rem;color:#46514b}
  body.letrao-mode .retirement-simulation-auto{font-size:.84rem;color:#36453d}
  body.letrao-mode .retirement-simulation-years-field>span{font-size:.86rem}
  body.letrao-mode .retirement-simulation-growth{font-size:.82rem;color:#4b5851}
  body.letrao-mode .retirement-simulation-result-label{font-size:.82rem;color:#4b5851}
  body.letrao-mode .retirement-simulation-income{font-size:.8rem;color:#4b5851}
  body.letrao-mode .retirement-simulation-boost-toggle{font-size:.86rem}
  body.letrao-mode .retirement-simulation-boost-field label{font-size:.8rem;color:#46514b}
  body.letrao-mode .contribution-note,
  body.letrao-mode .contribution-row span,
  body.letrao-mode .contribution-row b,
  body.letrao-mode .aporte-mini,
  body.letrao-mode .history-aporte,
  body.letrao-mode .sync-status{font-size:.82rem;color:#4b5851}
  body.letrao-mode .chart-header span,
  body.letrao-mode .chart-legend{font-size:.82rem;color:#4b5851}
}
</style>`;

const LETRAO_SCRIPT = `
<script id="letrao-script-v8">
(()=>{
  const key='patrimonio-letrao-mode';
  const button=document.getElementById('letraoToggle');
  if(!button)return;
  const apply=enabled=>{
    document.body.classList.toggle('letrao-mode',enabled);
    button.setAttribute('aria-pressed',String(enabled));
    button.title=enabled?'Voltar ao tamanho normal':'Aumentar textos pequenos';
  };
  let stored=false;
  try{stored=localStorage.getItem(key)==='true'}catch{}
  apply(stored);
  button.addEventListener('click',()=>{
    const enabled=!document.body.classList.contains('letrao-mode');
    apply(enabled);
    try{localStorage.setItem(key,String(enabled))}catch{}
  });
})();
</script>`;

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

  if (!updated.includes('id="letraoToggle"')) {
    updated = updated.replace(
      '<div class="topbar-actions"><button id="privacyToggle"',
      '<div class="topbar-actions"><button id="letraoToggle" class="letrao-toggle" type="button" aria-pressed="false">Módulo letrão</button><button id="privacyToggle"'
    );
  }

  if (!updated.includes('id="letrao-mode-v8"')) {
    updated = updated.replace('</head>', `${LETRAO_STYLE}\n</head>`);
  }

  if (!updated.includes('id="letrao-script-v8"')) {
    updated = updated.replace('</body>', `${LETRAO_SCRIPT}\n</body>`);
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
