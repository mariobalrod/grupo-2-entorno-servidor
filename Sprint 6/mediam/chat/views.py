from django.shortcuts import render

# Create your views here.
def chat(request):
    return render(request, 'chat/chat.html', {'range': [1, 2, 3, 4, 5, 6, 7, 8]})