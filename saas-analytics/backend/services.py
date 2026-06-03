from backend.database import run_query


COLUMN_MAPPING = {

    "customerid": "CustomerID",

    "gender": "Gender",

    "senior_citizen": "Senior Citizen",

    "partner": "Partner",

    "dependents": "Dependents",

    "tenure_months": "Tenure Months",

    "phone_service": "Phone Service",

    "multiple_lines": "Multiple Lines",

    "internet_service": "Internet Service",

    "online_security": "Online Security",

    "online_backup": "Online Backup",

    "device_protection": "Device Protection",

    "tech_support": "Tech Support",

    "streaming_tv": "Streaming TV",

    "streaming_movies": "Streaming Movies",

    "contract": "Contract",

    "paperless_billing": "Paperless Billing",

    "payment_method": "Payment Method",

    "monthly_charges": "Monthly Charges",

    "total_charges": "Total Charges",

    "churn_label": "Churn Label",

    "churn_value": "Churn Value",

    "churn_score": "Churn Score",

    "cltv": "CLTV",

    "churn_reason": "Churn Reason"
}


def get_customers():

    df = run_query(
        """
        SELECT *
        FROM customers
        """
    )

    return df.rename(
        columns=COLUMN_MAPPING
    )


def get_active_customers():

    df = run_query(
        """
        SELECT *
        FROM customers
        WHERE churn_value = 0
        """
    )

    return df.rename(
        columns=COLUMN_MAPPING
    )


def get_churned_customers():

    df = run_query(
        """
        SELECT *
        FROM customers
        WHERE churn_value = 1
        """
    )

    return df.rename(
        columns=COLUMN_MAPPING
    )