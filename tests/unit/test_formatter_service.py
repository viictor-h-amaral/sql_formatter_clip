import unittest

from services.formatter_service import FormatterService


class FormatterServiceTests(unittest.TestCase):
    def test_formats_sql_query(self):
        service = FormatterService()
        sql = "SELECT   a, b FROM table WHERE a = 'ABC'"

        formatted = service.format(sql)

        self.assertIn("select", formatted.lower())
        self.assertIn("from", formatted.lower())
        self.assertIn("where", formatted.lower())
        self.assertIn("'ABC'", formatted)


if __name__ == "__main__":
    unittest.main()
