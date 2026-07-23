import streamlit as st
from brain import generate_social_content

st.set_page_config(page_title="AI Social & Media Manager", page_icon="🚀", layout="wide")

# AI Manager Header
st.title("🚀 AI Social & Media Manager")
st.markdown("---")

# Sidebar Controls
st.sidebar.header("Campaign Settings")
niche = st.sidebar.selectbox("Select Niche", ["Digital Marketing", "E-commerce", "Tech & Software", "Fitness & Health"])
topic = st.sidebar.text_area("Campaign Topic", "Launching our new platform...")

st.sidebar.markdown("---")
st.sidebar.markdown("💰 **Paystack Checkout:** [Open Link](https://paystack.shop/pay/s52douy9ie)")

# Main Panel
if st.button("Generate Content"):
    with st.spinner("Generating marketing content..."):
        result = generate_social_content(topic, niche)
    st.success("Done!")
    st.write(result)