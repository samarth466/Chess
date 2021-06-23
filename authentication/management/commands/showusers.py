import sys
from django.core.management.base import BaseCommand
from django.db import DEFAULT_DB_ALIAS
from django.core import exceptions
from django.core.management.baseBaseCommand,  importBaseCommand,  CommandError
from ...models import User
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Shows all users, all users with a specific filter, or details about a specific user."
    requires_migrations_checks = True
    stealth_options = ('stdin',)

    def __init__(self, stdout: Optional[StringIO], stderr: Optional[StringIO], no_color: bool, force_color: bool) -> None:
        super().__init__(stdout=stdout, stderr=stderr, no_color=no_color, force_color=force_color)(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)(self, parser):
        parser.add_argument(
            '-a', '--all',
            action='store_true',
        )
        for field in self.UserModel._meta.get_fields():
            parser.add_arguments(
                '--'+field.name,
                type=str(type(field.to_python())).split(' ')[1][:-1]
            )
        parser.add_argument(
            '-n', '--name',
            type=str
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        if options['all']:
            users = self.UserModel.objects.all()
            for user in users:
                self.stderr(user.get_full_name, user.email,
                            user.logged_in, user.email, user.is_superuser)
        elif options['name'] == None:
            users = self.UserModel.objects.all()
            for field in self.UserModel._meta.get_fields():
                if options[field.name] != None:
                    filtered_users = self.UserModel.objects.filter(field.name=options[field.name]).exclude(is_staff=True)
                    users_temp = users
                    for user in users_temp:
                        if user not in filtered_users:
                            users.exclude(email=user.email)
            for user in users:
                self.stderr(user.get_full_name, user.email,
                            user.logged_in, user.email, user.is_superuser)
        elif options['name']:
            user = self.UserModel.objects.filter(
                first_name=options['name']).first()
