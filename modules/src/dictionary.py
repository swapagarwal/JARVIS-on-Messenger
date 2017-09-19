import os

import requests
import requests_cache

import config
from templates.text import TextTemplate

WORDS_API_KEY = os.environ.get('WORDS_API_KEY', config.WORDS_API_KEY)


def process(input, entities):
    output = {}
    try:
        word = entities['word'][0]['value']
        with requests_cache.enabled('dictionary_cache', backend='sqlite', expire_after=86400):
            r = requests.get('https://wordsapiv1.p.mashape.com/words/' + word + '/definitions', headers={
                'X-Mashape-Key': WORDS_API_KEY
            })
            data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(
            'Definition of ' + word + ':\n' + data['definitions'][0]['definition']).get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find that definition.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - define comfort'
        error_message += '\n  - cloud definition'
        error_message += '\n  - what does an accolade mean?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
