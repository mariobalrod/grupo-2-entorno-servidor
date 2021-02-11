import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mediam.settings')

import django
django.setup()

from chat.models import Message, Chat
from user.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        # Creating fake user
        fake_email = fakegen.email()
        fake_first_name = fakegen.name()
        fake_nick_name = fakegen.name()
        fake_password = fakegen.name()
        fake_phone_number = fakegen.phone_number()
        fake_description = fakegen.text()
        fake_image_user = fakegen.image_url() 

        fake_user = User.objects.create(email = fake_email,image = fake_image_user, first_name = fake_first_name, nick_name = fake_nick_name, password = fake_password, phone_number = fake_phone_number, description = fake_description)
        fake_user.save()

        # Creating fake message
        fake_text = fakegen.text()

        fake_message = Message.objects.create(user = fake_user, text = fake_text)
        fake_message.save()

        # Creating fake Chat
        fake_chat = Chat.objects.create(user = fake_user, messages = fake_message)
        fake_chat.save()

if __name__ == '__main__':
    print("RELLENANDO BASE DE DATOS")
    populate(10)
    print("COMPLETADO!")
