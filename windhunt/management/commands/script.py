from django.core.management.base import BaseCommand

from windhunt.models import Windforecast, WindMeasurement


from ._screen_scraping import *
from ._windfinder import *
from ._station_lippesee import *

class Command(BaseCommand):
    help = "<appropriate help text here>"
    def handle(self, *args, **options):
        self.stdout.write("Hello, World!")