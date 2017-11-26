import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate
from utils.Quotes import getQuote


def process(input, entities=None):
    output = {}
    try:
        quote = getQuote()
        message = TextTemplate(quote).get_message()
        print message
        message = add_quick_reply(message, 'Another one!', modules.generate_postback('quote'))
        message = add_quick_reply(message, 'Show me a fact.', modules.generate_postback('fact'))
        message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output