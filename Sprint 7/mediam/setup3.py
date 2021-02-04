from populates import chats, posts, users
from django.contrib.auth.models import User;
import os

if __name__ == '__main__':
    # Generate migrate
    os.system("python3 manage.py migrate")

    # Create super user
    User.objects.create_superuser('grupo2', 'sergioavilachacon@gmail.com', '1234')

    # Create faker data 
    chats.populate(10)
    posts.populate(10)
    users.populate(10)