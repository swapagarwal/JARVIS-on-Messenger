import requests
from templates.text import TextTemplate
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
            output['input'] = input
            output['output'] = TextTemplate(choice(quotes_list)).get_message()
            output['success'] = True
    except:
        output['success'] = False
    return output
