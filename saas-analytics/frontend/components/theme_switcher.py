import streamlit as st


def render_theme_switcher():

    if "theme" not in st.session_state:

        st.session_state.theme = "Dark"

    theme = st.selectbox(
        "🎨 Theme",
        [
            "Dark",
            "Light"
        ],
        index=0 if st.session_state.theme == "Dark" else 1
    )

    st.session_state.theme = theme

    return theme