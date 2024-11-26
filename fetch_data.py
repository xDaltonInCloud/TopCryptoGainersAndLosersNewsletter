import requests
import logging

def fetch_coins(order):
    """Fetch coins based on the specified order."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": order,
        "per_page": 250,
        "page": 1,
        "sparkline": False
    }
    headers = {"x-cg-demo-api-key": "YOUR_DEMO_API_KEY"}  # Replace with your CoinGecko API key

    all_data = []
    for page in range(1, 6):  # Fetch up to 5 pages
        params["page"] = page
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        all_data.extend(response.json())

    return all_data

def get_gainers_losers_by_market_cap():
    """Fetch categorized market cap data."""
    low_cap_data = fetch_coins("market_cap_asc")
    all_data = fetch_coins("market_cap_desc")

    # Categorize by market cap
    low_cap = [coin for coin in low_cap_data if coin.get("market_cap") is not None and coin["market_cap"] <= 25_000_000]
    medium_cap = [coin for coin in all_data if coin.get("market_cap") is not None and 25_000_000 < coin["market_cap"] <= 1_000_000_000]
    large_cap = [coin for coin in all_data if coin.get("market_cap") is not None and coin["market_cap"] > 1_000_000_000]

    # Sort gainers and losers
    def sort_gainers_losers(coins):
        gainers = sorted(coins, key=lambda x: x.get("price_change_percentage_24h", 0), reverse=True)[:3]
        losers = sorted(coins, key=lambda x: x.get("price_change_percentage_24h", 0))[:3]
        return gainers, losers

    return {
        "low_cap": sort_gainers_losers(low_cap),
        "medium_cap": sort_gainers_losers(medium_cap),
        "large_cap": sort_gainers_losers(large_cap),
    }
