import random
import time
from typing import Tuple

import pandas as pd
from card import BingoCard
from win_check import is_full_bingo
from draw_capitals import load_capitals_dataframe, normalize_answer, draw_random_question
from colorama import Fore, Style, init
init(autoreset=True)

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.progress import Progress, SpinnerColumn, TextColumn

from rich.markdown import Markdown

console = Console()

def ask_question_once(df: pd.DataFrame) -> tuple[bool, bool]:
    """Ask one capital question.

    Returns a tuple: (should_continue, is_correct).
    The early return on 'q' allows exiting the loop from the caller cleanly.
    """
    country, capital = draw_random_question(df)
    console.print(Rule("Question"))
    console.print(Panel.fit(f"What is the capital of [bold]{country}[/]?", border_style="magenta"))

    while True:
        user = console.input("Your answer (or 'q' to quit, 'h' for help): ")
        norm = normalize_answer(user)
        if norm == 'q':
            return False, False
        if norm == 'h':
            show_instructions()
            # re-ask the same question without consuming attempts
            continue

        is_correct = norm == normalize_answer(capital)
        if is_correct:
            console.print("[green]Correct![/]\n")
        else:
            console.print(f"[red]Incorrect.[/] The capital is [bold]{capital}[/].\n")
        return True, is_correct



def draw_unique_number(already_drawn: set[int], max_number: int) -> int:
    """Draw a new number not drawn before within 1..max_number.

    We compute the remaining pool on each draw to keep logic simple and robust,
    which is fine for small ranges like 1..99. The set ensures uniqueness.
    """
    available = [n for n in range(1, max_number + 1) if n not in already_drawn]
    if not available:
        raise RuntimeError("No more numbers to draw")
    n = random.choice(available)
    already_drawn.add(n)
    return n

def show_instructions() -> None:
    md = Markdown(
        """
### How to play GeoBingo

- You’ll be shown a **country**. Type its **capital**.
- If you’re **correct**, a **number is drawn**. If it’s on your card, it gets **marked** like `[ 7 ]`.
- Get the **whole card marked** to win **BINGO**.
- You have a limited number of **attempts**.
- Type **`h`**, **`i`** or **`?`** anytime to see these instructions.
- Type **`q`** or **`s`** to quit.
        """.strip()
    )
    console.print(Panel(md, border_style="blue", title="Instructions"))


def main():
    # Easy mode reduces the number range to make marking more likely each round.
    max_number = 50
    attempts_remaining = 5  # Lose after 5 incorrect answers.
    console.rule(f"[bold]Mode:[/] EASY (numbers 1..{max_number})")
    show_instructions()

    # The BingoCard uses the same max_number to keep drawing consistent with the grid.
    card = BingoCard(rows=3, cols=7, max_number=max_number)
    card.display_rich()
    try:
        # Centralized CSV loading lives in draw_capitals to keep data concerns together.
        df = load_capitals_dataframe()
    except FileNotFoundError as e:
        console.print(Panel.fit(str(e), border_style="red"))
        return

    drawn_numbers: set[int] = set()
    console.print("[dim]Type 'q' at any time to quit.[/]\n")
    while True:
        console.print(Panel.fit(f"Attempts left: [bold]{attempts_remaining}[/]", border_style="cyan"))
        should_continue, is_correct = ask_question_once(df)
        if not should_continue:
            console.print(Panel.fit("Goodbye!", border_style="dim"))
            break
        if is_correct:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
                console=console,
            ) as progress:
                progress.add_task(description="Drawing number...", total=None)
                time.sleep(0.7)
            number = draw_unique_number(drawn_numbers, max_number=max_number)
            console.print(Panel.fit(f"Number drawn: [bold cyan]{number}[/]", border_style="cyan"))
            if card.mark_number(number):
                console.print("[green]It's on your card! Marked.[/]")
            else:
                console.print("[yellow]Not on your card.[/]")
            card.display_rich()
            # Win condition is centralized in win_check for separation of concerns.
            if is_full_bingo(card):
                console.print(Panel.fit("BINGO! You completed the card. Congratulations!", border_style="green"))
                break
        else:
            attempts_remaining -= 1
            if attempts_remaining <= 0:
                console.print(Panel.fit("No attempts left. Game over!", border_style="red"))
                break


if __name__ == "__main__":
    main()
