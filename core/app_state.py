import threading
from typing import Any


class AppState:
    """Keep the application state without mixing UI or clipboard concerns."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._running = True
        self._paused = False
        self._last_clipboard_content: Any = object()

    @property
    def is_running(self) -> bool:
        return self._running

    @property
    def is_paused(self) -> bool:
        return self._paused

    @property
    def last_clipboard_content(self) -> Any:
        return self._last_clipboard_content

    @last_clipboard_content.setter
    def last_clipboard_content(self, value: Any) -> None:
        self._last_clipboard_content = value

    def start(self) -> None:
        with self._lock:
            self._running = True
            self._paused = False
            self._last_clipboard_content = object()

    def stop(self) -> None:
        with self._lock:
            self._running = False
            self._paused = False
            self._last_clipboard_content = object()

    def toggle_pause(self) -> bool:
        with self._lock:
            self._paused = not self._paused
            return self._paused
