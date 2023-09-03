from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('news.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path("accounts/", include("accounts.urls")),
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('simpleapp.urls')),
    path("accounts/", include("allauth.urls")),
]
