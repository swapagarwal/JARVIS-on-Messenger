import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        with open(config.QUOTES_SOURCE_FILE) as quotes_file:
            quotes = json.load(quotes_file)
            quotes_list = quotes['quotes']
            message = TextTemplate(choice(quotes_list)).get_message()
            message = add_quick_reply(message, 'Another one!', modules.generate_postback('quote'))
            message = add_quick_reply(message, 'Show me a fact.', modules.generate_postback('fact'))
            message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
