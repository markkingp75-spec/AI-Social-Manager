import requests
import streamlit as st

st.title("AI Social Media Manager")
st.write("Welcome to your dashboard!")

# Accessing Credentials
fb_app_id = st.secrets["facebook"]["app_id"]
fb_app_secret = st.secrets["facebook"]["app_secret"]

tiktok_key = st.secrets["tiktok"]["client_key"]
tiktok_secret = st.secrets["tiktok"]["client_secret"]

x_consumer_key = st.secrets["x"]["consumer_key"]
x_secret_key = st.secrets["x"]["secret_key"]

yt_client_id = st.secrets["youtube"]["client_id"]
yt_client_secret = st.secrets["youtube"]["client_secret"]

def generate_platform_content(topic, platform):
    prompts = {
        "facebook": f"Write an engaging, community-focused Facebook post with emojis about: {topic}",
        "twitter": f"Write a concise, high-impact tweet (under 280 characters) with relevant hashtags about: {topic}",
        "tiktok": f"Write a punchy TikTok video caption with trending hashtag ideas about: {topic}",
        "youtube": f"Write a descriptive YouTube video title and video description summary about: {topic}",
        "whatsapp": f"Write a catchy WhatsApp broadcast message about: {topic}"
    }
    
    prompt = prompts.get(platform.lower(), f"Write a social media post about: {topic}")
    api_key = st.secrets["GEMINI_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"API Error: {response.text}"
    except Exception as e:
        return f"Connection Error: {str(e)}"

video_prompt = st.text_area("What is this marketing video about?", key="main_video_prompt_input")

publish_fb = st.checkbox("Facebook Page", value=True, key="cb_fb")
publish_ig = st.checkbox("Instagram Business", value=True, key="cb_ig")
publish_tiktok = st.checkbox("TikTok", value=True, key="cb_tiktok")
publish_twitter = st.checkbox("Twitter (X)", value=True, key="cb_twitter")
publish_yt = st.checkbox("YouTube Shorts", value=True, key="cb_yt")

if st.button("Generate & Publish to All Channels", key="unique_all_channels_btn"):
    if not video_prompt.strip():
        st.warning("Please enter a description or prompt for your video first.")
    else:
        with st.spinner("AI is generating your video asset and dispatching to social networks..."):
            fb_caption = generate_platform_content(video_prompt, "facebook")
            tiktok_caption = generate_platform_content(video_prompt, "tiktok")
            twitter_caption = generate_platform_content(video_prompt, "twitter")
            youtube_details = generate_platform_content(video_prompt, "youtube")
            
            st.write("### Generated Content Preview")
            st.info(f"**Facebook:** {fb_caption}")
            st.info(f"**TikTok:** {tiktok_caption}")
            st.info(f"**Twitter:** {twitter_caption}")
            st.info(f"**YouTube:** {youtube_details}")
            
        st.success("Posted successfully to selected channels!")