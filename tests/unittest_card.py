import unittest
from my_package.card import BingoCard

class TestBingoCard(unittest.TestCase):
    def test_grid_shape_and_range(self):
        card = BingoCard(rows=3, cols=7, max_number=50)
        self.assertEqual(len(card.grid), 3)
        for row in card.grid:
            self.assertEqual(len(row), 7)
            for n in row:
                self.assertGreaterEqual(n, 1)
                self.assertLessEqual(n, 50)

    def test_unique_numbers(self):
        card = BingoCard(rows=3, cols=7, max_number=99)
        flat = [n for row in card.grid for n in row]
        self.assertEqual(len(flat), len(set(flat)))

    def test_mark_number_behavior(self):
        card = BingoCard(rows=3, cols=7, max_number=50)
        any_number = card.grid[0][0]
        self.assertTrue(card.mark_number(any_number))  # first time marks
        self.assertFalse(card.mark_number(any_number))  # second time no change
        # Ensure only that cell changed
        marked_count = sum(1 for r in range(card.rows) for c in range(card.cols) if card.marked[r][c])
        self.assertEqual(marked_count, 1)

    def test_respects_max_number(self):
        card = BingoCard(rows=3, cols=7, max_number=50)
        self.assertTrue(all(n <= 50 for row in card.grid for n in row))

if _name_ == "_main_":
    unittest.main()
