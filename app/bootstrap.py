import logging

from adapters.clipboard_adapter import ClipboardAdapter
from adapters.tray_adapter import TrayAdapter
from config.settings import SETTINGS
from core.app_state import AppState
from services.clipboard_monitor import ClipboardMonitor
from services.formatter_service import FormatterService
from services.tray_service import TrayService

logging.basicConfig(level=getattr(logging, SETTINGS.log_level.upper(), logging.INFO), format=SETTINGS.log_format)
logger = logging.getLogger(__name__)


class ClipboardSqlFormatterApp:
    """Background clipboard SQL formatter with tray controls."""

    def __init__(self) -> None:
        logger.info("Initializing SQL formatter app.")
        self.state = AppState()
        self.clipboard_adapter = ClipboardAdapter()
        self.formatter_service = FormatterService()
        self.monitor = ClipboardMonitor(self.state, self.clipboard_adapter, self.formatter_service)
        self.tray_adapter = TrayAdapter()
        self.tray_service = TrayService(
            self.state,
            self.tray_adapter,
            on_toggle_pause=self.toggle_pause,
            on_exit=self.shutdown,
        )

    @property
    def is_running(self) -> bool:
        return self.state.is_running

    @property
    def is_paused(self) -> bool:
        return self.state.is_paused

    def start(self) -> None:
        logger.info("Starting application loop.")
        self.state.start()
        self.monitor.start()
        self.refresh_tray()

    def stop(self) -> None:
        logger.info("Stopping application loop.")
        self.state.stop()
        self.refresh_tray()

    def toggle_pause(self) -> bool:
        paused = self.state.toggle_pause()
        logger.info("Application paused=%s", paused)
        self.refresh_tray()
        return paused

    def refresh_tray(self) -> None:
        self.tray_service.refresh()

    def shutdown(self) -> None:
        logger.info("Shutting down application.")
        self.stop()
        self.tray_service.stop()

    def run_tray(self) -> None:
        self.start()
        self.tray_service.run()


def main() -> None:
    app = ClipboardSqlFormatterApp()
    app.run_tray()
