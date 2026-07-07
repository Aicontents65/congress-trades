import json
import os
import requests
from datetime import datetime, timedelta

API_KEY = os.environ.get("FINNHUB_API_KEY", "")

# لیست سهام‌های معروف که معمولاً نماینده‌ها معامله می‌کنن
symbols = ["AAPL", "MSFT", "NVDA", "TSLA", "AMZN", "GOOGL", "META",
           "JPM", "BAC", "XOM", "PFE", "DIS", "NFLX", "AMD", "INTC"]

trades = []

# بازه‌ی زمانی: یک سال اخیر
to_date = datetime.utcnow().strftime("%Y-%m-%d")
from_date = (datetime.utcnow() - timedelta(days=365)).strftime("%Y-%m-%d")

for sym in symbols:
    url = f"https://finnhub.io/api/v1/stock/congressional-trading?symbol={sym}&from={from_date}&to={to_date}&token={API_KEY}"
    try:
        r = requests.get(url, timeout=30)
        print(f"{sym}: status {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            for item in data.get("data", []):
                trades.append({
                    "name": item.get("name", "-"),
                    "symbol": sym,
                    "transaction": item.get("transactionType", "-"),
                    "amount": item.get("amountFrom", "-"),
                    "date": item.get("transactionDate", "-")
                })
        else:
            print("  body:", r.text[:150])
    except Exception as e:
        print(f"  error {sym}: {repr(e)}")

trades.sort(key=lambda x: x.get("date", ""), reverse=True)

output = {
    "updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    "count": len(trades),
    "trades": trades
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Saved {len(trades)} trades")
