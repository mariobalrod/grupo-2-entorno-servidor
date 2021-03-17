from rest_framework import serializers
from chat.models import Message, Chat
from users.serializers import UserSerializer
from users.models import User
import datetime

class ChatSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    users = UserSerializer(required=False)

    class Meta:
        model = Chat
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('users', None)
        if user_data:
            user = User.objects.get_or_create(**user_data)[0]
            validated_data['users'] = user

        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('users', None)
        if user_data:
            user = User.objects.get_or_create(**user_data)[0]
            validated_data['users'] = user
        instance.users = validated_data.get('users', instance.users)
        instance.save()
        return instance

#==============================================================================================================

class MessageSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    text = serializers.CharField(max_length=300, required=True)
    message_date = serializers.DateTimeField(default=datetime.datetime.now)
    user = UserSerializer(required=False)
    chat = ChatSerializer(required=False)

    class Meta:
        model = Message
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = User.objects.get_or_create(**user_data)[0]
            validated_data['user'] = user

        chat_data = validated_data.pop('chat', None)
        if chat_data:
            chat = Chat.objects.get_or_create(**chat_data)[0]
            validated_data['chat'] = chat

        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.message_date = validated_data.get('message_date', instance.message_date)
        instance.user = validated_data.get('user', instance.user)
        instance.chat = validated_data.get('chat', instance.chat)
        instance.save()
        return instance