import pystray
from PIL import Image, ImageDraw


class TrayAdapter:
    """Encapsulates tray icon and menu creation."""

    def __init__(self, app_name: str = "sql_formatter_clip", title: str = "SQL Formatter") -> None:
        self.app_name = app_name
        self.title = title

    def make_icon(self, *, active: bool) -> Image.Image:
        image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        color = (34, 197, 94) if active else (107, 114, 128)
        draw.rounded_rectangle((8, 8, 56, 56), radius=12, fill=color)
        draw.text((18, 18), "SQL", fill=(255, 255, 255), anchor="mm")
        return image

    def build_menu(self, *, pause_label: str, on_pause, on_exit, enabled: bool):
        return pystray.Menu(
            pystray.MenuItem(
                pause_label,
                on_pause,
                enabled=enabled,
            ),
            pystray.MenuItem("Sair", on_exit),
        )

    def create_icon(self, *, active: bool, menu):
        return pystray.Icon(
            self.app_name,
            self.make_icon(active=active),
            self.title,
            menu,
        )
