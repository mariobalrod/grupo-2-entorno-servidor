from django.shortcuts import render
from home.models import Post

# Create your views here.
def index(request):
    return render(request, 'home/home.html', { "posts": Post.objects.order_by('created_at') })