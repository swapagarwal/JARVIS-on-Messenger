import os
import requests
import config

from datetime import datetime
from templates.text import TextTemplate
from utils import location

TIME_ZONE_DB_API_KEY = os.environ.get('TIME_ZONE_DB_API_KEY',
                                      config.TIME_ZONE_DB_API_KEY)


def process(input, entities):
    output = {}
    try:
        location_data = location.retrieve_data(
            entities['time_location'][0]['value'])
        r = requests.get('http://api.timezonedb.com/?'
                         + 'lat='
                         + str(location_data['geometry']['location']['lat'])
                         + '&lng='
                         + str(location_data['geometry']['location']['lng'])
                         + '&format=json&key=' + TIME_ZONE_DB_API_KEY)
        time_data = r.json()
        time = datetime.utcfromtimestamp(time_data['timestamp'])\
            .strftime('%a %b %d %Y %H:%M:%S')
        output['input'] = input
        output['output'] = TextTemplate(
            'Location: ' + str(location_data['formatted_address'])
            + '\nTime: ' + time + ' ' + time_data['abbreviation'])\
            .get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t get the time at the location you specified.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - time in new york'
        error_message += '\n  - india time'
        error_message += '\n  - time at paris'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
