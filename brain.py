import streamlit as st
import time
from google import genai
from google.genai import types

# 1. Set up a modern, premium page layout
st.set_page_config(
    page_title="Nexus AI Builder", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Initialize the Gemini Client with your key
client = genai.Client(api_key="AQ.Ab8RN6JorI2FOvw0H1_JkLYwoS1VF1cLGs_SRb3wizPAKR5Hpg")

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