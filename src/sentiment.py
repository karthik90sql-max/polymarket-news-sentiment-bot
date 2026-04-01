from typing import Dict, Any

from src.text_cleaner import combine_title_and_summary


POSITIVE_WORDS = {
    "gain", "gains", "rise", "rises", "up", "surge", "surges",
    "growth", "strong", "stronger", "beat", "beats", "bullish",
    "win", "wins", "positive", "optimistic", "improve", "improves"
}

NEGATIVE_WORDS = {
    "loss", "losses", "fall", "falls", "down", "drop", "drops",
    "weak", "weaker", "miss", "misses", "bearish", "risk", "risks",
    "negative", "concern", "concerns", "decline", "declines", "fear"
}


def classify_sentiment(score: int) -> str:
    """
    Convert numeric score to label.
    """
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    return "neutral"


def score_sentiment(text: str) -> Dict[str, Any]:
    """
    Score text using simple word matching.
    """
    words = text.split()

    positive_hits = sum(1 for word in words if word in POSITIVE_WORDS)
    negative_hits = sum(1 for word in words if word in NEGATIVE_WORDS)

    sentiment_score = positive_hits - negative_hits
    sentiment_label = classify_sentiment(sentiment_score)

    return {
        "sentiment_score": sentiment_score,
        "sentiment_label": sentiment_label,
        "positive_hits": positive_hits,
        "negative_hits": negative_hits,
    }


def score_news_item(news_item: Dict[str, Any]) -> Dict[str, Any]:
    """
    Combine title + summary, score sentiment, and return enriched record.
    """
    title = news_item.get("title", "")
    summary = news_item.get("summary", "")
    combined_text = combine_title_and_summary(title, summary)

    sentiment_result = score_sentiment(combined_text)

    enriched_item = {
        **news_item,
        "combined_text": combined_text,
        **sentiment_result,
    }

    return enriched_item