import pandas as pd

from backend.database import engine

import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FILE_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "data",
    "telco_churn.xlsx"
)

df = pd.read_excel(FILE_PATH)

df.columns = [
    c.lower()
     .replace(" ", "_")
     .replace("-", "_")
    for c in df.columns
]

print(df.head())

df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"Imported {len(df)} rows successfully"
)