from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, required=False)
    image = serializers.CharField(max_length=350, required=True)
    description = serializers.CharField(max_length=128, required=False)
    created_at = serializers.DateTimeField(required=False)
    comments = serializers.CharField(max_length=128, required=False)
    likes = serializers.IntegerField(required=False)
    user = serializers.CharField(max_length=20, required=True)

    class Meta:
        model: Post
        fields = [
            'id',
            'image',
            'description',
            'created_at',
            'comments',
            'likes',
            'user',
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, required=False)
    body = serializers.CharField(max_length=100, required=True)
    created_at = serializers.DateTimeField(required=False)
    user = serializers.CharField(max_length=20, required=True)

    class Meta:
        model: Comment
        fields = [
            'id',
            'body',
            'created_at',
            'user',
        ]

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        return instance

class LikeSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, required=False)
    user = serializers.CharField(max_length=20, required=True)

    class Meta:
        model: Like
        fields = [
            'id',
            'user',
        ]

    def create(self, validated_data):
        return Like.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        return instance
