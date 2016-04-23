import re
import requests

def process(input, entities=None):
    output = {}

    try:
        location = entities['location'][0]['value']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=adee94563461cdf1dcfe25956aea10a')
        data = r.json()
        output['input'] = input
        output['output'] = 'Current weather: ' + data['main']['temp'] + data['weather'][0]['description'] + \
        " information provided by OpenWeatherMap"
        output['success'] = True
    except:
        output['success'] = False
    return output