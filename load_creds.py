import os
import json
import streamlit as st
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def load_creds():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform'] # Adjust scopes if needed

    # 1. Attempt to load existing user credentials from Streamlit Secrets or session state
    if "google_user_creds" in st.session_state:
        creds = st.session_state["google_user_creds"]

    # 2. If no valid credentials exist, trigger the Web Application Authorization Flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Parse the secret dictionary directly from your Streamlit dashboard secrets
            client_config = json.loads(st.secrets["google_client_secret"]["web"])
            
            # Use the Web Flow instead of the Installed desktop client flow
            flow = Flow.from_client_config(
                client_config,
                scopes=SCOPES,
                redirect_uri="https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
            )
            
            # Generate the URL where users go to log in to Google
            authorization_url, state = flow.authorization_url(
                access_type='offline',
                include_granted_scopes='true'
            )
            
            st.link_button("🔐 Connect Your Google Account", authorization_url)
            st.info("Please click the button above to authenticate and authorize your social manager app.")
            st.stop() # Halts app execution until they complete authentication

    return creds