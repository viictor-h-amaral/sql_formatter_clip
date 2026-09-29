import pyperclip as clip


class ClipboardAdapter:
    """Small adapter for interacting with the system clipboard."""

    def paste(self) -> str:
        return clip.paste()

    def copy(self, value: str) -> None:
        clip.copy(value)
