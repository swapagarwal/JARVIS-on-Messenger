import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
import requests
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        URL = "https://api.quotable.io/random"
        r = requests.get(url=URL)
        data = r.json()

        message = TextTemplate(data['content'] + ' - ' + data['author']).get_message()

        message = add_quick_reply(message, 'Another one!', modules.generate_postback('quote'))
        message = add_quick_reply(message, 'Show me a fact.', modules.generate_postback('fact'))
        message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output
