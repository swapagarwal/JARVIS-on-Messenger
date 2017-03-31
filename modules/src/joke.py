import requests
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply
from random import choice
import json
import config

def process(input, entities=None):
    output = {}
    try:
        '''
        r = requests.get('http://tambal.azurewebsites.net/joke/random')
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['joke']).get_message()
        output['success'] = True
        '''
        with open(config.JOKES_SOURCE_FILE) as jokes_file:
            jokes = json.load(jokes_file)
            jokes_list = jokes['jokes']
            output['input'] = input
            joke = TextTemplate(choice(jokes_list)).get_message()
            postback = {
                'intent': 'joke',
                'entities': None
            }
            message = add_quick_reply(joke, 'Another one...', json.dumps(postback))
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
