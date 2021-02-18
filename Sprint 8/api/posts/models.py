from django.db import models
import uuid
import datetime
from users.models import User

# Create your models here.
class Like(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=350, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
class Post(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=350, blank=False, null=False, default='https://picsum.photos/id/237/200')
    description = models.CharField(max_length=350, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    likes = models.ForeignKey(Like,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

