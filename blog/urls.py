from django.urls import path
from .views import blog, signin, signup, signout, post_detail

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
]
