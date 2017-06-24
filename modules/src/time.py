import requests
import config
import os
from templates.text import TextTemplate
from datetime import datetime
from error_msg import LOCATION_ERROR, EXAMPLE_TIME

MAPQUEST_CONSUMER_KEY = os.environ.get('MAPQUEST_CONSUMER_KEY', config.MAPQUEST_CONSUMER_KEY)
TIME_ZONE_DB_API_KEY = os.environ.get('TIME_ZONE_DB_API_KEY', config.TIME_ZONE_DB_API_KEY)

def process(input, entities):
    output = {}
    try:
        r = requests.get('http://open.mapquestapi.com/nominatim/v1/search.php?key=' + MAPQUEST_CONSUMER_KEY + '&format=json&q='+ entities['time_location'][0]['value'] + '&limit=1')
        location_data = r.json()
        r = requests.get('http://api.timezonedb.com/?lat='+ location_data[0]['lat'] + '&lng='+ location_data[0]['lon'] + '&format=json&key=' + TIME_ZONE_DB_API_KEY)
        time_data = r.json()
        time = datetime.utcfromtimestamp(time_data['timestamp']).strftime('%a %b %d %Y %H:%M:%S')
        output['input'] = input
        output['output'] = TextTemplate('Location: ' + location_data[0]['display_name'] + '\nTime: ' + time + ' ' + time_data['abbreviation']).get_message()
        output['success'] = True
    except:
        error_message = LOCATION_ERROR.format('time') + EXAMPLE_TIME
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
