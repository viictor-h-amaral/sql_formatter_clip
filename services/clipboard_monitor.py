import threading
import time
from typing import Optional

from config.settings import POLL_INTERVAL_SECONDS
from core.interfaces import AppStateProtocol, ClipboardAdapterProtocol, FormatterServiceProtocol


class ClipboardMonitor:
    """Polls the clipboard and formats SQL when needed."""

    def __init__(
        self,
        state: AppStateProtocol,
        clipboard_adapter: ClipboardAdapterProtocol,
        formatter_service: FormatterServiceProtocol,
    ) -> None:
        self.state = state
        self.clipboard_adapter = clipboard_adapter
        self.formatter_service = formatter_service
        self._lock = threading.Lock()
        self._thread: Optional[threading.Thread] = None

    @property
    def thread(self) -> Optional[threading.Thread]:
        return self._thread

    def start(self) -> None:
        with self._lock:
            if self._thread and self._thread.is_alive():
                return
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self.state.stop()

    def _run_loop(self) -> None:
        while self.state.is_running:
            if self.state.is_paused:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            try:
                clipboard_content = self.clipboard_adapter.paste()
            except Exception:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            if clipboard_content == self.state.last_clipboard_content:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            self.state.last_clipboard_content = clipboard_content

            formatted_sql = self.formatter_service.format(clipboard_content)
            if formatted_sql != clipboard_content:
                self.clipboard_adapter.copy(formatted_sql)
                self.state.last_clipboard_content = formatted_sql

            time.sleep(POLL_INTERVAL_SECONDS)
