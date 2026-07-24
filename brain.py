import os
import streamlit as st
from google import genai

def generate_social_content(topic, niche, content_type="Digital Marketing Campaign"):
    # Paste your actual Google AI Studio API key directly here
    api_key = "AIzaSyYourActualApiKeyHere"
    
    if not api_key:
        return "Error: API key is missing."
    
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"Act as an expert creator. Generate a professional {content_type} about {topic} targeting {niche}."
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Request failed: {str(e)}"