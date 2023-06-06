import random

from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from phonenumber_field.phonenumber import PhoneNumber

from ads.models import Ad
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Faker('email')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    phone = PhoneNumber.from_string(f'+7{random.randint(9001000000, 9999999999)}')
    password = Faker('password')


class AdsFactory(DjangoModelFactory):
    class Meta:
        model = Ad

    title = Faker('pystr', min_chars=10, max_chars=100)
    author = SubFactory(UserFactory)
    price = Faker('pyint', min_value=0)
    description = Faker('paragraph')
