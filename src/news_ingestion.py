import feedparser
from typing import List, Dict, Any

from config import NEWS_FEEDS
from src.utils import get_utc_timestamp


def fetch_news() -> List[Dict[str, Any]]:
    all_items = []

    for feed_url in NEWS_FEEDS:
        parsed = feedparser.parse(feed_url)

        for entry in parsed.entries:
            item = {
                "source_feed": feed_url,
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "collected_at_utc": get_utc_timestamp()
            }
            all_items.append(item)

    return all_items