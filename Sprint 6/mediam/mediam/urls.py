from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('', include('auth.urls')),
    path('', include('perfil.urls')),
]
