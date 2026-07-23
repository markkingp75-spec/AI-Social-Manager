import os
import streamlit as st
import requests
import json

def generate_social_content(topic, niche, content_type="Digital Marketing Campaign"):
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Error: GEMINI_API_KEY is missing from Streamlit secrets."
        
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    prompt = f"Act as an expert creator. Generate a professional {content_type} for the {niche} niche based on this topic/prompt: {topic}. Include engaging hooks, captions, and structured formatting suitable for social media distribution."
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        res_json = response.json()
        if "candidates" in res_json:
            return res_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"API Response Error: {res_json}"
    except Exception as e:
        return f"Request failed: {str(e)}"