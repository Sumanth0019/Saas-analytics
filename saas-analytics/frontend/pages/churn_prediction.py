import streamlit as st
import pandas as pd

from ml.predict import (
    predict_proba,
    risk_label
)


def render_churn_prediction():

    st.title("🔮 Customer Churn Prediction")

    st.markdown(
        """
        Predict customer churn risk using the
        trained machine learning model.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        senior_citizen = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

        partner = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

        phone_service = st.selectbox(
            "Phone Service",
            ["No", "Yes"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        online_security = st.selectbox(
            "Online Security",
            ["No", "Yes"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No", "Yes"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["No", "Yes"]
        )

    with col2:

        tech_support = st.selectbox(
            "Tech Support",
            ["No", "Yes"]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No", "Yes"]
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["No", "Yes"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

        tenure_months = st.slider(
            "Tenure Months",
            0,
            72,
            12
        )

        monthly_charges = st.slider(
            "Monthly Charges",
            0.0,
            150.0,
            70.0
        )

        cltv = st.number_input(
            "CLTV",
            min_value=0,
            value=4000
        )

    st.divider()

    if st.button(
        "🚀 Predict Churn",
        use_container_width=True
    ):

        total_charges = (
            monthly_charges *
            tenure_months
        )

        input_df = pd.DataFrame([
            {
                "Gender": gender,
                "Senior Citizen": senior_citizen,
                "Partner": partner,
                "Dependents": dependents,
                "Tenure Months": tenure_months,
                "Phone Service": phone_service,
                "Multiple Lines": multiple_lines,
                "Internet Service": internet_service,
                "Online Security": online_security,
                "Online Backup": online_backup,
                "Device Protection": device_protection,
                "Tech Support": tech_support,
                "Streaming TV": streaming_tv,
                "Streaming Movies": streaming_movies,
                "Contract": contract,
                "Paperless Billing": paperless_billing,
                "Payment Method": payment_method,
                "Monthly Charges": monthly_charges,
                "Total Charges": total_charges,
                "CLTV": cltv
            }
        ])

        try:

            probability = float(
                predict_proba(input_df)[0]
            )

            risk = risk_label(
                probability
            )

            st.success(
                "Prediction Complete"
            )

            k1, k2, k3 = st.columns(3)

            with k1:
                st.metric(
                    "Churn Probability",
                    f"{probability:.2%}"
                )

            with k2:
                st.metric(
                    "Risk Level",
                    risk
                )

            with k3:
                st.metric(
                    "Retention Chance",
                    f"{1-probability:.2%}"
                )

            st.progress(probability)

            st.divider()

            st.subheader(
                "💡 Retention Recommendations"
            )

            recommendations = []

            if contract == "Month-to-month":
                recommendations.append(
                    "Offer annual contract discount."
                )

            if monthly_charges > 90:
                recommendations.append(
                    "Provide loyalty discount."
                )

            if tech_support == "No":
                recommendations.append(
                    "Offer premium tech support."
                )

            if online_security == "No":
                recommendations.append(
                    "Promote security add-ons."
                )

            if tenure_months < 12:
                recommendations.append(
                    "Increase customer engagement."
                )

            if probability > 0.70:
                recommendations.append(
                    "Immediate retention campaign recommended."
                )

            if not recommendations:
                recommendations.append(
                    "Customer appears stable."
                )

            for rec in recommendations:
                st.info(rec)

            st.divider()

            st.subheader(
                "📋 Customer Profile"
            )

            st.dataframe(
                input_df,
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"Prediction failed: {e}"
            )