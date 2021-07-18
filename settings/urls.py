from django.urls import path
from settings import views as ST_views

app_name = 'settings'

urlpatterns = [
    path('<str:email>/', ST_views.root, name='')
]
