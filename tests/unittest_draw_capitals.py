import unittest
import pandas as pd

import my_package.draw_capitals as dc


class TestDrawCapitals(unittest.TestCase):

    def setUp(self):
        # in each test we keep the pool clean inside the draw_capitals module.
        dc._QUESTION_POOL = None

    def test_normalize_answer_basic(self):
        # normalize_answer should strip() and convert to lowercase.
        self.assertEqual(dc.normalize_answer("  Paris "), "paris")
        self.assertEqual(dc.normalize_answer("LoNDoN"), "london")
        self.assertEqual(dc.normalize_answer("  BERLIN  "), "berlin")

    def test_normalize_answer_empty_and_none(self):
        # if we pass None or an empty string, it should return a normalized empty string.
        self.assertEqual(dc.normalize_answer(""), "")
        self.assertEqual(dc.normalize_answer("   "), "")
        self.assertEqual(dc.normalize_answer(None), "")

    def test_init_pool_creates_shuffled_deque(self):
        # _init_pool should create a deque with all (country, capital) pairs.
        df = pd.DataFrame(
            [
                {"Country": "Spain", "Capital": "Madrid"},
                {"Country": "France", "Capital": "Paris"},
                {"Country": "Italy", "Capital": "Rome"},
            ]
        )

        dc._init_pool(df)  # we initialize the pool in the module

        # _QUESTION_POOL should not be None and should have the correct length
        self.assertIsNotNone(dc._QUESTION_POOL)
        self.assertEqual(len(dc._QUESTION_POOL), len(df))

        # pool pairs should match dataframe pairs (even if order is random)
        expected_pairs = {
            ("Spain", "Madrid"),
            ("France", "Paris"),
            ("Italy", "Rome"),
        }
        pool_pairs = set(dc._QUESTION_POOL)
        self.assertEqual(pool_pairs, expected_pairs)

    def test_draw_random_question_no_repetition_until_exhausted(self):
        # draw_random_question should not repeat questions until the pool is exhausted.
        df = pd.DataFrame(
            [
                {"Country": "Spain", "Capital": "Madrid"},
                {"Country": "France", "Capital": "Paris"},
                {"Country": "Italy", "Capital": "Rome"},
            ]
        )

        dc._QUESTION_POOL = None  # make sure we start with a clean pool

        # draw as many questions as there are rows in the dataframe
        drawn = [dc.draw_random_question(df) for _ in range(len(df))]

        # all drawn questions should be unique
        self.assertEqual(len(drawn), len(set(drawn)))
        # and should match the dataframe pairs
        expected_pairs = {
            ("Spain", "Madrid"),
            ("France", "Paris"),
            ("Italy", "Rome"),
        }
        self.assertEqual(set(drawn), expected_pairs)

        # if we ask for a fourth question, the pool should have been reset
        next_q = dc.draw_random_question(df)
        # the new question should also be within the possible pairs
        self.assertIn(next_q, expected_pairs)

    def test_draw_random_question_reinitializes_when_pool_empty(self):
        # when the pool is empty, it should reinitialize automatically.
        df = pd.DataFrame(
            [
                {"Country": "Spain", "Capital": "Madrid"},
                {"Country": "France", "Capital": "Paris"},
            ]
        )

        dc._QUESTION_POOL = None  # start with no pool

        # draw two questions -> the pool should be exhausted
        first = dc.draw_random_question(df)
        second = dc.draw_random_question(df)

        self.assertNotEqual(first, second)  # they should be different

        # now the pool is empty, the next call should reset it without failing
        third = dc.draw_random_question(df)
        # the third should also be a valid pair from the dataframe
        expected_pairs = {("Spain", "Madrid"), ("France", "Paris")}
        self.assertIn(third, expected_pairs)

    def test_load_capitals_dataframe_has_expected_columns(self):
        # load_capitals_dataframe should return a dataframe with country and capital columns.
        df = dc.load_capitals_dataframe()

        # we check that the columns include country and capital
        self.assertIn("Country", df.columns)
        self.assertIn("Capital", df.columns)
        # optional: the csv should not be empty
        self.assertGreater(len(df), 0)


if __name__ == "__main__":
    unittest.main()
