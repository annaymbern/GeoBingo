import unittest
from my_package.draw_capitals import load_capitals_dataframe, normalize_answer, draw_random_question

class TestDrawCapitals(unittest.TestCase):
    def setUp(self):
        self.df = load_capitals_dataframe()

    def test_loader_columns(self):
        self.assertIn("Country", self.df.columns)
        self.assertIn("Capital", self.df.columns)
        self.assertGreater(len(self.df), 0)

    def test_normalize_answer(self):
        self.assertEqual(normalize_answer("  Madrid "), "madrid")
        self.assertEqual(normalize_answer("PARIS"), "paris")
        self.assertEqual(normalize_answer(None), "")

    def test_draw_random_question_tuple(self):
        country, capital = draw_random_question(self.df)
        self.assertIsInstance(country, str)
        self.assertIsInstance(capital, str)
        self.assertGreater(len(country.strip()), 0)
        self.assertGreater(len(capital.strip()), 0)

if __name__ == "__main__":
    unittest.main()
