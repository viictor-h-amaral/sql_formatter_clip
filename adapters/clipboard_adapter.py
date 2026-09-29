import pyperclip as clip


class ClipboardAdapterError(RuntimeError):
    """Raised when clipboard operations fail."""


class ClipboardAdapter:
    """Small adapter for interacting with the system clipboard."""

    def paste(self) -> str:
        try:
            return clip.paste()
        except clip.PyperclipException as exc:
            raise ClipboardAdapterError("Failed to read clipboard content.") from exc

    def copy(self, value: str) -> None:
        try:
            clip.copy(value)
        except clip.PyperclipException as exc:
            raise ClipboardAdapterError("Failed to write clipboard content.") from exc
