import unittest
from my_package.card import BingoCard
from my_package.win_check import is_full_bingo

class TestWinCheck(unittest.TestCase):
    def test_is_full_bingo_false_initially(self):
        card = BingoCard(rows=3, cols=7, max_number=50)
        self.assertFalse(is_full_bingo(card))

    def test_is_full_bingo_true_when_all_marked(self):
        card = BingoCard(rows=3, cols=7, max_number=50)
        for r in range(card.rows):
            for c in range(card.cols):
                num = card.grid[r][c]
                card.mark_number(num)
        self.assertTrue(is_full_bingo(card))

if __name__ == "__main__":
    unittest.main()
