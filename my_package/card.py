import random
from rich.console import Console
from rich.table import Table
from rich import box
_console = Console()
from rich.align import Align


class BingoCard:
    def __init__(self, rows=3, cols=7, max_number=99):
        """Generate a rows×cols grid with unique numbers in 1..max_number.

        Default max_number is 99, but callers can override it (e.g., 50 in Easy
        mode). We sample without replacement to ensure uniqueness, then sort so the
        card is easy to read (ordering has no gameplay effect).
        """
        self.rows = rows
        self.cols = cols
        self.max_number = max_number
        #sample, all nums in the card are unique no repetitions
        numbers = random.sample(range(1, max_number + 1), rows * cols)
        numbers.sort()
        self.grid = [numbers[i:i+cols] for i in range(0, rows * cols, cols)]
        #parallel matrix to track which cells are marked
        self.marked = [[False for _ in range(cols)] for _ in range(rows)]
        self.marked_set = set()

   #mark num if presented on the card
    def mark_number(self, number: int) -> bool:
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == number and not self.marked[r][c]:
                    self.marked[r][c] = True
                    self.marked_set.add(number)
                    return True #num found on the card
        return False #num not found

    def display_rich(self) -> None: #visual function to make the card look better and colorful

        table = Table(
            title="Your Bingo Card",
            box=box.ROUNDED,
            show_lines=True,
            show_header=False,
            pad_edge=False,
        )

        for _ in range(self.cols): #one column per bingo slot
            table.add_column(justify="center", width=6, no_wrap=True)

        for r in range(self.rows):
            row_cells = []
            for c in range(self.cols):
                n = self.grid[r][c]
                marked = self.marked[r][c] or (n in self.marked_set)
                cell = f"[bold green][[{n:>2}]][/]" if marked else f"{n:>2}"


                row_cells.append(cell)
            table.add_row(*row_cells)

        _console.print(Align.center(table))


