import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* =====================================
       GLOBAL
    ===================================== */

    .stApp {
        background: linear-gradient(
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
       FORCE TEXT COLORS
    ===================================== */

    html,
    body,
    p,
    span,
    label,
    small,
    div,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #ffffff !important;
    }

    .stMarkdown,
    .stText,
    .stCaption {
        color: #ffffff !important;
    }

    [data-testid="stMarkdownContainer"] {
        color: #ffffff !important;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] div,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4 {
        color: #ffffff !important;
    }

    /* =====================================
       SIDEBAR
    ===================================== */

    section[data-testid="stSidebar"] {
        background: rgba(
            15,
            23,
            42,
            0.95
        );

        border-right: 1px solid rgba(
            255,
            255,
            255,
            0.08
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* =====================================
       HERO SECTION
    ===================================== */

    .hero {

        background: linear-gradient(
            135deg,
            #0f172a,
            #1e293b
        );

        padding: 3rem;

        border-radius: 24px;

        color: white;

        text-align: center;

        margin-bottom: 1.5rem;

        backdrop-filter: none !important;

        opacity: 1 !important;

        box-shadow:
            0 15px 40px
            rgba(
                99,
                102,
                241,
                0.35
            );
    }

    .hero h1 {

        color: #ffffff !important;

        font-size: 3rem;

        font-weight: 700;

        margin-bottom: 0.5rem;
    }

    .hero p {

        color: #cbd5e1 !important;

        font-size: 1.1rem;
    }

    /* =====================================
       GLASS CARDS
    ===================================== */

    .glass {

        background: rgba(
            255,
            255,
            255,
            0.06
        );

        border: 1px solid rgba(
            255,
            255,
            255,
            0.12
        );

        border-radius: 18px;

        padding: 1.2rem;

        margin-bottom: 1rem;

        backdrop-filter: none !important;

        opacity: 1 !important;

        box-shadow:
            0 8px 30px rgba(
                0,
                0,
                0,
                0.2
            );
    }

    /* =====================================
       KPI CARDS
    ===================================== */

    .kpi-card {

        background: #111827;

        border: 1px solid rgba(
            255,
            255,
            255,
            0.10
        );

        border-radius: 18px;

        padding: 20px;

        text-align: center;

        min-height: 150px;

        opacity: 1 !important;

        backdrop-filter: none !important;

        transition: all 0.3s ease;
    }

    .kpi-card:hover {

        transform: translateY(-5px);

        box-shadow:
            0 12px 35px
            rgba(
                99,
                102,
                241,
                0.35
            );
    }

    .kpi-card h3 {

        color: #e2e8f0 !important;

        font-size: 1rem;

        font-weight: 600;
    }

    .kpi-card h1 {

        color: #ffffff !important;

        font-size: 2rem;

        font-weight: 700;
    }

    .kpi-card p {

        color: #cbd5e1 !important;

        font-weight: 600;
    }

    /* =====================================
       STREAMLIT METRICS
    ===================================== */

    div[data-testid="metric-container"] {

        background: #111827;

        border-radius: 16px;

        padding: 1rem;

        border: 1px solid rgba(
            255,
            255,
            255,
            0.08
        );

        opacity: 1 !important;

        box-shadow:
            0 4px 15px rgba(
                0,
                0,
                0,
                0.15
            );
    }

    div[data-testid="metric-container"] * {
        color: #ffffff !important;
    }

    /* =====================================
       BUTTONS
    ===================================== */

    .stButton button {

        background: linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );

        color: white !important;

        border: none;

        border-radius: 12px;

        font-weight: 600;
    }

    /* =====================================
       INPUTS
    ===================================== */

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div,
    .stMultiSelect div {

        color: white !important;

        border-radius: 10px;
    }

    /* =====================================
       FILE UPLOADER
    ===================================== */

    [data-testid="stFileUploader"] {

        border: 2px dashed #6366f1;

        border-radius: 18px;

        padding: 1rem;

        background: rgba(
            99,
            102,
            241,
            0.05
        );
    }

    /* =====================================
       DATAFRAME
    ===================================== */

    .stDataFrame {

        border-radius: 14px;

        overflow: hidden;
    }

    /* =====================================
       BADGES
    ===================================== */

    .badge-success {

        background: #16a34a;

        color: white;

        padding: 4px 10px;

        border-radius: 10px;

        font-size: 0.8rem;
    }

    .badge-warning {

        background: #eab308;

        color: black;

        padding: 4px 10px;

        border-radius: 10px;

        font-size: 0.8rem;
    }

    .badge-danger {

        background: #dc2626;

        color: white;

        padding: 4px 10px;

        border-radius: 10px;

        font-size: 0.8rem;
    }

    /* =====================================
       REMOVE ANY FADE EFFECTS
    ===================================== */

    * {
        filter: none !important;
    }

    .hero,
    .glass,
    .kpi-card,
    .main,
    .block-container {
        opacity: 1 !important;
        filter: none !important;
        backdrop-filter: none !important;
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

    </style>
    """, unsafe_allow_html=True)
