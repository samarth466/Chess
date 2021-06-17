from .models import GoogleTokens
from authentication.models import User
from requests import post
from json import load
from datetime import datetime, timedelta


def get_user_tokens(session_key):
    user_tokens = GoogleTokens.objects.filter(
        user=User.objects.filter(email=session_key)[0])
    if user_tokens.exists:
        return user_tokens[0]
    return None


def update_or_create_user_tokens(session_key, access_token, token_type, expiry, refresh_token):
    tokens = get_user_tokens(session_key)
    expiry = datetime.now()+timedelta(seconds=expiry)
    if tokens:
        tokens.access_token = access_token
        tokens.expiry = expiry
        tokens.refresh_token = refresh_token
        tokens.token_type = token_type
        tokens.user = User.objects.filter(email=session_key)[0]
        tokens.save(update_fields=[
                    'access_token', 'refresh_token', 'token_type', 'user', 'expiry'])
    else:
        tokens = GoogleTokens(user=User.objects.filter(email=session_key)[
                              0], refresh_token=refresh_token, access_token=access_token, token_type=token_type, expiry=expiry)
        tokens.save()


def renew_google_token(tokens):
    refresh_token = tokens.refresh_token
    with open('secrets.json') as datafile:
        data = load(datafile)
    response = post('https://www.googleapis.com/oauth2/v4/token', data={
                    'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': data['CLIENT_ID'], 'client_secret': data['CLIENT_SECRET']}).json()
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expiry = response.get('expires_in')
    refresh_token = response.get('refresh_token')
    update_or_create_user_tokens(
        tokens.user.email, access_token, token_type, expiry, refresh_token)


def is_google_authenticated(session_key):
    tokens = get_user_tokens(session_key)
    if tokens:
        expiry = tokens.expiry
        if expiry <= datetime.now():
            renew_google_token(tokens)
        return True
    return False