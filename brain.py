import time
from publisher import publish_to_social_media
import streamlit as st
from google import genai

# Page configuration
st.set_page_config(
    page_title="AI Social & Media Manager", page_icon="🚀", layout="wide"
)

st.title("🚀 AI Social & Media Manager")
st.markdown(
    "Generate professional marketing content and publish directly to your social"
    " channels using a single token."
)

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Campaign & Client Settings")

client_name = st.sidebar.text_input("Client / Brand Name", value="My Brand")
industry = st.sidebar.selectbox(
    "Select Industry / Niche",
    [
        "Marketing & Advertising",
        "E-Commerce & Retail",
        "Real Estate",
        "Fitness & Coaching",
        "Food & Restaurant",
        "Technology & SaaS",
    ],
)

content_type = st.sidebar.selectbox(
    "Content Format",
    [
        "Social Media Post",
        "Video Script & Concept",
        "Ad Copy",
        "Broadcast Message",
    ],
)

topic = st.sidebar.text_area(
    "What is your campaign about?",
    "Launching a cutting-edge platform for global brands.",
)

selected_platforms = st.sidebar.multiselect(
    "Select Target Platforms",
    ["Facebook", "Instagram", "TikTok", "Twitter", "YouTube"],
    default=["Facebook", "Instagram", "TikTok"],
)

# --- MAIN EXECUTION BLOCK ---
if st.sidebar.button("Generate & Publish Campaign", type="primary"):
  if not topic.strip():
    st.warning("Please enter a campaign topic.")
  elif not selected_platforms:
    st.warning("Please select at least one platform.")
  else:
    try:
      gemini_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
      st.error("GEMINI_API_KEY is missing from Streamlit secrets.")
      st.stop()

    client = genai.Client(api_key=gemini_key)

    with st.spinner(
        f"Crafting unified AI campaign content for {client_name}..."
    ):
      custom_prompt = (
          f"Create an engaging {content_type.lower()} tailored for multi-platform"
          f" syndication within the {industry} industry for the brand"
          f" '{client_name}'. The campaign is about: {topic}. Include"
          f" high-converting hooks, calls to action, and relevant hashtags."
      )

      try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=custom_prompt,
        )
        generated_text = response.text
        st.success("Campaign content generated successfully!")
        st.write(generated_text)
        st.markdown("---")

        # --- UNIFIED PUBLISHER PIPELINE ---
        st.markdown("### 🚀 Unified Publishing Status")
        pub_msg = publish_to_social_media(generated_text, selected_platforms)
        st.info(pub_msg)

      except Exception as e:
        st.error(f"Generation or Publishing Error: {e}")

    st.balloons()
    st.success("Workflow completed successfully!")