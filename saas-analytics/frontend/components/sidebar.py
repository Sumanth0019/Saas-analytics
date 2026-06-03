import streamlit as st


def render_sidebar():

    with st.sidebar:

        # =========================
        # BRAND
        # =========================

        st.markdown(
            """
            ## 📊 SaaS Analytics

            <div style="color:#94a3b8;">
                Business Intelligence Platform
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # =========================
        # USER PANEL
        # =========================

        user = st.session_state.get(
            "user",
            {
                "name": "Guest User",
                "email": "guest@example.com"
            }
        )

        st.subheader("👤 User")

        st.write(
            user["name"]
        )

        st.caption(
            user["email"]
        )

        st.success("Active")

        st.divider()

        # =========================
        # NAVIGATION
        # =========================

        page = st.radio(
            "Navigation",
            [
                "📈 Dashboard",

                "📂 Upload & Analyze",

                "👥 Customer Analytics",

                "🔮 Churn Prediction",

                "🎯 Segmentation",

                "🔄 Retention Cohort",

                "👤 Profile",

                "⚙️ Settings"
            ],
            label_visibility="collapsed"
        )

        st.divider()

        # =========================
        # QUICK ACTIONS
        # =========================

        st.markdown(
            "### ⚡ Quick Actions"
        )

        if st.button(
            "🔄 Refresh Data",
            use_container_width=True
        ):
            st.rerun()

        st.button(
            "📤 Export Report",
            use_container_width=True
        )

        st.button(
            "📥 Download Analytics",
            use_container_width=True
        )

        st.divider()

        # =========================
        # NOTIFICATIONS
        # =========================

        st.markdown(
            "### 🔔 Notifications"
        )

        st.info(
            "15 High-Risk Customers"
        )

        st.success(
            "Revenue ↑ 8.2%"
        )

        st.warning(
            "Forecast Updated"
        )

        st.divider()

        # =========================
        # SYSTEM INFO
        # =========================

        st.caption(
            "Version 1.0.0"
        )

        st.caption(
            "Powered by Streamlit + Supabase"
        )

        st.divider()

        # =========================
        # LOGOUT
        # =========================

        logout_clicked = st.button(
            "🚪 Logout",
            use_container_width=True
        )

        return page, logout_clicked