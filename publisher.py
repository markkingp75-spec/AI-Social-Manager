import requests
import streamlit as st


def publish_to_facebook(content):
  # Replace with your Facebook Page Access Token and Page ID from Meta Developer Portal
  page_id = st.secrets.get("FB_PAGE_ID", "")
  access_token = st.secrets.get("FB_ACCESS_TOKEN", "")

  if not page_id or not access_token:
    return "Error: Facebook credentials missing in secrets."

  url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
  payload = {"message": content, "access_token": access_token}

  response = requests.post(url, data=payload)
  if response.status_code == 200:
    return "Successfully published to Facebook!"
  else:
    return f"Facebook API Error: {response.text}"


def publish_to_instagram(content):
  # Instagram requires an IG Business Account ID and access token via Meta Graph API
  ig_user_id = st.secrets.get("IG_USER_ID", "")
  access_token = st.secrets.get("FB_ACCESS_TOKEN", "")

  if not ig_user_id or not access_token:
    return "Error: Instagram credentials missing in secrets."

  # Step 1: Create media container
  container_url = f"https://graph.facebook.com/v18.0/{ig_user_id}/media"
  container_payload = {
      "caption": content,
      "access_token": access_token,
      # Note: For images/videos, a media URL (image_url or video_url) is required by Instagram
  }

  # For text-only or general integration placeholder:
  return "Instagram integration container ready. (Requires image/video asset link for direct publishing)."


def publish_to_tiktok(content):
  # TikTok Content Posting API integration placeholder
  tiktok_token = st.secrets.get("TIKTOK_ACCESS_TOKEN", "")
  if not tiktok_token:
    return "Error: TikTok access token missing in secrets."

  return "TikTok publisher configured."