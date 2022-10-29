"""PokeSearch URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from PokeSearch import settings
from PokeSearch.views import prueba, prueba2,fecha
from django.conf.urls.static import static
urlpatterns = [
    path('admin/' , admin.site.urls),
    path("prueba/", prueba),
    path("prueba2/", prueba2),
    path("", include("PokeSearch.urls")),
] + static(settings.settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
