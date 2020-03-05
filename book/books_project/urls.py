from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounting/', include('django.contrib.auth.urls')),
    path('accounting/', include('user.urls')),
    path('', include('pages.urls')),
]
