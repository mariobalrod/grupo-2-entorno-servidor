# Generated by Django 3.1.7 on 2021-02-25 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210217_1904'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user2',
        ),
        migrations.AddField(
            model_name='chat',
            name='users',
            field=models.ForeignKey(default='efeofenmf', on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chat'),
            preserve_default=False,
        ),
    ]
