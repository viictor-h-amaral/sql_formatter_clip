import unittest

from main import ClipboardSqlFormatterApp


class ClipboardSqlFormatterAppTests(unittest.TestCase):
    def test_starts_in_running_state(self):
        app = ClipboardSqlFormatterApp()
        self.assertTrue(app.is_running)
        self.assertFalse(app.is_paused)

    def test_toggle_pause_and_resume(self):
        app = ClipboardSqlFormatterApp()
        app.toggle_pause()
        self.assertTrue(app.is_paused)
        app.toggle_pause()
        self.assertFalse(app.is_paused)

    def test_stop_and_start(self):
        app = ClipboardSqlFormatterApp()
        app.stop()
        self.assertFalse(app.is_running)
        app.start()
        self.assertTrue(app.is_running)


if __name__ == "__main__":
    unittest.main()
