import os
import json
import streamlit as st
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def load_creds():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    
    # 1. Catch the authorization code sent back from Google in the website URL
    query_params = st.query_params
    if "code" in query_params and "google_user_creds" not in st.session_state:
        auth_code = query_params["code"]
        
        client_config = json.loads(st.secrets["google_client_secret"]["web"])
        
        flow = Flow.from_client_config(
            client_config,
            scopes=SCOPES,
            redirect_uri="https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
        )
        
        flow.fetch_token(code=auth_code)
        st.session_state["google_user_creds"] = flow.credentials
        
        st.query_params.clear()
        st.rerun()

    # 2. Attempt to load existing user credentials from session state
    if "google_user_creds" in st.session_state:
        creds = st.session_state["google_user_creds"]
        
    # 3. If no valid credentials exist, trigger the Web Application Authorization Flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            client_config = json.loads(st.secrets["google_client_secret"]["web"])
            
            flow = Flow.from_client_config(
                client_config,
                scopes=SCOPES,
                redirect_uri="https://ai-social-manager-4ds4mj8rwpzynvwt4wtjht.streamlit.app"
            )
            
            authorization_url, state = flow.authorization_url(
                access_type='offline',
                include_granted_scopes='true'
            )
            
            st.link_button("🔐 Connect Your Google Account", authorization_url)
            st.info("Please click the button above to authenticate and authorize your social manager app.")
            st.stop() 

    return creds