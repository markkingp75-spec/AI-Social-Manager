import os
from supabase import create_client, Client
import publisher
# Initialize Supabase client using environment variables
# This bypasses hardcoded keys completely!
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY")

supabase: Client = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_social_tokens(user_id: str):
    """
    Bypasses hardcoded keys by grabbing saved social media tokens 
    directly from the database.
    """
    if not supabase:
        return None
    response = supabase.table("user_credentials").select("*").eq("user_id", user_id).execute()
    return response.data[0] if response.data else None

import streamlit as st
import time
from google import genai
from google.genai import types
from load_creds import load_creds
# 1. Set up a modern, premium page layout
st.set_page_config(
    page_title="Nexus AI Builder",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)  # <-- Check if this closing parenthesis is missing!

# 2. Initialize the Gemini Client with your key
# Load your secure Google Cloud credentials
creds = load_creds()

# Initialize the Gemini client using your credentials
import streamlit as st
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def generate_ai_response(prompt_text: str) -> str:
    """Helper function to generate copy, scripts, and code."""
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents=prompt_text
    )
    return response.text

def generate_video_asset(video_prompt: str) -> str:
    """Uses Veo 3.1 to generate an 8-second cinematic vertical video clip with native audio."""
    operation = client.models.generate_videos(
        model="veo-3.1-generate-preview",
        prompt=video_prompt,
        config=types.GenerateVideosConfig(
            aspect_ratio="9:16",     # Perfect for TikTok/Reels
            duration=8,              # 8-second premium clip
            person_generation="allow_adult"
        )
    )

    # Poll the API until the video generation is completed
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)

    # Grab the video result, download, and save it locally
    generated_video = operation.response.generated_videos[0]
    output_filename = "nexus_generated_video.mp4"
    
    # Save the file
    client.files.download(file=generated_video.video)
    generated_video.video.save(output_filename)
    return output_filename

# ==================== PREMIUM SIDEBAR CONTROLS ====================
with st.sidebar:
    st.title("⚡ Nexus Control Panel")
    st.write("Configure your AI asset generation parameters.")
    st.markdown("---")
    
    mode = st.selectbox(
        "What are we building today?",
        ["Social Media Campaign", "Website Landing Page", "Mobile App Structure", "Video Campaign & Script"]
    )
    
    tone = st.select_slider(
        "Tone / Style Brand Identity",
        options=["Witty & Casual", "Creative & Bold", "Highly Professional", "Aggressive Marketing"]
    )
    
    include_emojis = st.checkbox("Optimize with Emojis & Visual Formatting", value=True)

# ==================== MAIN DASHBOARD INTERFACE ====================
st.title(f"🚀 Nexus Builder: {mode}")
st.write(f"Generate high-converting {mode.lower()} assets powered by Google AI.")

# Configure prompts based on dropdown selection
if mode == "Social Media Campaign":
    placeholder = "e.g., An engaging thread about starting a tech company with zero budget..."
    system_instruction = f"Act as an elite social media director. Write a complete promotional post. Tone: {tone}."

elif mode == "Website Landing Page":
    placeholder = "e.g., A modern landing page for an organic meal prep delivery service targeting busy professionals..."
    system_instruction = f"Act as an expert UX/UI Copywriter and Web Designer. Create a complete Website Landing Page Structure. Tone: {tone}."

elif mode == "Mobile App Structure":
    placeholder = "e.g., A minimalist fitness tracking mobile app that gamifies morning workouts..."
    system_instruction = f"Act as a Principal Product Manager and Mobile Architect. Tone: {tone}."

elif mode == "Video Campaign & Script":
    placeholder = "e.g., A 60-second high-energy TikTok/Reels ad script selling premium sneakers in Lagos..."
    system_instruction = f"Act as an award-winning Video Producer. Create a detailed video production blueprint, storyboard, and highly descriptive visual prompts for text-to-video tools. Tone: {tone}."

user_input = st.text_area("Describe your vision or project requirements:", placeholder=placeholder, height=150)

# Main Generation Action
if st.button(f"Generate {mode} Asset ✨", use_container_width=True):
    if not user_input.strip():
        st.warning("Please type in your project requirements first!")
    else:
        with st.spinner("Nexus AI is engineering your blueprint..."):
            try:
                full_prompt = f"{system_instruction}\n\nProject Requirements:\n{user_input}\n\nFormatting: Use Markdown."
                if include_emojis:
                    full_prompt += " Use contextual emojis."
                
                # Store the generated text output in session state so it doesn't vanish on page reload
                st.session_state["generated_text"] = generate_ai_response(full_prompt)
                st.success("✨ Asset Engineered Successfully!")
                
            except Exception as e:
                st.error(f"Engine encountered an error: {e}")

# If we have generated text, display it
if "generated_text" in st.session_state:
    st.markdown("---")
    st.subheader("📋 Generated Asset Blueprint")
    st.markdown(st.session_state["generated_text"])

    # ==================== VIDEO GENERATOR ENGINE (VEO 3.1) ====================
    if mode == "Video Campaign & Script":
        st.markdown("---")
        st.header("🎬 AI Video Renderer (Powered by Veo 3.1)")
        st.write("Ready to make it real? Paste a scene description below to render an 8-second cinematic video with audio.")
        
        video_prompt = st.text_area(
            "Visual Scene Prompt:", 
            placeholder="e.g., Slow motion tracking shot of a young, stylish Nigerian walking down a street in Lagos wearing premium sneakers. Dynamic lighting. Upbeat Afrobeat rhythm playing in the background."
        )
        
        if st.button("Render AI Video Scene 🎥", use_container_width=True):
            if not video_prompt.strip():
                st.warning("Please enter a visual scene prompt first!")
            else:
                with st.spinner("Veo 3.1 is rendering your cinematic video (this can take up to 60 seconds)..."):
                    try:
                        video_file_path = generate_video_asset(video_prompt)
                        st.success("Video Render Complete!")
                        st.video(video_file_path)
                    except Exception as e:
                        st.error(f"Video engine error: {e}")
              # ==========================================
# 🔗 ACCOUNTS & INTEGRATIONS MANAGEMENT
# ==========================================
def render_connections_management():
    st.markdown("---")
    st.subheader("🔗 Connected Integrations")
    st.write("Authorize Nexus to manage campaigns, publish media, and track ad performance autonomously.")
    
    # 1. Define the columns first
    col1, col2, col3 = st.columns(3)
    
    # 2. Render the content inside each column
    with col1:
        st.markdown("### Facebook / Instagram")
        if st.button("Connect Meta Business Account", key="connect_fb"):
            st.info("Initiating secure OAuth handshake with Meta Developers Portal...")
            
    with col2:
        st.markdown("### TikTok")
        if st.button("Connect TikTok Commercial Account", key="connect_tt"):
            st.info("Redirecting to TikTok for Business verification...")
            
    with col3:
        st.markdown("### LinkedIn")
        if st.button("Connect LinkedIn Page", key="connect_li"):
            st.info("Opening secure LinkedIn authorization channel...")
import os
def compile_marketing_video(script_text):
    """
    Uses Gemini to generate a professional, structured video script and storyboard.
    """
    st.info("🎬 Nexus Video Engine: Generating storyboard and script...")
    
    system_prompt = (
        "You are an elite video marketing producer. Convert the user's idea into a highly engaging, "
        "step-by-step video script and storyboard optimized for social media (TikTok/Reels/Shorts). "
        "Format it beautifully with Markdown, using emojis for visuals and bold text for voiceovers."
    )
    
    try:
        response = client.models.generate_content(
            model='gemini-3.1-flash-lite',
            contents=f"{system_prompt}\n\nUser Idea: {script_text}"
        )
        return response.text
    except Exception as e:
        return f"### 🎬 Storyboard Draft\n* **Visual:** Upbeat text overlay.\n* **Voiceover:** 'Nexus has you covered!'\n\n*(Error: {str(e)})*"

# ==========================================
# 🎬 VIDEO GENERATION INTERFACE
# ==========================================
st.markdown("---")  # Adds a clean visual dividing line
st.markdown("### 🎬 Nexus Autonomous Video Creator")
video_prompt = st.text_area("What is this marketing video about?", placeholder="e.g., A 15-second TikTok ad explaining how our software automates database management...")
if st.button("Generate Video Campaign", key="generate_campaign_btn"):
if st.button("Generate Video Campaign", key="generate_video"):
    if video_prompt:
        with st.spinner("Gemini is drafting your high-converting storyboard..."):
            # 1. Get the generated script from Gemini
            video_script = compile_marketing_video(video_prompt)
            
            # 2. Display the success message
            st.success("✨ Storyboard & Script Rendered Successfully!")
            
            # 3. Render the script beautifully in an expander block
            with st.expander("📝 View Generated Storyboard & Voiceover Script", expanded=True):
                st.markdown(video_script)
    else:
        st.warning("Please enter a prompt describing your video asset first!")
# Place this after your AI generation code in brain.py
if 'draft' in st.session_state:
    st.subheader("Review & Publish")
    # This allows you to edit the AI output before posting
    edited_content = st.text_area("Edit your draft:", st.session_state.draft)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Publish to LinkedIn"):
            # This calls the function you just wrote in publisher.py
            success = publisher.publish_to_platform("LinkedIn", edited_content)
            if success: st.success("Published to LinkedIn!")
    with col2:
        if st.button("Publish to Instagram"):
            success = publisher.publish_to_platform("Instagram", edited_content)
            if success: st.success("Published to Instagram!")
            st.markdown("### 🎬 Nexus Autonomous Video Creator")
st.write("Generate high-converting marketing videos and social content powered by AI.")

# User prompt input for the video
video_prompt = st.text_area(
    "What is this marketing video about?",
    placeholder="e.g., A 15-second TikTok ad explaining how our software automates database management"
)

if st.button("Generate Video Asset"):
    if video_prompt.strip() == "":
        st.warning("Please enter a description or prompt for your video first.")
    else:
        with st.spinner("Generating your video script and assets..."):
            # Placeholder for your AI video/script generation logic
            # You can connect this to your Gemini API call
            st.success("Video assets and script successfully generated!")
            
            # Show a mock preview or output box
            st.text_area("Generated Script & Caption Output", value=f"Script for: {video_prompt}\n\n[Scene 1]: Hook the audience with a fast-paced problem statement...\n[Call to Action]: Try our app today!")
st.markdown("### 🚀 Connect Social Channels")
st.write("Link your accounts to push your generated videos directly to your channels.")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Connect Facebook"):
        # Replace with your Meta/Facebook OAuth URL and Client ID
        fb_client_id = "YOUR_FACEBOOK_CLIENT_ID"
        fb_redirect_uri = "https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
        fb_url = f"https://www.facebook.com/v18.0/dialog/oauth?client_id={fb_client_id}&redirect_uri={fb_redirect_uri}&scope=pages_manage_posts,instagram_content_publish"
        st.markdown(f"**[Click here to authorize Facebook]({fb_url})**", unsafe_allow_html=True)

    if st.button("Connect Instagram"):
        # Instagram uses the Meta Graph API (often bundled with Facebook login)
        st.info("Instagram login connects via your Meta Business account authorization.")

with col2:
    if st.button("Connect TikTok"):
        # Replace with your TikTok Client Key
        tiktok_client_key = "YOUR_TIKTOK_CLIENT_KEY"
        tiktok_redirect_uri = "https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
        tiktok_url = "https://www.tiktok.com/v2/auth/authorize/" # Add query parameters for your client key and scope
        st.markdown(f"**[Click here to authorize TikTok]({tiktok_url})**", unsafe_allow_html=True)

    if st.button("Connect Twitter (X)"):
        # Replace with your Twitter Client ID
        twitter_client_id = "YOUR_TWITTER_CLIENT_ID"
        twitter_redirect_uri = "https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
        twitter_url = f"https://twitter.com/i/oauth2/authorize?response_type=code&client_id={twitter_client_id}&redirect_uri={twitter_redirect_uri}&scope=tweet.write%20users.read&state=state&code_challenge=challenge&code_challenge_method=plain"
        st.markdown(f"**[Click here to authorize Twitter (X)]({twitter_url})**", unsafe_allow_html=True)

with col3:
    if st.button("Connect YouTube"):
        try:
            from load_creds import load_creds
            flow = load_creds()
            auth_url, _ = flow.authorization_url(prompt='consent')
            st.markdown(f"**[Click here to authorize YouTube]({auth_url})**", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"YouTube connection failed: {e}")
            import streamlit as st

st.markdown("### 🎬 Nexus Autonomous Video Creator")
video_prompt = st.text_area(
    "What is this marketing video about?",
    placeholder="e.g., A 15-second TikTok ad explaining our software..."
)

if st.button("Generate Video Asset"):
    if video_prompt.strip() == "":
        st.warning("Please enter a description or prompt for your video first.")
    else:
        with st.spinner("Generating your video script and assets..."):
            st.success("Video assets and script successfully generated!")
            st.text_area("Generated Script Output", value=f"Script for: {video_prompt}\n\n[Scene 1]: Engaging intro...\n[CTA]: Try our app today!")

st.markdown("### 🚀 Connect Social Channels")
st.write("Link your accounts to push your generated videos directly to your channels.")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Connect Facebook"):
        fb_client_id = "YOUR_FACEBOOK_CLIENT_ID"
        fb_redirect_uri = "https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
        fb_url = f"https://www.facebook.com/v18.0/dialog/oauth?client_id={fb_client_id}&redirect_uri={fb_redirect_uri}&scope=pages_manage_posts,instagram_content_publish"
        st.markdown(f"**[Click here to authorize Facebook]({fb_url})**", unsafe_allow_html=True)

    if st.button("Connect Instagram"):
        st.info("Instagram login connects via your Meta Business account authorization.")

with col2:
    if st.button("Connect TikTok"):
        tiktok_client_key = "YOUR_TIKTOK_CLIENT_KEY"
        tiktok_url = "https://www.tiktok.com/v2/auth/authorize/"
        st.markdown(f"**[Click here to authorize TikTok]({tiktok_url})**", unsafe_allow_html=True)

    if st.button("Connect Twitter (X)"):
        twitter_client_id = "YOUR_TWITTER_CLIENT_ID"
        twitter_url = f"https://twitter.com/i/oauth2/authorize?response_type=code&client_id={twitter_client_id}&redirect_uri=https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app&scope=tweet.write%20users.read&state=state&code_challenge=challenge&code_challenge_method=plain"
        st.markdown(f"**[Click here to authorize Twitter (X)]({twitter_url})**", unsafe_allow_html=True)

with col3:
    if st.button("Connect YouTube"):
        try:
            from load_creds import load_creds
            flow = load_creds()
            auth_url, _ = flow.authorization_url(prompt='consent')
            st.markdown(f"**[Click here to authorize YouTube]({auth_url})**", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"YouTube connection failed: {e}")
            import streamlit as st

st.markdown("### 🎬 Nexus Autonomous Video Creator")
video_prompt = st.text_area(
    "What is this marketing video about?",
    placeholder="e.g., A 15-second TikTok ad explaining our software..."
)

# Choose platforms to broadcast to automatically
st.markdown("#### Select Target Channels for Autonomous Posting")
publish_fb = st.checkbox("Facebook Page", value=True)
publish_ig = st.checkbox("Instagram Business", value=True)
publish_tiktok = st.checkbox("TikTok", value=True)
publish_twitter = st.checkbox("Twitter (X)", value=True)
publish_yt = st.checkbox("YouTube Shorts", value=True)

if st.button("Generate & Publish to All Channels"):
    if video_prompt.strip() == "":
            if st.button("Generate & Publish to All Channels", key="generate_all_channels_btn"):
    if video_prompt.strip() == "":
        st.warning("Please enter a description or prompt for your video first.")
    else:
        with st.spinner("AI is generating your video asset and dispatching to social networks..."):
            # 1. Simulate or execute AI Video/Content Generation
            generated_script = f"Marketing Campaign: {video_prompt}\n[Visual]: Dynamic product showcase"
            
            # 2. Automated multi-platform dispatch logic loop
            results = []
            if publish_fb:
                results.append("Posted successfully to Facebook Page")
            
            # 1. Simulate or execute AI Video/Content Generation
            generated_script = f"Marketing Campaign: {video_prompt}\n[Visual]: Dynamic product showcase\n[CTA]: Get it now!"
            
            # 2. Automated multi-platform dispatch logic loop
            results = []
            if publish_fb:
                # Insert Meta Graph API call for Facebook posting here
                results.append("✅ Posted successfully to Facebook Page")
            if publish_ig:
                # Insert Instagram Graph API container publish call here
                results.append("✅ Published to Instagram Reels container")
            if publish_tiktok:
                # Insert TikTok Content Posting API call here
                results.append("✅ Dispatched to TikTok queue")
            if publish_twitter:
                # Insert Twitter v2 API tweet endpoint call here
                results.append("✅ Tweeted successfully")
            if publish_yt:
                # Insert YouTube Data API v3 upload call here
                results.append("✅ Uploaded to YouTube Shorts")
            
            st.success("Autonomous campaign execution complete!")
            for res in results:
                st.write(res)
                from apscheduler.schedulers.background import BackgroundScheduler
import streamlit as st

def daily_autonomous_job():
    # This runs automatically every day in the background
    print("Executing daily automated social media campaign...")
    # Add your video generation and publishing logic here

# Check if scheduler is already running to prevent duplicate threads in Streamlit
if "scheduler" not in st.session_state:
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_autonomous_job, 'interval', days=1)
    scheduler.start()
    st.session_state["scheduler"] = scheduler
# 3. Call the function at the absolute bottom (flush left, no indentation)
render_connections_management()


    
    