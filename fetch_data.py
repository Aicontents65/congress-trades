import json
import requests

# دیتای معاملات مجلس نمایندگان از مخزن GitHub (همیشه فعال)
URL = "https://raw.githubusercontent.com/timothycarambat/house-stock-watcher-data/main/data/all_transactions.json"

def main():
    r = requests.get(URL, timeout=60)
    print("status:", r.status_code)
    print("body (first 200):", r.text[:200])
    r.raise_for_status()
    raw = r.json()

    raw.sort(key=lambda t: t.get("transaction_date", ""), reverse=True)

    trades = []
    for t in raw[:200]:
        trades.append({
            "symbol": t.get("ticker", ""),
            "name": t.get("representative", ""),
            "transactionType": t.get("type", ""),
            "transactionDate": t.get("transaction_date", ""),
            "amount": t.get("amount", ""),
            "assetName": t.get("asset_description", ""),
        })

    with open("data.json", "w") as f:
        json.dump(trades, f, indent=2)

    print(f"Saved {len(trades)} trades")

if __name__ == "__main__":
    main()
