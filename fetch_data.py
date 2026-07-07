import json
import requests
from datetime import datetime

# چند منبع پشتیبان امتحان می‌کنیم
urls = [
    "https://raw.githubusercontent.com/timothycarambat/house-stock-watcher-data/main/data/all_transactions.json",
    "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json",
]

trades = []
data = None

for url in urls:
    try:
        print("Trying:", url)
        r = requests.get(url, timeout=60)
        print("STATUS CODE:", r.status_code)
        if r.status_code == 200:
            data = r.json()
            print("SUCCESS! LENGTH:", len(data))
            break
    except Exception as e:
        print("ERROR:", repr(e))

if data:
    for item in data:
        trades.append({
            "name": item.get("representative", item.get("senator", "-")),
            "symbol": item.get("ticker", "-"),
            "transaction": item.get("type", "-"),
            "amount": item.get("amount", "-"),
            "date": item.get("transaction_date", "-")
        })

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
