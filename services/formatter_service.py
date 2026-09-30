from domain.sql_formatting.detector import text_is_query_sql as is_sql_query
from domain.sql_formatting.indentation import add_tab
from domain.sql_formatting.line_breaks import add_enter
from domain.sql_formatting.normalizer import format_text


class FormatterService:
    """Orchestrates the SQL formatting pipeline."""

    def format(self, text: str) -> str:
        if not text or not is_sql_query(text):
            return text

        formatted_sql = format_text(text)
        formatted_sql = add_enter(formatted_sql)
        formatted_sql = add_tab(formatted_sql)
        return formatted_sql
