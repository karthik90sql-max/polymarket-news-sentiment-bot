import re


def clean_text(text: str) -> str:
    """
    Clean text by:
    - converting None to empty string
    - lowercasing
    - removing extra spaces
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text


def combine_title_and_summary(title: str, summary: str) -> str:
    """
    Combine title and summary into one text field.
    """
    title = clean_text(title)
    summary = clean_text(summary)

    combined = f"{title} {summary}".strip()
    return combined