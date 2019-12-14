import requests
from datetime import datetime
import pytz
from pytz import timezone
import json

class WeatherGetter():
    """This class contains methods needed to return the weather at Berlin by 
    using the requests library to access the DarkSky API.

    The API calls for latitude, longitude, and time. Berlin's latitude and longitude
    are 52.52 and 13.405

    Berlin timezone = UTC + 2, Europe/Berlin
    """

    bertz = timezone('Europe/Berlin')

    def __init__(self):
        pass
        #self.date = date

    @classmethod
    def get_weather(self, date):
        """ This method takes in the date and accesses the Dark Sky API to return the 
        historical weather/forecast. The date needs to be given in the form of [YYYY]-[MM]-[DD].
        
        Dark Sky API requests time as well, but the game time is assumed to be 18:00:00.

        This also excludes any alerts, the daily forecast, minute by minute forecast for the hour,
        and hourly forecast, but the hourly forecast can be restored for use in finding if it rained
        during a certain period of time.
        """
        self.date = date

        api_key_path = '../secrets/dark_sky_api.json'
        with open(api_key_path, 'r') as fo:
            api_key =  json.load(api_key_path)
        key = api_key['key']
        lat = '52.52'
        lon = '13.405'
        time = '18:00:00'
        exclus = 'exclude=alerts,daily,minutely,hourly,flags'
        req_str = f'https://api.darksky.net/forecast/{key}/{lat},{lon},{date}T{time}?{exclus}'
        resp = requests.get(req_str)

        if resp.status_code == 200:
            response_dict = resp.json()
            if response_dict['currently']['icon'] == 'rain':
                result = 1
            else:
                result = 0

        else:
            print("Error, unable to retrieve. Server response code is: ", resp.status_code)

        return result

