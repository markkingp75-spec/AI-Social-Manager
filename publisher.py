import requests
import streamlit as st


def publish_to_social_media(content, platforms):
  """Publishes content across multiple platforms simultaneously using the Zernio API."""
  api_key = st.secrets.get("ZERNIO_API_KEY", "")

  if not api_key:
    return "Error: ZERNIO_API_KEY missing in Streamlit secrets."

  url = "https://zernio.com/api/v1/posts"

  # Map platform names to Zernio identifiers
  platform_mapping = {
      "Facebook": "facebook",
      "Instagram": "instagram",
      "TikTok": "tiktok",
      "Twitter": "twitter",
      "YouTube": "youtube",
  }

  # Format platforms array according to Zernio API structure
  formatted_platforms = []
  for p in platforms:
    key = platform_mapping.get(p)
    if key:
      formatted_platforms.append({"platform": key})

  if not formatted_platforms:
    return "Error: No valid platforms selected for publishing."

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
      return "Successfully published across all selected channels via Zernio!"
    else:
      return f"Zernio API Error: {response.text}"
  except Exception as e:
    return f"Connection Error: {e}"