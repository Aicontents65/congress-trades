import json
import requests

URL = "https://housestockwatcher.com/data/all_transactions.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

def main():
    r = requests.get(URL, headers=HEADERS, timeout=60)
    print("status:", r.status_code)
    print("body (first 300):", r.text[:300])
    r.raise_for_status()
    raw = r.json()

    raw.sort(key=lambda t: t.get("transaction_date", ""), reverse=True)

    trades = []
    for t in raw[:200]:
        trades.append({
            "symbol": t.get("ticker", ""),
            "name": t.get("representative", t.get("senator", "")),
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
