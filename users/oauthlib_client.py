from authlib.integrations.requests_client import OAuth2Session
from django.conf import settings
from dotenv import load_dotenv
import os


def get_oauth_client(provider_name):
    provider = settings.OAUTH_PROVIDERS[provider_name]
    load_dotenv()
    return OAuth2Session(
        client_id=provider["client_id"],
        client_secret=provider["client_secret"],
        redirect_uri=os.getenv("REDIRECT_URI"),
    )