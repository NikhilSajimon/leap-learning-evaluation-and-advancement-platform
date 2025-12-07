from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
QUESTIONS_FILE = DATA_DIR / "questions" / "questions.csv"

def load_question_bank() -> pd.DataFrame:
    if QUESTIONS_FILE.exists():
        return pd.read_csv(QUESTIONS_FILE)
    else:
        raise FileNotFoundError(f"Questions file not found at {QUESTIONS_FILE}")
