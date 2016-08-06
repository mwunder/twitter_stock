from django.core.management.base import BaseCommand, CommandError
from sentiment.models import *

class Command(BaseCommand):
    help = 'searching stocks'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        import search_symbols 

