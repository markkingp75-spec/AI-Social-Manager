import requests
import streamlit as st


def publish_to_social_media(content, platforms):
  """Publishes content across selected platforms using Zernio API."""
  api_key = st.secrets.get("ZERNIO_API_KEY", "")

  if not api_key:
    return "Error: ZERNIO_API_KEY is missing from Streamlit secrets."

  url = "https://zernio.com/api/v1/posts"

  platform_mapping = {
      "TikTok": "tiktok",
      "Facebook": "facebook",
      "Instagram": "instagram",
      "Twitter": "twitter",
      "YouTube": "youtube",
  }

  formatted_platforms = []
  for p in platforms:
    key = platform_mapping.get(p)
    if key:
      formatted_platforms.append({"platform": key})

  if not formatted_platforms:
    return "Error: No valid platforms selected."

  payload = {
      "content": content,
      "platforms": formatted_platforms,
      "publishNow": True,
  }

  headers = {
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json",
  }

  try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
      return "Successfully published via Zernio!"
    else:
      return f"Zernio API Error: {response.text}"
  except Exception as e:
    return f"Connection Error: {e}"