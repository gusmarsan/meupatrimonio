from pathlib import Path
import re

idx=Path('index.html')
html=idx.read_text(encoding='utf-8')

# Remove the temporary Home placeholder styling.
html=re.sub(r'\n<style id="td-real-placeholder-v1">.*?</style>\n','\n',html,flags=re.S)

# Remove the temporary Home placeholder markup and restore the investment row.
old_home='let tdRealPlaceholder=x.category===RETIREMENT_CATEGORY?\'<div class="td-real-placeholder"><span>TD 2029 (rendimento real): R$ xx.xxx,xx</span><span>TD 2033 (rendimento real): R$ xx.xxx,xx</span></div>\':"";r.innerHTML=`<div><b>${esc(x.category)}</b><span class="tap">Inserir manualmente ou por print</span></div><div><div class="v">${brl(x.value)}</div><div class="s"><span>${pct(share)}</span><span class="sep"> | </span><span class="${variationClass}">${signedPct(variation)}</span></div>${investmentDateLine}${aporte?`<div class="s aporte-mini">Aporte: ${brl(aporte)}</div>`:""}${tdRealPlaceholder}</div><span class="chev">›</span>`;'
new_home='r.innerHTML=`<div><b>${esc(x.category)}</b><span class="tap">Inserir manualmente ou por print</span></div><div><div class="v">${brl(x.value)}</div><div class="s"><span>${pct(share)}</span><span class="sep"> | </span><span class="${variationClass}">${signedPct(variation)}</span></div>${investmentDateLine}${aporte?`<div class="s aporte-mini">Aporte: ${brl(aporte)}</div>`:""}</div><span class="chev">›</span>`;'
if old_home not in html:
    raise SystemExit('Home TD placeholder markup not found')
html=html.replace(old_home,new_home,1)

# Add the new Projections section after retirement.
section='''<section class="td-real-section" aria-labelledby="tdRealTitle">
  <div class="td-real-head">
    <p class="section-kicker">Tesouro Direto</p>
    <h2 id="tdRealTitle">Rendimento real</h2>
    <p>Informe os valores atuais. Depois, o cálculo poderá ser atualizado automaticamente.</p>
  </div>
  <div class="td-real-grid">
    <label class="td-real-field" for="tdReal2029Input"><span>TD 2029</span><small>Rendimento real</small><input id="tdReal2029Input" type="text" inputmode="decimal" placeholder="R$ 0,00" autocomplete="off"></label>
    <label class="td-real-field" for="tdReal2033Input"><span>TD 2033</span><small>Rendimento real</small><input id="tdReal2033Input" type="text" inputmode="decimal" placeholder="R$ 0,00" autocomplete="off"></label>
  </div>
  <button id="saveTdRealValues" class="btn primary td-real-save" type="button">Salvar valores</button>
</section>
'''
anchor='  </div>\n</section>\n</div>\n</section>\n<section id="settings"'
if 'id="tdRealTitle"' not in html:
    if anchor not in html:
        raise SystemExit('Projection/retirement closing anchor not found')
    html=html.replace(anchor,'  </div>\n</section>\n'+section+'</div>\n</section>\n<section id="settings"',1)

# Add section styling that follows the Projections visual language.
style='''<style id="td-real-projections-v1">
.td-real-section{margin-top:44px;padding-top:38px;border-top:1px solid var(--line)}
.td-real-head{margin-bottom:18px}
.td-real-head .section-kicker{margin-bottom:7px}
.td-real-head h2{margin:0;font-family:"Inter",sans-serif;font-size:1.55rem;font-weight:600;letter-spacing:-.035em;color:var(--txt)}
.td-real-head>p:last-child{max-width:620px;margin:8px 0 0;color:var(--mut);font-size:.72rem;line-height:1.5}
.td-real-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.td-real-field{display:grid;gap:6px;padding:16px;border:1px solid var(--line);border-radius:18px;background:var(--card)}
.td-real-field>span{color:var(--txt);font-size:.88rem;font-weight:650}
.td-real-field>small{color:var(--mut);font-size:.66rem;font-weight:600}
.td-real-field input{margin-top:4px;background:var(--card2);color:var(--txt);font-weight:650;font-variant-numeric:tabular-nums}
.td-real-save{width:auto;min-width:150px;margin-top:12px}
@media(min-width:761px){
  .td-real-section{margin-top:58px;padding-top:46px}
  .td-real-head{margin-bottom:22px}
  .td-real-head h2{font-size:1.9rem}
  .td-real-grid{gap:16px}
  .td-real-field{padding:20px;border-color:#17201b17;border-radius:13px;background:#fff}
  .td-real-field input{background:#f7f8f5}
}
@media(max-width:620px){.td-real-grid{grid-template-columns:1fr}.td-real-save{width:100%}}
body.letrao-mode #projections .td-real-section{display:none!important}
</style>\n'''
if 'id="td-real-projections-v1"' not in html:
    html=html.replace('</head>',style+'</head>',1)

# Add state.
old_state='retirementSimulationBoost=false,retirementSimulationMonthlyContribution=0;let currentUser=null'
new_state='retirementSimulationBoost=false,retirementSimulationMonthlyContribution=0,tdReal2029=0,tdReal2033=0;let currentUser=null'
if old_state not in html:
    raise SystemExit('state anchor not found')
html=html.replace(old_state,new_state,1)

# Add per-account storage helpers after retirement simulation helpers.
storage_anchor='function saveRetirementSimulationLocal(uid=currentUser?.uid){if(!uid)return;localStorage.setItem(retirementSimulationKey(uid),JSON.stringify(cleanRetirementSimulation({capital:retirementSimulationCapital,auto:retirementSimulationAuto,years:retirementSimulationYears,boost:retirementSimulationBoost,monthlyContribution:retirementSimulationMonthlyContribution})))}'
storage_add='''const tdRealKey=uid=>`patrimonio-td-real-${uid||"anonymous"}`;function cleanTdReal(value){let raw=value&&typeof value==="object"?value:{};return{td2029:Math.max(0,Number(raw.td2029)||0),td2033:Math.max(0,Number(raw.td2033)||0)}}function loadTdReal(uid){try{return cleanTdReal(JSON.parse(localStorage.getItem(tdRealKey(uid))||"{}"))}catch{return cleanTdReal({})}}function applyTdReal(value){let clean=cleanTdReal(value);tdReal2029=clean.td2029;tdReal2033=clean.td2033}function saveTdRealLocal(uid=currentUser?.uid){if(!uid)return;localStorage.setItem(tdRealKey(uid),JSON.stringify(cleanTdReal({td2029:tdReal2029,td2033:tdReal2033})))}'''
if 'const tdRealKey=' not in html:
    if storage_anchor not in html:
        raise SystemExit('retirement storage anchor not found')
    html=html.replace(storage_anchor,storage_anchor+storage_add,1)

# Render inputs and save handler.
render_anchor='function renderProjections(){let o=ordered()'
render_helper='''function renderTdRealInputs(){let input2029=$("#tdReal2029Input"),input2033=$("#tdReal2033Input");if(input2029&&document.activeElement!==input2029)input2029.value=tdReal2029?tdReal2029.toFixed(2).replace(".",","):"";if(input2033&&document.activeElement!==input2033)input2033.value=tdReal2033?tdReal2033.toFixed(2).replace(".",","):""}async function saveTdRealValues(){let input2029=$("#tdReal2029Input"),input2033=$("#tdReal2033Input"),value2029=parse(input2029?.value||"0"),value2033=parse(input2033?.value||"0");tdReal2029=Math.max(0,Number(value2029)||0);tdReal2033=Math.max(0,Number(value2033)||0);saveTdRealLocal();renderTdRealInputs();await syncCloudNow();toast("Valores dos Tesouros atualizados.")}
'''
if 'function renderTdRealInputs()' not in html:
    if render_anchor not in html:
        raise SystemExit('renderProjections anchor not found')
    html=html.replace(render_anchor,render_helper+render_anchor,1)

# Always refresh the fields when Projections renders.
old_render='function renderProjections(){let o=ordered(),last=o.at(-1),prev=o.at(-2),prevPrev=o.at(-3),hasTarget=projectionTarget>0;'
new_render='function renderProjections(){renderTdRealInputs();let o=ordered(),last=o.at(-1),prev=o.at(-2),prevPrev=o.at(-3),hasTarget=projectionTarget>0;'
if old_render not in html:
    raise SystemExit('renderProjections exact anchor not found')
html=html.replace(old_render,new_render,1)

# Sync with Firebase.
old_payload='function cloudPayload(version=Date.now()){return{formatVersion:8,clientUpdatedAt:version,updatedAt:serverTimestamp(),projectionTarget:cleanProjectionTarget(projectionTarget),retirementSimulation:cleanRetirementSimulation({capital:retirementSimulationCapital,auto:retirementSimulationAuto,years:retirementSimulationYears,boost:retirementSimulationBoost,monthlyContribution:retirementSimulationMonthlyContribution}),categories:[...categories],pendingContributions:cleanPendingContributions(pendingContributions),closings:ordered()}}'
new_payload='function cloudPayload(version=Date.now()){return{formatVersion:9,clientUpdatedAt:version,updatedAt:serverTimestamp(),projectionTarget:cleanProjectionTarget(projectionTarget),retirementSimulation:cleanRetirementSimulation({capital:retirementSimulationCapital,auto:retirementSimulationAuto,years:retirementSimulationYears,boost:retirementSimulationBoost,monthlyContribution:retirementSimulationMonthlyContribution}),tdRealValues:cleanTdReal({td2029:tdReal2029,td2033:tdReal2033}),categories:[...categories],pendingContributions:cleanPendingContributions(pendingContributions),closings:ordered()}}'
if old_payload not in html:
    raise SystemExit('cloud payload anchor not found')
html=html.replace(old_payload,new_payload,1)

old_start='currentUser=user;projectionTarget=loadProjectionTarget(user.uid);applyRetirementSimulation(loadRetirementSimulation(user.uid));updateUserIdentity(user);'
new_start='currentUser=user;projectionTarget=loadProjectionTarget(user.uid);applyRetirementSimulation(loadRetirementSimulation(user.uid));applyTdReal(loadTdReal(user.uid));updateUserIdentity(user);'
if old_start not in html:
    raise SystemExit('startCloudSync local load anchor not found')
html=html.replace(old_start,new_start,1)

old_remote='if(Object.prototype.hasOwnProperty.call(data,"retirementSimulation"))applyRetirementSimulation(data.retirementSimulation);saveRetirementSimulationLocal(user.uid);const remoteRaw='
new_remote='if(Object.prototype.hasOwnProperty.call(data,"retirementSimulation"))applyRetirementSimulation(data.retirementSimulation);saveRetirementSimulationLocal(user.uid);if(Object.prototype.hasOwnProperty.call(data,"tdRealValues"))applyTdReal(data.tdRealValues);saveTdRealLocal(user.uid);const remoteRaw='
if old_remote not in html:
    raise SystemExit('remote initial load anchor not found')
html=html.replace(old_remote,new_remote,1)

old_listener='if(Object.prototype.hasOwnProperty.call(data,"retirementSimulation")){applyRetirementSimulation(data.retirementSimulation);saveRetirementSimulationLocal(user.uid);renderProjections()}if(version&&version===lastPushedVersion)'
new_listener='if(Object.prototype.hasOwnProperty.call(data,"retirementSimulation")){applyRetirementSimulation(data.retirementSimulation);saveRetirementSimulationLocal(user.uid);renderProjections()}if(Object.prototype.hasOwnProperty.call(data,"tdRealValues")){applyTdReal(data.tdRealValues);saveTdRealLocal(user.uid);renderTdRealInputs()}if(version&&version===lastPushedVersion)'
if old_listener not in html:
    raise SystemExit('snapshot listener anchor not found')
html=html.replace(old_listener,new_listener,1)

# Hook save action.
handler_anchor='$("#retirementSimulationMonthlyContribution").addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();e.target.blur()}});$("#addRetirementCdb").onclick=openRetirementSheet;'
handler_new='$("#retirementSimulationMonthlyContribution").addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();e.target.blur()}});$("#saveTdRealValues").onclick=saveTdRealValues;["#tdReal2029Input","#tdReal2033Input"].forEach(selector=>$(selector).addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();saveTdRealValues()}}));$("#addRetirementCdb").onclick=openRetirementSheet;'
if handler_anchor not in html:
    raise SystemExit('handler anchor not found')
html=html.replace(handler_anchor,handler_new,1)

# Bump PWA.
html=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=39',html)
idx.write_text(html,encoding='utf-8')

sw=Path('sw.js')
s=sw.read_text(encoding='utf-8')
s=re.sub(r"meu-patrimonio-pwa-v\d+","meu-patrimonio-pwa-v39",s,count=1)
sw.write_text(s,encoding='utf-8')
