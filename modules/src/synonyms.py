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
        with requests_cache.enabled('synonym_cache', backend='sqlite', expire_after=86400):
            r = requests.get('https://wordsapiv1.p.mashape.com/words/' + word + '/synonyms', headers={
                'X-Mashape-Key': WORDS_API_KEY
            })
            data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(
            'Synonyms of ' + word + ':\n' + data['synonyms']).get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any synonyms for that word.'
        error_message += '\nWord your query like this:'
        error_message += '\n  - synonym for happy'
        error_message += '\n  - run synonym'
        error_message += '\n  - synonymous with quiet?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
    