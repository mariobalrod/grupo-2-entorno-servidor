from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('', include('user.urls')),
    path('', include('chat.urls')),
    path('', include('upload_image.urls')),
]
