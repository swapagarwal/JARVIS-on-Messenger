import os

import requests

import config
from templates.text import TextTemplate

MAPQUEST_CONSUMER_KEY = os.environ.get('MAPQUEST_CONSUMER_KEY', config.MAPQUEST_CONSUMER_KEY)
OPEN_WEATHER_MAP_ACCESS_TOKEN = os.environ.get('OPEN_WEATHER_MAP_ACCESS_TOKEN', config.OPEN_WEATHER_MAP_ACCESS_TOKEN)
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', config.GOOGLE_MAPS_API_KEY)

def process(input, entities):
    output = {}
    try:
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + entities['location'][0][
            'value'] + '&key=' + GOOGLE_MAPS_API_KEY)
        location_data = r.json()
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=' + str(
            location_data['results'][0]['geometry']['location']['lat']) + '&lon=' + str(
            location_data['results'][0]['geometry']['location'][
                'lng']) + '&units=metric&appid=' + OPEN_WEATHER_MAP_ACCESS_TOKEN)
        weather_data = r.json()
        output['input'] = input
        temperature_in_fahrenheit = weather_data['main']['temp'] * 1.8 + 32
        degree_sign = u'\N{DEGREE SIGN}'
        output['output'] = TextTemplate(
            'Location: ' + location_data[0]['display_name'] + '\nWeather: ' + weather_data['weather'][0][
                'description'] + '\nTemperature: ' + str(
                weather_data['main']['temp']) + ' ' + degree_sign + 'C / ' + str(
                temperature_in_fahrenheit) + ' ' + degree_sign + 'F\n- Info provided by OpenWeatherMap').get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t get the weather info you asked for.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - tell me the weather in London'
        error_message += '\n  - weather Delhi'
        error_message += '\n  - What\'s the weather in Texas?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
