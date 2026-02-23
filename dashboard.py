import streamlit as st
import pandas as pd

st.set_page_config(page_title="NexCore Operations Audit", layout="centered")

st.title("NexCore Operations Audit Dashboard")

uploaded_file = st.file_uploader("Upload Task CSV", type=["csv"])

if uploaded_file is not None:

    # Read Data
    df = pd.read_csv(uploaded_file)

    # Core Calculations
    total_hours = df["Hours_Per_Week"].sum()
    founder_hours = df[df["Owner"] == "Founder"]["Hours_Per_Week"].sum()

    if total_hours > 0:
        founder_dependency_score = (founder_hours / total_hours) * 100
    else:
        founder_dependency_score = 0

    health_score = 100 - founder_dependency_score

    workload = df.groupby("Owner")["Hours_Per_Week"].sum()

    average_load = workload.mean()
    max_load = workload.max()

    if average_load > 0:
        imbalance_index = round(max_load / average_load, 2)
    else:
        imbalance_index = 0

    # ===== KPI SECTION =====
    st.subheader("Operational Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Weekly Hours", total_hours)
    col2.metric("Founder Dependency %", round(founder_dependency_score, 2))
    col3.metric("Operational Health Score", round(health_score, 2))

    # Risk Level Logic
    if founder_dependency_score > 60:
        risk_level = "High Risk"
        st.error(f"Risk Level: {risk_level}")
    elif founder_dependency_score > 40:
        risk_level = "Moderate Risk"
        st.warning(f"Risk Level: {risk_level}")
    else:
        risk_level = "Low Risk"
        st.success(f"Risk Level: {risk_level}")

    st.write(f"Role Imbalance Index: {imbalance_index}")

    # ===== WORKLOAD CHART =====
    st.subheader("Workload Distribution")
    st.bar_chart(workload)

    # ===== DELEGATION TABLE =====
    st.subheader("Delegation Candidates")
    founder_tasks = df[df["Owner"] == "Founder"]
    st.dataframe(founder_tasks)

    # Footer
    st.markdown("---")
    st.caption("NexCore Intelligence Engine v1.0 | Founder Scalability Diagnostics")