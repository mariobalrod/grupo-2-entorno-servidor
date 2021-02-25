from rest_framework import serializers
from .models import Post, Comment, Like
from users.serializers import UserSerializer
from users.models import User

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    image = serializers.CharField(max_length=350, required=False)
    description = serializers.CharField(max_length=350, required=False)
    created_at = serializers.DateTimeField(required=False)
    user = UserSerializer(required=False)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = User.objects.get_or_create(**user_data)[0]
            validated_data['user'] = user

        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    body = serializers.CharField(max_length=100, required=True)
    created_at = serializers.DateTimeField(read_only=True)
    user = UserSerializer(required=False)
    post = PostSerializer(required=False)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = User.objects.get_or_create(**user_data)[0]
            validated_data['user'] = user
        
        post_data = validated_data.pop('post', None)
        if post_data:
            user_data2 = post_data.pop('user', None)
            if user_data2:
                user2 = User.objects.get_or_create(**user_data2)[0]
                post_data['user'] = user2

            post = Post.objects.get_or_create(**post_data)[0]
            
            validated_data['post'] = post

        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.body = validated_data.get('body', instance.body)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.user = validated_data.get('user', instance.user)
        instance.post = validated_data.get('post', instance.post)
        instance.save()

        return instance

class LikeSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    user = UserSerializer(required=False)
    post = PostSerializer(many=False, required=False)

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = User.objects.get_or_create(**user_data)[0]
            validated_data['user'] = user
        
        post_data = validated_data.pop('post', None)
        if post_data:
            user_data2 = post_data.pop('user', None)
            if user_data2:
                user2 = User.objects.get_or_create(**user_data2)[0]
                post_data['user'] = user2

            post = Post.objects.get_or_create(**post_data)[0]
            
            validated_data['post'] = post

        return Like.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.user = validated_data.get('user', instance.user)
        instance.post = validated_data.get('post', instance.post)
        instance.save()

        return instance
