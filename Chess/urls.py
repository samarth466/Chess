from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    path('downloads/', views.downloads, name='downloads'),
    path('resources/', views.resources.as_view(), name='resources')
]
