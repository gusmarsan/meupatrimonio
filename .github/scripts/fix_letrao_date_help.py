from pathlib import Path
import re

idx=Path('index.html')
html=idx.read_text(encoding='utf-8')

html=html.replace('<h2>Como adicionar investimento</h2>','<h2>Como atualizar seus investimentos</h2>',1)
html=html.replace('<li><span class="letrao-help-number">2</span><p>Escolha o mês que quer atualizar.</p></li>','<li><span class="letrao-help-number">2</span><p>Escolha a data que quer atualizar.</p></li>',1)

old='<div class="card"><div class="field"><label for="month">Mês do fechamento</label><input id="month" type="month"><button id="letraoMonthTrigger" class="letrao-month-trigger" type="button" aria-haspopup="dialog" aria-expanded="false"><span id="letraoMonthTriggerLabel">Escolher mês</span><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/></svg></button></div></div>'
new='<div class="card"><div class="field closing-month-field"><label for="month">Mês do fechamento</label><input id="month" type="month"><button id="letraoMonthTrigger" class="letrao-month-trigger" type="button" aria-haspopup="dialog" aria-expanded="false"><span id="letraoMonthTriggerLabel">Escolher mês</span><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/></svg></button></div><div id="letraoClosingDateField" class="field" hidden><label for="letraoClosingDate">Data do fechamento</label><input id="letraoClosingDate" type="date"></div></div>'
if old not in html:
    raise SystemExit('new closing month card not found')
html=html.replace(old,new,1)

css='''\n/* Modo Letrao: escolha por data, não por mês */\n@media(min-width:761px){\n  body.letrao-mode #new .closing-month-field{display:none!important}\n  body.letrao-mode #new #letraoClosingDateField{display:grid!important}\n  body.letrao-mode #new #letraoClosingDate{min-height:72px;font-size:1.18rem;background:#fff;color:#17201b}\n}\n'''
marker='/* Letrao help content */'
if '/* Modo Letrao: escolha por data, não por mês */' not in html:
    if marker not in html: raise SystemExit('help CSS marker not found')
    html=html.replace(marker,css+'\n'+marker,1)

html=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=33',html)
idx.write_text(html,encoding='utf-8')

sw=Path('sw.js')
s=sw.read_text(encoding='utf-8')
if 'meu-patrimonio-pwa-v32' not in s: raise SystemExit('cache v32 not found')
s=s.replace('meu-patrimonio-pwa-v32','meu-patrimonio-pwa-v33',1)
s=s.replace("dateLabel.textContent='Dia do fechamento'","dateLabel.textContent='Data do fechamento'",1)
s=s.replace("simple?'Dia do fechamento':'Mês do fechamento'","simple?'Data do fechamento':'Mês do fechamento'",1)
s=s.replace('id="letrao-script-v12"','id="letrao-script-v13"',1)
s=s.replace('letrao-script-v(?:8|11)','letrao-script-v(?:8|11|12)',1)
s=s.replace("if (!updated.includes('id=\"letrao-script-v12\"'))","if (!updated.includes('id=\"letrao-script-v13\"'))",1)
sw.write_text(s,encoding='utf-8')
