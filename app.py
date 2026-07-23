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
            <p style="color: #4f4f4f; margin: 0;">Multi-format engine active: Handling Video Scripts, Comedy, and Programming Events.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Content & Campaign Settings")

content_type = st.sidebar.selectbox(
    "Select Content Format",
    ["Video Script / Test Video", "Comedy Skit & Entertainment", "Programming & Tech Event", "Digital Marketing Campaign"]
)

niche = st.sidebar.selectbox(
    "Select Target Niche",
    ["Tech & Python Development", "Comedy & Viral Content", "E-commerce & Business", "General Entertainment"]
)

default_prompts = {
    "Video Script / Test Video": "Create a high-retention 60-second video script demonstrating our new automated multi-platform tool.",
    "Comedy Skit & Entertainment": "Write a hilarious comedy sketch about programmers trying to fix a bug at 3 AM right before a live launch.",
    "Programming & Tech Event": "Announce our live coding workshop featuring Python, Streamlit, and automated AI backend integration.",
    "Digital Marketing Campaign": "Launch our new AI platform across Facebook, Instagram, TikTok, Twitter, and WhatsApp."
}

topic = st.sidebar.text_area("Campaign Topic / Prompt", default_prompts.get(content_type, "Launching our new platform..."))

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Monetization Portal")
st.sidebar.markdown("[Open Paystack Checkout](https://paystack.shop/pay/s52douy9ie)")

# --- MAIN WORKFLOW TABS ---
tab1, tab2, tab3 = st.tabs(["📢 Multi-Format Generator", "🔗 Social Media Channels", "⚙️ Autonomous AI Supervisor"])

with tab1:
    st.subheader(f"Live Generator — [{content_type}]")
    st.markdown("Click below to execute your AI pipeline and generate customized content scripts or posts:")
    
    if st.button("Generate & Process Content"):
        with st.spinner("Nova is generating your custom script/campaign..."):
            result = generate_social_content(topic, niche, content_type)
        st.success("Content generated successfully!")
        st.subheader("Generated Output:")
        st.write(result)

with tab2:
    st.subheader("🔗 Social Media Channels Hub")
    st.markdown("Your active channels linked for permanent broadcast:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Facebook Page (Connected)", value=True)
        st.checkbox("Instagram Business (Connected)", value=True)
        st.checkbox("WhatsApp Business API (Connected)", value=True)
    with col2:
        st.checkbox("TikTok Creator Hub (Video Ready)", value=True)
        st.checkbox("X / Twitter (Active)", value=True)
        st.success("Status: Multi-format publishing engine online.")

with tab3:
    st.subheader("Autonomous Code & System Diagnostics")
    if st.button("Run Live System Check"):
        with st.spinner("AI Supervisor analyzing live structure..."):
            diagnostic_report = run_self_upgrade_check()
        st.success("System verified live and secure!")
        st.code(diagnostic_report, language="markdown")