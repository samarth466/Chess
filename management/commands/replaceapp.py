import ArgumentParser
from django.core.management.commands.startapp import Command as SuperCommand


class Command(SuperCommand):

    def add_arguments(self, parser: ArgumentParser) -> None:
        super().add_arguments(parser)
        parser.add_argument('--replace', '-r', action='store', nargs=2,
                            type=list, help="Replaces the given app name with the new name")
