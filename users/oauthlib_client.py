from authlib.integrations.requests_client import OAuth2Session
from django.conf import settings


def get_oauth_client(provider_name):
    provider = settings.OAUTH_PROVIDERS[provider_name]
    return OAuth2Session(
        client_id=provider["client_id"],
        client_secret=provider["client_secret"],
        redirect_uri="http://127.0.0.1:8000/users/auth/callback/"
    )
