import time
import streamlit as st
from brain import generate_social_content

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Social & Media Manager",
    page_icon="🚀",
    layout="wide"
)

# --- BOOT SEQUENCE WALLPAPER & ANIMATION ---
if 'booted' not in st.session_state:
    with st.spinner("⚡ Booting AI Social Manager core systems & loading secure environment..."):
        time.sleep(1.2)
    st.session_state['booted'] = True

# --- HUMAN-LIKE AI MANAGER WIDGET ---
def render_ai_manager_avatar():
    st.markdown(
        """
        <div style="display: flex; align-items: center; background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <div style="font-size: 40px; margin-right: 15px;">🤖</div>
            <div>
                <h4 style="margin: 0; color: #1f1f1f;">Nova — Your AI Operations Manager</h4>
                <p style="margin: 0; font-size: 14px; color: #4f4f4f;">"All systems nominal, Boss! Ready to generate content and collect your Paystack earnings."</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- DASHBOARD HEADER ---
st.title("🚀 AI Social & Media Manager")
st.markdown("Generate professional marketing content and publish directly to your social platforms.")

# Render Nova the AI Manager
render_ai_manager_avatar()

# --- SIDEBAR & MONETIZATION PROMOTION ---
st.sidebar.header("Campaign Settings")
niche = st.sidebar.selectbox("Select Niche", ["Digital Marketing", "E-commerce", "Tech & Software", "Fitness & Health", "Content Creation"])
topic = st.sidebar.text_area("What is your campaign about?", "Launching our new AI-powered platform...")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Partner & Earnings")
st.sidebar.markdown("Upgrade your user access or buy credits via your active Paystack portal:")
st.sidebar.markdown("[Open Paystack Checkout](https://paystack.shop/pay/s52douy9ie)")

# --- MAIN GENERATION WORKFLOW ---
if st.button("Publish & Generate Campaign"):
    with st.spinner("Nova is generating your content and preparing channels..."):
        result = generate_social_content(topic, niche)
        
    st.success("Workflow completed successfully!")
    st.subheader("Generated Content Preview:")
    st.write(result)