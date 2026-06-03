import streamlit as st
import plotly.express as px

from backend.services import get_customers

from backend.analytics import (
    total_customers,
    active_customers,
    churn_rate,
    retention_rate,
    total_revenue,
    average_cltv,
)

from frontend.components.cards import kpi_card
from frontend.components.hero import render_hero
from frontend.components.profile_card import render_profile_card
from frontend.components.quick_actions import render_quick_actions


# =====================================
# Dashboard Page
# =====================================

def render_dashboard():

    df = get_customers()

    render_hero()

    render_kpi_section(df)

    render_quick_actions()

    st.divider()

    render_business_analytics(df)

    st.divider()

    render_customer_insights(df)

    st.divider()

    render_customer_table(df)


# =====================================
# KPI SECTION
# =====================================

def render_kpi_section(df):

    st.subheader("📈 Executive Dashboard")

    metrics = [
        ("Customers", f"{total_customers(df):,}", "+4.2%", ""),
        ("Active", f"{active_customers(df):,}", "+2.1%", ""),
        ("Revenue", f"${total_revenue(df):,.0f}", "+8.4%", ""),
        ("Retention", f"{retention_rate(df):.1f}%", "+1.8%", ""),
        ("Churn", f"{churn_rate(df):.1f}%", "-1.2%", ""),
        ("Avg CLTV", f"${average_cltv(df):,.0f}", "+3.5%", ""),
    ]

    cols = st.columns(len(metrics))

    for col, metric in zip(cols, metrics):
        with col:
            kpi_card(*metric)

    st.markdown("<br>", unsafe_allow_html=True)


# =====================================
# BUSINESS ANALYTICS
# =====================================

def render_business_analytics(df):

    left, right = st.columns([3, 1])

    with right:
        render_profile_card()

    with left:

        st.subheader(" Business Analytics")

        chart1, chart2 = st.columns(2)

        with chart1:

            contract_dist = df["Contract"].value_counts()

            fig = px.pie(
                values=contract_dist.values,
                names=contract_dist.index,
                hole=0.45,
                title="Contract Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with chart2:

            fig = px.histogram(
                df,
                x="Monthly Charges",
                nbins=30,
                title="Revenue Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# =====================================
# CUSTOMER INSIGHTS
# =====================================

def render_customer_insights(df):

    st.subheader(" Customer Insights")

    c1, c2 = st.columns(2)

    with c1:

        churn_breakdown = (
            df["Churn Label"]
            .value_counts()
            .reset_index()
        )

        churn_breakdown.columns = [
            "Status",
            "Count"
        ]

        fig = px.bar(
            churn_breakdown,
            x="Status",
            y="Count",
            title="Customer Churn Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.scatter(
            df,
            x="Monthly Charges",
            y="CLTV",
            color="Churn Label",
            title="CLTV vs Revenue"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =====================================
# CUSTOMER TABLE
# =====================================

def render_customer_table(df):

    st.subheader(" Customer Snapshot")

    cols = [
        "CustomerID",
        "Contract",
        "Monthly Charges",
        "CLTV",
        "Churn Label",
    ]

    available_cols = [
        c for c in cols
        if c in df.columns
    ]

    st.dataframe(
        df[available_cols].head(20),
        use_container_width=True
    )
