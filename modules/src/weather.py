import re
import config
import os
import requests
from templates.button import *

OPEN_WEATHER_MAP_ACCESS_TOKEN = os.environ.get('OPEN_WEATHER_MAP_ACCESS_TOKEN', config.OPEN_WEATHER_MAP_ACCESS_TOKEN)
def process(input, entities):
    output = {}

    try:
        location = entities['location'][0]['value']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + OPEN_WEATHER_MAP_ACCESS_TOKEN)
        data = r.json()
        output['input'] = input
        output['output'] = data
    except:
        output['error_msg'] = TextTemplate('Sorry, I was not able to get weather info for ' + location + '. Please try again.').get_message()
        output['success'] = False
    return output