import sys
from django.db import DEFAULT_DB_ALIAS
from django.core import exceptions
from django.core.management.base import CommandError
from django.contrib.auth.management.commands import createsuperuser
from django.contrib.auth.management import get_default_username
from ...models import User
from django.contrib.auth import get_user_model

class Command(createsuperuser.Command):
    help = 'Deletes a specified or all superusers.'
    requires_migrations_checks = True
    stealth_options = ('stdin',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()
        self.username_field = self.UserModel._meta.get_field(self.UserModel.USERNAME_FIELD)

    def add_arguments(self,parser):
        parser.add_argument(
            '--%s' % self.UserModel.USERNAME_FIELD,
            help='Specifies the login for the superuser.'
        )
        parser.add_argument(
            '--noinput', '--no-input', action='store_false', dest='interactive',
            help=(
                'Tells Django to NOT prompt the user for input of any kind. '
                'You must use --%s with --noinput, along with an option for '
                'any other required fields. Superusers created with --noinput will not be able to log in until they\'re given a valid password.' %
                self.UserModel.USERNAME_FIELD
            ),
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Indicates to delete all the superusers.'
        )
        parser.add_argument(
            '--database',
            default=DEFAULT_DB_ALIAS,
            help='specifies the database to use. Default is "default".',
        )
    
    def execute(self, *args, **options):
        self.stdin = options.get('stdin', sys.stdin)  # Used for testing
        return super().execute(*args, **options)
    
    def handle(self, *args, **options):
        username = options[self.UserModel.USERNAME_FIELD]
        database = options['database']
        user_data = {}
        verbose_field_name = self.username_field.verbose_name
        if not options['all']:
            username = None
            default_username = get_default_username()
            while username is None:
                message = self._get_input_message(self.username_field,default_username)
                username = self.get_input_data(self.username_field,message,default_username)
                if username:
                    error_message = self._validate_username(username,verbose_field_name,database)
                    if error_message:
                        self.stderr.write(error_message)
                        username = None
            user_data[self.UserModel.USERNAME_FIELD] = username
            users = self.UserModel.objects.filter(username=user_data[self.UserModel.USERNAME_FIELD],is_staff=True)
            for user in users:
                user.delete()
        else:
            users = self.UserModel.objects.filter(is_staff=True)
            for user in users:
                user.delete()