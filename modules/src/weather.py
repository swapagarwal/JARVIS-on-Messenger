import re
import config
import os
import requests

OPEN_WEATHER_MAP_ACCESS_TOKEN = os.environ.get('OPEN_WEATHER_MAP_ACCESS_TOKEN', config.OPEN_WEATHER_MAP_ACCESS_TOKEN)
def process(input, entities=None):
    output = {}

    try:
        location = entities['location'][0]['value']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + OPEN_WEATHER_MAP_ACCESS_TOKEN)
        data = r.json()
        output['input'] = input
        output['output'] = 'Current weather: ' + data['main']['temp'] + data['weather'][0]['description'] + \
        " information provided by OpenWeatherMap"
        output['success'] = True
    except:
        output['success'] = False
    return output