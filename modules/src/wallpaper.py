import os

import requests
import requests_cache

import config
from templates.button import *
from templates.generic import GenericTemplate

UNSPLASH_API_KEY = os.environ.get('UNSPLASH_API_KEY', config.UNSPLASH_API_KEY)

# Required by Unsplash's API in any url which links back to Unsplash
utm_params = '?utm_source=jarvis&utm_medium=referral&utm_campaign=api-credit'


def process(input, entities=None):
    output = {}
    try:
        with requests_cache.enabled('wallpaper_cache', backend='sqlite', expire_after=3600):
            headers = {
                'Accept-Version': 'v1',
                'Authorization': 'Client-ID %s' % UNSPLASH_API_KEY
            }
            r = requests.get('https://api.unsplash.com/photos/random', headers=headers)
            data = r.json()

        photographer = data['user']['name']
        photographer_url = data['user']['links']['html'] + utm_params

        title = 'Wallpaper: %s x %s' % (data['width'], data['height'])
        description = '<%s / Unsplash>' % photographer
        image_url = data['urls']['full'] + utm_params
        item_url = data['links']['html'] + utm_params

        buttons = ButtonTemplate()
        buttons.add_web_url(photographer, photographer_url)
        buttons.add_web_url('Unsplash', 'https://unsplash.com' + utm_params)

        template = GenericTemplate()
        template.add_element(title=title, item_url=item_url, image_url=image_url,
                             subtitle=description, buttons=buttons.get_buttons())

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'Error encountered when querying the Unsplash API.'
        output['error_msg'] = error_message
        output['success'] = False
    return output
