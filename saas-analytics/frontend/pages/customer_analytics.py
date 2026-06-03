import streamlit as st
import pandas as pd
import plotly.express as px

from backend.services import get_customers


def render_customer_analytics():

    st.title(" Customer Analytics")

    df = get_customers()

    if df.empty:
        st.warning("No customer data found.")
        return

    # ==========================================
    # FILTERS
    # ==========================================

    st.subheader(" Filters")

    f1, f2, f3, f4 = st.columns(4)

    with f1:
        contract_filter = st.multiselect(
            "Contract",
            sorted(df["Contract"].dropna().unique())
        )

    with f2:
        gender_filter = st.multiselect(
            "Gender",
            sorted(df["Gender"].dropna().unique())
        )

    with f3:
        internet_filter = st.multiselect(
            "Internet Service",
            sorted(df["Internet Service"].dropna().unique())
        )

    with f4:
        churn_filter = st.multiselect(
            "Churn Status",
            sorted(df["Churn Label"].dropna().unique())
        )

    filtered_df = df.copy()

    if contract_filter:
        filtered_df = filtered_df[
            filtered_df["Contract"].isin(contract_filter)
        ]

    if gender_filter:
        filtered_df = filtered_df[
            filtered_df["Gender"].isin(gender_filter)
        ]

    if internet_filter:
        filtered_df = filtered_df[
            filtered_df["Internet Service"].isin(
                internet_filter
            )
        ]

    if churn_filter:
        filtered_df = filtered_df[
            filtered_df["Churn Label"].isin(
                churn_filter
            )
        ]

    # ==========================================
    # CLEAN NUMERIC COLUMNS
    # ==========================================

    filtered_df["Monthly Charges"] = pd.to_numeric(
        filtered_df["Monthly Charges"],
        errors="coerce"
    )

    filtered_df["CLTV"] = pd.to_numeric(
        filtered_df["CLTV"],
        errors="coerce"
    )

    # ==========================================
    # KPI SECTION
    # ==========================================

    total_customers = len(filtered_df)

    active_customers = len(
        filtered_df[
            filtered_df["Churn Value"] == 0
        ]
    )

    churned_customers = len(
        filtered_df[
            filtered_df["Churn Value"] == 1
        ]
    )

    churn_rate = (
        churned_customers /
        total_customers * 100
    ) if total_customers else 0

    avg_cltv = filtered_df["CLTV"].mean()

    k1, k2, k3, k4, k5 = st.columns(5)

    k1.metric(
        "Customers",
        f"{total_customers:,}"
    )

    k2.metric(
        "Active",
        f"{active_customers:,}"
    )

    k3.metric(
        "Churned",
        f"{churned_customers:,}"
    )

    k4.metric(
        "Churn Rate",
        f"{churn_rate:.1f}%"
    )

    k5.metric(
        "Avg CLTV",
        f"${avg_cltv:,.0f}"
    )

    st.divider()

    # ==========================================
    # CHARTS
    # ==========================================

    c1, c2 = st.columns(2)

    with c1:

        fig = px.pie(
            filtered_df,
            names="Contract",
            title="Contract Distribution",
            hole=0.45
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.bar(
            filtered_df["Churn Label"]
            .value_counts()
            .reset_index(),
            x="Churn Label",
            y="count",
            title="Customer Churn Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    c3, c4 = st.columns(2)

    with c3:

        fig = px.histogram(
            filtered_df,
            x="Monthly Charges",
            nbins=30,
            title="Monthly Charges Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c4:

        fig = px.histogram(
            filtered_df,
            x="CLTV",
            nbins=30,
            title="CLTV Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ==========================================
    # SCATTER
    # ==========================================

    st.subheader(
        " Customer Value Analysis"
    )

    fig = px.scatter(
        filtered_df,
        x="Monthly Charges",
        y="CLTV",
        color="Churn Label",
        hover_data=["CustomerID"],
        title="Revenue vs CLTV"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # SEARCH
    # ==========================================

    st.subheader(" Search Customer")

    search = st.text_input(
        "Customer ID"
    )

    if search:

        results = filtered_df[
            filtered_df["CustomerID"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

        st.dataframe(
            results,
            use_container_width=True
        )

    else:

        st.dataframe(
            filtered_df.head(100),
            use_container_width=True
        )

    st.download_button(
        "📥 Export Filtered Data",
        filtered_df.to_csv(index=False),
        "customer_analytics.csv",
        "text/csv"
    )
