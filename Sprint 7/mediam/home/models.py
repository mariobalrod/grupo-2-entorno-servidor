from django.db import models
from user.models import User
import uuid
import datetime

# Create your models here.
class Comment(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=350, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=350, blank=False, null=False)
    description = models.CharField(max_length=350, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
