from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'cabecera/home.html')

def post(request):
    return render(request, 'cabecera/post.html')

def (request):
    return render(request, 'cabecera/chat.html')