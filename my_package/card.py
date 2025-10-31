import random

class BingoCard:
    def __init__(self, rows=3, cols=7, max_number=75):
        """Generate a rows×cols grid with unique numbers in 1..max_number.

        Default max_number is 99, but callers can override it (e.g., 50 in Easy
        mode). We sample without replacement to ensure uniqueness, then sort so the
        card is easy to read (ordering has no gameplay effect).
        """
        self.rows = rows
        self.cols = cols
        self.max_number = max_number
        numbers = random.sample(range(1, max_number + 1), rows * cols)
        numbers.sort()
        self.grid = [numbers[i:i+cols] for i in range(0, rows * cols, cols)]
        # Parallel matrix tracks which cells are marked.
        self.marked = [[False for _ in range(cols)] for _ in range(rows)]

    def display(self):
        """Print a simple ASCII card; marked cells are shown in brackets."""
        print("-" * (self.cols * 6))
        for r, row in enumerate(self.grid):
            cells = []
            for c, n in enumerate(row):
                if self.marked[r][c]:
                    cells.append(f"[{n:^3}]")
                else:
                    cells.append(f" {n:^3} ")
            print("|".join(cells))
            print("-" * (self.cols * 6))

    def mark_number(self, number: int) -> bool:
        """Mark number on the card if present; return True if a cell changed."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == number and not self.marked[r][c]:
                    self.marked[r][c] = True
                    return True
        return False
