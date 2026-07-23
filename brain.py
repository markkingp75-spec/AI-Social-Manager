import os
import streamlit as st
import requests
import json

def generate_social_content(topic, niche):
    # Securely retrieve the Gemini API key from Streamlit secrets or environment variables
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Error: GEMINI_API_KEY is missing from Streamlit secrets."
        
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    prompt = f"Create an engaging, high-converting social media post and campaign strategy for the {niche} niche about: {topic}"
    
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