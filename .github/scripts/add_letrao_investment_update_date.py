from pathlib import Path
import re

idx=Path('index.html')
html=idx.read_text(encoding='utf-8')

style='''<style id="letrao-investment-date-v1">
.investment-update-date{display:none}
@media(min-width:761px){
  body.letrao-mode #home .investment-update-date{display:block;margin-top:8px;font-size:.82rem;font-weight:650;line-height:1.2;color:#536159;white-space:nowrap}
}
</style>\n'''
if 'id="letrao-investment-date-v1"' not in html:
    html=html.replace('</head>',style+'</head>',1)

old='r.innerHTML=`<div><b>${esc(x.category)}</b><span class="tap">Inserir manualmente ou por print</span></div><div><div class="v">${brl(x.value)}</div><div class="s"><span>${pct(share)}</span><span class="sep"> | </span><span class="${variationClass}">${signedPct(variation)}</span></div>${aporte?`<div class="s aporte-mini">Aporte: ${brl(aporte)}</div>`:""}</div><span class="chev">›</span>`;'
new='let investmentDateParts=String(last.closingDate||"").split("-"),investmentDateShort=investmentDateParts.length===3?`${investmentDateParts[2]}/${investmentDateParts[1]}`:"",investmentDateLine=Number.isFinite(variation)&&investmentDateShort?`<div class="investment-update-date">Última atualização em: ${investmentDateShort}</div>`:"";r.innerHTML=`<div><b>${esc(x.category)}</b><span class="tap">Inserir manualmente ou por print</span></div><div><div class="v">${brl(x.value)}</div><div class="s"><span>${pct(share)}</span><span class="sep"> | </span><span class="${variationClass}">${signedPct(variation)}</span></div>${investmentDateLine}${aporte?`<div class="s aporte-mini">Aporte: ${brl(aporte)}</div>`:""}</div><span class="chev">›</span>`;'
if old not in html:
    raise SystemExit('investment row markup not found')
html=html.replace(old,new,1)

html=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=35',html)
idx.write_text(html,encoding='utf-8')

sw=Path('sw.js')
s=sw.read_text(encoding='utf-8')
s=re.sub(r"meu-patrimonio-pwa-v\d+","meu-patrimonio-pwa-v35",s,count=1)
sw.write_text(s,encoding='utf-8')
