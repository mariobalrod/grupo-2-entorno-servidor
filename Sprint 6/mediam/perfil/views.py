from django.shortcuts import render

# Create your views here.
def perfil(request):
    return render(request, 'perfil/perfil.html')

def settings(request):
    return render(request, 'perfil/settings.html')