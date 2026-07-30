from pathlib import Path

import pandas as pd


DATA_FOLDER = Path(__file__).resolve().parents[2] / "data"
JOBS_FILE = DATA_FOLDER / "jobs_raw.parquet"


df = pd.read_parquet(JOBS_FILE)

print("Total rows:", len(df))
print("Total columns:", len(df.columns))

print("\nColumn names:")
for column in df.columns:
    print(column)