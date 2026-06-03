import streamlit as st

def render_quick_actions():

    st.markdown(
        """
        <div class="glass">
        <h3>⚡ Quick Actions</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1,c2,c3 = st.columns(3)

    with c1:

        st.button(
            "📂 Upload Dataset",
            use_container_width=True
        )

    with c2:

        st.button(
            "📈 Generate Report",
            use_container_width=True
        )

    with c3:

        st.button(
            "📥 Export Results",
            use_container_width=True
        )