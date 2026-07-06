import json
import requests
from datetime import datetime

url = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"

trades = []

try:
    r = requests.get(url, timeout=60)
    print("STATUS CODE:", r.status_code)
    print("FIRST 300 CHARS:", r.text[:300])
    
    data = r.json()
    print("TYPE OF DATA:", type(data))
    print("LENGTH:", len(data) if hasattr(data, "__len__") else "?")

    for item in data:
        trades.append({
            "name": item.get("representative", "-"),
            "symbol": item.get("ticker", "-"),
            "transaction": item.get("type", "-"),
            "amount": item.get("amount", "-"),
            "date": item.get("transaction_date", "-")
        })
except Exception as e:
    print("ERROR:", repr(e))

trades.sort(key=lambda x: x.get("date", ""), reverse=True)
trades = trades[:500]

output = {
    "updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    "count": len(trades),
    "trades": trades
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Saved {len(trades)} trades")
