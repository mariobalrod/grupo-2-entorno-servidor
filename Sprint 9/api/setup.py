from populates import users, posts, chats
from django.contrib.auth.models import User
import os

if __name__ == '__main__':
    # Generate migrate
    os.system("python manage.py migrate")

    # Create super user
    User.objects.create_superuser('grupo2', 'sergioavilachacon@gmail.com', '1234')

    # Create faker data
    users.populate(10)
    posts.populate(10)
    chats.populate(10)