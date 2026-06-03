import streamlit as st
import pandas as pd
import plotly.express as px

from backend.services import get_customers


def render_retention_cohort():

    st.title(
        "🔄 Customer Retention Analysis"
    )

    df = get_customers()

    if df.empty:

        st.warning(
            "No customer data available."
        )

        return

    # =========================
    # TENURE BUCKETS
    # =========================

    df["Retention Group"] = pd.cut(
        pd.to_numeric(
            df["Tenure Months"],
            errors="coerce"
        ),
        bins=[0, 12, 24, 48, 72],
        labels=[
            "0-12 Months",
            "13-24 Months",
            "25-48 Months",
            "49-72 Months"
        ]
    )

    retention = (
        df.groupby(
            "Retention Group"
        )
        .agg(
            Customers=(
                "CustomerID",
                "count"
            ),
            Churned=(
                "Churn Value",
                "sum"
            )
        )
        .reset_index()
    )

    retention["Retained"] = (
        retention["Customers"]
        -
        retention["Churned"]
    )

    retention["Retention %"] = (
        retention["Retained"]
        /
        retention["Customers"]
        * 100
    )

    retention["Churn %"] = (
        retention["Churned"]
        /
        retention["Customers"]
        * 100
    )

    # =========================
    # KPI CARDS
    # =========================

    total_retention = (
        (
            len(
                df[
                    df["Churn Value"] == 0
                ]
            )
            /
            len(df)
        )
        * 100
    )

    avg_tenure = (
        pd.to_numeric(
            df["Tenure Months"],
            errors="coerce"
        )
        .mean()
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Overall Retention",
        f"{total_retention:.1f}%"
    )

    c2.metric(
        "Average Tenure",
        f"{avg_tenure:.1f} Months"
    )

    st.divider()

    # =========================
    # RETENTION CHART
    # =========================

    fig = px.bar(
        retention,
        x="Retention Group",
        y="Retention %",
        text="Retention %",
        title="Retention by Tenure Group"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =========================
    # CHURN CHART
    # =========================

    fig = px.bar(
        retention,
        x="Retention Group",
        y="Churn %",
        text="Churn %",
        title="Churn by Tenure Group"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =========================
    # RETENTION TABLE
    # =========================

    st.subheader(
        "📊 Retention Summary"
    )

    st.dataframe(
        retention,
        use_container_width=True
    )

    st.download_button(
        "📥 Export Retention Report",
        retention.to_csv(
            index=False
        ),
        "retention_report.csv",
        "text/csv"
    )