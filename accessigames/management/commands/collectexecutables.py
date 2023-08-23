from typing import Any, Optional
from os import listdir, mkdir, sep
from os.path import join, isfile, exists
from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError, CommandParser


class Command(BaseCommand):

    help = "Collect executable files in a single location."

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('-p', '--app', action='store', nargs='*')

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        if not exists(join(settings.BASE_DIR, 'executables')):
            mkdir(join(settings.BASE_DIR, 'executables'))
        if options['p'] or options['app']:
            app_names = options['p'] or options['app']
            for app in apps.get_app_configs():
                if app.label in app_names:
                    path = app.path
                    while True:
                        files_counter = 0
                        total_items = len(listdir(path))
                        for dir in listdir(path):
                            if isfile(join(path, dir)) and dir.endswith(f".{settings.EXECUTABLE_EXTENSIONS}"):
                                with open(join(path, dir), 'rb') as f:
                                    lines = [line for line in f.readlines()]
                                with open(join(settings.BASE_DIR, 'executables', dir), 'wb') as f:
                                    f.writelines(lines)
                                files_counter += 1
                            else:
                                path = join(path, dir)
                        if total_items == files_counter:
                            path = join(*path.split(sep))
                        if path == app.path:
                            break
        else:
            for app in apps.get_app_configs():
                path = app.path
                while True:
                    files_counter = 0
                    total_items = len(listdir(path))
                    for dir in listdir(path):
                        if isfile(join(path, dir)) and dir.endswith(f".{settings.EXECUTABLE_EXTENSIONS}"):
                            with open(join(path, dir), 'rb') as f:
                                lines = [line for line in f.readlines()]
                            with open(join(settings.BASE_DIR, 'executables', dir), 'wb') as f:
                                f.writelines(lines)
                            files_counter += 1
                        else:
                            path = join(path, dir)
                    if total_items == files_counter:
                        path = join(*path.split(sep))
                    if path == app.path:
                        break
