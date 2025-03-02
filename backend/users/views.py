from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.conf import settings
from google.oauth2 import credentials
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import requests

# Initialize the OAuth flow
def get_google_oauth_flow():
    return Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
                "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [settings.GOOGLE_OAUTH2_REDIRECT_URI],
            }
        },
        scopes=["https://www.googleapis.com/auth/userinfo.profile"],
    )

# Redirect to Google OAuth consent screen
def google_auth(request):
    flow = get_google_oauth_flow()
    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )
    request.session["oauth_state"] = state
    return redirect(authorization_url)

# Handle OAuth callback
def google_auth_callback(request):
    state = request.session.get("oauth_state")
    flow = get_google_oauth_flow()
    flow.fetch_token(authorization_response=request.build_absolute_uri())

    # Fetch user profile data
    credentials = flow.credentials
    user_info_service = build("oauth2", "v2", credentials=credentials)
    user_info = user_info_service.userinfo().get().execute()

    # Save user data to session or database
    request.session["user_info"] = user_info

    return redirect("/")

# Fetch user data
def fetch_user_data(access_token):
    response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return response.json()
