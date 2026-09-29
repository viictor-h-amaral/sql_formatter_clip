import threading
import time
from typing import Optional

import pyperclip as clip
import pystray
from PIL import Image, ImageDraw

from helpers.identor_formatter import add_tab
from helpers.sql_identifier import text_is_query_sql as is_sql_query
from helpers.basic_text_formatter import format_text
from helpers.line_separator_formatter import add_enter


POLL_INTERVAL_SECONDS = 0.5


class ClipboardSqlFormatterApp:
    """Background clipboard SQL formatter with tray controls."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._running = True
        self._paused = False
        self._thread: Optional[threading.Thread] = None
        self._last_clipboard_content = object()
        self._tray_icon: Optional[pystray.Icon] = None

    @property
    def is_running(self) -> bool:
        return self._running

    @property
    def is_paused(self) -> bool:
        return self._paused

    def start(self) -> None:
        with self._lock:
            if self._thread and self._thread.is_alive():
                return

            self._running = True
            self._paused = False
            self._last_clipboard_content = object()
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()

        self.refresh_tray()

    def stop(self) -> None:
        with self._lock:
            self._running = False
            self._paused = False
            self._last_clipboard_content = object()

        self.refresh_tray()

    def toggle_pause(self) -> bool:
        with self._lock:
            self._paused = not self._paused
            paused = self._paused

        self.refresh_tray()
        return paused

    def _run_loop(self) -> None:
        while self.is_running:
            if self.is_paused:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            try:
                clipboard_content = clip.paste()
            except clip.PyperclipException:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            if clipboard_content == self._last_clipboard_content:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            self._last_clipboard_content = clipboard_content

            if is_sql_query(clipboard_content):
                formatted_sql = format_text(clipboard_content)
                formatted_sql = add_enter(formatted_sql)
                formatted_sql = add_tab(formatted_sql)
                if formatted_sql != clipboard_content:
                    clip.copy(formatted_sql)
                    self._last_clipboard_content = formatted_sql

            time.sleep(POLL_INTERVAL_SECONDS)

    def _make_icon(self, *, active: bool) -> Image.Image:
        image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        color = (34, 197, 94) if active else (107, 114, 128)
        draw.rounded_rectangle((8, 8, 56, 56), radius=12, fill=color)
        draw.text((18, 18), "SQL", fill=(255, 255, 255), anchor="mm")
        return image

    def _build_menu(self):
        pause_label = "Pausar" if self.is_running and not self.is_paused else "Despausar"
        return pystray.Menu(
            pystray.MenuItem(
                pause_label,
                self.toggle_pause,
                enabled=self.is_running,
            ),
            pystray.MenuItem("Sair", self.shutdown),
        )

    def refresh_tray(self) -> None:
        if self._tray_icon is None:
            return

        self._tray_icon.icon = self._make_icon(active=self.is_running and not self.is_paused)
        self._tray_icon.menu = self._build_menu()
        try:
            self._tray_icon.update_menu()
        except AttributeError:
            pass

    def shutdown(self) -> None:
        self.stop()
        if self._tray_icon is not None:
            self._tray_icon.stop()

    def run_tray(self) -> None:
        self.start()
        self._tray_icon = pystray.Icon(
            "sql_formatter_clip",
            self._make_icon(active=True),
            "SQL Formatter",
            self._build_menu(),
        )
        self._tray_icon.run()


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