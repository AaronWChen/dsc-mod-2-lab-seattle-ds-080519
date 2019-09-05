""" This script is a tester to try out the Dark Sky API to return weather data.
The script is to call the API and return the historical forecast for Berlin, Germany.
Berlin's latitude and longitude are 52.52 and 13.405

The request also requires a time (in Unix time) and key

key: 60e44c5191a3e42cd7d6316c5ca466b8
Berlin timezone = UTC + 2, Europe/Berlin

"""

import requests
from datetime import datetime
import pytz
from pytz import timezone

bertz = timezone('Europe/Berlin')
dt = datetime(year=2011, month=11,day=1,hour=18,minute=00,second=00,tzinfo=bertz).timestamp() 
int_dt = int(dt)

# request_string = f'https://api.darksky.net/forecast/60e44c5191a3e42cd7d6316c5ca466b8/52.52,13.405,{int_dt}?exclude=alerts,daily,minutely,hourly'

# resp = requests.get(request_string)

# if resp.status_code == 200:
#     response_dict = resp.json()
#     print(response_dict)

# else:
#     print("Error, unable to retrieve. Server response code is: ", resp.status_code)

request_string2 = f'https://api.darksky.net/forecast/60e44c5191a3e42cd7d6316c5ca466b8/52.52,13.405,2011-11-01T18:00:00?exclude=alerts,daily,minutely,hourly'
resp2 = requests.get(request_string2)

if resp2.status_code == 200:
    response_dict = resp2.json()
    print(response_dict)

else:
    print("Error, unable to retrieve. Server response code is: ", resp2.status_code)
