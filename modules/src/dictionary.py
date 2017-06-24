import requests
import requests_cache
import config
import os
from templates.text import TextTemplate
from error_msg import QUERY_ERROR, EXAMPLE_DEFINITIONS

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
        output['output'] = TextTemplate('Definition of ' + word + ':\n' + data['definitions'][0]['definition']).get_message()
        output['success'] = True
    except:
        error_message = QUERY_ERROR.format('definition') + EXAMPLE_DEFINITIONS
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
