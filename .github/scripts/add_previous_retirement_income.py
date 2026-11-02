from pathlib import Path
import re

idx=Path('index.html')
html=idx.read_text(encoding='utf-8')

style='''<style id="retirement-previous-income-v1">
.retirement-simulation-previous{margin:5px 0 0;color:var(--mut);font-size:.62rem;line-height:1.45}
.retirement-simulation-previous strong{color:var(--txt);font-weight:650;font-variant-numeric:tabular-nums}
.retirement-simulation-previous-change{margin-left:4px;font-weight:700;font-variant-numeric:tabular-nums}
@media(min-width:761px){.retirement-simulation-previous{font-size:.68rem}}
body.letrao-mode .retirement-simulation-previous{display:none!important}
</style>\n'''
if 'id="retirement-previous-income-v1"' not in html:
    html=html.replace('</head>',style+'</head>',1)

cards=[
('Conservative','retirement-simulation-card--conservative'),
('Moderate','retirement-simulation-card--moderate'),
('Optimistic','retirement-simulation-card--optimistic')
]
for name,cls in cards:
    old=f'<p class="retirement-simulation-income">Vivendo de rendimentos, você tiraria uns: <strong id="retirementSimulation{name}Income">—</strong></p>'
    new=old+f'<p id="retirementSimulation{name}Previous" class="retirement-simulation-previous hidden">No mês anterior: <strong id="retirementSimulation{name}PreviousIncome">—</strong><span id="retirementSimulation{name}PreviousChange" class="retirement-simulation-previous-change"></span></p>'
    if old not in html and f'id="retirementSimulation{name}Previous"' not in html:
        raise SystemExit(f'{name} income markup not found')
    if f'id="retirementSimulation{name}Previous"' not in html:
        html=html.replace(old,new,1)

start=html.index('function renderRetirementSimulation(')
end=html.index('\nfunction renderWealthSplit(',start)
old_render=html[start:end]
new_render='''function renderRetirementSimulation(retirementTotal=0,previousRetirementTotal=null){let value=retirementSimulationAuto?Math.max(0,Number(retirementTotal)||0):retirementSimulationCapital,previousValue=retirementSimulationAuto&&previousRetirementTotal!==null?Math.max(0,Number(previousRetirementTotal)||0):null,years=retirementSimulationYears>0?retirementSimulationYears:0;let future=years?value*Math.pow(1.006,years*12):null,conservative=years?retirementScenarioValue(value,years,.06):null,moderate=years?retirementScenarioValue(value,years,.08):null,optimistic=years?retirementScenarioValue(value,years,.1066):null,conservativeIncome=conservative===null?null:conservative*.008,moderateIncome=moderate===null?null:moderate*.008,optimisticIncome=optimistic===null?null:optimistic*.008,previousConservative=years&&previousValue!==null?retirementScenarioValue(previousValue,years,.06):null,previousModerate=years&&previousValue!==null?retirementScenarioValue(previousValue,years,.08):null,previousOptimistic=years&&previousValue!==null?retirementScenarioValue(previousValue,years,.1066):null,previousConservativeIncome=previousConservative===null?null:previousConservative*.008,previousModerateIncome=previousModerate===null?null:previousModerate*.008,previousOptimisticIncome=previousOptimistic===null?null:previousOptimistic*.008;el.retirementSimulationCapitalValue.textContent=brl(value);el.retirementSimulationFutureValue.textContent=future===null?"—":brl(future);el.retirementSimulationConservativeValue.textContent=conservative===null?"—":brl(conservative);el.retirementSimulationModerateValue.textContent=moderate===null?"—":brl(moderate);el.retirementSimulationOptimisticValue.textContent=optimistic===null?"—":brl(optimistic);el.retirementSimulationConservativeIncome.textContent=conservativeIncome===null?"—":brl(conservativeIncome);el.retirementSimulationModerateIncome.textContent=moderateIncome===null?"—":brl(moderateIncome);el.retirementSimulationOptimisticIncome.textContent=optimisticIncome===null?"—":brl(optimisticIncome);[["Conservative",conservativeIncome,previousConservativeIncome],["Moderate",moderateIncome,previousModerateIncome],["Optimistic",optimisticIncome,previousOptimisticIncome]].forEach(([name,currentIncome,previousIncome])=>{let row=$("#retirementSimulation"+name+"Previous"),previousEl=$("#retirementSimulation"+name+"PreviousIncome"),changeEl=$("#retirementSimulation"+name+"PreviousChange"),show=retirementSimulationAuto&&currentIncome!==null&&previousIncome!==null;if(!row||!previousEl||!changeEl)return;row.classList.toggle("hidden",!show);if(!show){previousEl.textContent="—";changeEl.textContent="";changeEl.className="retirement-simulation-previous-change";return}previousEl.textContent=brl(previousIncome);let change=previousIncome>0?(currentIncome/previousIncome-1)*100:null;changeEl.textContent=change===null?"":` · ${signedPct(change)}`;changeEl.className="retirement-simulation-previous-change "+(change===null?"":changeClass(change))});el.retirementSimulationAuto.checked=retirementSimulationAuto;el.retirementSimulationYears.value=retirementSimulationYears||"";let boost=$("#retirementSimulationBoost"),boostField=$("#retirementSimulationBoostField"),monthlyInput=$("#retirementSimulationMonthlyContribution");boost.checked=retirementSimulationBoost;boost.setAttribute("aria-expanded",String(retirementSimulationBoost));boostField.classList.toggle("hidden",!retirementSimulationBoost);if(document.activeElement!==monthlyInput)monthlyInput.value=retirementSimulationMonthlyContribution?String(retirementSimulationMonthlyContribution).replace(".",","):"";$("#editRetirementSimulationCapital").disabled=retirementSimulationAuto;$("#editRetirementSimulationCapital").setAttribute("aria-disabled",String(retirementSimulationAuto))}'''
html=html[:start]+new_render+html[end:]

start=html.index('function renderWealthSplit(')
end=html.index('\nfunction openRetirementSimulationCapitalSheet',start)
old_wealth=html[start:end]
new_wealth='''function renderWealthSplit(last){let hasBaseCategory=categories.includes(RETIREMENT_CATEGORY),base=hasBaseCategory?catValue(last,RETIREMENT_CATEGORY):0,cdb=Math.max(0,Number(last?.retirementCdb)||0),retirement=base+cdb,myMoney=last.total-retirement,combined=retirement+myMoney,mismatch=Math.abs(combined-last.total)>.01,history=ordered(),previous=history.length>1?history.at(-2):null,previousBase=previous&&hasBaseCategory?catValue(previous,RETIREMENT_CATEGORY):0,previousCdb=previous?Math.max(0,Number(previous.retirementCdb)||0):0,previousRetirement=previous?previousBase+previousCdb:null;el.retirementBaseLabel.textContent=hasBaseCategory?RETIREMENT_CATEGORY:"Investimentos de aposentadoria";el.retirementBase.textContent=brl(base);el.retirementCdbValue.textContent=brl(cdb);el.retirementValue.textContent=brl(retirement);el.myMoneyValue.textContent=brl(myMoney);el.wealthSplitTotal.textContent=brl(combined);el.wealthSplitWarning.classList.toggle("hidden",!mismatch);renderRetirementSimulation(retirement,previousRetirement)}'''
html=html[:start]+new_wealth+html[end:]

html=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=37',html)
idx.write_text(html,encoding='utf-8')

sw=Path('sw.js')
s=sw.read_text(encoding='utf-8')
s=re.sub(r"meu-patrimonio-pwa-v\d+","meu-patrimonio-pwa-v37",s,count=1)
sw.write_text(s,encoding='utf-8')
