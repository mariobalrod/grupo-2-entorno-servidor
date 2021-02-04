from django.shortcuts import render
from chat.models import Chat

# Create your views here.
def chat(request):
    chat_list = Chat.objects.order_by('user')
    context = {'chats' : chat_list, 'current_chat' : chat_list[0]}
    return render(request, 'chat/chat.html', context)


    