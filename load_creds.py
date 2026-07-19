import json
import streamlit as st
from google_auth_oauthlib.flow import Flow
# Define the scopes your app needs
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly'] # Replace with your actual required scopes

def load_creds():
    # Load the entire JSON string from the new secret
    client_config = json.loads(st.secrets["GOOGLE_CLIENT_SECRETS"])

    flow = Flow.from_client_config(
        client_config,
        scopes=SCOPES,
        redirect_uri="https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
    )
    return flow