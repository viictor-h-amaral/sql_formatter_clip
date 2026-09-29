class TrayService:
    """Coordinates tray UI updates for the app state."""

    def __init__(self, state, tray_adapter, *, on_toggle_pause, on_exit) -> None:
        self.state = state
        self.tray_adapter = tray_adapter
        self._on_toggle_pause = on_toggle_pause
        self._on_exit = on_exit
        self._tray_icon = None

    @property
    def tray_icon(self):
        return self._tray_icon

    def build_menu(self):
        pause_label = "Pausar" if self.state.is_running and not self.state.is_paused else "Despausar"
        return self.tray_adapter.build_menu(
            pause_label=pause_label,
            on_pause=self._on_toggle_pause,
            on_exit=self._on_exit,
            enabled=self.state.is_running,
        )

    def refresh(self) -> None:
        if self._tray_icon is None:
            return

        self._tray_icon.icon = self.tray_adapter.make_icon(active=self.state.is_running and not self.state.is_paused)
        self._tray_icon.menu = self.build_menu()
        try:
            self._tray_icon.update_menu()
        except AttributeError:
            pass

    def run(self) -> None:
        self._tray_icon = self.tray_adapter.create_icon(
            active=True,
            menu=self.build_menu(),
        )
        self._tray_icon.run()

    def stop(self) -> None:
        if self._tray_icon is not None:
            self._tray_icon.stop()
