from django.db import models
from user.models import User
import uuid
import datetime

# Create your models here.
class Comment(models.Model):
    id: models.CharField(max_length=100, primary_key=True)
    body: models.CharField(max_length=350)
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __init__(self):
        super(Comment, self).__init__()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()


class Post(models.Model):
    id: models.CharField(max_length=100, primary_key=True)
    image: models.CharField(max_length=350, blank=False, null=False)
    description = models.CharField(max_length=350)
    created_at = models.DateTimeField()
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __init__(self):
        super(Post, self).__init__()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
