import streamlit as st

def render_profile():

    st.title("👤 Profile")

    user = st.session_state.get(
        "user",
        {}
    )

    st.info(
        f"""
        Name:
        {user.get('name','')}

        Email:
        {user.get('email','')}
        """
    )