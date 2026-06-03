def total_customers(df):

    return len(df)


def active_customers(df):

    return len(
        df[df["Churn Value"] == 0]
    )


def churned_customers(df):

    return len(
        df[df["Churn Value"] == 1]
    )


def churn_rate(df):

    return (
        churned_customers(df)
        / len(df)
    ) * 100


def retention_rate(df):

    return (
        active_customers(df)
        / len(df)
    ) * 100


def total_revenue(df):

    return df[
        "Monthly Charges"
    ].sum()


def average_revenue(df):

    return df[
        "Monthly Charges"
    ].mean()


def average_cltv(df):

    return df[
        "CLTV"
    ].mean()


def average_tenure(df):

    return df[
        "Tenure Months"
    ].mean()