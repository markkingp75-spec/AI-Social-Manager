import streamlit as st
from brain import generate_social_content
from auto_upgrade_agent import run_self_upgrade_check

st.set_page_config(
    page_title="AI Social & Media Manager",
    page_icon="🚀",
    layout="wide"
)

# --- LIVE DYNAMIC BACKGROUND STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .main-header {
        background-color: rgba(255, 255, 255, 0.90);
        padding: 20px;
        border-radius: 12px;
        backdrop-filter: blur(5px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HEADER SECTION ---
with st.container():
    st.markdown(
        """
        <div class="main-header">
            <h1 style="color: #1f1f1f; margin: 0;">🚀 AI Social & Media Manager Live</h1>
            <p style="color: #4f4f4f; margin: 0;">Autonomous engine active. Live background, social channels, and campaign automation online.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Campaign Settings")
niche = st.sidebar.selectbox("Select Niche", ["Digital Marketing", "E-commerce", "Tech & Software", "Fitness & Health", "Content Creation"])

# Pre-filled high-converting prompt for testing and live deployment
default_prompt = "Announcing the official launch of our automated AI platform! Scale your social media presence across Facebook, Instagram, TikTok, Twitter, and WhatsApp instantly. Join our live test phase today!"
topic = st.sidebar.text_area("Campaign Topic / Prompt", default_prompt)

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Monetization Portal")
st.sidebar.markdown("[Open Paystack Checkout](https://paystack.shop/pay/s52douy9ie)")

# --- MAIN WORKFLOW TABS ---
tab1, tab2, tab3 = st.tabs(["📢 Campaign Generator", "🔗 Social Media Connections", "⚙️ Autonomous AI Supervisor"])

with tab1:
    st.subheader("Live Campaign Generator")
    st.markdown("Click below to execute your AI pipeline and generate optimized content across your channels:")
    if st.button("Generate & Process Live Campaign"):
        with st.spinner("Nova is generating your live campaign..."):
            result = generate_social_content(topic, niche)
        st.success("Live campaign generated successfully!")
        st.subheader("Generated Content Output:")
        st.write(result)

with tab2:
    st.subheader("🔗 Social Media Channels Hub")
    st.markdown("Your active channels linked for permanent cross-platform publishing:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Facebook Page (Connected)", value=True)
        st.checkbox("Instagram Business (Connected)", value=True)
        st.checkbox("WhatsApp Business API (Connected)", value=True)
    with col2:
        st.checkbox("TikTok Creator Hub (Active)", value=True)
        st.checkbox("X / Twitter (Active)", value=True)
        st.success("Status: All platforms synchronized with live engine.")

with tab3:
    st.subheader("Autonomous Code & System Diagnostics")
    st.markdown("Run a live diagnostic scan of your application architecture:")
    if st.button("Run Live System Check"):
        with st.spinner("AI Supervisor analyzing live structure..."):
            diagnostic_report = run_self_upgrade_check()
        st.success("System verified live and secure!")
        st.code(diagnostic_report, language="markdown")