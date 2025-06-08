import requests
import pandas as pd
import os
from datetime import datetime, timedelta

# Your Finnhub API key
API_KEY = "api_key"

# Output directory
os.makedirs("scraping_finance/data", exist_ok=True)

# Time range (e.g., past 7 days)
today = datetime.utcnow().date()
last_week = today - timedelta(days=7)

# Tickers to fetch news for
tickers = ["AAPL", "MSFT", "AMZN"]

all_news = []

for ticker in tickers:
    print(f"📡 Fetching news for {ticker}")
    url = f"https://finnhub.io/api/v1/company-news?symbol={ticker}&from={last_week}&to={today}&token={API_KEY}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f" Error fetching {ticker}: {response.status_code}")
        continue
    
    articles = response.json()
    for article in articles:
        all_news.append({
            "ticker": ticker,
            "datetime": datetime.utcfromtimestamp(article.get("datetime", 0)).isoformat(),
            "headline": article.get("headline"),
            "summary": article.get("summary"),
            "source": article.get("source"),
            "url": article.get("url")
        })

# Save to CSV
df = pd.DataFrame(all_news)
timestamp = datetime.now().strftime("%Y%m%d")
csv_path = f"scraping_finance/data/finnhub_news_{timestamp}.csv"
df.to_csv(csv_path, index=False)
print(f"Saved {len(df)} articles to {csv_path}")
