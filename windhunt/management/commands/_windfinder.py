#__all__ = ['GetSuperForecast', 'GetForecast']

from . import _screen_scraping
from datetime import datetime, timedelta
import pandas as pd

def GetDay(tree, xpath):
    day1 = _screen_scraping.GetText(tree, xpath)[0]
    day1 = (day1[day1.find(",")+2:])
    return day1;


def GetDates(tree, xpath_runtime, xpath_day, xpath_hour):
    year = str(datetime.today().year)[2:] 
    forecast_hour = _screen_scraping.GetText(tree, xpath_hour)

    day1 = GetDay(tree, xpath_day)

    time = _screen_scraping.GetText(tree, xpath_runtime)[0]
    runtime = [datetime.strptime(year + " " + day1+" "+ time, '%y %b %d %H:%M') for hour in forecast_hour]
    forecast_date = [datetime.strptime(year + " " + day1+" "+ hour[:-1], '%y %b %d %H') for hour in forecast_hour]
    return runtime, forecast_date;


def GetAngle(tree, xpath_angle):
    wind_angle = _screen_scraping.GetText(tree, xpath_angle)
    wind_angle = [s.replace('\n', '').replace('°', '').strip() for s in wind_angle]
    return wind_angle

def GetSuperForecast():
    page = 'https://www.windfinder.com/weatherforecast/lippesee_paderborn'

    xpath_day1_wind_max = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section[1]/div/div[2]/div/div[5]/div[2]/span[2]'
    xpath_day2_wind_max = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section[3]/div/div[2]/div/div[5]/div[2]/span[2]'
    xpath_day2_wind_max = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section[5]/div/div[2]/div/div[5]/div[2]/span[2]'
    xpath_day1_wind_average = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section[1]/div/div[2]/div/div[5]/div[1]/div[1]/span/span[1]'

    xpath_average = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section[1]/div/div[2]/div/div[5]/div[1]/div[1]/span/span[1]'
    xpath_day = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section[1]/div/div[1]/h4/'  

    xpath_wind_speed_max = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section[1]/div/div[2]/div/div[5]/div[2]/span[2]'
    xpath_runtime = '//*[@id="last-update"]'


    xpath_day2 = '/html/body/div[1]/main/div[3]/div/div[1]/section/section[3]/div/div[2]/div[9]/div[5]/div[1]/div[1]/span/span[1]'
    tree = _screen_scraping.GetHtmlData(page)



    #wind_forecast = [forecast_time, wind_speed_average, wind_speed_max]
    df = pd.DataFrame(columns = ["runtime", "forecast_time","average","max", "angle"])
    days = ["1","3","5"]
    for x,d in enumerate(days):
        xpath_wind_max = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section['+d+']/div/div[2]/div/div[5]/div[2]/span[2]'
        xpath_wind_average = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section['+d+']/div/div[2]/div/div[5]/div[1]/div[1]/span/span[1]'
        xpath_angle ='//*[@id="sidebar-ad-scaffold"]/div[1]/section/section['+d+']/div/div[2]/div/div[4]/span[1]'
        xpath_hour = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/section['+d+']/div/div[2]/div/div[2]/div/span'
        wind_speed_average = _screen_scraping.GetList(tree, xpath_wind_average)
        wind_speed_max = _screen_scraping.GetList(tree, xpath_wind_max)
        wind_angle = GetAngle(tree, xpath_angle)
        runtime, forecast_time = GetDates(tree, xpath_runtime, xpath_day, xpath_hour)
        print(len(wind_angle), len(wind_speed_max), len(runtime), len(forecast_time), len(wind_speed_average))
        for i,f in enumerate(runtime):
          df.loc[len(df)] = [pd.to_datetime(runtime[i]), pd.to_datetime(forecast_time[i]+ timedelta(days=x)), wind_speed_average[i], wind_speed_max[i], wind_angle[i]]
    #	wind_forecast['forecast_time'] = (pd.to_datetime(forecast_time))
	#wind_forecast['average'] = wind_speed_average
	    #wind_forecast['max']    = wind_speed_max
	    #wind_forecast['runtime'] = pd.to_datetime(runtime)


    #wind_forecast.set_index('forecast_time', inplace=True)
    return df

def GetForecast():
    page = 'https://www.windfinder.com/forecast/lippesee_paderborn'
    tree = _screen_scraping.GetHtmlData(page)

    # Data frame for the scraped data
    df = pd.DataFrame(columns = ["runtime", "forecast_time","average","max", "angle"])
    # Rows and column numbers of scraped website
    rows = ["3","5","6","8","9"]
    columns = ['1','2']
    
    xpath_runtime = '//*[@id="last-update"]'
    xpath_day = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/div[3]/div[1]/div[1]/h4'
    
    # counter for forecast days
    day = 0

    # Loop for rows and columns in html
    for x,d in enumerate(rows):
        for y,column in enumerate(columns):
            xpath_wind_max = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/div['+d+']/div['+column+']/div[2]/div/div[4]/div[2]/span[2]'
            wind_speed_max = _screen_scraping.GetList(tree, xpath_wind_max)

            xpath_wind_average = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/div['+d+']/div['+column+']/div[2]/div/div[4]/div[1]/div[1]/span/span[1]'
            wind_speed_average = _screen_scraping.GetList(tree, xpath_wind_average)
            
            xpath_angle ='//*[@id="sidebar-ad-scaffold"]/div[1]/section/div['+d+']/div['+column+']/div[2]/div/div[3]/span[1]'
            wind_angle = GetAngle(tree, xpath_angle)
            
            xpath_hour = '//*[@id="sidebar-ad-scaffold"]/div[1]/section/div['+d+']/div['+column+']/div[2]/div/div[2]/div/span'
            xpath_runtime = '//*[@id="last-update"]'
            
            runtime, forecast_time = GetDates(tree, xpath_runtime, xpath_day, xpath_hour)
            for i,f in enumerate(runtime):
                  df.loc[len(df)] = [pd.to_datetime(runtime[i]), pd.to_datetime(forecast_time[i]+timedelta(days = day)), wind_speed_average[i], wind_speed_max[i], wind_angle[i]]
            day +=1
    return df