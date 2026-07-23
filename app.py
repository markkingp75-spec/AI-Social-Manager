import streamlit as st
from brain import generate_social_content

st.set_page_config(
    page_title="AI Social & Media Manager",
    page_icon="🚀",
    layout="wide"
)

# --- AI OPERATIONS MANAGER (NOVA) ---
st.markdown(
    """
    <div style="display: flex; align-items: center; background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <div style="font-size: 40px; margin-right: 15px;">🤖</div>
        <div>
            <h4 style="margin: 0; color: #1f1f1f;">Nova — Your AI Operations Manager</h4>
            <p style="margin: 0; font-size: 14px; color: #4f4f4f;">"All systems operational, Boss! Ready to handle content generation and track your upgrades."</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🚀 AI Social & Media Manager")
st.markdown("Manage, generate, and distribute professional marketing campaigns across your connected channels.")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Campaign Settings")
niche = st.sidebar.selectbox("Select Niche", ["Digital Marketing", "E-commerce", "Tech & Software", "Fitness & Health", "Content Creation"])
topic = st.sidebar.text_area("Campaign Topic / Prompt", "Launching our new AI-powered platform...")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Monetization & Upgrades")
st.sidebar.markdown("Upgrade your user access via your active Paystack portal:")
st.sidebar.markdown("[Open Paystack Checkout](https://paystack.shop/pay/s52douy9ie)")

# --- MAIN WORKFLOW PANEL ---
if st.button("Generate & Process Campaign"):
    with st.spinner("Nova is generating your content and preparing channels..."):
        result = generate_social_content(topic, niche)
        
    st.success("Workflow completed successfully!")
    st.subheader("Generated Content Preview:")
    st.write(result)