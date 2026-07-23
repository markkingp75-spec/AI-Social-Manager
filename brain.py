import os
import google.generativeai as genai

# Configure Gemini AI
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)

PAYSTACK_CHECKOUT_LINK = "https://paystack.shop/pay/s52douy9ie"

def generate_social_content(prompt_topic, niche):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        full_prompt = f"Create a high-converting social media marketing post for the niche: {niche}. Topic: {prompt_topic}."
        response = model.generate_content(full_prompt)
        return f"{response.text}\n\n💳 Unlock full access & upgrade your tool: {PAYSTACK_CHECKOUT_LINK}"
    except Exception as e:
        return f"Generation Error: {str(e)}"