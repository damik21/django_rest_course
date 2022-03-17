from .models import User
from factory import django as fd, Faker as ff


class FakeUserFactory(fd.DjangoModelFactory):
    class Meta:
        model = User


    username = ff('user_name')
    first_name = ff('first_name')
    last_name = ff('last_name')
    email = ff('email')
    password = ff('password')
    is_staff = False
    is_superuser = False
    is_active = True
