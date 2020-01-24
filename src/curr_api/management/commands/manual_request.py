from django.core.management.base import BaseCommand

from curr_api.utils import fixer_request


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        fixer_request()