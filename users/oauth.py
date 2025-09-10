from authlib.integrations.requests_client import OAuth2Session
from django.conf import settings

SUAP_AUTHORIZE_URL = 'https://suap.ifrn.edu.br/o/authorize/'
SUAP_TOKEN_URL = 'https://suap.ifrn.edu.br/o/token/'
SUAP_API_BASE = 'https://suap.ifrn.edu.br/api/'

def get_suap_oauth(session=None, token=None):
    return OAuth2Session(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        redirect_uri='http://localhost:8000/suap/callback/',
        token=token,
    )

# Para pegar o URL de autorização:
def get_authorize_url():
    oauth = get_suap_oauth()
    uri, state = oauth.create_authorization_url(SUAP_AUTHORIZE_URL)
    return uri, state
