import streamlit as st
import plotly.express as px

from backend.services import get_customers
from ml.segmentation import customer_segmentation


def render_segmentation():

    st.title(
        " Customer Segmentation"
    )

    df = get_customers()

    df = customer_segmentation(df)

    # =====================
    # KPI
    # =====================

    counts = (
        df["Segment Name"]
        .value_counts()
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Budget Customers",
        counts.get(
            "Budget",
            0
        )
    )

    c2.metric(
        "Premium Customers",
        counts.get(
            "Premium",
            0
        )
    )

    c3.metric(
        "Loyal Customers",
        counts.get(
            "Loyal",
            0
        )
    )

    st.divider()

    # =====================
    # Segment Distribution
    # =====================

    fig = px.pie(
        df,
        names="Segment Name",
        title="Customer Segments",
        hole=0.45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================
    # Scatter
    # =====================

    fig = px.scatter(
        df,
        x="Monthly Charges",
        y="CLTV",
        color="Segment Name",
        hover_data=[
            "CustomerID"
        ],
        title="Customer Value Segmentation"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================
    # Segment Table
    # =====================

    segment_filter = st.selectbox(
        "Select Segment",
        [
            "All",
            "Budget",
            "Premium",
            "Loyal"
        ]
    )

    if segment_filter != "All":

        display_df = df[
            df["Segment Name"]
            == segment_filter
        ]

    else:

        display_df = df

    st.dataframe(
        display_df[
            [
                "CustomerID",
                "Monthly Charges",
                "CLTV",
                "Segment Name"
            ]
        ],
        use_container_width=True
    )

    st.download_button(
        " Export Segments",
        display_df.to_csv(
            index=False
        ),
        "customer_segments.csv",
        "text/csv"
    )
