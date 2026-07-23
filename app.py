import streamlit as st
from brain import generate_social_content

st.set_page_config(page_title="AI Social & Media Manager", page_icon="🚀", layout="wide")

# AI Operations Manager Header
st.markdown(
    """
    <div style="display: flex; align-items: center; background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <div style="font-size: 40px; margin-right: 15px;">🤖</div>
        <div>
            <h4 style="margin: 0; color: #1f1f1f;">Nova — Your AI Operations Manager</h4>
            <p style="margin: 0; font-size: 14px; color: #4f4f4f;">"All systems operational! Ready to manage content and handle upgrades."</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🚀 AI Social & Media Manager")

# Sidebar Controls
st.sidebar.header("Campaign Settings")
niche = st.sidebar.selectbox("Select Niche", ["Digital Marketing", "E-commerce", "Tech & Software", "Fitness & Health"])
topic = st.sidebar.text_area("Campaign Topic", "Launching our new platform...")

st.sidebar.markdown("---")
st.sidebar.markdown("💰 **Paystack Checkout:** [Open Link](https://paystack.shop/pay/s52douy9ie)")

# Main Workflow
if st.button("Generate Content"):
    with st.spinner("Nova is processing your request..."):
        result = generate_social_content(topic, niche)
    st.success("Done!")
    st.write(result)