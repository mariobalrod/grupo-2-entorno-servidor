from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'cabecera/home.html')

def post(request):
    return render(request, 'cabecera/post.html')

def chat(request):
    return render(request, 'cabecera/chat.html')

def setting(request):
    return render(request, 'cabecera/setting.html')