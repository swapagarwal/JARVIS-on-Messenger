import json
import os

import requests

import config
from templates.text import TextTemplate

GOOGLE_URL_SHORTENER_API_KEY = os.environ.get('GOOGLE_URL_SHORTENER_API_KEY', config.GOOGLE_URL_SHORTENER_API_KEY)


def process(input, entities):
    output = {}
    try:
        url = entities['url'][0]['value']
        action = entities['url_action'][0]['value']
        if action == 'expand':
            r = requests.get('https://www.googleapis.com/urlshortener/v1/url', params={
                'key': GOOGLE_URL_SHORTENER_API_KEY,
                'shortUrl': url
            })
            data = r.json()
            response = 'Here\'s the shortened URL:\n' + url
            response += '\nHere\'s your original URL:\n' + data['longUrl']
        else:
            assert (action == 'shorten')
            r = requests.post('https://www.googleapis.com/urlshortener/v1/url?key=' + GOOGLE_URL_SHORTENER_API_KEY,
                              data=json.dumps({
                                  'longUrl': url
                              }), headers={
                    'Content-Type': 'application/json'
                })
            data = r.json()
            response = 'Here\'s your original URL:\n' + url
            response += '\nHere\'s your shortened URL:\n' + data['id']
        output['input'] = input
        output['output'] = TextTemplate(response).get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t perform that action.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - shorten google.com'
        error_message += '\n  - give me a short version of bing.com'
        error_message += '\n  - expand http://goo.gl/7aqe'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
