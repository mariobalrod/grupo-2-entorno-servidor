from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from chat.models import Chat, Message
from chat.serializers import ChatSerializer, MessageSerializer

# Create your views here.

@csrf_exempt
def chat_list(request):

    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many = True)
        return JsonResponse(serializer.data, safe=False, status=200)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChatSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
def chat_details(request, value):

    try:
        chat = Chat.objects.get(nick=value)
    except Chat.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChatSerializer(chat)
        return JsonResponse(serializer.data, safe=False, status=200)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChatSerializer(chat, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)

    elif request.method == 'DELETE':
        try:
            chat.delete()
            return HttpResponse(status = 200)
        except:
            return HttpResponse(status = 409)
#========================================================================
@csrf_exempt
def message_list(request):

    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many = True)

        return JsonResponse(serializer.data, safe=False, status=200)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data) 

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
               
        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
def message_details(request, value):

    try:
        message = Message.objects.get(nick=value)
    except Message.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return JsonResponse(serializer.data, safe=False, status=200)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(message, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)

    elif request.method == 'DELETE':
        try:
            message.delete()
            return HttpResponse(status = 200)
        except:
            return HttpResponse(status = 409)