from pathlib import Path
import re

index=Path("index.html")
s=index.read_text(encoding="utf-8")
old='''    <label class="td-real-field" for="tdReal2033Input"><span>TD 2033</span><small>Rendimento real</small><input id="tdReal2033Input" type="text" inputmode="decimal" placeholder="R$ 0,00" autocomplete="off"></label>'''
new='''    <article class="td-real-field td-real-field--auto"><span>TD 2033</span><small>Valor líquido teórico</small><strong class="td-real-output" id="tdReal2033Value" aria-live="polite">Calculando...</strong><p class="td-real-meta" id="tdReal2033Details">13,27% a.a. · IR 15% · B3 estimada</p><p class="td-real-note">Considera os cupons semestrais já pagos, sem reinvestimento. Não é o valor de venda.</p></article>'''
if old not in s: raise SystemExit("Current TD 2033 manual card not found")
s=s.replace(old,new,1)
s=s.replace('O TD 2029 é calculado automaticamente. O TD 2033 continua com preenchimento manual.','Valores líquidos teóricos pela rentabilidade contratada, sem oscilação de mercado.',1)
s=s.replace('<button id="saveTdRealValues" class="btn primary td-real-save" type="button">Salvar TD 2033</button>','',1)

anchor='function renderTdRealInputs(){let input2033=$("#tdReal2033Input");if(input2033&&document.activeElement!==input2033)input2033.value=tdReal2033?tdReal2033.toFixed(2).replace(".",","):"";renderTdReal2029()}\nasync function saveTdRealValues(){let input2033=$("#tdReal2033Input");tdReal2033=Math.max(0,parse(input2033?.value||"0")||0);saveTdRealLocal();renderTdRealInputs();await syncCloudNow();toast("Valor do TD 2033 atualizado.")}'
if anchor not in s: raise SystemExit("TD 2033 manual render/save functions not found")

newcalc=r'''// TD 2033: Tesouro Prefixado com Juros Semestrais (NTN-F).
// Returns the present theoretical position, not previously withdrawn coupons.
const TD2033_QUANTITY=55.70,TD2033_PRICE=843.83,TD2033_RATE=.1327,
      TD2033_BUY_MS=Date.UTC(2023,1,15),TD2033_MATURITY_MS=Date.UTC(2033,0,1),
      TD2033_FACE=1000,TD2033_COUPON=TD2033_FACE*(Math.sqrt(1.10)-1),
      TD2033_B3_ANCHOR_MS=Date.UTC(2026,10,17),TD2033_B3_ANCHOR_VALUE=35.94,
      TD2033_DAY=86400000;
function td2033Easter(year){let a=year%19,b=Math.floor(year/100),c=year%100,d=Math.floor(b/4),e=b%4,f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),h=(19*a+b-d-g+15)%30,i=Math.floor(c/4),k=c%4,l=(32+2*e+2*i-h-k+7)%7,m=Math.floor((a+11*h+22*l)/451),month=Math.floor((h+l-7*m+114)/31)-1,day=(h+l-7*m+114)%31+1;return Date.UTC(year,month,day)}
function td2033BusinessDay(time){let d=new Date(time),dow=d.getUTCDay(),month=d.getUTCMonth()+1,day=d.getUTCDate(),year=d.getUTCFullYear();if(dow===0||dow===6)return false;
if(["1-1","4-21","5-1","9-7","10-12","11-2","11-15","11-20","12-25"].includes(month+"-"+day))return false;
let easter=td2033Easter(year);
if(time===easter-48*TD2033_DAY||time===easter-47*TD2033_DAY||time===easter-2*TD2033_DAY||time===easter+60*TD2033_DAY)return false;
return true}
function td2033NextBusinessDay(time){while(!td2033BusinessDay(time))time+=TD2033_DAY;return time}
function td2033BusinessDays(from,to){if(to<=from)return 0;let count=0;for(let day=from+TD2033_DAY;day<=to;day+=TD2033_DAY)if(td2033BusinessDay(day))count++;return count}
function td2033Coupons(){let coupons=[];for(let year=2023;year<=2033;year++)for(let month of [0,6]){let nominal=Date.UTC(year,month,1);if(nominal>TD2033_MATURITY_MS)continue;let payment=td2033NextBusinessDay(nominal);if(payment>TD2033_BUY_MS)coupons.push(payment)}return coupons.sort((a,b)=>a-b)}
const TD2033_COUPON_DATES=td2033Coupons(),TD2033_INITIAL=TD2033_QUANTITY*TD2033_PRICE;
function td2033PriceAt(time){let t=Math.max(TD2033_BUY_MS,Math.min(time,td2033NextBusinessDay(TD2033_MATURITY_MS)));
let value=TD2033_PRICE*Math.pow(1+TD2033_RATE,td2033BusinessDays(TD2033_BUY_MS,t)/252);
for(let couponTime of TD2033_COUPON_DATES)if(couponTime<=t){let coupon=TD2033_COUPON+(couponTime===TD2033_COUPON_DATES.at(-1)?TD2033_FACE:0);value-=coupon*Math.pow(1+TD2033_RATE,td2033BusinessDays(couponTime,t)/252)}
return Math.max(0,value)}
function td2033B3Fee(time){let fee=TD2033_B3_ANCHOR_VALUE,anchor=TD2033_B3_ANCHOR_MS,t=Math.max(anchor,time),end=Math.min(t,td2033NextBusinessDay(TD2033_MATURITY_MS));for(let day=anchor+TD2033_DAY;day<=end;day+=TD2033_DAY){if(TD2033_COUPON_DATES.includes(day))fee=0;else fee+=td2033PriceAt(day)*TD2033_QUANTITY*.002/365}return Math.max(0,fee)}
function td2033Theory(time=td2029BrazilToday()){let t=Math.max(TD2033_BUY_MS,Math.min(time,td2033NextBusinessDay(TD2033_MATURITY_MS))),days=Math.floor((t-TD2033_BUY_MS)/TD2033_DAY),gross=td2033PriceAt(t)*TD2033_QUANTITY,rate=days<=180?.225:days<=360?.20:days<=720?.175:.15,tax=Math.max(0,gross-TD2033_INITIAL)*rate,b3=td2033B3Fee(t);return{gross,net:Math.max(0,gross-tax-b3),tax,b3,days,rate,coupon:TD2033_COUPON*TD2033_QUANTITY,couponsPaid:TD2033_COUPON_DATES.filter(d=>d<=t).length}}
function renderTdReal2033(){let value=$("#tdReal2033Value"),details=$("#tdReal2033Details");if(!value||!details)return;let calc=td2033Theory();value.textContent=brl(calc.net);details.textContent="13,27% a.a. · "+calc.days+" dias · IR "+pct(calc.rate*100)+" · B3 "+brl(calc.b3)+" (estimada) · "+calc.couponsPaid+" cupons pagos"}
function renderTdRealInputs(){renderTdReal2029();renderTdReal2033()}
'''
s=s.replace(anchor,newcalc,1)
listener='$("#saveTdRealValues").onclick=saveTdRealValues;$("#tdReal2033Input").addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();saveTdRealValues()}});'
if listener not in s: raise SystemExit("TD2033 listener not found")
s=s.replace(listener,"",1)
s=re.sub(r'\./sw\.js\?v=\d+','./sw.js?v=41',s)
index.write_text(s,encoding="utf-8")
swfile=Path("sw.js")
sw=swfile.read_text(encoding="utf-8")
sw=re.sub(r"meu-patrimonio-pwa-v\d+","meu-patrimonio-pwa-v41",sw,count=1)
swfile.write_text(sw,encoding="utf-8")
