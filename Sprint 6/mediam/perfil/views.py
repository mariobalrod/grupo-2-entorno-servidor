from django.shortcuts import render

# Create your views here.
def perfil(request):
    return render(request, 'perfil/perfil.html')

def setting(request):
    return render(request, 'perfil/setting.html')