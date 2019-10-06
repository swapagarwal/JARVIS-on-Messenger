import json
from random import choice

import requests

import config
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        r = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
        data = r.json()
        message = data[quoteText] + ' - ' + data[quoteAuthor]

        message = TextTemplate(message).get_message()
        message = add_quick_reply(message, 'Another one!', modules.generate_postback('quote'))
        message = add_quick_reply(message, 'Show me a fact.', modules.generate_postback('fact'))
        message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
            
        output['input'] = input
        output['output'] = message
        output['success'] = True
        
    except:
        output['success'] = False
    return output
