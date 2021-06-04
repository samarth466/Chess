from django.urls import path
from settings import views as ST_views

urlpatterns = [
    path('',ST_views.root,name='')
]