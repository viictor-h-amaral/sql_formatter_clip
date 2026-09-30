def tokenize_sql(text: str):
    """Split SQL text into meaningful chunks for downstream formatting."""
    return [part.strip() for part in text.split() if part.strip()]
