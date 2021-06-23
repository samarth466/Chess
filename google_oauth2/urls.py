from django.urls import path
from .views import AuthURL, google_callback

app_name = 'google'

urlpatterns = [
    path('get-auth-url/', AuthURL.as_view(),name='get_auth_url'),
    path('callback',google_callback,name='callback')
]