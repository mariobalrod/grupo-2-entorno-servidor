import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mediam.settings')

import django
django.setup()

from user.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_email = fakegen.email()
        fake_image = fakegen.image_url()
        fake_first_name = fakegen.name()
        fake_nick_name = fakegen.name()
        fake_password = fakegen.name()
        fake_phone_number = fakegen.phone_number()
        fake_description = fakegen.name()

        #Nueva Entrada de datos
        user = User.objects.get_or_create(
            email = fake_email, 
            image = fake_image,
            first_name = fake_first_name, 
            nick_name = fake_nick_name, 
            password = fake_password, 
            phone_number = fake_phone_number, 
            description = fake_description
            )[0]

if __name__ == '__main__':
    print("RELLENANDO BASE DE DATOS")
    populate(10)
    print("COMPLETADO!")
