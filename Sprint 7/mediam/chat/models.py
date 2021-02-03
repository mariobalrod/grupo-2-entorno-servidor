from django.db import models
from django.http import request
from user.models import User
import uuid

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=264)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_date = models.DateField()
    id = models.CharField(max_length=264, primary_key=True)

    def __init__(self):
        super(Message, self).__init__()
        self.id = str(uuid.uuid4())

class Chat(models.Model):
    id = models.CharField(max_length=264, primary_key=True)
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __init__(self):
        super(Chat, self).__init__()
        self.id = str(uuid.uuid4())