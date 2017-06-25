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
        # Programming quotes
        r = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['quote'] + ' - ' + data['author']).get_message()
        output['success'] = True
        '''
        with open(config.QUOTES_SOURCE_FILE) as quotes_file:
            quotes = json.load(quotes_file)
            quotes_list = quotes['quotes']
            message = TextTemplate(choice(quotes_list)).get_message()
            postback_quote = {
                'intent': 'quote',
                'entities': None
            }
            postback_fact = {
                'intent': 'fact',
                'entities': None
            }
            postback_joke = {
                'intent': 'joke',
                'entities': None
            }
            message = add_quick_reply(message, 'Another one!', json.dumps(postback_quote))
            message = add_quick_reply(message, 'Show me a fact.', json.dumps(postback_fact))
            message = add_quick_reply(message, 'Tell me a joke.', json.dumps(postback_joke))
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
