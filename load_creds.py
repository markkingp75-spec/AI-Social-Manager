import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# The scope needed to run your Gemini models securely
SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Manages secure Google login and saves a local session token."""
    creds = None
    
    # If you've already logged in once, reuse the saved login session
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    # If we need to log in or refresh expired credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
            
        # Save the credentials so you don't have to log in every single time
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    return creds