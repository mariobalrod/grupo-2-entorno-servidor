from django.db import models
from django.http import request
from user.models import User

# Create your models here.
class Chat(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE)
    message_user = models.CharField(max_length=264, unique=True)

class Message(models.Model):
    message = models.CharField(max_length=264, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_date = models.DateField()

