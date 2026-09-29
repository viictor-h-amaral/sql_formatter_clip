import time

from app.bootstrap import ClipboardSqlFormatterApp
from config.settings import POLL_INTERVAL_SECONDS


def format_clipboard_sql() -> None:
    """Backward-compatible alias for the original loop."""
    app = ClipboardSqlFormatterApp()
    app.start()
    while app.is_running:
        time.sleep(POLL_INTERVAL_SECONDS)


def main() -> None:
    app = ClipboardSqlFormatterApp()
    app.run_tray()


if __name__ == "__main__":
    main()