import streamlit as st

st.set_page_config(page_title="NexCore Startup Operations Checkup", layout="centered")

st.title("NexCore Startup Operations Checkup")
st.subheader("2-Minute Operational Health Diagnostic for Startups")

st.write("Answer a few quick questions to evaluate operational health.")

# -------------------------
# INPUT QUESTIONS
# -------------------------

team_size = st.selectbox(
    "Team Size",
    ["1-3", "4-10", "11-25"]
)

founder_hours = st.selectbox(
    "Founder Weekly Working Hours",
    ["<40", "40-60", "60-80", "80+"]
)

founder_tasks = st.selectbox(
    "Tasks handled directly by founder",
    ["<5", "5-10", "10-20", "20+"]
)

meetings = st.selectbox(
    "Meetings per week",
    ["<5", "5-10", "10-20", "20+"]
)

deadlines = st.selectbox(
    "Missed deadlines this week",
    ["None", "1-2", "3-5", "5+"]
)

process_docs = st.selectbox(
    "Are processes documented?",
    ["Yes clearly", "Partially", "No"]
)

approvals = st.selectbox(
    "Decision approvals mostly handled by",
    ["Team leads", "Shared", "Founder"]
)

# -------------------------
# CALCULATE SCORE
# -------------------------

risk_score = 0

if founder_hours in ["60-80", "80+"]:
    risk_score += 20

if founder_tasks in ["10-20", "20+"]:
    risk_score += 20

if meetings in ["10-20", "20+"]:
    risk_score += 15

if deadlines in ["3-5", "5+"]:
    risk_score += 15

if process_docs == "No":
    risk_score += 20

if approvals == "Founder":
    risk_score += 20

# -------------------------
# BUTTON
# -------------------------

if st.button("Generate Operations Report"):

    st.subheader("Startup Operations Health Report")

    st.metric("Operations Risk Score", risk_score)

    if risk_score <= 30:
        status = "Healthy Operations"
    elif risk_score <= 60:
        status = "Moderate Risk"
    else:
        status = "High Operational Stress"

    st.write("Status:", status)

    st.subheader("Insights")

    if risk_score > 60:
        st.error("Founder dependency and operational overload detected.")

    st.write("Key Observations:")
    st.write("- Founder involved in operational tasks")
    st.write("- Workflow structure may need improvement")
    st.write("- Team execution may depend on founder approvals")

    st.subheader("Recommended Actions")

    st.write("• Delegate repeat operational tasks")
    st.write("• Introduce weekly operations dashboard")
    st.write("• Reduce meeting load and use async updates")
    st.write("• Define clear task ownership")

    st.success("NexCore Operational Diagnostic Complete")