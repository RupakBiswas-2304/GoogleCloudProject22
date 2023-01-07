"""gcp_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from user.urls import urlpatterns
from events.urls import urlpatterns
from django.shortcuts import redirect


def huh(_):
    return redirect("http://127.0.0.1:3000")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('user/', include('user.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('accounts/', include('allauth.urls')),
    path('', huh)
]
