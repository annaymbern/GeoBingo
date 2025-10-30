import random
from card import BingoCard
from win_check import is_full_bingo
from draw_capitals import load_capitals_dataframe, normalize_answer, draw_random_question
import pandas as pd


def ask_question_once(df: pd.DataFrame) -> tuple[bool, bool]:
    """Ask one capital question.

    Returns a tuple: (should_continue, is_correct).
    The early return on 'q' allows exiting the loop from the caller cleanly.
    """
    country, capital = draw_random_question(df)
    print(f"What is the capital of {country}?")
    user = input("Your answer (or 'q' to quit): ")
    if normalize_answer(user) == 'q':
        return False, False
    is_correct = normalize_answer(user) == normalize_answer(capital)
    if is_correct:
        print("Correct!\n")
    else:
        print(f"Incorrect. The capital is {capital}.\n")
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


def main():
    # Easy mode reduces the number range to make marking more likely each round.
    max_number = 50
    attempts_remaining = 5  # Lose after 5 incorrect answers.
    print(f"Mode: EASY (numbers 1..{max_number})\n")

    # The BingoCard uses the same max_number to keep drawing consistent with the grid.
    card = BingoCard(rows=3, cols=7, max_number=max_number)
    card.display()
    try:
        # Centralized CSV loading lives in draw_capitals to keep data concerns together.
        df = load_capitals_dataframe()
    except FileNotFoundError as e:
        print(str(e))
        return

    drawn_numbers: set[int] = set()
    print("Type 'q' at any time to quit.\n")
    while True:
        print(f"Attempts left: {attempts_remaining}")
        should_continue, is_correct = ask_question_once(df)
        if not should_continue:
            print("Goodbye!")
            break
        if is_correct:
            number = draw_unique_number(drawn_numbers, max_number=max_number)
            print(f"Number drawn: {number}")
            if card.mark_number(number):
                print("It's on your card! Marked.")
            else:
                print("Not on your card.")
            card.display()
            # Win condition is centralized in win_check for separation of concerns.
            if is_full_bingo(card):
                print("BINGO! You completed the card. Congratulations!")
                break
        else:
            attempts_remaining -= 1
            if attempts_remaining <= 0:
                print("No attempts left. Game over!")
                break


if __name__ == "__main__":
    main()


