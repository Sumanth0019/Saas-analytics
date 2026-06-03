import streamlit as st

def render_hero():

    st.markdown("""
    <div style="
        background: linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6,
            #ec4899
        );
        padding:40px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-bottom:20px;
    ">
        <h1>SaaS Business Analytics & Prediction Platform</h1>
        <p>
            Customer Intelligence • Revenue Analytics •
            Churn Prediction • Forecasting
        </p>
    </div>
    """, unsafe_allow_html=True)