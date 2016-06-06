import requests
import config
import os
from templates.text import TextTemplate
from datetime import datetime

MAPQUEST_ACCESS_TOKEN = os.environ.get('MAPQUEST_ACCESS_TOKEN', config.MAPQUEST_ACCESS_TOKEN)
TIME_ZONE_ACCESS_TOKEN = os.environ.get('TIME_ZONE_ACCESS_TOKEN', config.TIME_ZONE_ACCESS_TOKEN)

def process(input, entities):
    output = {}
    try:
        l = requests.get('http://open.mapquestapi.com/nominatim/v1/search.php?key=' + MAPQUEST_ACCESS_TOKEN + '&format=json&q='+ entities['time'][0]['value'] + '&addressdetails=0&limit=1')
        location = l.json()
        r = requests.get('http://api.timezonedb.com/?lat='+ location[0]['lat'] + '&lng='+ location[0]['lon'] + '&format=json&key=' + TIME_ZONE_ACCESS_TOKEN)
        time_data = r.json()
        the_time = datetime.utcfromtimestamp(time_data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        output['input'] = input
        output['output'] = TextTemplate('Location: ' + location[0]['display_name'] + '\nTime: ' + the_time + '\nTime Zone: ' + time_data['abbreviation']).get_message()
        output['success'] = True
    except:
        output['success'] = False

    return output
