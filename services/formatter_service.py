from helpers.basic_text_formatter import format_text
from helpers.identor_formatter import add_tab
from helpers.line_separator_formatter import add_enter
from helpers.sql_identifier import text_is_query_sql as is_sql_query


class FormatterService:
    """Orchestrates the SQL formatting pipeline."""

    def format(self, text: str) -> str:
        if not text or not is_sql_query(text):
            return text

        formatted_sql = format_text(text)
        formatted_sql = add_enter(formatted_sql)
        formatted_sql = add_tab(formatted_sql)
        return formatted_sql
