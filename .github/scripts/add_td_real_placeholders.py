from pathlib import Path
import re

idx=Path('index.html')
html=idx.read_text(encoding='utf-8')

style='''<style id="td-real-placeholder-v1">
.td-real-placeholder{margin-top:7px;display:grid;gap:2px;color:#2b6fa8;font-size:.66rem;font-weight:600;line-height:1.35;text-align:right}
body.letrao-mode .td-real-placeholder{display:none!important}
@media(max-width:760px){.td-real-placeholder{font-size:.62rem}}
</style>\n'''
if 'id="td-real-placeholder-v1"' not in html:
    html=html.replace('</head>',style+'</head>',1)

old='r.innerHTML=`<div><b>${esc(x.category)}</b><span class="tap">Inserir manualmente ou por print</span></div><div><div class="v">${brl(x.value)}</div><div class="s"><span>${pct(share)}</span><span class="sep"> | </span><span class="${variationClass}">${signedPct(variation)}</span></div>${investmentDateLine}${aporte?`<div class="s aporte-mini">Aporte: ${brl(aporte)}</div>`:""}</div><span class="chev">›</span>`;'
new='let tdRealPlaceholder=x.category===RETIREMENT_CATEGORY?\'<div class="td-real-placeholder"><span>TD 2029 (rendimento real): R$ xx.xxx,xx</span><span>TD 2033 (rendimento real): R$ xx.xxx,xx</span></div>\':"";r.innerHTML=`<div><b>${esc(x.category)}</b><span class="tap">Inserir manualmente ou por print</span></div><div><div class="v">${brl(x.value)}</div><div class="s"><span>${pct(share)}</span><span class="sep"> | </span><span class="${variationClass}">${signedPct(variation)}</span></div>${investmentDateLine}${aporte?`<div class="s aporte-mini">Aporte: ${brl(aporte)}</div>`:""}${tdRealPlaceholder}</div><span class="chev">›</span>`;'
if old not in html:
    raise SystemExit('investment row template not found')
html=html.replace(old,new,1)

html=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=38',html)
idx.write_text(html,encoding='utf-8')

sw=Path('sw.js')
s=sw.read_text(encoding='utf-8')
s=re.sub(r"meu-patrimonio-pwa-v\d+","meu-patrimonio-pwa-v38",s,count=1)
sw.write_text(s,encoding='utf-8')
