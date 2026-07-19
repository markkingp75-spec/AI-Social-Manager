import streamlit as st
from google_auth_oauthlib.flow import Flow

# Define the scopes here
SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']

def load_creds():
    # Get the raw configuration
    raw_config = st.secrets["google_client_secret"]["web"]
    
    # Wrap it in a dictionary with the key "web"
    wrapped_config = {"web": raw_config}
    
    # Now pass the wrapped_config to the flow
    flow = Flow.from_client_config(
        wrapped_config,
        scopes=SCOPES,
        redirect_uri="https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
    )
    return flow