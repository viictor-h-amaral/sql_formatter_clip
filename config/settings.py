from dataclasses import dataclass

POLL_INTERVAL_SECONDS = 0.5
APP_NAME = "sql_formatter_clip"
APP_TITLE = "SQL Formatter"
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


@dataclass(frozen=True)
class AppSettings:
    app_name: str = APP_NAME
    app_title: str = APP_TITLE
    poll_interval_seconds: float = POLL_INTERVAL_SECONDS
    log_level: str = LOG_LEVEL
    log_format: str = LOG_FORMAT


SETTINGS = AppSettings()
