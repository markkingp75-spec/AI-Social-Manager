import streamlit as st
from google_auth_oauthlib.flow import Flow

# Define the scopes here
SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']



def load_creds():
    # Access the 'web' dictionary inside the 'google_client_secret' section
    web_config = st.secrets["google_client_secret"]["web"]
    
    # Now use these values to construct your flow
    flow = Flow.from_client_config(
        web_config,
        scopes=SCOPES,
        redirect_uri="https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
    )
    return flow