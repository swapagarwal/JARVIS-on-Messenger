import requests
import config
import os
import json
from templates.text import TextTemplate


GOOGLE_URL_SHORTENER = os.environ.get('GOOGLE_URL_SHORTENER', config.GOOGLE_URL_SHORTENER)


def process(input, entities=None):
    output = {}
    try:
        long_url = entities['word'][0]['value']
        headers = {'content-type': 'application/json'}
        r = requests.post('https://www.googleapis.com/urlshortener/v1/url?key=' + GOOGLE_URL_SHORTENER, data=json.dumps({'longUrl': long_url}), headers=headers)
        data = r.json()

        output['input'] = input
        output['output'] = TextTemplate(data['id']).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output