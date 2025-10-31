"""
capitals.py – Script to load and process the capitals.csv dataset.
This utility is used for data preparation and validation, not during gameplay.
"""

import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "capitals.csv")

def load_capitals() -> pd.DataFrame:
    """Load the capitals.csv file and return a pandas DataFrame."""
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"File not found: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    return df

def clean_capitals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize the DataFrame:
    - Strip whitespace
    - Ensure consistent capitalization
    - Drop duplicates or empty rows
    """
    df = df.dropna(subset=["country", "capital"])
    df["country"] = df["country"].str.strip().str.title()
    df["capital"] = df["capital"].str.strip().str.title()
    df = df.drop_duplicates(subset=["country"])
    return df

def save_clean_data(df: pd.DataFrame):
    """Overwrite the capitals.csv file with the cleaned dataset."""
    df.to_csv(DATA_PATH, index=False)
    print(f"Cleaned data saved to {DATA_PATH}")

if __name__ == "__main__":
    df = load_capitals()
    df = clean_capitals(df)
    save_clean_data(df)
