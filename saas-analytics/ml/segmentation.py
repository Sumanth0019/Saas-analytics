import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def customer_segmentation(df):

    df = df.copy()

    cols = [
        "Tenure Months",
        "Monthly Charges",
        "Total Charges",
        "CLTV"
    ]

    for col in cols:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

        df[col] = df[col].fillna(
            df[col].median()
        )

    X = df[cols]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Segment"] = model.fit_predict(
        X_scaled
    )

    segment_names = {
        0: "Budget",
        1: "Premium",
        2: "Loyal"
    }

    df["Segment"] = model.fit_predict(
        X_scaled
    )

    segment_labels = {
        0: "Budget",
        1: "Premium",
        2: "Loyal"
    }

    df["Segment Name"] = (
        df["Segment"]
        .map(segment_labels)
    )

    return df