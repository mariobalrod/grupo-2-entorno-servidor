from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=128, primary_key= True)
    image = models.CharField(max_length=350, blank= False, null= False, default= None)
    first_name = models.CharField(max_length=128, blank= False, null= False)
    nick_name = models.CharField(max_length=128, blank= False, null= False)
    password = models.CharField(max_length=20, blank= False, null= False)
    phone_number = models.CharField(max_length=20, blank= False, null= False)
    description = models.TextField(max_length=350, blank= False, null= False )