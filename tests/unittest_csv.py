import unittest
from my_package.draw_capitals import load_capitals_dataframe


class TestGeoBingoDataset(unittest.TestCase):
    def setUp(self):
        self.df = load_capitals_dataframe()

    def test_all_rows_nonempty(self):
        """each row must have non-empty country and capital"""
        self.assertTrue(self.df["Country"].notnull().all(), "some countries are missing")
        self.assertTrue(self.df["Capital"].notnull().all(), "some capitals are missing")
        self.assertTrue((self.df["Country"].str.strip() != "").all(), "empty country found")
        self.assertTrue((self.df["Capital"].str.strip() != "").all(), "empty capital found")

    def test_no_duplicates(self):
        """no duplicate countries allowed"""
        duplicates = self.df["Country"].duplicated().sum()
        self.assertEqual(duplicates, 0, f"{duplicates} duplicate countries found")


if __name__ == "__main__":
    unittest.main()
