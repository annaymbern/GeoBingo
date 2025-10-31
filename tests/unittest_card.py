import unittest
import random
from my_package.card import BingoCard

class TestBingoCard(unittest.TestCase):
    # Opcional: reproducibilidad
    # def setUp(self):
    #     random.seed(0)

    def test_grid_shape_and_range(self):
        card = BingoCard(rows=3, cols=7, max_number=75)
        self.assertEqual(len(card.grid), 3)
        for row in card.grid:
            self.assertEqual(len(row), 7)
            for n in row:
                self.assertGreaterEqual(n, 1)
                self.assertLessEqual(n, 75)

    def test_unique_numbers(self):
        card = BingoCard(rows=3, cols=7, max_number=75)
        flat = [n for row in card.grid for n in row]
        self.assertEqual(len(flat), len(set(flat)))

    def test_mark_number_behavior(self):
        card = BingoCard(rows=3, cols=7, max_number=75)
        any_number = card.grid[0][0]
        self.assertTrue(card.mark_number(any_number))   # primera vez marca
        self.assertFalse(card.mark_number(any_number))  # segunda vez no cambia
        # Solo una celda marcada
        marked_count = sum(
            1 for r in range(card.rows) for c in range(card.cols) if card.marked[r][c]
        )
        self.assertEqual(marked_count, 1)

    def test_sorted_rows_optional(self):
        """Opcional: comprueba que los números están ordenados si tu clase lo promete."""
        card = BingoCard(rows=3, cols=7, max_number=75)
        flat = [n for row in card.grid for n in row]
        self.assertEqual(flat, sorted(flat))

    def test_raises_if_population_too_small(self):
        """random.sample debe lanzar ValueError si pides más números de los disponibles."""
        with self.assertRaises(ValueError):
            BingoCard(rows=4, cols=6, max_number=10)  # 24 > 10

if __name__ == "__main__":
    unittest.main()
