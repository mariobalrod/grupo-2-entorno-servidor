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
    user_list = User.objects.order_by('first_name')
    context = {'person': user_list[0]}
    return render(request, 'perfil/perfil.html', context )

def settings(request):
    return render(request, 'perfil/settings.html')

