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
            message = TextTemplate(choice(jokes_list)).get_message()
            postback_joke = {
                'intent': 'joke',
                'entities': None
            }
            postback_quote = {
                'intent': 'quote',
                'entities': None
            }
            postback_fact = {
                'intent': 'fact',
                'entities': None
            }
            message = add_quick_reply(message, 'One more!', json.dumps(postback_joke))
            message = add_quick_reply(message, 'Show me a quote.', json.dumps(postback_quote))
            message = add_quick_reply(message, 'Tell me a fact.', json.dumps(postback_fact))
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
