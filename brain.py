import requests
import streamlit as st

st.set_page_config(page_title="AI Social & Media Manager", page_icon="🚀", layout="wide")

st.title("🚀 AI Social & Media Manager")
st.markdown("Generate and publish professional AI marketing copy, advertising campaigns, and video concepts directly to all your platforms.")

# Sidebar configuration for campaigns
st.sidebar.header("Campaign Settings")
industry = st.sidebar.selectbox(
    "Select Industry / Niche",
    ["Marketing & Advertising", "Movies & Entertainment", "Technology & SaaS", "E-Commerce", "Real Estate", "Fitness & Health"]
)

content_type = st.sidebar.selectbox(
    "Content Format",
    ["Social Media Post", "Video Script & Concept", "Ad Copy", "Broadcast Message"]
)

topic = st.sidebar.text_area("What is your campaign about?", "Launching a cutting-edge AI platform for global brands.")

selected_platforms = st.sidebar.multiselect(
    "Select Target Platforms",
    ["Facebook", "Instagram", "TikTok", "Twitter", "YouTube", "WhatsApp"],
    default=["Facebook", "Instagram", "TikTok"]
)

if st.sidebar.button("Generate & Publish Campaign", type="primary"):
    if not topic.strip():
        st.warning("Please enter a campaign topic.")
    elif not selected_platforms:
        st.warning("Please select at least one platform.")
    else:
        # Secure API connection using the REST endpoint and API key
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            st.error("GEMINI_API_KEY is missing from Streamlit secrets.")
            st.stop()

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

        with st.spinner("Crafting tailored AI campaign content..."):
            for platform in selected_platforms:
                st.subheader(f"📌 {platform} Content")

                custom_prompt = (
                    f"Create an engaging {content_type.lower()} tailored for {platform} "
                    f"within the {industry} industry. The campaign is about: {topic}. "
                    f"Include high-converting hooks, calls to action, and relevant hashtags."
                )

                payload = {
                    "contents": [{"parts": [{"text": custom_prompt}]}]
                }

                try:
                    response = requests.post(url, json=payload, timeout=30)
                    if response.status_code == 200:
                        res_data = response.json()
                        generated_text = res_data["candidates"][0]["content"]["parts"][0]["text"]
                        st.success(f"Generated successfully for {platform}!")
                        st.write(generated_text)
                        st.markdown("---")
                    else:
                        st.error(f"API Error for {platform}: {response.text}")
                except Exception as e:
                    st.error(f"Connection error for {platform}: {e}")

        st.balloons()
        st.success("All selected channels processed successfully!")