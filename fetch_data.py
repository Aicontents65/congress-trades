import os
import json
import requests
from datetime import datetime

API_KEY = os.environ.get("FINNHUB_API_KEY", "")

# چند سناتور معروف برای تست
symbols_to_check = ["AAPL", "MSFT", "TSLA", "NVDA", "AMZN", "GOOGL", "META"]

trades = []

for sym in symbols_to_check:
    url = f"https://finnhub.io/api/v1/stock/congressional-trading?symbol={sym}&token={API_KEY}"
    try:
        r = requests.get(url, timeout=15)
        data = r.json()
        for item in data.get("data", []):
            trades.append({
                "name": item.get("name", "-"),
                "symbol": item.get("symbol", sym),
                "transaction": item.get("transactionType", "-"),
                "amount": item.get("amount", "-"),
                "date": item.get("transactionDate", "-")
            })
    except Exception as e:
        print(f"error for {sym}: {e}")

# مرتب‌سازی بر اساس تاریخ (جدیدترین اول)
trades.sort(key=lambda x: x.get("date", ""), reverse=True)

output = {
    "updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    "count": len(trades),
    "trades": trades
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Saved {len(trades)} trades")
