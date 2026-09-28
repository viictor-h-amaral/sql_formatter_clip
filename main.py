from helpers.identor_formatter import add_tab
from helpers.sql_identifier import text_is_query_sql as is_sql_query
from helpers.basic_text_formatter import format_text
from helpers.line_separator_formatter import add_enter
import time
import pyperclip as clip


POLL_INTERVAL_SECONDS = 0.5


def format_clipboard_sql() -> None:
    """Monitor the clipboard and format newly copied SQL text."""
    last_clipboard_content = object()

    while True:
        try:
            clipboard_content = clip.paste()
        except clip.PyperclipException:
            time.sleep(POLL_INTERVAL_SECONDS)
            continue

        if clipboard_content == last_clipboard_content:
            time.sleep(POLL_INTERVAL_SECONDS)
            continue

        last_clipboard_content = clipboard_content

        if is_sql_query(clipboard_content):
            formatted_sql = format_text(clipboard_content)
            formatted_sql = add_enter(formatted_sql)
            formatted_sql = add_tab(formatted_sql)
            if formatted_sql != clipboard_content:
                clip.copy(formatted_sql)
                last_clipboard_content = formatted_sql

        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    format_clipboard_sql()