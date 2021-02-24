from rest_framework import serializers
from chat.models import Message, Chat
import datetime

class ChatSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, required=False)
    messages = serializers.CharField(max_length=300, required=False)
    user = serializers.CharField(max_length=20, required=True)
    user2 = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = Chat
        fields = [
            'id',
            'user',
            'user2',
            'messages'
            ]
    
    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.message_date = validated_data.get('message_date', instance.message_date)
        instance.save()
        return instance

#==============================================================================================================

class MessageSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, required=False)
    text = serializers.CharField(max_length=300, required=False)
    user = serializers.CharField(max_length=20, required=True)
    message_date = serializers.DateTimeField(default=datetime.datetime.now)

    class Meta:
        model = Message
        fields = [
            'id',
            'text',
            'user',
            'message_date'
        ]
    
    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.message_date = validated_data.get('message_date', instance.message_date)
        instance.save()
        return instance