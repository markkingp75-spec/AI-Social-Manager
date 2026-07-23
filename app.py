import streamlit as st
from brain import generate_social_content
from auto_upgrade_agent import run_self_upgrade_check

st.set_page_config(
    page_title="AI Social & Media Manager",
    page_icon="🚀",
    layout="wide"
)

# --- AI OPERATIONS MANAGER & AUTONOMOUS AGENT ---
st.markdown(
    """
    <div style="display: flex; align-items: center; background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <div style="font-size: 40px; margin-right: 15px;">🤖</div>
        <div>
            <h4 style="margin: 0; color: #1f1f1f;">Nova & Autonomous Code Supervisor — Active</h4>
            <p style="margin: 0; font-size: 14px; color: #4f4f4f;">"Self-upgrading engine is active in the background. Monitoring state changes automatically."</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🚀 AI Social & Media Manager")
st.markdown("Manage campaigns, generate high-converting text, and monitor autonomous system upgrades.")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Campaign Settings")
niche = st.sidebar.selectbox("Select Niche", ["Digital Marketing", "E-commerce", "Tech & Software", "Fitness & Health", "Content Creation"])
topic = st.sidebar.text_area("Campaign Topic / Prompt", "Launching our new AI-powered platform...")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Monetization Portal")
st.sidebar.markdown("[Open Paystack Checkout](https://paystack.shop/pay/s52douy9ie)")

# --- MAIN WORKFLOW PANEL ---
tab1, tab2 = st.tabs(["📢 Campaign Generator", "⚙️ Autonomous AI Supervisor"])

with tab1:
    if st.button("Generate & Process Campaign"):
        with st.spinner("Nova is generating your content..."):
            result = generate_social_content(topic, niche)
        st.success("Workflow completed successfully!")
        st.subheader("Generated Content Preview:")
        st.write(result)

with tab2:
    st.subheader("Autonomous Code & System Diagnostics")
    st.markdown("Run a live diagnostic check to let the AI agent evaluate codebase health and apply automated optimizations:")
    if st.button("Run Autonomous Diagnostic & Upgrade"):
        with st.spinner("AI Supervisor analyzing code structure..."):
            diagnostic_report = run_self_upgrade_check()
        st.success("Autonomous check passed!")
        st.code(diagnostic_report, language="markdown")