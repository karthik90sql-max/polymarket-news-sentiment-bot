from src.news_ingestion import fetch_news
from src.market_ingestion import fetch_markets
from src.sentiment import score_news_item
from src.storage import save_raw_json, save_processed_news_csv


def main() -> None:
    print("Fetching news...")
    news_items = fetch_news()
    print(f"Fetched {len(news_items)} news items.")

    print("Scoring news sentiment...")
    scored_news = [score_news_item(item) for item in news_items]
    print(f"Scored {len(scored_news)} news items.")

    print("Fetching Polymarket markets...")
    markets = fetch_markets()
    print(f"Fetched {len(markets)} markets.")

    news_file = save_raw_json(news_items, "news")
    markets_file = save_raw_json(markets, "markets")
    scored_news_file = save_processed_news_csv(scored_news)

    print(f"Saved raw news data to: {news_file}")
    print(f"Saved raw market data to: {markets_file}")
    print(f"Saved scored news data to: {scored_news_file}")

    print("\nSample scored headlines:")
    for item in scored_news[:5]:
        print("-" * 80)
        print(f"Title: {item.get('title', '')}")
        print(f"Sentiment: {item.get('sentiment_label', '')}")
        print(f"Score: {item.get('sentiment_score', 0)}")
        print(f"Positive hits: {item.get('positive_hits', 0)}")
        print(f"Negative hits: {item.get('negative_hits', 0)}")

    print("\nSample markets:")
    for market in markets[:5]:
        print("-" * 80)
        print(market.get("question") or market.get("title"))


if __name__ == "__main__":
    main()