import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

import django

django.setup()

from users.models import User
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

        user = User.objects.get_or_create(
            email=fake_email,
            avatar_image=fake_avatar_image,
            first_name=fake_first_name,
            last_name=fake_last_name,
            username=fake_username,
            password=fake_password,
            phone_number=fake_phone_number,
            description=fake_description
        )[0]
