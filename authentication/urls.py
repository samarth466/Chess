from django.urls import path
from authentication import views as auth_views
from django.contrib.auth.views import PasswordChangeView

app_name = 'authentication'

urlpatterns = [
    path('', auth_views.authentication_method_chooser, name='home'),
    path('database-check-in/', auth_views.database_check, name='view'),
    path('sign-in/', auth_views.forum, name='forum'),
    path('register/', auth_views.create_user_account, name='register'),
    path('login/', auth_views.login, name='auth_login'),
    #path('profile/', auth_views.profile, name="profile"),
    path('password-change/', PasswordChangeView.as_view(
        template_name="authentication/password_change.html"), name="password-change")
]
