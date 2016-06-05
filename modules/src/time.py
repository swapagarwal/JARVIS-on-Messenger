import requests
from templates.text import TextTemplate
from datetime import datetime

def process(input, entities):
    output = {}
    try:
        l = requests.get('http://open.mapquestapi.com/nominatim/v1/search.php?key=CcNE2f13xlbD9bMBYzWHsyasWeyGDfwA&format=json&q='+ entities['time'][0]['value'] + '&addressdetails=0&limit=1')
        location = l.json()
        r = requests.get('http://api.timezonedb.com/?lat='+ location[0]['lat'] + '&lng='+ location[0]['lon'] + '&format=json&key=M4K04AV6U6IT')
        time_data = r.json()
        the_time = datetime.utcfromtimestamp(time_data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        output['input'] = input
        output['output'] = TextTemplate('Location: ' + location[0]['display_name'] + '\nTime: ' + the_time + '\nTime Zone: ' + time_data['abbreviation']).get_message()
        output['success'] = True
    except:
        output['success'] = False

    return output
