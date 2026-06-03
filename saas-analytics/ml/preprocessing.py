import pandas as pd

from ml.config import FEATURES, TARGET
from ml.feature_engineering import create_features


def preprocess(df):

    df = df.copy()

    df = create_features(df)

    df["Total Charges"] = pd.to_numeric(
        df["Total Charges"],
        errors="coerce"
    )

    df["Total Charges"] = df["Total Charges"].fillna(
        df["Total Charges"].median()
    )

    X = df[FEATURES]

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    y = df[TARGET]

    return X, y