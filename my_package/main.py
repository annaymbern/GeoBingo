import random
import time
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
import signal

console = Console()
DIFFICULTY = "medium"  #we put it in default, will be overwritten by choose_difficulty()


def ask_question_once(df: pd.DataFrame) -> tuple[bool, bool]:
    """Ask one capital question depending on difficulty.

    Returns a tuple: (should_continue, is_correct).
    The early return on 'q' allows exiting the loop from the caller cleanly.
    """
    country, capital = draw_random_question(df)
    console.print(Rule("Question"))

    #difficulty chosen at the start of the game
    if DIFFICULTY == "easy":
        return ask_multiple_choice(df, country, capital)

    if DIFFICULTY == "hard":
        return ask_with_timer(country, capital, seconds=6)

    #default
    return ask_open_answer(country, capital)

def ask_open_answer(country: str, capital: str) -> tuple[bool, bool]:
    """Medium mode: same behavior as your original function."""
    console.print(Panel.fit(f"What is the capital of [bold]{country}[/]?", border_style="magenta"))

    while True:
        user = console.input("Your answer (or 'q' to quit, 'h' for help): ")
        norm = normalize_answer(user)

        #if answer related to dynamic of game
        if norm == "q":
            return False, False
        if norm == "h":
            show_quick_help()
            continue

        is_correct = norm == normalize_answer(capital)
        if is_correct:
            console.print("[green]Correct![/]\n")
        else:
            console.print(f"[red]Incorrect.[/] The capital is [bold]{capital}[/].\n")
        return True, is_correct


def ask_multiple_choice(df: pd.DataFrame, country: str, capital: str) -> tuple[bool, bool]:
    """EASY mode: multiple-choice question."""
    #esay mode gives 4 options: 3 wrong capitals and the correct one
    wrong_options = (
        df[df["Capital"] != capital]
        .sample(3)["Capital"]
        .tolist()
    )

    options = wrong_options + [capital]
    random.shuffle(options)

    console.print(Panel.fit(f"What is the capital of [bold]{country}[/]?", border_style="magenta"))
    for i, opt in enumerate(options, start=1):
        console.print(f"{i}. {opt}")

    user = console.input("Choose 1-4 (or 'q' to quit, 'h' for help): ").strip().lower()
    if user == "q":
        return False, False
    if user == "h":
        show_quick_help()
        #ask capital again
        return ask_multiple_choice(df, country, capital)

    if user.isdigit():
        idx = int(user)
        if 1 <= idx <= 4:
            chosen = options[idx - 1]
            if normalize_answer(chosen) == normalize_answer(capital):
                console.print("[green]Correct![/]\n")
                return True, True
            console.print(f"[red]Incorrect.[/] The capital is [bold]{capital}[/].\n")
            return True, False

    console.print("[red]Invalid choice.[/] This counts as incorrect.\n")
    return True, False

def _timeout_handler(signum, frame):
    raise TimeoutError


def ask_with_timer(country: str, capital: str, seconds: int = 6) -> tuple[bool, bool]:
    """Hard mode: open answer but with a time limit."""
    #6seconds
    console.print(Panel.fit(
        f"You have [bold red]{seconds} seconds[/bold red]!\nWhat is the capital of [bold]{country}[/]?",
        border_style="magenta"
    ))

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(seconds)

    try:
        user = console.input("Your answer (or 'q' to quit, 'h' for help): ")
        signal.alarm(0)  #end timer
    except TimeoutError:
        console.print("[red]Time's up! Incorrect.[/]\n")
        return True, False

    norm = normalize_answer(user)
    if norm == "q":
        return False, False
    if norm == "h":
        show_quick_help()
        # ask capital again (without substracting attempt)
        return ask_with_timer(country, capital, seconds)


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
    """Show game instructions loaded from docs/instructions.md."""
    with open("docs/instructions.md", "r", encoding="utf-8") as f:
        md_text = f.read().strip()

    md = Markdown(md_text)
    console.print(Panel(md, border_style="blue", title="Instructions"))

def show_quick_help() -> None:
    """Short in-game help when the user presses 'h'."""
     console.print(Panel.fit(
        "How to play GeoBingo - Quick Help\n"
        "\n"
        "- You’ll be shown a country. Type its capital.\n"
        "- If you’re correct, a number is drawn. If it’s on your card, "
        "it gets marked like [[bold cyan]7[/bold cyan]].\n"
        "- Get the whole card marked to win BINGO.\n"
        "- You have a limited number of attempts.\n"
        "- Type '[bold cyan]h[/bold cyan]' anytime to see these instructions.\n"
        "- Type '[bold cyan]q[/bold cyan]' to quit.",
        border_style="blue",
        title="Help"
    ))
    #they appear when de user presses h, (at the begining a longer version is displayed)

def choose_difficulty() -> str:
    console.print(Panel("[bold cyan]Choose difficulty level[/bold cyan]"))
    console.print("1. Easy (multiple choice)")
    console.print("2. Medium (normal questions)")
    console.print("3. Hard (normal questions + timer)")

    while True:
        #user is asked which level they want to play
        choice = console.input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return "easy"
        if choice == "2":
            return "medium"
        if choice == "3":
            return "hard"
        console.print("[red]Invalid option.[/] Please choose 1–3.")

def main():
    global DIFFICULTY
    DIFFICULTY = choose_difficulty()

    #different parameters for each level of difficulty
    if DIFFICULTY == "easy":
        max_number = 50          
        attempts_remaining = 7   
    elif DIFFICULTY == "medium":
        max_number = 70
        attempts_remaining = 5
    else:  
        max_number = 99
        attempts_remaining = 4   

    console.rule(f"[bold]Mode:[/] {DIFFICULTY.upper()} (numbers 1..{max_number})")
    show_instructions()

    card = BingoCard(rows=3, cols=7, max_number=max_number)
    card.display_rich()
    try:
        df = load_capitals_dataframe()
    #if csv not found in the folder
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
