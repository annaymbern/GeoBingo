import unittest
from my_package.card import BingoCard


class TestBingoCard(unittest.TestCase):

    def test_grid_dimensions(self):
        # the card should have rows x cols elements.
        rows, cols = 3, 7  # we define example parameters to test
        card = BingoCard(rows=rows, cols=cols, max_number=99)  # we create the card

        # we check that the number of rows is correct
        self.assertEqual(len(card.grid), rows)
        # we check that each row has the correct number of columns
        for row in card.grid:
            self.assertEqual(len(row), cols)

    def test_numbers_unique_and_in_range(self):
        # all numbers must be unique and within the allowed range.
        rows, cols, max_number = 3, 7, 50  # max_number, rows and cols so that random.sample works
        card = BingoCard(rows=rows, cols=cols, max_number=max_number)  # we generate a card

        nums = [n for row in card.grid for n in row]  # we flatten the grid to analyze it

        # correct size, there should be exactly rows * cols numbers
        self.assertEqual(len(nums), rows * cols)

        # uniqueness, converting to set() should not remove elements
        self.assertEqual(len(set(nums)), len(nums))

        # range, all numbers must be between 1 and max_number
        self.assertTrue(all(1 <= n <= max_number for n in nums))

    def test_card_is_sorted_row_wise(self):
        # since sort() is applied before splitting into rows, the card should be ordered.
        # this means that if we read it as a flat list, it should match sorted().
        card = BingoCard(rows=3, cols=7, max_number=99)  # we generate an example card

        flat = [n for row in card.grid for n in row]  # we turn the card into a single list
        self.assertEqual(flat, sorted(flat))  # we verify that it is actually sorted

    def test_mark_number_marks_and_returns_true(self):
        # if the number is on the card, mark_number should mark it and return true.
        card = BingoCard(rows=3, cols=7, max_number=99)  # we create an example card

        target = card.grid[0][0]  # we pick a number that is definitely on the card
        result = card.mark_number(target)  # we try to mark it

        # we check that mark_number returns true when marking an existing number
        self.assertTrue(result)
        # we check that the corresponding cell is marked
        self.assertTrue(card.marked[0][0])
        # we check that the number also appears in marked_set
        self.assertIn(target, card.marked_set)

    def test_mark_number_twice_returns_false(self):
        # marking the same number twice: the first should return true and the second false.
        card = BingoCard(rows=3, cols=7, max_number=99)  # we generate an example card
        target = card.grid[0][0]  # we choose a number that is definitely on the card

        first = card.mark_number(target)   # first time we mark it, should be true
        second = card.mark_number(target)  # second time, should be false

        # we check that the first call returns true
        self.assertTrue(first)
        # we check that the second returns false
        self.assertFalse(second)
        # we check that the cell stays marked
        self.assertTrue(card.marked[0][0])
        # we check that the number is in the marked set
        self.assertIn(target, card.marked_set)

    def test_mark_number_not_on_card_returns_false(self):
        # if the number is not on the card, mark_number should return false and not mark anything.
        card = BingoCard(rows=3, cols=7, max_number=99)  # max_number large enough

        missing = card.max_number + 1  # we pick a number out of range to ensure it is not present
        result = card.mark_number(missing)  # we try to mark it

        # we check that the function returns false for non existing numbers
        self.assertFalse(result)
        # we check that no cell has been marked
        self.assertTrue(all(not m for row in card.marked for m in row))
        # we check that the number does not appear in marked_set
        self.assertNotIn(missing, card.marked_set)

    def test_marked_set_consistent_with_marked_matrix(self):
        # numbers marked in 'marked' and in 'marked_set' must match.
        card = BingoCard(rows=3, cols=7, max_number=99)  # we create a card

        # we mark two numbers in a controlled way
        nums_to_mark = [card.grid[0][0], card.grid[1][2]]
        for n in nums_to_mark:
            card.mark_number(n)

        # we collect the numbers marked in the marked matrix
        matrix_marked = {
            card.grid[r][c]
            for r in range(card.rows)
            for c in range(card.cols)
            if card.marked[r][c]
        }

        # they should be exactly the same as those in marked_set
        self.assertEqual(matrix_marked, card.marked_set)

    def test_display_rich_does_not_raise(self):
        # display_rich should not raise exceptions when run.
        card = BingoCard(rows=3, cols=7, max_number=99)  # we create a card

        try:
            card.display_rich()  # we simply call the function
        except Exception as e:
            # if any exception is raised, the test fails
            self.fail(f"display_rich lanzó una excepción: {e}")


if __name__ == "__main__":
    unittest.main()

