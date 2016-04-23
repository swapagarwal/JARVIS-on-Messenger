import re
import requests

def process(input, entities=None):
    output = {}

    try:
        city = entities['city'][0]['value']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=adee94563461cdf1dcfe25956aea10ae')
        data = r.json()
        output['input'] = input
        output['output'] = 'Current weather: ' + data['main.temp']
        output['success'] = True
    except:
        output['success'] = False
    return output