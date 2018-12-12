from django.core.management.base import BaseCommand

from windhunt.models import Windforecast, WindMeasurement


from ._screen_scraping import *
from ._windfinder import *
from ._station_lippesee import *

class Command(BaseCommand):
	help = "<appropriate help text here>"
	def handle(self, *args, **options):
		self.stdout.write("Hello, World!")
		df = GetSuperForecast_Windfinder()
		day1 = "1"
		for index, row in df.iterrows():
			try:
				Windforecast.objects.create(wind_average = row['average'], 
					wind_max = row['max'],
					runtime = row['runtime'],
					forecast_time = row['forecast_time'],
					wind_angle = row['angle']
					)
			except:
				day1 += str(row['runtime']) +"\n\n"

		df = GetActualWind()
		for index, row in df.iterrows():
			try:
				WindMeasurement.objects.create(wind_average = row['average'], wind_max = row['max'], runtime = row['runtime'])
			except:
				day1 += str(row['runtime']) +"\n\n"

	    #return render(request,'windhunt/showimage.html', {'out': day1})