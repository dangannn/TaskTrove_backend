from django.core.management.base import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Creates a new user with the given username and password'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Specifies the username for the new user')
        parser.add_argument('password', type=str, help='Specifies the password for the new user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']

        # Проверяем, не существует ли пользователь с таким именем
        if CustomUser.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'The user with username "{username}" already exists.'))
            return

        # Создаем нового пользователя
        CustomUser.objects.create_user(username=username, password=password)

        self.stdout.write(self.style.SUCCESS(f'Successfully created user with username "{username}"'))
