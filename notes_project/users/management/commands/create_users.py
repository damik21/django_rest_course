from django.core.management.base import BaseCommand
from users.models import User

from users.utils import FakeUserFactory


class Command(BaseCommand):
    help = 'Creates 5 custom users'

    def add_arguments(self, parser):
        parser.add_argument('user_count', type=int)

    def handle(self, *args, **options):
        if options['user_count']:
            custom_su_data = {
                'username': "admin_test",
                'password': "admin",
                'first_name': "Admin",
                'last_name': "Admin",
                'email': "admin@test.admin",
                'is_staff': True,
                'is_active': True,
                'is_superuser': True,
            }
            User.objects.create_superuser(**custom_su_data)
            for el in range(options['user_count']):
                FakeUserFactory()
        else:
            self.stdout.write(self.style.ERROR('Where must be count of users!'))
