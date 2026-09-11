from pathlib import Path
import re

idx=Path('index.html')
html=idx.read_text(encoding='utf-8')

style='''<style id="letrao-return-date-v1">
.home-return-date{display:none}
.home-return-stack{display:inline-flex;align-items:center}
@media(min-width:761px){
  body.letrao-mode #home .home-return-stack{display:inline-flex;flex-direction:column;align-items:center;gap:7px}
  body.letrao-mode #home .home-return-date:not(:empty){display:block;font-size:.84rem;font-weight:700;line-height:1;color:#4b5851;letter-spacing:.03em}
}
</style>\n'''
if 'id="letrao-return-date-v1"' not in html:
    html=html.replace('</head>',style+'</head>',1)

old='<div class="home-performance-line"><p id="latestDelta" class="delta"></p><span id="homeReturnBadge" class="home-return-badge"></span></div>'
new='<div class="home-performance-line"><p id="latestDelta" class="delta"></p><span class="home-return-stack"><span id="homeReturnBadge" class="home-return-badge"></span><small id="homeReturnDate" class="home-return-date"></small></span></div>'
if old not in html:
    raise SystemExit('home return badge markup not found')
html=html.replace(old,new,1)

old_js='$("#homeReturnBadge").textContent=prev?signedPct(monthRate):"Primeiro fechamento";$("#homeReturnBadge").className="home-return-badge "+(prev?changeClass(monthRate):"");if(!prev){'
new_js='$("#homeReturnBadge").textContent=prev?signedPct(monthRate):"Primeiro fechamento";$("#homeReturnBadge").className="home-return-badge "+(prev?changeClass(monthRate):"");let closingDateParts=String(last.closingDate||"").split("-"),closingDateShort=closingDateParts.length===3?`${closingDateParts[2]}/${closingDateParts[1]}`:"";$("#homeReturnDate").textContent=prev?closingDateShort:"";if(!prev){'
if old_js not in html:
    raise SystemExit('home return badge JS not found')
html=html.replace(old_js,new_js,1)

html=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=34',html)
idx.write_text(html,encoding='utf-8')

sw=Path('sw.js')
s=sw.read_text(encoding='utf-8')
s=re.sub(r"meu-patrimonio-pwa-v\d+","meu-patrimonio-pwa-v34",s,count=1)
sw.write_text(s,encoding='utf-8')
