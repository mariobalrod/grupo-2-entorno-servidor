from django.urls import path
from .views import posts_list, post_datails, comments_list, comment_datails, likes_list, like_datails

urlpatterns = [
    path('likes/', likes_list),
    path('like/<slug:value>/', like_datails),
    path('comments/', comments_list),
    path('comment/<slug:value>/', comment_datails),
    path('posts/', posts_list),
    path('post/<slug:value>/', post_datails),
]