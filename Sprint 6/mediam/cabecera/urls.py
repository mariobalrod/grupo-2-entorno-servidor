from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('setting/', views.setting),
    path('post/', views.post),
    path('chat/', views.chat),
]