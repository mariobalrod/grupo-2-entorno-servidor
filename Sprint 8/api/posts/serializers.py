from rest_framework import serializers
from .models import Post, Comment, Like
from users.serializers import UserSerializer

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    image = serializers.CharField(max_length=350, required=True)
    description = serializers.CharField(max_length=350, required=False)
    created_at = serializers.DateTimeField(required=False)
    user = UserSerializer(required=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model: Post
        fields = [
            'id',
            'image',
            'description',
            'created_at',
            'user',
            'likes',
            'comments',
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.user = validated_data.get('user', instance.user)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.save()

        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    body = serializers.CharField(max_length=100, required=True)
    created_at = serializers.DateTimeField(read_only=True)
    user = UserSerializer(required=True)
    post = PostSerializer(required=True)

    class Meta:
        model: Comment
        fields = [
            'id',
            'body',
            'created_at',
            'user',
            'post',
        ]

    def create(self, validated_data):
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
    user = UserSerializer(required=True)
    post = PostSerializer(many=False, required=True)

    class Meta:
        model: Like
        fields = [
            'id',
            'user',
            'post'
        ]

    def create(self, validated_data):
        return Like.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.user = validated_data.get('user', instance.user)
        instance.post = validated_data.get('post', instance.post)
        instance.save()

        return instance
