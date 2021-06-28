from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('/join-game/',join_game),
    path('<str:code>/',game)
]