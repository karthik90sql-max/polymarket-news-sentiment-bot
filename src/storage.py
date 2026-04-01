import csv
import json
import os
from typing import Any, List, Dict

from config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from src.utils import safe_filename_timestamp


def ensure_directories() -> None:
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)


def save_raw_json(data: Any, prefix: str) -> str:
    ensure_directories()
    file_path = os.path.join(RAW_DATA_DIR, f"{prefix}_{safe_filename_timestamp()}.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    return file_path


def save_processed_news_csv(news_items: List[Dict[str, Any]]) -> str:
    """
    Save scored news items to CSV.
    """
    ensure_directories()
    file_path = os.path.join(PROCESSED_DATA_DIR, f"scored_news_{safe_filename_timestamp()}.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "source_feed",
            "title",
            "summary",
            "published",
            "collected_at_utc",
            "combined_text",
            "sentiment_score",
            "sentiment_label",
            "positive_hits",
            "negative_hits",
            "link"
        ])

        for item in news_items:
            writer.writerow([
                item.get("source_feed", ""),
                item.get("title", ""),
                item.get("summary", ""),
                item.get("published", ""),
                item.get("collected_at_utc", ""),
                item.get("combined_text", ""),
                item.get("sentiment_score", 0),
                item.get("sentiment_label", ""),
                item.get("positive_hits", 0),
                item.get("negative_hits", 0),
                item.get("link", ""),
            ])

    return file_path