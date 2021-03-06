# Generated by Django 2.2.5 on 2021-02-01 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('text', models.CharField(max_length=264)),
                ('message_date', models.DateField()),
                ('id', models.CharField(max_length=264, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Message')),
            ],
        ),
    ]
