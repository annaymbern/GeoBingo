import os
import random
from collections import deque
from typing import Deque, Optional, Tuple
d
import pandas as pd


def load_capitals_dataframe() -> pd.DataFrame:
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
            return pd.read_csv(path, sep=";", header=None, names=["Country", "Capital"])
    raise FileNotFoundError("capitals.csv not found in expected locations")


def normalize_answer(text: str) -> str:
    """Normalize user input and dataset values for case/space-insensitive compare."""
    return (text or "").strip().lower()



_QUESTION_POOL: Optional[Deque[Tuple[str, str]]] = None  # no repeats of capitals until all of them have been asked

def _init_pool(df: pd.DataFrame) -> None:
    """Initialize (or reinitialize) the non-repeating question pool."""
    global _QUESTION_POOL
    pairs = list(df[["Country", "Capital"]].itertuples(index=False, name=None))
    random.shuffle(pairs)
    _QUESTION_POOL = deque(pairs)

def draw_random_question(df: pd.DataFrame) -> Tuple[str, str]:
    """Return (country, capital) without repetition until the pool is exhausted.
    When the pool is empty, it automatically resets and starts a new round
    with a different random order.
    """
    global _QUESTION_POOL
    if _QUESTION_POOL is None or not _QUESTION_POOL:
        _init_pool(df)
    return _QUESTION_POOL.popleft()

