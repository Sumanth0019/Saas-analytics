import os
import sys
import streamlit as st

# ==================================================
# PROJECT ROOT
# ==================================================

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="SaaS Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# AUTH IMPORTS
# ==================================================

from backend.supabase_client import supabase

from backend.auth import (
    logout,
    restore_session
)

from frontend.auth.auth_page import (
    render_auth
)

# ==================================================
# GOOGLE OAUTH CALLBACK
# ==================================================

params = st.query_params

if "code" in params:

    try:

        code = params["code"]

        session = (
            supabase.auth.exchange_code_for_session(
                {
                    "auth_code": code
                }
            )
        )

        user = session.user

        st.session_state.logged_in = True

        st.session_state.user = {
            "name": (
                user.user_metadata.get(
                    "full_name",
                    user.user_metadata.get(
                        "name",
                        "Google User"
                    )
                )
            ),
            "email": user.email
        }

        st.query_params.clear()

        st.rerun()

    except Exception as e:

        st.error(
            f"Google Login Error: {e}"
        )

# ==================================================
# SESSION STATE
# ==================================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False
    restore_session()

# ==================================================
# SHOW LOGIN PAGE
# ==================================================

if not st.session_state.get(
    "logged_in",
    False
):

    render_auth()

    st.stop()

# ==================================================
# COMPONENTS
# ==================================================

from components.styles import load_css
from components.sidebar import render_sidebar
from components.navbar import render_navbar
#from components.theme_switcher import render_theme_switcher

# ==================================================
# PAGES
# ==================================================

from pages.dashboard import render_dashboard
from pages.upload_analysis import render_upload_analysis
from pages.customer_analytics import render_customer_analytics
from pages.churn_prediction import render_churn_prediction
from pages.segmentation import render_segmentation
from pages.retention_cohort import render_retention_cohort
from pages.profile import render_profile
from pages.settings import render_settings

# ==================================================
# DEFAULT USER
# ==================================================

if "user" not in st.session_state:

    st.session_state.user = {
        "name": "User",
        "email": ""
    }

# ==================================================
# LOAD CSS
# ==================================================

load_css()

# ==================================================
# THEME
# ==================================================

#render_theme_switcher()

# ==================================================
# SIDEBAR
# ==================================================

page, logout_clicked = render_sidebar()

# ==================================================
# NAVBAR
# ==================================================

render_navbar()

# ==================================================
# LOGOUT
# ==================================================

if logout_clicked:

    logout()

    st.rerun()

# ==================================================
# ROUTES
# ==================================================

PAGE_ROUTES = {

    "📈 Dashboard":
        render_dashboard,

    "📂 Upload & Analyze":
        render_upload_analysis,

    "👥 Customer Analytics":
        render_customer_analytics,

    "🔮 Churn Prediction":
        render_churn_prediction,

    "🎯 Segmentation":
        render_segmentation,


    "🔄 Retention Cohort":
        render_retention_cohort,

    "👤 Profile":
        render_profile,

    "⚙️ Settings":
        render_settings,
}

if page == "💳 Transactions":

    st.title(
        "💳 Transactions"
    )

    st.info(
        "Transactions page coming soon."
    )

else:

    PAGE_ROUTES.get(
        page,
        render_dashboard
    )()

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "© 2026 SaaS Business Analytics & Prediction Platform"
)
