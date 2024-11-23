from django.urls import path
from .views import welcome, list_posts

urlpatterns = [
    path('', welcome, name='welcome'),
    path('your_articles/', list_posts, name='list_posts'),
]
