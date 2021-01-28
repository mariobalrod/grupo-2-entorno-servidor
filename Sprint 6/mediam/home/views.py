from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html', { "posts": [1, 2, 3, 4, 5, 6] })