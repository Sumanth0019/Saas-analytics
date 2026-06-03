import pandas as pd


def create_features(df):

    df = df.copy()

    # Convert string column to numeric
    df["Total Charges"] = pd.to_numeric(
        df["Total Charges"],
        errors="coerce"
    )

    # Fill blanks/nulls
    df["Total Charges"] = df["Total Charges"].fillna(0)

    print(df["Total Charges"].dtype)

    # Monthly revenue per month of tenure
    df["Revenue_Per_Month"] = (
        df["Total Charges"] /
        (df["Tenure Months"] + 1)
    )

    # Long term customer flag
    df["Long_Term_Customer"] = (
        df["Tenure Months"] >= 24
    ).astype(int)

    # High value customer flag
    df["High_Value_Customer"] = (
        df["CLTV"] >
        df["CLTV"].median()
    ).astype(int)

    # Contract encoding
    df["Annual_Contract"] = (
        df["Contract"] != "Month-to-month"
    ).astype(int)

    return df