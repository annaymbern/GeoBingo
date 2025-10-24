import random

class BingoCard:
    def __init__(self, rows=3, cols=7):
        self.rows = rows
        self.cols = cols
        numbers = random.sample(range(1, 99), rows * cols)
        numbers.sort()
        self.grid = [numbers[i:i+cols] for i in range(0, rows * cols, cols)]

    def display(self):
        print("-" * (self.cols * 6))
        for row in self.grid:
            print(" | ".join(f"{str(n):^3}" for n in row))
            print("-" * (self.cols * 6))