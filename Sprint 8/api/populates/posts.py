import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

import django

django.setup()

from users.models import User
from posts.models import Post, Comment, Like
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_email = fakegen.email()
        fake_avatar_image = fakegen.image_url()
        fake_first_name = fakegen.name()
        fake_last_name = fakegen.name()
        fake_username = fakegen.name()
        fake_password = fakegen.name()
        fake_phone_number = fakegen.phone_number()
        fake_description = fakegen.text()

        user = User.objects.create(
            email=fake_email,
            avatar_image=fake_avatar_image,
            first_name=fake_first_name,
            last_name=fake_last_name,
            username=fake_username,
            password=fake_password,
            phone_number=fake_phone_number,
            description=fake_description
        )
        user.save()

        fake_image = fakegen.image_url()
        fake_description_post = fakegen.text()

        post = Post.objects.create(
            image=fake_image, 
            description=fake_description_post,
            user=user
        )
        post.save()


        fake_comments = []

        for entry2 in range(N):
            fake_body = fakegen.text()
            fake_comment = Comment.objects.create(body=fake_body, user = user, post=post)
            fake_comment.save()
            fake_comments.append(fake_comment)

        fake_likes = []

        for entry3 in range(N):
            fake_like = Like.objects.create(user = user, post=post)
            fake_like.save()
            fake_likes.append(fake_like)
