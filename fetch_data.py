import json

trades = [
    {"symbol": "AAPL", "name": "Nancy Pelosi", "transactionType": "buy",
     "transactionDate": "2024-01-15", "amount": "$1M-$5M", "assetName": "Apple Inc"},
    {"symbol": "NVDA", "name": "Nancy Pelosi", "transactionType": "buy",
     "transactionDate": "2024-01-10", "amount": "$1M-$5M", "assetName": "NVIDIA Corp"},
    {"symbol": "MSFT", "name": "Tommy Tuberville", "transactionType": "sell",
     "transactionDate": "2024-01-05", "amount": "$15K-$50K", "assetName": "Microsoft"},
    {"symbol": "TSLA", "name": "Ro Khanna", "transactionType": "buy",
     "transactionDate": "2024-01-03", "amount": "$1K-$15K", "assetName": "Tesla Inc"},
    {"symbol": "GOOGL", "name": "Josh Gottheimer", "transactionType": "buy",
     "transactionDate": "2024-01-02", "amount": "$50K-$100K", "assetName": "Alphabet Inc"},
]

with open("data.json", "w") as f:
    json.dump(trades, f, indent=2)

print(f"Saved {len(trades)} trades")
