"""SQL formatting domain primitives."""

from .detector import text_is_query_sql
from .indentation import add_tab
from .line_breaks import add_enter
from .normalizer import format_text

__all__ = ["format_text", "add_enter", "add_tab", "text_is_query_sql"]
