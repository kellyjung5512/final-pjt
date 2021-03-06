from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
]
