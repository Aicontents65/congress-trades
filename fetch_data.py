import json
import requests

URL = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json"

def main():
    r = requests.get(URL, timeout=60)
    print("status:", r.status_code)
    r.raise_for_status()
    raw = r.json()

    # جدیدترین‌ها اول
    raw.sort(key=lambda t: t.get("transaction_date", ""), reverse=True)

    trades = []
    for t in raw[:200]:  # ۲۰۰ معامله‌ی آخر
        trades.append({
            "symbol": t.get("ticker", ""),
            "name": t.get("senator", ""),
            "transactionType": t.get("type", ""),
            "transactionDate": t.get("transaction_date", ""),
            "amount": t.get("amount", ""),
            "assetName": t.get("asset_description", ""),
            "link": t.get("ptr_link", ""),
        })

    with open("data.json", "w") as f:
        json.dump(trades, f, indent=2)

    print(f"Saved {len(trades)} trades")

if __name__ == "__main__":
    main()
