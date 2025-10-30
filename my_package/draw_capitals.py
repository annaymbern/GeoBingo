import os
import pandas as pd


def load_capitals_dataframe():
    """Load the capitals CSV, trying common relative locations.

    Multiple candidates support running from project root or module path
    without requiring a fixed working directory.
    """
    base_dir = os.path.dirname(__file__)
    candidates = [
        os.path.normpath(os.path.join(base_dir, "../data/capitals.csv")),
        os.path.normpath(os.path.join(base_dir, "data/capitals.csv")),
        "../data/capitals.csv",
        "data/capitals.csv",
    ]
    for path in candidates:
        if os.path.exists(path):
            return pd.read_csv(path, sep=';', header=None, names=["Country", "Capital"])
    raise FileNotFoundError("capitals.csv not found in expected locations")


def normalize_answer(text: str) -> str:
    """Normalize user input and dataset values for case/space-insensitive compare."""
    return (text or "").strip().lower()


def draw_random_question(df: pd.DataFrame) -> tuple[str, str]:
    """Pick a random (country, capital) pair.

    Repetition is allowed by design to keep gameplay simple and endless.
    """
    row = df.sample(1).iloc[0]
    return row["Country"], row["Capital"]
