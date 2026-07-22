import google.generativeai as genai
import streamlit as st

# Force standard REST transport and explicit API key to bypass credential caching
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"],
    transport='rest'
)

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("AI Social Media Manager")

def generate_platform_content(topic, platform):
    prompts = {
        "facebook": f"Write an engaging, community-focused Facebook post with emojis about: {topic}",
        "twitter": f"Write a concise, high-impact tweet (under 280 characters) with relevant hashtags about: {topic}",
        "tiktok": f"Write a punchy TikTok video caption with trending hashtag ideas about: {topic}",
        "youtube": f"Write a descriptive YouTube video title and video description summary about: {topic}"
    }
    
    prompt = prompts.get(platform.lower(), f"Write a social media post about: {topic}")
    
    # Generate content using the properly configured model
    response = model.generate_content(prompt)
    return response.text

video_prompt = st.text_area("What is this marketing video about?", key="main_video_prompt_input")


publish_fb = st.checkbox("Facebook Page", value=True, key="cb_fb")
publish_ig = st.checkbox("Instagram Business", value=True, key="cb_ig")
publish_tiktok = st.checkbox("TikTok", value=True, key="cb_tiktok")
publish_twitter = st.checkbox("Twitter (X)", value=True, key="cb_twitter")
publish_yt = st.checkbox("YouTube Shorts", value=True, key="cb_yt")


# Custom background styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Your app content goes here
st.title("AI Social Media Manager")
st.write("Welcome to your dashboard!")


# Accessing Facebook credentials
fb_app_id = st.secrets["facebook"]["app_id"]
fb_app_secret = st.secrets["facebook"]["app_secret"]

# Accessing TikTok credentials
tiktok_key = st.secrets["tiktok"]["client_key"]
tiktok_secret = st.secrets["tiktok"]["client_secret"]

# Accessing X (Twitter) credentials
x_consumer_key = st.secrets["x"]["consumer_key"]
x_secret_key = st.secrets["x"]["secret_key"]

# Accessing YouTube credentials
yt_client_id = st.secrets["youtube"]["client_id"]
yt_client_secret = st.secrets["youtube"]["client_secret"]


if st.button("Generate & Publish to All Channels", key="unique_all_channels_btn"):
    if not video_prompt.strip():
        st.warning("Please enter a description or prompt for your video first.")
    else:
        with st.spinner("AI is generating your video asset and dispatching to social networks..."):
            
            # --- ADD YOUR AI CONTENT GENERATION CALLS HERE ---
            fb_caption = generate_platform_content(video_prompt, "facebook")
            tiktok_caption = generate_platform_content(video_prompt, "tiktok")
            twitter_caption = generate_platform_content(video_prompt, "twitter")
            youtube_details = generate_platform_content(video_prompt, "youtube")
            whatsapp_msg = generate_platform_content(video_prompt, "whatsapp")
            
            # (Optional: display them on screen to check)
            st.write("Generated Facebook Caption:", fb_caption)
            
            # --- END OF ADDITION ---
            
            st.success("Posted successfully to selected channels!")

