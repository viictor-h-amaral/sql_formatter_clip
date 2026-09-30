"""SQL formatting domain primitives."""

from .detector import is_sql_query, text_is_query_sql
from .formatter import format_sql
from .indentation import add_tab
from .line_breaks import add_enter
from .normalizer import format_text

__all__ = [
    "format_sql",
    "format_text",
    "add_enter",
    "add_tab",
    "is_sql_query",
    "text_is_query_sql",
]
