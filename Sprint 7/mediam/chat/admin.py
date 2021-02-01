from django.contrib import admin
from chat.models import Chat, Message

# Register your models here.
admin.site.register(Chat)
admin.site.register(Message)