import os
import requests
import config

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY',
                                     config.GOOGLE_MAPS_API_KEY)


def retrieve_data(address):
    output = {}
    try:
        response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address='
            + address + '&key=' + GOOGLE_MAPS_API_KEY)
        location_data = response.json()

        output = location_data['results'][0]
    except:
        output['error_msg'] = 'Could not fetch location from provided address'
    return output
