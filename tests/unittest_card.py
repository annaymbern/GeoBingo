import unittest
import pandas as pd
import os 

class TestGeoBingo(unittest.TestCase):

    def setUp(self):
        # Load dataset into DataFrame
        self.df = pd.read_csv("../data/capitals.csv")  # change path if needed

    def test_load_csv(self):
        """Dataset should load correctly"""
        self.assertIsInstance(self.df, pd.DataFrame)

    def test_all_rows_valid(self):
        """Each row must have non-empty Country and Capital"""
        self.assertTrue(self.df['Country'].notnull().all(), "Some countries are missing")
        self.assertTrue(self.df['Capital'].notnull().all(), "Some capitals are missing")
        self.assertTrue((self.df['Country'].str.strip() != "").all(), "Empty country found")
        self.assertTrue((self.df['Capital'].str.strip() != "").all(), "Empty capital found")

    def test_no_duplicates(self):
        """No duplicate countries allowed"""
        duplicates = self.df['Country'].duplicated().sum()
        self.assertEqual(duplicates, 0, f"{duplicates} duplicate countries found")

if __name__ == "__main__":
    unittest.main()
