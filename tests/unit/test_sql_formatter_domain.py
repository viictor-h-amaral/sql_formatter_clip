import unittest

from domain.sql_formatting.formatter import format_sql


class SqlFormattingDomainTests(unittest.TestCase):
    def test_format_sql_pipeline(self):
        sql = "SELECT   a, b FROM table WHERE a = 'ABC'"

        formatted = format_sql(sql)

        self.assertIn("select", formatted.lower())
        self.assertIn("from", formatted.lower())
        self.assertIn("where", formatted.lower())
        self.assertIn("'ABC'", formatted)


if __name__ == "__main__":
    unittest.main()
