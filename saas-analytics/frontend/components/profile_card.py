import streamlit as st

def render_profile_card():

    user = st.session_state.get(
        "user",
        {
            "name": "Guest User",
            "email": "guest@example.com"
        }
    )

    with st.container(border=True):

        st.subheader("👤 Profile")

        st.write(
            f"**Name:** {user['name']}"
        )

        st.write(
            f"**Email:** {user['email']}"
        )

        st.success("Active")