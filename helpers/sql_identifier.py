def text_is_query_sql(text: str) -> bool:
    """
    Check if the given text is a SQL query statement.

    Args:
        text (str): The text to check.

    Returns:
        bool: True if the text is a SQL query statement, False otherwise.
    """
    text_upper = text.upper().strip()
    return text_upper.find("SELECT") != -1 and text_upper.find("FROM") != -1