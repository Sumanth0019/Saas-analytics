import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text

load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL"),
    pool_pre_ping=True
)


def run_query(sql, params=None):

    return pd.read_sql(
        text(sql),
        engine,
        params=params or {}
    )


def execute(sql, params=None):

    with engine.begin() as conn:

        conn.execute(
            text(sql),
            params or {}
        )