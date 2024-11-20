from django.urls import path
from .views import blog, signin, signup

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
]