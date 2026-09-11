const CACHE_NAME = 'meu-patrimonio-pwa-v21';
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
<style id="letrao-mode-v10">
.letrao-toggle{display:none}
@media (min-width:761px){
  .letrao-toggle{display:inline-flex;align-items:center;justify-content:center;gap:7px;min-height:42px;padding:0 14px;border:1px solid rgba(23,32,27,.16);border-radius:10px;background:rgba(255,255,255,.72);color:#344139;font-size:.78rem;font-weight:700;cursor:pointer;white-space:nowrap}
  .letrao-toggle svg{width:18px;height:18px;flex:0 0 18px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}.letrao-toggle span{display:inline-block}.letrao-toggle:hover{border-color:rgba(23,32,27,.34);background:#fff}
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

const LETRAO_SIMPLE_STYLE = `
<style id="letrao-simple-v1">
@media (min-width:761px){
  body.letrao-mode .privacy-toggle,
  body.letrao-mode nav .user-control,
  body.letrao-mode .nav[data-view="settings"],
  body.letrao-mode #home #graphBtn,
  body.letrao-mode #new #uploadLabel,
  body.letrao-mode #new .note,
  body.letrao-mode #review #more,
  body.letrao-mode #projections .projection-current,
  body.letrao-mode #projections .projection-target:has(+ .wealth-split),
  body.letrao-mode #projections .wealth-split,
  body.letrao-mode #projections .wealth-check,
  body.letrao-mode #projections .wealth-warning,
  body.letrao-mode #projections .retirement-simulation,
  body.letrao-mode #retirementSimulationCapitalSheet,
  body.letrao-mode #retirementSheet,
  body.letrao-mode #evolution .rowact,
  body.letrao-mode #review details,
  body.letrao-mode #review pre{display:none!important}

  body.letrao-mode .app{padding-left:250px}
  body.letrao-mode header{min-height:76px}
  body.letrao-mode header h1{font-size:1.75rem;font-weight:650}
  body.letrao-mode header .eyebrow{font-size:.88rem;color:#38463e}
  body.letrao-mode .letrao-toggle{min-height:48px;padding:0 17px;font-size:.9rem;border-width:2px}
  body.letrao-mode .letrao-toggle svg{width:20px;height:20px;flex-basis:20px}
  body.letrao-mode #newTop{width:auto;min-width:0;height:48px;padding:0 17px;border-radius:10px;font-size:0;font-weight:700}
  body.letrao-mode #newTop::after{content:"+  Novo mês";font-size:.96rem;white-space:nowrap}

  body.letrao-mode nav .nav{min-height:58px;margin-bottom:8px;padding:10px 12px}
  body.letrao-mode nav .nav small{font-size:.96rem;font-weight:650}
  body.letrao-mode nav .nav span svg{width:22px;height:22px}
  body.letrao-mode nav::before,
  body.letrao-mode nav .nav,
  body.letrao-mode nav .nav:hover,
  body.letrao-mode nav .nav.active,
  body.letrao-mode nav .nav small,
  body.letrao-mode nav .nav span,
  body.letrao-mode nav .nav svg{color:#f6d65b!important}

  body.letrao-mode #home .allocation-overview{grid-template-columns:380px minmax(0,1fr);gap:52px}
  body.letrao-mode #home .allocation-chart{width:360px}
  body.letrao-mode #home .allocation-chart::before{width:232px}
  body.letrao-mode #home .allocation-legend{gap:20px}
  body.letrao-mode #home .allocation-legend-item{grid-template-columns:14px minmax(0,1fr) auto;gap:14px;font-size:1.52rem;line-height:1.25}
  body.letrao-mode #home .allocation-legend-item i{width:14px;height:14px}
  body.letrao-mode #home .allocation-legend-item b{font-size:1.44rem}

  body.letrao-mode #home .home-dashboard{max-width:1120px;margin:0 auto;grid-template-columns:1fr;grid-template-areas:"balance" "metrics" "contribution" "allocation" "contributors" "positions" "history"}
  body.letrao-mode #home .home-balance{min-height:auto;padding:54px 0 44px}
  body.letrao-mode #home .home-updated{display:none!important}
  body.letrao-mode #home .home-balance .actions{align-items:center;flex-wrap:wrap}
  body.letrao-mode #home .home-balance .actions .contribution-toggle{display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:0 20px;border:1px solid #17201b2b;border-radius:14px;background:#fff;color:#365d4b;font-size:.8rem;font-weight:700;cursor:pointer}
  body.letrao-mode #home .total{font-size:clamp(4.3rem,6vw,5.8rem);line-height:.92}
  body.letrao-mode #home .home-performance-line{margin-top:26px}
  body.letrao-mode #home .delta{font-size:1.08rem;color:#33423a}
  body.letrao-mode #home .home-return-badge{font-size:.94rem;min-height:36px;padding-inline:13px}
  body.letrao-mode #home .home-metrics{min-height:auto;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;padding:10px 0 38px}
  body.letrao-mode #home .metric-block{display:block;min-height:132px;padding:22px;border:1px solid #17201b20;border-radius:14px;background:#fff}
  body.letrao-mode #home .metric-block>span{display:block;margin:0 0 13px;font-size:.92rem;color:#35443c;letter-spacing:.04em}
  body.letrao-mode #home .metric-block strong{display:block;font-size:2rem;line-height:1.08;text-align:left}
  body.letrao-mode #home .metric-block small{display:block;margin-top:9px;font-size:.9rem;color:#4a5850}
  body.letrao-mode #home .mobile-contribution-slot{padding:0;border-bottom:0}
  body.letrao-mode #home .mobile-contribution-slot:has(#contributionPanel:not(.hidden)){padding:22px 0 34px;border-bottom:1px solid var(--home-rule,rgba(23,32,27,.12))}
  body.letrao-mode #home .portfolio-section{padding-top:46px}
  body.letrao-mode #home .section-heading h2{font-size:2.25rem}
  body.letrao-mode #home .portfolio-section .section-heading>.small{display:none}
  body.letrao-mode #home .catlist{grid-template-columns:1fr;column-gap:0}
  body.letrao-mode #home .cat{min-height:92px;padding:20px 4px;border-top:0;border-bottom:1px solid #17201b20}
  body.letrao-mode #home .cat b{font-size:1.12rem}
  body.letrao-mode #home .cat .tap{display:inline-flex;margin-top:12px;font-size:0;color:inherit}
  body.letrao-mode #home .cat .tap::after{content:"Atualizar valor";min-height:44px;display:inline-flex;align-items:center;justify-content:center;padding:0 17px;border:1px solid #17201b;border-radius:10px;background:#17201b;color:#fff;font-size:.94rem;font-weight:700;line-height:1;white-space:nowrap}
  body.letrao-mode #categorySheet #sheetPrint{display:none!important}
  body.letrao-mode #home .cat .v{font-size:1.28rem}
  body.letrao-mode #home .cat .s{font-size:.92rem;color:#44534b}
  body.letrao-mode #home .home-history-section{padding-top:52px}
  body.letrao-mode #home #homeHistoryButton{min-height:48px;padding-inline:16px;font-size:.9rem}

  body.letrao-mode #new{max-width:880px}
  body.letrao-mode #new .card{padding:30px}
  body.letrao-mode #new label{font-size:1rem;color:#35433b}
  body.letrao-mode #new input,
  body.letrao-mode #new select{min-height:58px;font-size:1.05rem}
  body.letrao-mode #new .upload{min-height:250px}
  body.letrao-mode #new .upload strong{font-size:1.35rem}
  body.letrao-mode #new .upload span span{font-size:1rem;line-height:1.55}
  body.letrao-mode #new .note{font-size:.94rem;line-height:1.55}
  body.letrao-mode #new .btn{min-height:56px;font-size:1rem}

  body.letrao-mode #review{max-width:980px}
  body.letrao-mode #review .review{grid-template-columns:1fr}
  body.letrao-mode #review .review-intro p{font-size:.98rem}
  body.letrao-mode #review .monthline span{font-size:.9rem}
  body.letrao-mode #review .monthline b{font-size:1.05rem}
  body.letrao-mode #review .fname{font-size:1rem}
  body.letrao-mode #review label{font-size:.92rem}
  body.letrao-mode #review input,
  body.letrao-mode #review select{min-height:54px;font-size:1rem}
  body.letrao-mode #review .month-summary-row,
  body.letrao-mode #review .month-summary-value b,
  body.letrao-mode #review .month-summary-value small,
  body.letrao-mode #review .count-note,
  body.letrao-mode #review .warn{font-size:.9rem}
  body.letrao-mode #review .btn{min-height:54px;font-size:.96rem}
  body.letrao-mode #review .summary{position:static;bottom:auto;z-index:auto;margin-top:24px;padding:0;border:0;background:transparent;backdrop-filter:none}
  body.letrao-mode #review .summary-details{padding:22px;border:1px solid #17201b20;border-radius:14px;background:#fff}
  body.letrao-mode #review .summary-bar{position:static;margin-top:12px;padding:0;border:0;background:transparent;box-shadow:none;backdrop-filter:none}
  body.letrao-mode #review .summary-bar .btn{width:100%;min-height:58px}

  body.letrao-mode #projections{max-width:900px}
  body.letrao-mode #projections .projection-target-row{margin-top:34px;padding:30px 32px;border:1px solid #17201b20;border-radius:14px;background:#fff;align-items:center}
  body.letrao-mode #projections .projection-target{margin:0;font-size:2rem;line-height:1.2}
  body.letrao-mode #projections .projection-target-edit{width:48px;height:48px;flex:0 0 48px}
  body.letrao-mode #projections .projection-target-edit svg{width:22px;height:22px}
  body.letrao-mode #projections .projection-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:22px}
  body.letrao-mode #projections .projection-case{padding:28px 22px;min-height:220px}
  body.letrao-mode #projections .projection-case h3{font-size:1.05rem;line-height:1.35}
  body.letrao-mode #projections .projection-rate{font-size:.9rem;margin-top:10px}
  body.letrao-mode #projections .projection-case small{font-size:.88rem}
  body.letrao-mode #projections .projection-date{font-size:1.55rem;margin-top:8px}
  body.letrao-mode #projections .projection-previous{font-size:.86rem;line-height:1.45}
  body.letrao-mode #projections .projection-previous b{font-size:.95rem}
  body.letrao-mode #projections .projection-note{font-size:.92rem;line-height:1.55;color:#435149}
  body.letrao-mode #evolution{max-width:1050px}
  body.letrao-mode #evolution>.head h2{font-size:2.55rem}
  body.letrao-mode #evolution .chart-header span,
  body.letrao-mode #evolution .chart-legend{font-size:.9rem;color:#435149}
  body.letrao-mode #evolution .chart-header strong{font-size:1.8rem}
  body.letrao-mode #evolution .hm{font-size:1.08rem}
  body.letrao-mode #evolution .meta{font-size:.92rem;color:#45534b}
  body.letrao-mode #evolution .hv{font-size:1.22rem}
  body.letrao-mode #evolution .hrow{min-height:96px}
}
</style>`;

const LETRAO_SCRIPT = `
<script id="letrao-script-v11">
(()=>{
  const key='patrimonio-letrao-mode';
  const button=document.getElementById('letraoToggle');
  if(!button)return;
  const desktop=matchMedia('(min-width:761px)');
  const navNew=document.querySelector('.nav[data-view="new"] small');
  const navHome=document.querySelector('.nav[data-view="home"] small');
  const navEvolution=document.querySelector('.nav[data-view="evolution"] small');
  const homeNav=document.querySelector('.nav[data-view="home"]');
  const contributionButton=document.getElementById('toggleContribution');
  const contributionWrap=document.getElementById('contributionWrap');
  const homeActions=document.querySelector('#home .home-balance .actions');
  const printInput=document.getElementById('files');
  const manualButton=document.getElementById('manual');
  const sheetManualButton=document.getElementById('sheetManual');
  const cats=document.getElementById('cats');
  const reviewTitle=document.querySelector('#review>.head h2');
  const setLabels=simple=>{
    if(navNew)navNew.textContent=simple?'Novo mês':'Fechamento';
    if(navHome)navHome.textContent=simple?'Início':'Carteira';
    if(navEvolution)navEvolution.textContent=simple?'Histórico':'Evolução';
    if(reviewTitle)reviewTitle.textContent=simple?'Atualização':'Montar fechamento';
  };
  const apply=enabled=>{
    const active=!!enabled&&desktop.matches;
    document.body.classList.toggle('letrao-mode',active);
    button.setAttribute('aria-pressed',String(active));
    button.title=active?'Sair do Modo Letrão':'Abrir versão simplificada';
    setLabels(active);
    if(contributionButton){
      if(active&&homeActions){homeActions.append(contributionButton)}
      else if(contributionWrap&&contributionButton.parentElement!==contributionWrap){contributionWrap.insertBefore(contributionButton,contributionWrap.firstChild)}
    }
    if(printInput)printInput.disabled=active;
    if(manualButton)manualButton.textContent=active?'Inserir valores':'Adicionar valor manualmente';
    if(sheetManualButton)sheetManualButton.textContent=active?'Atualizar valor':'Inserir manualmente';
    if(active&&(document.body.dataset.view||'')==='settings')homeNav?.click();
  };
  let stored=false;
  try{stored=localStorage.getItem(key)==='true'}catch{}
  apply(stored);
  if(cats)cats.addEventListener('click',event=>{if(document.body.classList.contains('letrao-mode')&&event.target.closest?.('.tap'))setTimeout(()=>sheetManualButton?.click(),0)});
  button.addEventListener('click',()=>{
    stored=!document.body.classList.contains('letrao-mode');
    try{localStorage.setItem(key,String(stored))}catch{}
    apply(stored);
  });
  const sync=()=>apply(stored);
  if(desktop.addEventListener)desktop.addEventListener('change',sync);else if(desktop.addListener)desktop.addListener(sync);
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

  updated = updated.replace(
    '<button id="letraoToggle" class="letrao-toggle" type="button" aria-pressed="false">Módulo letrão</button>',
    '<button id="letraoToggle" class="letrao-toggle" type="button" aria-pressed="false" aria-label="Modo Letrão"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8.2 7.5 5.6 6.2 2.8 13.6a3.1 3.1 0 1 0 5.8 2.2l1.1-4.1M15.8 7.5l2.6-1.3 2.8 7.4a3.1 3.1 0 1 1-5.8 2.2l-1.1-4.1M9.7 8.1h4.6M8.6 15.8h6.8M9.7 8.1l-1.1 7.7M14.3 8.1l1.1 7.7"/></svg><span>Modo Letrão</span></button>'
  );

  if (!updated.includes('id="letraoToggle"')) {
    updated = updated.replace(
      '<div class="topbar-actions"><button id="privacyToggle"',
      '<div class="topbar-actions"><button id="letraoToggle" class="letrao-toggle" type="button" aria-pressed="false" aria-label="Modo Letrão"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8.2 7.5 5.6 6.2 2.8 13.6a3.1 3.1 0 1 0 5.8 2.2l1.1-4.1M15.8 7.5l2.6-1.3 2.8 7.4a3.1 3.1 0 1 1-5.8 2.2l-1.1-4.1M9.7 8.1h4.6M8.6 15.8h6.8M9.7 8.1l-1.1 7.7M14.3 8.1l1.1 7.7"/></svg><span>Modo Letrão</span></button><button id="privacyToggle"'
    );
  }

  if (!updated.includes('id="letrao-mode-v10"')) {
    updated = updated.replace('</head>', `${LETRAO_STYLE}\n</head>`);
  }

  if (!updated.includes('id="letrao-simple-v1"')) {
    updated = updated.replace('</head>', `${LETRAO_SIMPLE_STYLE}\n</head>`);
  }

  if (!updated.includes('id="letrao-script-v8"')) {
    updated = updated.replace('</body>', `${LETRAO_SCRIPT}\n</body>`);
  }

  if (!updated.includes('id="letrao-script-v11"')) {
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
