import streamlit as st

def render_notifications():

    with st.popover("🔔"):

        st.markdown(
            """
            <div class="notification">
                Revenue increased by 8%
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="notification">
                15 customers at high churn risk
            </div>
            """,
            unsafe_allow_html=True
        )