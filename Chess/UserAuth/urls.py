from django.urls import path
from UserAuth import views as UA_views

urlpatterns = [
    path('sign-in/',UA_views.database_check,name='view'),
    path('',UA_views.forum,name='registration'),
    path('register/',UA_views.create_user_account,name='create_user_account'),
    path('login/',UA_views.login,name='login'),
    path('profile/',UA_views.profile,name="Profile")
    ]