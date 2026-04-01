from datetime import datetime, timezone


def get_utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_filename_timestamp() -> str:
    return get_utc_timestamp().replace(":", "-")