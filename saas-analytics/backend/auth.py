import streamlit as st

from backend.supabase_client import supabase


# ==========================================
# SIGNUP
# ==========================================

def signup_user(
    name,
    email,
    password
):

    try:

        result = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
                "options": {
                    "data": {
                        "name": name
                    }
                }
            }
        )

        return (
            True,
            "Account created successfully. Please verify your email."
        )

    except Exception as e:

        return False, str(e)


# ==========================================
# LOGIN
# ==========================================

def login_user(
    email,
    password
):

    try:

        result = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )

        st.session_state.logged_in = True

        st.session_state.user = result.user

        return True, "Login Successful"

    except Exception as e:

        return False, str(e)


# ==========================================
# GOOGLE LOGIN
# ==========================================

def login_with_google():

    try:

        response = (
            supabase.auth.sign_in_with_oauth(
                {
                    "provider": "google",
                    "options": {
                        "redirect_to":
                        "https://saas-analytics.streamlit.app/"
                    }
                }
            )
        )

        return response.url

    except Exception as e:

        print("Google Login Error:", e)

        return None


# ==========================================
# RESTORE SESSION
# ==========================================

def restore_session():

    try:

        session = supabase.auth.get_session()

        if (
            session
            and
            session.session
            and
            session.session.user
        ):

            st.session_state.logged_in = True

            st.session_state.user = (
                session.session.user
            )

            return True

    except Exception as e:

        print(
            "Session Restore Error:",
            e
        )

    return False


# ==========================================
# LOGOUT
# ==========================================

def logout():

    try:

        supabase.auth.sign_out()

    except Exception:

        pass

    st.session_state.clear()
