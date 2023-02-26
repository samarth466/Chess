from django.shortcuts import render, redirect
import json
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from requests import Request, post
from .utils import *
from os.path import join
from django.conf import settings

# Create your views here.


class AuthURL(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        scopes = '...auth/userinfo.email,...auth/userinfo.profile,openid'.encode(
            encoding='utf-8')
        data = {}
        with open(str(join(settings.BASE_DIR, 'google_oauth2/secrets.json'))) as f:
            data = json.load(f)
        if data:
            headers = {'scope': scopes, 'response_type': 'code',
                       'redirect_uri': data['REDIRECT_URI'], 'client_id': data['CLIENT_ID']}
            url = Request(
                'get', 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount', headers=headers).prepare().url
            return Response({'url': url}, status.HTTP_200_OK)
        else:
            return Response({}, status.HTTP_400_BAD_REQUEST)


def make_request(request):
    return render(Request, 'google_oauth2/request.html')


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
    return redirect('settings:')
