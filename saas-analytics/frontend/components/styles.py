import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* =====================================
       GLOBAL
    ===================================== */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #0f172a,
                #111827,
                #1e293b
            );
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 95%;
    }

    /* =====================================
       SIDEBAR
    ===================================== */

    section[data-testid="stSidebar"] {

        background:
            rgba(
                15,
                23,
                42,
                0.95
            );

        border-right:
            1px solid rgba(
                255,
                255,
                255,
                0.08
            );
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* =====================================
       HERO
    ===================================== */

    .hero {

        background:
            linear-gradient(
                135deg,
                #6366f1,
                #8b5cf6,
                #ec4899
            );

        padding: 3rem;

        border-radius: 24px;

        color: white;

        text-align: center;

        margin-bottom: 1.5rem;

        box-shadow:
            0 15px 40px
            rgba(
                99,
                102,
                241,
                .35
            );
    }

    .hero h1 {

        color: white !important;
    }

    .hero p {

        color: #cbd5e1 !important;
    }

    /* =====================================
       GLASS CARDS
    ===================================== */

    .glass {

        background:
            rgba(
                255,
                255,
                255,
                0.06
            );

        backdrop-filter:none;

        border:
            1px solid rgba(
                255,
                255,
                255,
                .12
            );

        border-radius: 18px;

        padding: 1.2rem;

        box-shadow:
            0 8px 30px rgba(
                0,
                0,
                0,
                .2
            );

        margin-bottom: 1rem;
    }

    /* =====================================
       KPI CARDS
    ===================================== */

    .kpi-card {

        background:rgba(15, 23, 42, 0.9);

        backdrop-filter:none;

        border:
            1px solid rgba(
                255,
                255,
                255,
                .12
            );

        border-radius: 18px;

        padding: 20px;

        text-align: center;

        transition:
            all .3s ease;

        min-height: 150px;
    }

    .kpi-card:hover {

        transform:
            translateY(-6px);

        box-shadow:
            0 12px 35px
            rgba(
                99,
                102,
                241,
                .35
            );
    }

    .kpi-card h3 {

        color: #e2e8f0 !important;
        font-weight: 600;
    }

    .kpi-card h1 {

        color: #ffffff !important;
        font-weight: 700;
    }

    .kpi-card p {

        color: #22c55e;

        font-weight: 600;
    }

    /* =====================================
       METRICS
    ===================================== */

    div[data-testid="metric-container"] {

        background:rgba(15, 23, 42, 0.9);

        border-radius: 16px;

        padding: 1rem;

        border:
            1px solid rgba(
                255,
                255,
                255,
                .1
            );

        box-shadow:
            0 4px 15px rgba(
                0,
                0,
                0,
                .15
            );
    }

    /* =====================================
       BUTTONS
    ===================================== */

    .stButton button {

        background:
            linear-gradient(
                90deg,
                #6366f1,
                #8b5cf6
            );

        color: white;

        border: none;

        border-radius: 12px;

        font-weight: 600;

        transition:
            all .25s ease;
    }

    .stButton button:hover {

        transform:
            scale(1.04);

        box-shadow:
            0 5px 20px rgba(
                99,
                102,
                241,
                .45
            );
    }

    /* =====================================
       FILE UPLOADER
    ===================================== */

    [data-testid="stFileUploader"] {

        border:
            2px dashed #6366f1;

        border-radius: 18px;

        padding: 1rem;

        background:
            rgba(
                99,
                102,
                241,
                .05
            );
    }

    /* =====================================
       TABLES
    ===================================== */

    .stDataFrame {

        border-radius: 14px;

        overflow: hidden;
    }

    /* =====================================
       INPUTS
    ===================================== */

    .stTextInput input,
    .stNumberInput input {

        border-radius: 10px;
    }

    /* =====================================
       STATUS BADGES
    ===================================== */

    .badge-success {

        background: #16a34a;

        color: white;

        padding: 4px 10px;

        border-radius: 10px;

        font-size: .8rem;
    }

    .badge-warning {

        background: #eab308;

        color: black;

        padding: 4px 10px;

        border-radius: 10px;

        font-size: .8rem;
    }

    .badge-danger {

        background: #dc2626;

        color: white;

        padding: 4px 10px;

        border-radius: 10px;

        font-size: .8rem;
    }

    /* =====================================
       NOTIFICATIONS
    ===================================== */

    .notification {

        background:
            rgba(
                99,
                102,
                241,
                .1
            );

        border-left:
            4px solid #6366f1;

        padding: 12px;

        border-radius: 10px;
    }

    /* =====================================
       SCROLLBAR
    ===================================== */

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-thumb {

        background: #6366f1;

        border-radius: 8px;
    }

    /* =====================================
       FOOTER
    ===================================== */

    footer {
        visibility: hidden;
    }
    * {
        opacity: 1 !important;
    }
    """,
    unsafe_allow_html=True)
