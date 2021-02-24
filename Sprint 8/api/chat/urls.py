from django.urls import path
from .views import chat_details, chat_list, message_details, message_list

urlpatterns = [
    path('chat/', chat_list),
    path('chat/<slug:value>/', chat_details),

    path('chat/', message_list),
    path('message/<slug:value>/', message_details),
]