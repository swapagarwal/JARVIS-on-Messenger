import requests
import config
import os
from templates.text import TextTemplate

WORDS_API_KEY = os.environ.get('WORDS_API_KEY', config.WORDS_API_KEY)

def process(input, entities):
    output = {}
    try:
        word = entities['word'][0]['value']
        r = requests.get('https://wordsapiv1.p.mashape.com/words/' + word + '/definitions', headers={
            'X-Mashape-Key': WORDS_API_KEY
        })
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate('Definition of ' + word + ':\n' + data['definitions'][0]['definition']).get_message()
        output['success'] = True
    except:
        output['error_msg'] = TextTemplate('I could not find the definition of ' + word + '.\nPlease ask me something else.').get_message()
        output['success'] = False
    return output
