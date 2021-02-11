from django.db import models
from user.models import User
import uuid
import datetime

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=264)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_date = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
        
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)

        