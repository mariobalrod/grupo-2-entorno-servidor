from django.shortcuts import render
from user.models import User

# Create your views here.
def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/register.html')

def reset_password(request):
    return render(request, 'auth/reset_password.html')

def perfil(request):
    return render(request, 'perfil/perfil.html')

def settings(request):
    return render(request, 'perfil/settings.html')

