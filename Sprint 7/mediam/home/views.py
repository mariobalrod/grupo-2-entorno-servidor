from django.shortcuts import render
from home.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('created_at')[:5]
    context = { "posts": posts }
    return render(request, 'home/home.html', context)