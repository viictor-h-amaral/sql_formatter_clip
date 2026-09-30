from .detector import text_is_query_sql
from .indentation import add_tab
from .line_breaks import add_enter
from .normalizer import format_text


def format_sql(text: str) -> str:
    """Apply the full SQL formatting pipeline in a clear, explicit order."""
    if not text or not text_is_query_sql(text):
        return text

    normalized_sql = format_text(text)
    with_line_breaks = add_enter(normalized_sql)
    return add_tab(with_line_breaks)
