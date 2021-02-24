from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=128, required=True)
    avatar_image = serializers.CharField(max_length=350, required=False)
    first_name = serializers.CharField(max_length=128, required=True)
    last_name = serializers.CharField(max_length=128, required=True)
    username = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=20, required=True)
    phone_number = serializers.CharField(max_length=20, required=False)
    description = serializers.CharField(max_length=350, required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model: User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'avatar_image',
            'password',
            'phone_number',
            'description',
            'created_at'
        ]

    def create(self, validated_data):
        print('USERR', validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('USERR', validated_data)
        instance.id = validated_data.get('id', instance.id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.avatar_image = validated_data.get('avatar_image', instance.avatar_image)
        instance.password = validated_data.get('password', instance.password)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()

        return instance