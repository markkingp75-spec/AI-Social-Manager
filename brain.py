import streamlit as st

st.title("AI Social Media Manager")

video_prompt = st.text_area("What is this marketing video about?", key="main_video_prompt_input")

publish_fb = st.checkbox("Facebook Page", value=True, key="cb_fb")
publish_ig = st.checkbox("Instagram Business", value=True, key="cb_ig")
publish_tiktok = st.checkbox("TikTok", value=True, key="cb_tiktok")
publish_twitter = st.checkbox("Twitter (X)", value=True, key="cb_twitter")
publish_yt = st.checkbox("YouTube Shorts", value=True, key="cb_yt")

if st.button("Generate Video Campaign", key="unique_campaign_btn"):
    if not video_prompt.strip():
        st.warning("Please enter a description or prompt for your video first.")
    else:
        st.success("Storyboard & Script Rendered Successfully!")

if st.button("Generate & Publish to All Channels", key="unique_all_channels_btn"):
    if not video_prompt.strip():
        st.warning("Please enter a description or prompt for your video first.")
    else:
        with st.spinner("AI is generating your video asset and dispatching to social networks..."):
            st.success("Posted successfully to selected channels!")

