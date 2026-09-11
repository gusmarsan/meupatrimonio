from pathlib import Path
import re

idx = Path('index.html')
html = idx.read_text(encoding='utf-8')

old = '<section id="letraoHelp" class="view" aria-label="Dúvidas"></section>'
new = '''<section id="letraoHelp" class="view" aria-label="Dúvidas">
<div class="letrao-help-content">
<h2>Como adicionar investimento</h2>
<ol class="letrao-help-steps">
<li><span class="letrao-help-number">1</span><p>Clique em <b>ATUALIZAR INVESTIMENTOS</b>.</p></li>
<li><span class="letrao-help-number">2</span><p>Escolha o mês que quer atualizar.</p></li>
<li><span class="letrao-help-number">3</span><p>Clique em <b>INSERIR VALORES</b>.</p></li>
<li><span class="letrao-help-number">4</span><p>Digite o valor atual de cada investimento.</p></li>
<li><span class="letrao-help-number">5</span><p>Confira os valores e clique em <b>SALVAR MÊS</b>.</p></li>
</ol>
</div>
</section>'''
if old not in html:
    raise SystemExit('blank Letrao help section not found')
html = html.replace(old, new, 1)

css_marker = '/* Modo Letrao month-only picker */'
css = '''/* Letrao help content */
@media(min-width:761px){
  body.letrao-mode #letraoHelp .letrao-help-content{max-width:820px;padding:34px 0 56px}
  body.letrao-mode #letraoHelp .letrao-help-content h2{margin:0 0 28px;font-size:2rem;line-height:1.2;font-weight:700;color:#17201b}
  body.letrao-mode #letraoHelp .letrao-help-steps{list-style:none;margin:0;padding:0;display:grid;gap:0}
  body.letrao-mode #letraoHelp .letrao-help-steps li{display:grid;grid-template-columns:56px minmax(0,1fr);gap:18px;align-items:center;min-height:88px;padding:16px 0;border-bottom:1px solid #17201b1f}
  body.letrao-mode #letraoHelp .letrao-help-steps li:first-child{border-top:1px solid #17201b1f}
  body.letrao-mode #letraoHelp .letrao-help-number{width:48px;height:48px;display:grid;place-items:center;border-radius:50%;background:#17201b;color:#fff;font-size:1.15rem;font-weight:800}
  body.letrao-mode #letraoHelp .letrao-help-steps p{margin:0;color:#17201b;font-size:1.15rem;line-height:1.45}
  body.letrao-mode #letraoHelp .letrao-help-steps b{font-weight:800}
}

'''
if '/* Letrao help content */' not in html:
    if css_marker not in html:
        raise SystemExit('Letrao CSS marker not found')
    html = html.replace(css_marker, css + css_marker, 1)

html = re.sub(r'\./sw\.js\?v=\d+', './sw.js?v=32', html)
idx.write_text(html, encoding='utf-8')

sw = Path('sw.js')
s = sw.read_text(encoding='utf-8')
if 'meu-patrimonio-pwa-v31' not in s:
    raise SystemExit('cache v31 not found')
s = s.replace('meu-patrimonio-pwa-v31', 'meu-patrimonio-pwa-v32', 1)
sw.write_text(s, encoding='utf-8')
