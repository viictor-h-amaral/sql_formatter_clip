from domain.sql_formatting.formatter import format_sql


class FormatterService:
    """Orchestrates the SQL formatting pipeline."""

    def format(self, text: str) -> str:
        return format_sql(text)
