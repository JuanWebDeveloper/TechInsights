from django.urls import path
from .views import welcome, list_posts, create_post

urlpatterns = [
    path('', welcome, name='welcome'),
    path('list_posts/', list_posts, name='list_posts'),
    path('create_post/', create_post, name='create_post'),
]
