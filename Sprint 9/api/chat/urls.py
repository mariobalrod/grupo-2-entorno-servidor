from django.urls import path
from .views import chat_details, chat_list, message_details, message_list

urlpatterns = [
    path('chats/', chat_list),
    path('chat/<slug:value>/', chat_details),

    path('messages/', message_list),
    path('message/<slug:value>/', message_details),
]