import streamlit as st

def kpi_card(
    title,
    value,
    delta=None,
    icon="📊"
):

    st.metric(
        label=f"{icon} {title}",
        value=value,
        delta=delta
    )