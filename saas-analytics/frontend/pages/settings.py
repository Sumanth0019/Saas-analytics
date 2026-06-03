import streamlit as st


def render_settings():

    st.title("⚙️ Settings")

    dark_mode = st.toggle(
        "Dark Mode",
        value=st.session_state.get(
            "dark_mode",
            False
        )
    )

    st.session_state.dark_mode = dark_mode

    email_alerts = st.checkbox(
        "Email Alerts",
        value=st.session_state.get(
            "email_alerts",
            True
        )
    )

    st.session_state.email_alerts = email_alerts

    weekly_reports = st.checkbox(
        "Weekly Reports",
        value=st.session_state.get(
            "weekly_reports",
            True
        )
    )

    st.session_state.weekly_reports = weekly_reports

    st.success("Settings saved")