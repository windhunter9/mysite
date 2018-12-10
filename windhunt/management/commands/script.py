from django.core.management.base import BaseCommand

from windhunt.models import Windforecast, WindMeasurement



class Command(BaseCommand):
    help = "<appropriate help text here>"
    def handle(self, *args, **options):
        self.stdout.write("Hello, World!")