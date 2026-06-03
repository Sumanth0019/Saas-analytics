import streamlit as st

from components.notification_center import (
    render_notifications
)


def render_navbar():

    c1, c2, c3 = st.columns(
        [
            6,
            1,
            1
        ]
    )

    with c1:

        st.markdown(
            """
            # 📊 SaaS Analytics
            """
        )

    with c2:

        render_notifications()

    with c3:

        st.write("👤")