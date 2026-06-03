import os
import joblib
import pandas as pd

from ml.config import FEATURES
from ml.feature_engineering import create_features

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "churn_model.pkl"
)

bundle = joblib.load(MODEL_PATH)


def predict_proba(df):
    # Create engineered features used during training
    df = create_features(df)

    # Keep only training features
    X = pd.get_dummies(
        df[FEATURES],
        drop_first=True
    )

    # Match training columns exactly
    X = X.reindex(
        columns=bundle["columns"],
        fill_value=0
    )

    # Return churn probabilities
    return bundle["model"].predict_proba(X)[:, 1]


def risk_label(prob):
    if prob >= 0.7:
        return "High"

    elif prob >= 0.4:
        return " Medium"

    return "Low"