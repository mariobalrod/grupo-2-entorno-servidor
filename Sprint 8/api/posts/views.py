from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


# Create your views here.
@csrf_exempt
def likes_list(req):
    if req.method == 'GET':
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)

        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        print('DATA', data)
        serializer = LikeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
def like_datails(req, value):
    try:
        like = Like.objects.get(id=value)
    except Like.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        serializer = LikeSerializer(like)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = LikeSerializer(like, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=204)

    elif req.method == 'DELETE':
        try:
            like.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)



@csrf_exempt
def comments_list(req):
    if req.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
def comment_datails(req, value):
    try:
        comment = Comment.objects.get(id=value)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = CommentSerializer(comment, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=204)

    elif req.method == 'DELETE':
        try:
            comment.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)


@csrf_exempt
def posts_list(req):
    if req.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
def post_datails(req, value):
    try:
        post = Post.objects.get(id=value)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = PostSerializer(post, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=204)

    elif req.method == 'DELETE':
        try:
            post.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)

