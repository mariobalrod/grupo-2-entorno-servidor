from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('reset_password/', views.reset_password),
    path('perfil/', views.perfil),
    path('settings/', views.settings),
]