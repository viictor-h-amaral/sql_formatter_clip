def text_is_query_sql(text: str) -> bool:
    """Return True when the text looks like a SQL query with SELECT and FROM."""
    text_upper = text.upper().strip()
    return text_upper.find("SELECT") != -1 and text_upper.find("FROM") != -1
