from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('', include('blog.urls')),
    path('dashboard/', include('dashboard.urls'))
]
