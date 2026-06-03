import streamlit as st


def render_ai_widget():

    with st.expander(
        "🤖 AI Insights"
    ):

        st.success(
            """
            Churn increased by 3%.

            Enterprise customers
            contribute 48% of revenue.

            Retention improved by 5%.
            """
        )