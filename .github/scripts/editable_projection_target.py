from pathlib import Path
path=Path("index.html")
text=path.read_text(encoding="utf-8")

def rep(old,new,label):
    global text
    count=text.count(old)
    if count!=1:
        raise RuntimeError(f"{label}: expected 1 match, found {count}")
    text=text.replace(old,new,1)

rep(
'.projection-target{margin:22px 0 11px;font-size:1.2rem}',
'.projection-target-row{display:flex;align-items:center;gap:8px;margin:22px 0 11px}.projection-target{margin:0;font-size:1.2rem}.projection-target-edit{width:34px;height:34px;display:grid;place-items:center;flex:0 0 auto;border:0;border-radius:9px;background:transparent;color:var(--green);cursor:pointer}.projection-target-edit:hover{background:#137a520d}.projection-target-edit:focus-visible{outline:2px solid var(--green);outline-offset:2px}.projection-target-edit svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}',
'projection target CSS'
)

rep(
'<h2 class="projection-target">Projeção para R$ 1 milhão</h2>',
'<div class="projection-target-row"><h2 id="projectionTargetLabel" class="projection-target">Defina seu objetivo</h2><button id="editProjectionTarget" class="projection-target-edit" type="button" aria-label="Editar objetivo"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m4 20 4.2-1 10.5-10.5a2.1 2.1 0 0 0-3-3L5.2 16 4 20Z"/><path d="m14.5 6.5 3 3"/></svg></button></div>',
'projection target HTML'
)

retirement_sheet='<div id="retirementSheet" class="sheet hidden"><div class="sheet-card"><button type="button" id="retirementSheetClose" class="sheet-close" aria-label="Fechar">×</button><p class="eyebrow">Divisão do patrimônio</p><h2>Adicionar CDBs</h2>'
goal_sheet='<div id="projectionTargetSheet" class="sheet hidden" aria-hidden="true"><div class="sheet-card"><button type="button" id="projectionTargetSheetClose" class="sheet-close" aria-label="Fechar">×</button><p class="eyebrow">Projeções</p><h2>Definir objetivo</h2><p class="sheet-copy">Informe o valor de patrimônio que você quer alcançar. As datas serão recalculadas com base nesse objetivo.</p><div class="field"><label for="projectionTargetInput">Valor do objetivo</label><input id="projectionTargetInput" type="text" inputmode="decimal" placeholder="R$ 1.000.000"></div><div class="sheet-actions"><button type="button" id="saveProjectionTarget" class="btn primary full">Salvar objetivo</button><button type="button" id="cancelProjectionTarget" class="btn secondary full">Cancelar</button></div></div></div>\n'+retirement_sheet
rep(retirement_sheet,goal_sheet,'projection target sheet')

rep(
'categoryCreationOrigin="settings";let currentUser=null',
'categoryCreationOrigin="settings",projectionTarget=0;let currentUser=null',
'projection target state'
)

rep(
'const OWNER_KEY="patrimonio-firebase-owner";',
'const OWNER_KEY="patrimonio-firebase-owner";const projectionTargetKey=uid=>`patrimonio-projection-target-${uid||"anonymous"}`;function cleanProjectionTarget(value){let n=Number(value);return Number.isFinite(n)&&n>0?n:0}function loadProjectionTarget(uid){return cleanProjectionTarget(localStorage.getItem(projectionTargetKey(uid)))}function saveProjectionTargetLocal(uid=currentUser?.uid){if(!uid)return;if(projectionTarget>0)localStorage.setItem(projectionTargetKey(uid),String(projectionTarget));else localStorage.removeItem(projectionTargetKey(uid))}',
'projection target storage helpers'
)

rep(
'projectionCurrent:$("#projectionCurrent"),projectionLastRate:$("#projectionLastRate")',
'projectionCurrent:$("#projectionCurrent"),projectionTargetLabel:$("#projectionTargetLabel"),projectionTargetSheet:$("#projectionTargetSheet"),projectionTargetInput:$("#projectionTargetInput"),projectionLastRate:$("#projectionLastRate")',
'projection target element refs'
)

rep(
'function cloudPayload(version=Date.now()){return{formatVersion:5,clientUpdatedAt:version,updatedAt:serverTimestamp(),categories:[...categories],pendingContributions:cleanPendingContributions(pendingContributions),closings:ordered()}}',
'function cloudPayload(version=Date.now()){return{formatVersion:6,clientUpdatedAt:version,updatedAt:serverTimestamp(),projectionTarget:cleanProjectionTarget(projectionTarget),categories:[...categories],pendingContributions:cleanPendingContributions(pendingContributions),closings:ordered()}}',
'cloud payload target'
)

rep(
'async function startCloudSync(user){unsubscribeCloud?.();currentUser=user;updateUserIdentity(user);',
'async function startCloudSync(user){unsubscribeCloud?.();currentUser=user;projectionTarget=loadProjectionTarget(user.uid);updateUserIdentity(user);',
'load local target on account'
)

rep(
'const snapshot=await getDoc(cloudRef);const data=snapshot.exists()?snapshot.data()||{}:{};const remoteRaw=',
'const snapshot=await getDoc(cloudRef);const data=snapshot.exists()?snapshot.data()||{}:{};if(Object.prototype.hasOwnProperty.call(data,"projectionTarget"))projectionTarget=cleanProjectionTarget(data.projectionTarget);saveProjectionTargetLocal(user.uid);const remoteRaw=',
'load cloud target'
)

rep(
'const data=snap.data()||{},version=Number(data.clientUpdatedAt)||0;',
'const data=snap.data()||{},version=Number(data.clientUpdatedAt)||0;if(Object.prototype.hasOwnProperty.call(data,"projectionTarget")){projectionTarget=cleanProjectionTarget(data.projectionTarget);saveProjectionTargetLocal(user.uid);renderProjections()}',
'live cloud target'
)

rep(
'const PROJECTION_TARGET=1000000;\nfunction monthsToTarget',
'function projectionTargetText(value){return new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL",maximumFractionDigits:0}).format(cleanProjectionTarget(value))}\nfunction monthsToTarget',
'remove fixed target'
)

rep(
'function projectionData(current,baseMonth,rate,missingLabel="Não atingiria"){let months=monthsToTarget(current,PROJECTION_TARGET,rate);',
'function projectionData(current,baseMonth,rate,missingLabel="Não atingiria"){let months=monthsToTarget(current,projectionTarget,rate);',
'projection data dynamic target'
)

old_render='function renderProjections(){let o=ordered(),last=o.at(-1),prev=o.at(-2),prevPrev=o.at(-3);el.projectionEmpty.classList.toggle("hidden",!!last);el.projectionContent.classList.toggle("hidden",!last);if(!last)return;el.projectionCurrentLabel.textContent="Valor atual · "+mshort(last.month);el.projectionCurrent.textContent=brl(last.total);let lastPerformance=prev?performancePct(last,prev):null,previousPerformance=prev&&prevPrev?performancePct(prev,prevPrev):null;let lastRate=Number.isFinite(lastPerformance)?lastPerformance/100:null;let previousLastRate=Number.isFinite(previousPerformance)?previousPerformance/100:null;if(lastRate===null){el.projectionLastRate.textContent="Sem mês anterior";el.projectionLastRate.className="projection-rate"}else{el.projectionLastRate.textContent=(lastRate>0?"+":"")+pct(lastRate*100)+" ao mês";el.projectionLastRate.className="projection-rate "+(lastRate>0?"up":lastRate<0?"down":"")}let currentLast=projectionData(last.total,last.month,lastRate,lastRate===null?"Histórico insuficiente":"Não atingiria");let previousLast=prev?projectionData(prev.total,prev.month,previousLastRate,previousLastRate===null?"Histórico insuficiente":"Não atingiria"):{months:null,label:"Histórico insuficiente",short:"—"};let current08=projectionData(last.total,last.month,.008);let previous08=prev?projectionData(prev.total,prev.month,.008):{months:null,label:"—",short:"—"};let current10=projectionData(last.total,last.month,.01);let previous10=prev?projectionData(prev.total,prev.month,.01):{months:null,label:"—",short:"—"};setProjectionScenario(el.projectionLastDate,el.projectionLastPrevious,currentLast,previousLast,!!prevPrev);setProjectionScenario(el.projection08Date,el.projection08Previous,current08,previous08,!!prev);setProjectionScenario(el.projection10Date,el.projection10Previous,current10,previous10,!!prev);renderWealthSplit(last)}'
new_render='function resetProjectionScenarios(){el.projectionLastRate.textContent="0,00% ao mês";el.projectionLastRate.className="projection-rate";[el.projectionLastDate,el.projection08Date,el.projection10Date].forEach(node=>{node.textContent="—";node.className="projection-date unavailable"});[el.projectionLastPrevious,el.projection08Previous,el.projection10Previous].forEach(node=>node.textContent="—")}\nfunction renderProjections(){let o=ordered(),last=o.at(-1),prev=o.at(-2),prevPrev=o.at(-3),hasTarget=projectionTarget>0;el.projectionEmpty.classList.add("hidden");el.projectionContent.classList.remove("hidden");el.projectionTargetLabel.textContent=hasTarget?`Projeção para ${projectionTargetText(projectionTarget)}`:"Defina seu objetivo";el.projectionCurrentLabel.textContent=last?`Valor atual · ${mshort(last.month)}`:"Valor atual";el.projectionCurrent.textContent=brl(last?.total||0);if(!last||!hasTarget){resetProjectionScenarios();renderWealthSplit(last||{total:0,entries:[],retirementCdb:0});return}let lastPerformance=prev?performancePct(last,prev):null,previousPerformance=prev&&prevPrev?performancePct(prev,prevPrev):null;let lastRate=Number.isFinite(lastPerformance)?lastPerformance/100:null;let previousLastRate=Number.isFinite(previousPerformance)?previousPerformance/100:null;if(lastRate===null){el.projectionLastRate.textContent="Sem mês anterior";el.projectionLastRate.className="projection-rate"}else{el.projectionLastRate.textContent=(lastRate>0?"+":"")+pct(lastRate*100)+" ao mês";el.projectionLastRate.className="projection-rate "+(lastRate>0?"up":lastRate<0?"down":"")}let currentLast=projectionData(last.total,last.month,lastRate,lastRate===null?"Histórico insuficiente":"Não atingiria");let previousLast=prev?projectionData(prev.total,prev.month,previousLastRate,previousLastRate===null?"Histórico insuficiente":"Não atingiria"):{months:null,label:"Histórico insuficiente",short:"—"};let current08=projectionData(last.total,last.month,.008);let previous08=prev?projectionData(prev.total,prev.month,.008):{months:null,label:"—",short:"—"};let current10=projectionData(last.total,last.month,.01);let previous10=prev?projectionData(prev.total,prev.month,.01):{months:null,label:"—",short:"—"};setProjectionScenario(el.projectionLastDate,el.projectionLastPrevious,currentLast,previousLast,!!prevPrev);setProjectionScenario(el.projection08Date,el.projection08Previous,current08,previous08,!!prev);setProjectionScenario(el.projection10Date,el.projection10Previous,current10,previous10,!!prev);renderWealthSplit(last)}'
rep(old_render,new_render,'render projections dynamic')

insert_before='function renderWealthSplit(last){'
goal_funcs='function openProjectionTargetSheet(){el.projectionTargetInput.value=projectionTarget?String(projectionTarget).replace(".",","):"";el.projectionTargetSheet.classList.remove("hidden");el.projectionTargetSheet.setAttribute("aria-hidden","false");setTimeout(()=>el.projectionTargetInput.focus(),50)}\nfunction closeProjectionTargetSheet(){el.projectionTargetSheet.classList.add("hidden");el.projectionTargetSheet.setAttribute("aria-hidden","true")}\nasync function saveProjectionTarget(){let value=parse(el.projectionTargetInput.value);if(!(value>0))return toast("Informe um objetivo maior que zero.");projectionTarget=value;saveProjectionTargetLocal();closeProjectionTargetSheet();renderProjections();await syncCloudNow();toast("Objetivo atualizado.")}\n'+insert_before
rep(insert_before,goal_funcs,'projection target functions')

events='$("#addRetirementCdb").onclick=openRetirementSheet;$("#retirementSheetClose").onclick=closeRetirementSheet;$("#cancelRetirementCdb").onclick=closeRetirementSheet;el.retirementSheet.onclick=e=>{if(e.target===el.retirementSheet)closeRetirementSheet()};$("#saveRetirementCdb").onclick=saveRetirementCdb;'
events_new='$("#editProjectionTarget").onclick=openProjectionTargetSheet;$("#projectionTargetSheetClose").onclick=closeProjectionTargetSheet;$("#cancelProjectionTarget").onclick=closeProjectionTargetSheet;$("#saveProjectionTarget").onclick=saveProjectionTarget;el.projectionTargetSheet.onclick=e=>{if(e.target===el.projectionTargetSheet)closeProjectionTargetSheet()};el.projectionTargetInput.addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();saveProjectionTarget()}});'+events
rep(events,events_new,'projection target events')

path.write_text(text,encoding="utf-8")
