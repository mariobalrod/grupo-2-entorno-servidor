from django.db import models
import uuid
import datetime


# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=128, null=False, blank=False)
    avatar_image = models.CharField(max_length=350, blank=False, null=False, default='https://picsum.photos/id/237/200/300')
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    username = models.CharField(max_length=128, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=350, blank=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)