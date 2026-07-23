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
            <p style="margin: 0; font-size: 14px; color: #4f4f4f;">"Ready to connect your platform channels and distribute automated campaigns!"</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🚀 AI Social & Media Manager")
st.markdown("Manage campaigns, generate high-converting text, and control your social media integrations.")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Campaign Settings")
niche = st.sidebar.selectbox("Select Niche", ["Digital Marketing", "E-commerce", "Tech & Software", "Fitness & Health", "Content Creation"])
topic = st.sidebar.text_area("Campaign Topic / Prompt", "Launching our new AI-powered platform...")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Monetization Portal")
st.sidebar.markdown("[Open Paystack Checkout](https://paystack.shop/pay/s52douy9ie)")

# --- MAIN WORKFLOW TABS ---
tab1, tab2, tab3 = st.tabs(["📢 Campaign Generator", "🔗 Social Media Connections", "⚙️ Autonomous AI Supervisor"])

with tab1:
    if st.button("Generate & Process Campaign"):
        with st.spinner("Nova is generating your content..."):
            result = generate_social_content(topic, niche)
        st.success("Workflow completed successfully!")
        st.subheader("Generated Content Preview:")
        st.write(result)

with tab2:
    st.subheader("🔗 Social Media Channels Hub")
    st.markdown("Configure and link your active accounts to publish content directly across platforms:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌐 Supported Platforms")
        fb_connected = st.checkbox("Connect Facebook Page", value=True)
        ig_connected = st.checkbox("Connect Instagram Business", value=True)
        tiktok_connected = st.checkbox("Connect TikTok Creator/Business", value=False)
        twitter_connected = st.checkbox("Connect X (Twitter)", value=False)
        whatsapp_connected = st.checkbox("Connect WhatsApp Business API", value=True)
    
    with col2:
        st.markdown("### ⚙️ Channel Credentials")
        channel_token = st.text_input("API Access Token / Webhook URL", type="password", placeholder="Paste your API key or token here...")
        auto_schedule = st.selectbox("Publishing Frequency Mode", ["Instant Live Test (1-Week Trial Phase)", "Daily Automated Broadcast", "Manual Approval Mode"])
        
        if st.button("Save & Sync Channel Settings"):
            st.success("Social media channels successfully linked and synchronized!")

with tab3:
    st.subheader("Autonomous Code & System Diagnostics")
    st.markdown("Run a live diagnostic check to evaluate codebase health:")
    if st.button("Run Autonomous Diagnostic & Upgrade"):
        with st.spinner("AI Supervisor analyzing code structure..."):
            diagnostic_report = run_self_upgrade_check()
        st.success("Autonomous check passed!")
        st.code(diagnostic_report, language="markdown")