import streamlit as st
import pandas as pd
import plotly.express as px

from ml.predict import (
    predict_proba,
    risk_label,
    FEATURES
)


def render_upload_analysis():

    st.title("📂 Upload & Analyze")

    uploaded = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )

    if uploaded is None:
        st.info(
            "Upload any CSV/XLSX dataset to generate analytics."
        )
        return

    # ==========================================
    # LOAD DATA
    # ==========================================

    try:

        if uploaded.name.endswith(".csv"):

            df = pd.read_csv(uploaded)

        else:

            df = pd.read_excel(uploaded)

    except Exception as e:

        st.error(f"Unable to read file: {e}")
        return

    st.success("Dataset Loaded Successfully")

    # ==========================================
    # DATASET OVERVIEW
    # ==========================================

    st.subheader("📊 Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        len(df)
    )

    c2.metric(
        "Columns",
        len(df.columns)
    )

    c3.metric(
        "Missing Values",
        int(df.isna().sum().sum())
    )

    c4.metric(
        "Duplicates",
        int(df.duplicated().sum())
    )

    # ==========================================
    # PREVIEW
    # ==========================================

    st.subheader("📋 Data Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    # ==========================================
    # COLUMN TYPES
    # ==========================================

    st.subheader("🧾 Column Information")

    info_df = pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        }
    )

    st.dataframe(
        info_df,
        use_container_width=True
    )

    # ==========================================
    # NUMERIC ANALYSIS
    # ==========================================

    numeric_cols = list(
        df.select_dtypes(
            include="number"
        ).columns
    )

    if numeric_cols:

        st.subheader("📈 Numeric Statistics")

        st.dataframe(
            df[numeric_cols].describe(),
            use_container_width=True
        )

    # ==========================================
    # MISSING VALUES
    # ==========================================

    missing = (
        df.isna()
        .sum()
        .reset_index()
    )

    missing.columns = [
        "Column",
        "Missing Values"
    ]

    missing = missing[
        missing["Missing Values"] > 0
    ]

    if not missing.empty:

        st.subheader("⚠ Missing Values")

        fig = px.bar(
            missing,
            x="Column",
            y="Missing Values",
            title="Missing Values by Column"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # CORRELATION
    # ==========================================

    if len(numeric_cols) >= 2:

        st.subheader("🔥 Correlation Heatmap")

        corr = (
            df[numeric_cols]
            .corr()
        )

        fig = px.imshow(
            corr,
            text_auto=".2f",
            aspect="auto"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # DISTRIBUTIONS
    # ==========================================

    if numeric_cols:

        st.subheader("📊 Distribution Analysis")

        selected_num = st.selectbox(
            "Choose Numeric Column",
            numeric_cols
        )

        fig = px.histogram(
            df,
            x=selected_num,
            nbins=30,
            title=f"{selected_num} Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # CATEGORICAL ANALYSIS
    # ==========================================

    cat_cols = list(
        df.select_dtypes(
            exclude="number"
        ).columns
    )

    if cat_cols:

        st.subheader("🏷 Category Analysis")

        selected_cat = st.selectbox(
            "Choose Category Column",
            cat_cols
        )

        counts = (
            df[selected_cat]
            .astype(str)
            .value_counts()
            .head(15)
            .reset_index()
        )

        counts.columns = [
            selected_cat,
            "Count"
        ]

        fig = px.bar(
            counts,
            x=selected_cat,
            y="Count",
            title=f"{selected_cat} Frequency"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # CHURN PREDICTION
    # ==========================================

    st.subheader("🤖 ML Prediction")

    missing_features = [
        col
        for col in FEATURES
        if col not in df.columns
    ]

    if len(missing_features) == 0:

        try:

            probs = predict_proba(df)

            result_df = df.copy()

            result_df["Churn Probability"] = probs

            result_df["Risk"] = (
                result_df[
                    "Churn Probability"
                ].apply(
                    risk_label
                )
            )

            st.success(
                "Churn Prediction Available"
            )

            st.dataframe(
                result_df.head(20),
                use_container_width=True
            )

            st.download_button(
                "📥 Download Predictions",
                result_df.to_csv(
                    index=False
                ),
                file_name="prediction_results.csv",
                mime="text/csv"
            )

        except Exception as e:

            st.warning(
                f"Prediction failed: {e}"
            )

    else:

        st.info(
            "Uploaded dataset does not match churn model features."
        )

    # ==========================================
    # AUTO INSIGHTS
    # ==========================================

    st.subheader("💡 Automated Insights")

    st.write(
        f"""
        • Dataset contains **{len(df):,} rows**

        • Dataset contains **{len(df.columns)} columns**

        • Missing values detected:
        **{df.isna().sum().sum()}**

        • Duplicate rows:
        **{df.duplicated().sum()}**
        """
    )