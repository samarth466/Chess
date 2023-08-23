from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:title>/', views.details, name='details'),
    path('create-post', views.create_post, name='create-post'),
    path('create-comment/<int:id>/', views.add_comment, name='create-comment'),
    path('delete-post/<str:title>/', views.delete_post, name='delete-post'),
    path('delete-comment/<int:id>/', views.delete_comment, name='delete_comment')
]
