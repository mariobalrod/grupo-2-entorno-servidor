from django.urls import path
from .views import users_list, user_datails

urlpatterns = [
    path('users/', users_list),
    path('user/<slug:value>/', user_datails),
]