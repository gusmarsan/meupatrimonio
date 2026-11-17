#!/usr/bin/env python3
"""Refresh official IPCA monthly rates for the TD 2029 theoretical calculation."""
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DEST = Path("ipca-data.json")
BASE = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados"
today = datetime.now(timezone.utc).strftime("%d/%m/%Y")
url = BASE + "?" + urllib.parse.urlencode({
    "formato": "json",
    "dataInicial": "01/01/2025",
    "dataFinal": today
})
request = urllib.request.Request(url, headers={
    "Accept": "application/json",
    "User-Agent": "MeuPatrimonio-IPCA-updater/1.0"
})
with urllib.request.urlopen(request, timeout=35) as response:
    rows = json.load(response)
if not isinstance(rows, list):
    raise ValueError("Banco Central did not return a list")
months = {}
for row in rows:
    d = datetime.strptime(row["data"], "%d/%m/%Y")
    key = d.strftime("%Y-%m")
    rate = float(str(row["valor"]).replace(",", "."))
    if key >= "2025-01" and -30 < rate < 30:
        months[key] = rate
if len(months) < 20 or "2025-01" not in months:
    raise ValueError("Official IPCA series is incomplete; not replacing existing data")
existing = json.loads(DEST.read_text("utf-8")) if DEST.exists() else {}
old_months = existing.get("months", {})
if old_months and max(months) < max(old_months):
    raise ValueError("Official IPCA series is older than the current data")
if months == old_months:
    print("IPCA unchanged; no commit needed")
else:
    payload = {
        "source": "Banco Central do Brasil — SGS 433 (IPCA mensal, %)",
        "months": dict(sorted(months.items()))
    }
    DEST.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated official IPCA through " + max(months))
