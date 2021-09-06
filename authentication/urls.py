from authentication.views import authentication_method_chooser, database_check
from django.urls import path
from authentication import views as auth_views

app_name = 'authentication'

urlpatterns = [
    path('', auth_views.authentication_method_chooser, name=''),
    path('database-check-in/', auth_views.database_check, name='view'),
    path('sign-in/', auth_views.forum, name='forum'),
    path('register/', auth_views.create_user_account, name='register'),
    path('login/', auth_views.login, name='login'),
    path('profile/', auth_views.profile, name="profile")
]
