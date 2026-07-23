import os
import requests
import json

PAYSTACK_CHECKOUT_LINK = "https://paystack.shop/pay/s52douy9ie"

def generate_social_content(prompt_topic, niche):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return f"Configuration Error: GEMINI_API_KEY secret is missing.\n\n💳 Unlock full access & upgrade your tool: {PAYSTACK_CHECKOUT_LINK}"
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    full_prompt = f"Create a high-converting social media marketing post for the niche: {niche}. Topic: {prompt_topic}."
    payload = {
        "contents": [{
            "parts": [{"text": full_prompt}]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        res_json = response.json()
        
        if "candidates" in res_json:
            raw_text = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return f"{raw_text}\n\n💳 Unlock full access & upgrade your tool: {PAYSTACK_CHECKOUT_LINK}"
        else:
            return f"API Response Error: {str(res_json)}\n\n💳 Upgrade your tool: {PAYSTACK_CHECKOUT_LINK}"
            
    except Exception as e:
        return f"Generation Error: {str(e)}\n\n💳 Upgrade your tool: {PAYSTACK_CHECKOUT_LINK}"