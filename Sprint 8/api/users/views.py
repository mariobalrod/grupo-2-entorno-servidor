from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer


# Create your views here.
@csrf_exempt
def users_list(req):
    if req.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=204)


@csrf_exempt
def user_datails(req, value):
    try:
        user = User.objects.get(id=value)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = UserSerializer(user, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=204)

    elif req.method == 'DELETE':
        try:
            user.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)
