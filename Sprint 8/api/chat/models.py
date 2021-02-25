from django.db import models
import uuid
import datetime
from users.models import User

# Create your models here.

class Chat(models.Model):
    id = models.CharField(primary_key=True,max_length=128, default=uuid.uuid4, editable=False)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')

class Message(models.Model):
    id = models.CharField(primary_key=True,max_length=128, default=uuid.uuid4, editable=False) 
    text = models.CharField(max_length = 264)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_date = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)