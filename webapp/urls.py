"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from decouple import config
from django.conf import settings

urlpatterns = [
    path( config("ADMIN_URL") , admin.site.urls),
    path('api/', include('API.urls')),
    # path('rest-urls/', include('rest_framework.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('api/dj-rest-auth/registration/', 
       include('dj_rest_auth.registration.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
