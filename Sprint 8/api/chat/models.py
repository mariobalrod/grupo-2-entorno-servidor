from django.db import models
import uuid
import datetime
from users.models import User

# Create your models here.
class Message(models.Model):
    id = models.CharField(primary_key=True,max_length=128, default=uuid.uuid4, editable=False) 
    text = models.CharField(max_length = 264)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_date = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)


class Chat(models.Model):
    id = models.CharField(primary_key=True,max_length=128, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)
