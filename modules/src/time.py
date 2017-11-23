import os
from datetime import datetime

import requests

import config
from templates.text import TextTemplate

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', config.GOOGLE_MAPS_API_KEY)
MAPQUEST_CONSUMER_KEY = os.environ.get('MAPQUEST_CONSUMER_KEY', config.MAPQUEST_CONSUMER_KEY)
TIME_ZONE_DB_API_KEY = os.environ.get('TIME_ZONE_DB_API_KEY', config.TIME_ZONE_DB_API_KEY)


def process(input, entities):
    output = {}
    try:
        r = requests.get(
                'https://maps.googleapis.com/maps/api/geocode/json?address=' + entities['location'][0]['value'] + '&key=' + GOOGLE_MAPS_API_KEY)
        location_data = r.json()
        r = requests.get('http://api.timezonedb.com/?lat=' + str( location_data['results'][0]['geometry']['location']['lat'])  + '&lng='+ str(location_data['results'][0]['geometry']['location']['lng'])
             + '&format=json&key=' + TIME_ZONE_DB_API_KEY)
        time_data = r.json()
        time = datetime.utcfromtimestamp(time_data['timestamp']).strftime('%a %b %d %Y %H:%M:%S')
        output['input'] = input
        output['output'] = TextTemplate(
            'Location: ' + location_data['results'][0]['formatted_address'] + '\nTime: ' + time + ' ' + time_data[
                'abbreviation']).get_message()
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
