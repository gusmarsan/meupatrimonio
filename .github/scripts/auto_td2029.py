from pathlib import Path
import re

index=Path('index.html')
s=index.read_text(encoding='utf-8')

old='''    <label class="td-real-field" for="tdReal2029Input"><span>TD 2029</span><small>Rendimento real</small><input id="tdReal2029Input" type="text" inputmode="decimal" placeholder="R$ 0,00" autocomplete="off"></label>
    <label class="td-real-field" for="tdReal2033Input"><span>TD 2033</span><small>Rendimento real</small><input id="tdReal2033Input" type="text" inputmode="decimal" placeholder="R$ 0,00" autocomplete="off"></label>'''
new='''    <article class="td-real-field td-real-field--auto"><span>TD 2029</span><small>Valor líquido teórico</small><strong class="td-real-output" id="tdReal2029Value" aria-live="polite">Calculando...</strong><p class="td-real-meta" id="tdReal2029Details">Buscando IPCA oficial...</p><p class="td-real-note">Estimativa pela taxa contratada, sem marcação a mercado. Não é o valor de venda.</p></article>
    <label class="td-real-field" for="tdReal2033Input"><span>TD 2033</span><small>Rendimento real</small><input id="tdReal2033Input" type="text" inputmode="decimal" placeholder="R$ 0,00" autocomplete="off"></label>'''
if old not in s: raise SystemExit('TD cards anchor not found')
s=s.replace(old,new,1)
s=s.replace('Informe os valores atuais. Depois, o cálculo poderá ser atualizado automaticamente.','O TD 2029 é calculado automaticamente. O TD 2033 continua com preenchimento manual.',1)
s=s.replace('<button id="saveTdRealValues" class="btn primary td-real-save" type="button">Salvar valores</button>','<button id="saveTdRealValues" class="btn primary td-real-save" type="button">Salvar TD 2033</button>',1)

style='''<style id="td-2029-auto-v1">
.td-real-field--auto{align-content:start}
.td-real-output{display:block;align-self:center;margin:8px 0 3px;color:var(--txt);font-size:clamp(1.35rem,2.2vw,1.85rem);font-weight:680;letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.td-real-meta{margin:0;color:var(--mut);font-size:.67rem;line-height:1.45}
.td-real-note{margin:4px 0 0;color:var(--mut);font-size:.62rem;line-height:1.45}
@media(max-width:760px){.td-real-output{font-size:1.4rem}}
</style>\n'''
if 'id="td-2029-auto-v1"' not in s:
    s=s.replace('</head>',style+'</head>',1)

start=s.index('function renderTdRealInputs(){')
end=s.index('function renderProjections(){',start)
helper='''const TD2029_INITIAL=24985.45,TD2029_RATE=.0778,TD2029_ANCHOR_FEE=101.86,TD2029_ANCHOR_DAYS=666,TD2029_START_MS=Date.UTC(2025,0,20),TD2029_MATURITY_MS=Date.UTC(2029,4,15);
let td2029Ipca=null,td2029Refreshing=false,td2029RefreshAt=0;
function td2029BrazilToday(){let parts=new Intl.DateTimeFormat("en-US",{timeZone:"America/Sao_Paulo",year:"numeric",month:"2-digit",day:"2-digit"}).formatToParts(new Date()),values={};parts.forEach(part=>values[part.type]=part.value);return Date.UTC(Number(values.year),Number(values.month)-1,Number(values.day))}
function td2029Series(payload){let months={};if(Array.isArray(payload)){payload.forEach(item=>{let parts=String(item.data||"").split("/");if(parts.length!==3)return;let key=parts[2]+"-"+parts[1],number=Number(String(item.valor).replace(",","."));if(/^20\\d{2}-(0[1-9]|1[0-2])$/.test(key)&&Number.isFinite(number)&&Math.abs(number)<30)months[key]=number})}else if(payload&&typeof payload==="object"&&payload.months){Object.entries(payload.months).forEach(([key,value])=>{let number=Number(value);if(/^20\\d{2}-(0[1-9]|1[0-2])$/.test(key)&&Number.isFinite(number)&&Math.abs(number)<30)months[key]=number})}let keys=Object.keys(months).filter(key=>key>="2025-01").sort();if(keys.length<20||!keys.includes("2025-01"))return null;return{months,latest:keys.at(-1)}}
function td2029Theory(todayMs=td2029BrazilToday()){if(!td2029Ipca)return null;let targetMs=Math.min(Math.max(todayMs,TD2029_START_MS),TD2029_MATURITY_MS),days=Math.floor((targetMs-TD2029_START_MS)/86400000),cutoff=new Date(targetMs).toISOString().slice(0,7),factor=1,latest="";Object.keys(td2029Ipca.months).sort().forEach(month=>{if(month>="2025-01"&&month<=cutoff){factor*=1+td2029Ipca.months[month]/100;latest=month}});if(!latest)return null;let gross=TD2029_INITIAL*factor*Math.pow(1+TD2029_RATE,days/365),taxRate=days<=180?.225:days<=360?.20:days<=720?.175:.15,tax=Math.max(0,gross-TD2029_INITIAL)*taxRate,custody=TD2029_ANCHOR_FEE+Math.max(0,days-TD2029_ANCHOR_DAYS)*gross*.002/365;return{net:gross-tax-custody,gross,tax,custody,days,taxRate,ipcaLatest:latest}}
function renderTdReal2029(){let value=$("#tdReal2029Value"),info=$("#tdReal2029Details");if(!value||!info)return;let calc=td2029Theory();if(!calc){value.textContent="—";info.textContent="IPCA ainda não disponível para calcular.";return}value.textContent=brl(calc.net);info.textContent="IPCA até "+mshort(calc.ipcaLatest)+" · "+calc.days+" dias · IR "+pct(calc.taxRate*100)+" · B3 "+brl(calc.custody)+" (estimada)"}
function renderTdRealInputs(){let input2033=$("#tdReal2033Input");if(input2033&&document.activeElement!==input2033)input2033.value=tdReal2033?tdReal2033.toFixed(2).replace(".",","):"";renderTdReal2029()}
async function saveTdRealValues(){let input2033=$("#tdReal2033Input");tdReal2033=Math.max(0,parse(input2033?.value||"0")||0);saveTdRealLocal();renderTdRealInputs();await syncCloudNow();toast("Valor do TD 2033 atualizado.")}
async function refreshTd2029(){if(td2029Refreshing)return;td2029Refreshing=true;td2029RefreshAt=Date.now();try{try{let cached=localStorage.getItem("patrimonio-ipca-sgs433-cache"),series=cached?td2029Series(JSON.parse(cached)):null;if(series){td2029Ipca=series;renderTdReal2029()}}catch(e){console.warn("IPCA local indisponível",e)}try{let fallback=await fetch("./ipca-data.json",{cache:"no-store"});if(fallback.ok){let series=td2029Series(await fallback.json());if(series&&(!td2029Ipca||series.latest>=td2029Ipca.latest)){td2029Ipca=series;renderTdReal2029();localStorage.setItem("patrimonio-ipca-sgs433-cache",JSON.stringify({months:series.months}))}}}catch(e){console.warn("IPCA de referência indisponível",e)}try{let url="https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2025&dataFinal="+new Intl.DateTimeFormat("pt-BR",{timeZone:"America/Sao_Paulo",day:"2-digit",month:"2-digit",year:"numeric"}).format(new Date());let response=await fetch(url,{cache:"no-store",signal:AbortSignal.timeout(7000)});if(!response.ok)throw Error("BCB HTTP "+response.status);let series=td2029Series(await response.json());if(series&&(!td2029Ipca||series.latest>=td2029Ipca.latest)){td2029Ipca=series;renderTdReal2029();localStorage.setItem("patrimonio-ipca-sgs433-cache",JSON.stringify({months:series.months}))}}catch(e){console.warn("Consulta direta ao IPCA não disponível; usando a série de referência.",e)}}finally{td2029Refreshing=false;renderTdReal2029()}}
'''
s=s[:start]+helper+s[end:]

s=s.replace('["#tdReal2029Input","#tdReal2033Input"].forEach(selector=>$(selector).addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();saveTdRealValues()}}));','$("#tdReal2033Input").addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();saveTdRealValues()}});',1)

before='async function initializeLocalApp(){'
after='''addEventListener("focus",()=>{renderTdReal2029();if(Date.now()-td2029RefreshAt>60000)refreshTd2029()});document.addEventListener("visibilitychange",()=>{if(!document.hidden){renderTdReal2029();if(Date.now()-td2029RefreshAt>60000)refreshTd2029()}});
async function initializeLocalApp(){'''
if before not in s: raise SystemExit('initializeLocalApp not found')
s=s.replace(before,after,1)
old_init='renderAll();renderReview();appInitialized=true}'
new_init='renderAll();renderReview();appInitialized=true;refreshTd2029()}'
if old_init not in s: raise SystemExit('init closing anchor not found')
s=s.replace(old_init,new_init,1)

s=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=40',s)
index.write_text(s,encoding='utf-8')

swfile=Path('sw.js')
sw=swfile.read_text(encoding='utf-8')
sw=re.sub(r'meu-patrimonio-pwa-v\d+','meu-patrimonio-pwa-v40',sw,count=1)
old_sw="  if (url.origin !== self.location.origin) return;\n\n  if (event.request.mode === 'navigate') {"
new_sw="""  if (url.origin !== self.location.origin) return;

  // IPCA must be network-first so the daily official index update is visible.
  if (url.pathname.endsWith('/ipca-data.json')) {
    event.respondWith((async () => {
      try {
        const response = await fetch(event.request, { cache: 'no-store' });
        if (response.ok) {
          const store = await caches.open(CACHE_NAME);
          await store.put('./ipca-data.json', response.clone());
        }
        return response;
      } catch (error) {
        const cached = await caches.match('./ipca-data.json');
        if (cached) return cached;
        throw error;
      }
    })());
    return;
  }

  if (event.request.mode === 'navigate') {"""
if old_sw not in sw: raise SystemExit('sw fetch route anchor not found')
sw=sw.replace(old_sw,new_sw,1)
sw=sw.replace("  './icon.svg?v=3'","  './icon.svg?v=3',\n  './ipca-data.json'",1)
swfile.write_text(sw,encoding='utf-8')
