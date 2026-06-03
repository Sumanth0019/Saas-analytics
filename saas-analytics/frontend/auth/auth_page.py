import streamlit as st

from backend.auth import (
    login_user,
    signup_user,
    login_with_google
)


def render_auth():

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Signup"
        ]
    )

    with tab1:

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pw"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            success, msg = login_user(
                email,
                password
            )

            if success:

                st.success(msg)

                st.rerun()

            else:

                st.error(msg)

        if st.button(
            "Continue with Google",
            use_container_width=True
        ):

            url = login_with_google()

            if url:

                st.link_button(
                    "Open Google Login",
                    url
                )

    with tab2:

        name = st.text_input(
            "Name"
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            success, msg = signup_user(
                name,
                email,
                password
            )

            if success:

                st.success(msg)

            else:

                st.error(msg)