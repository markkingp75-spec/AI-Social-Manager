import os
import google.generativeai as genai

# Configure Gemini securely using your Streamlit Secrets environment variable
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)

# Your live Paystack payment link
PAYSTACK_CHECKOUT_LINK = "https://paystack.shop/pay/s52douy9ie"

def generate_social_content(prompt_topic, niche):
    """
    Generates high-converting marketing copy via Gemini AI and embeds your Paystack payment link.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        full_prompt = (
            f"Create a high-converting, professional social media marketing post "
            f"for the niche: {niche}. Topic: {prompt_topic}. "
            f"Keep it engaging and include call-to-action hooks."
        )
        
        response = model.generate_content(full_prompt)
        raw_text = response.text
        
        # Automatically attach your Paystack link to every generated post
        final_post = f"{raw_text}\n\n💳 Unlock full access & upgrade your tool: {PAYSTACK_CHECKOUT_LINK}"
        
        return final_post
        
    except Exception as e:
        return f"Generation Error: {str(e)}"