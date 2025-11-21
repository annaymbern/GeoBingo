import unittest
from my_package.card import BingoCard
from my_package.win_check import is_full_bingo


class TestWinCheck(unittest.TestCase):

    def test_full_bingo_false_initially(self):
        # when creating the card, no cell is marked -> result should be false.
        card = BingoCard(rows=3, cols=7, max_number=99)

        self.assertFalse(is_full_bingo(card))

    def test_full_bingo_true_when_all_marked(self):
        # if all cells are marked, is_full_bingo should return true.
        card = BingoCard(rows=3, cols=7, max_number=99)

        # we mark all cells manually
        for r in range(card.rows):
            for c in range(card.cols):
                card.marked[r][c] = True  # we mark directly

        self.assertTrue(is_full_bingo(card))

    def test_full_bingo_false_if_one_cell_unmarked(self):
        # if even one cell is not marked, it should return false.
        card = BingoCard(rows=3, cols=7, max_number=99)

        # we mark all cells except one
        for r in range(card.rows):
            for c in range(card.cols):
                card.marked[r][c] = True

        card.marked[1][3] = False  # one cell left unmarked

        self.assertFalse(is_full_bingo(card))


if __name__ == "__main__":
    unittest.main()
