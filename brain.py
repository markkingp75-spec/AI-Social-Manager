import streamlit as st
from google import genai

st.set_page_config(page_title="AI Social & Media Manager", page_icon="🚀", layout="wide")

st.title("🚀 AI Social & Media Manager")
st.markdown("Generate and publish professional AI marketing copy directly to all your platforms.")

# Sidebar configuration
st.sidebar.header("Campaign Settings")
industry = st.sidebar.selectbox(
    "Select Industry / Niche",
    ["Marketing & Advertising", "Movies & Entertainment", "Technology & SaaS", "E-Commerce", "Real Estate", "Fitness & Health"]
)

content_type = st.sidebar.selectbox(
    "Content Format",
    ["Social Media Post", "Video Script & Concept", "Ad Copy", "Broadcast Message"]
)

topic = st.sidebar.text_area("What is your campaign about?", "Launching a cutting-edge platform for global brands.")

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
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            st.error("GEMINI_API_KEY is missing from Streamlit secrets.")
            st.stop()

        # Initialize the official client
        client = genai.Client(api_key=api_key)

        with st.spinner("Crafting tailored AI campaign content..."):
            for platform in selected_platforms:
                st.subheader(f"📌 {platform} Content")

                custom_prompt = (
                    f"Create an engaging {content_type.lower()} tailored for {platform} "
                    f"within the {industry} industry. The campaign is about: {topic}. "
                    f"Include high-converting hooks, calls to action, and relevant hashtags."
                )

                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=custom_prompt,
                    )
                    st.success(f"Generated successfully for {platform}!")
                    st.write(response.text)
                    st.markdown("---")
                except Exception as e:
                    st.error(f"API Error for {platform}: {e}")

        st.balloons()
        st.success("All selected channels processed successfully!")