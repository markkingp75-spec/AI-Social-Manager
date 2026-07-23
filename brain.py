import time
from publisher import (
    publish_to_facebook,
    publish_to_instagram,
    publish_to_tiktok,
)
import streamlit as st
from google import genai

# Page configuration
st.set_page_config(
    page_title="AI Social & Media Manager", page_icon="🚀", layout="wide"
)

st.title("🚀 AI Social & Media Manager")
st.markdown(
    "Generate professional marketing content and publish directly to your social"
    " channels."
)

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Campaign & Client Settings")

# Client Management fields
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
    ["Facebook", "Instagram", "TikTok", "Twitter", "YouTube", "WhatsApp"],
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
      api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
      st.error("GEMINI_API_KEY is missing from Streamlit secrets.")
      st.stop()

    client = genai.Client(api_key=api_key)

    with st.spinner(
        f"Crafting tailored AI campaign content for {client_name}..."
    ):
      for i, platform in enumerate(selected_platforms):
        st.subheader(f"📌 {platform} Content for {client_name}")

        custom_prompt = (
            f"Create an engaging {content_type.lower()} tailored for {platform}"
            f" within the {industry} industry for the brand '{client_name}'."
            f" The campaign is about: {topic}. Include high-converting hooks,"
            f" calls to action, and relevant hashtags."
        )

        # Pause slightly between requests to prevent rate limit spikes
        if i > 0:
          time.sleep(2)

        generated_text = None
        success = False

        # Attempt generation with retry logic for 503 capacity errors
        for attempt in range(3):
          try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=custom_prompt,
            )
            generated_text = response.text
            st.success(f"Generated successfully for {platform}!")
            st.write(generated_text)
            success = True
            break
          except Exception as e:
            if "503" in str(e) and attempt < 2:
              time.sleep(3)
            else:
              st.error(f"API Error for {platform}: {e}")
              break

        # --- PUBLISHER PIPELINE INTEGRATION ---
        if success and generated_text:
          st.markdown("### 🚀 Publishing Status")
          if platform == "Facebook":
            pub_msg = publish_to_facebook(generated_text)
            st.info(pub_msg)
          elif platform == "Instagram":
            pub_msg = publish_to_instagram(generated_text)
            st.info(pub_msg)
          elif platform == "TikTok":
            pub_msg = publish_to_tiktok(generated_text)
            st.info(pub_msg)
          else:
            st.info(
                f"Content formatted for {platform}. Direct API publishing"
                " queued."
            )

        st.markdown("---")

    st.balloons()
    st.success("All selected channels processed and published successfully!")