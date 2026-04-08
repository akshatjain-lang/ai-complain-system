import streamlit as st
from model import predict_priority
import pandas as pd

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Complaint AI", layout="centered")

# ------------------ BEIGE THEME STYLE ------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f5f5dc, #e8d8c3, #d6c1a3);
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

h1 {
    text-align: center;
    color: #4b3f2f;
}

textarea {
    border-radius: 10px;
    border: 2px solid #c2a887;
}

button[kind="primary"] {
    background-color: #a67c52;
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1rem;
}

button[kind="primary"]:hover {
    background-color: #8b5e34;
}

.stAlert {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION STORAGE ------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ------------------ UI ------------------
st.title("🤖 AI Complaint Prioritization System")

st.markdown("""
<div style='text-align: center; color: #5c4a36;'>
Enter your complaint below and let AI decide its priority level.
</div>
""", unsafe_allow_html=True)

complaint = st.text_area("Enter your complaint")

if st.button("Predict Priority"):
    if complaint.strip() != "":
        result = predict_priority(complaint)

        # Save to history
        st.session_state.history.append({"Complaint": complaint, "Priority": result})

        if result == "High":
            st.error("🔴 High Priority")
        elif result == "Medium":
            st.warning("🟡 Medium Priority")
        else:
            st.success("🟢 Low Priority")
    else:
        st.warning("Please enter a complaint")

# ------------------ DASHBOARD ------------------
st.markdown("---")
st.subheader("📊 Complaint Dashboard")

if len(st.session_state.history) > 0:
    df = pd.DataFrame(st.session_state.history)

    # Show table
    st.dataframe(df)

    # Count priorities
    priority_counts = df["Priority"].value_counts()

    st.write("### 📈 Priority Distribution")
    st.bar_chart(priority_counts)

    st.write("### 🥧 Priority Pie Chart")
    st.pyplot(priority_counts.plot.pie(autopct='%1.1f%%').figure)

else:
    st.info("No complaints yet. Enter a complaint to see dashboard.")

# ------------------ FOOTER ------------------
st.markdown("""
<hr>
<div style='text-align: center; color: #5c4a36;'>
</div>
""", unsafe_allow_html=True)
