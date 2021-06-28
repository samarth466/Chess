from django.shortcuts import render, redirect
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from requests import Request, post
from .utils import *

# Create your views here.


class AuthURL(APIView):

    def get(self, request, format=None):
        scopes = ['.../auth/userinfo.email',
                  '.../auth/userinfo.profile', 'openid']
        data = json.load('credentials.json')
        headers = {'scope': scopes, 'response_type': 'code',
                   'redirect_uri': data['REDIRECT_URI'], 'client_id': data['CLIENT_ID']}
        url = Request(
            'get', 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount', headers).prepare().url()
        return Response({'url': url}, status.HTTP_200_OK)


def google_callback(request, format=None):
    code = request.get.get('code')
    vars = json.load('secrets.json')
    data = {'grant_type': 'authorization_code', 'code': code,
            'redirect_uri': vars['REDIRECT_URI'], 'client_id': vars['CLIENT_ID'], 'client_secret': vars['CLIENT_SECRET']}
    response = post(
        'https://www.googleapis.com/oauth2/v4/token', data=data).json()
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expiry = response.get('expires_in')
    error = response.get('error')
    if not request.session.exists(request.session.get('email')):
        request.session['email'] = ''
    update_or_create_user_tokens(request.session.get(
        'email'), access_token, token_type, expiry, refresh_token)
    return redirect('game:')
