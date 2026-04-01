import requests
from typing import List, Dict, Any

from config import POLYMARKET_API_BASE, MAX_MARKETS


def fetch_markets() -> List[Dict[str, Any]]:
    url = f"{POLYMARKET_API_BASE}/markets"
    params = {
        "closed": "false",
        "limit": MAX_MARKETS
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    if isinstance(data, list):
        return data

    if isinstance(data, dict) and "markets" in data:
        return data["markets"]

    return []