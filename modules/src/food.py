import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        with open(config.FOOD_SOURCE_FILE) as food_file:
            food = json.load(food_file)
            food_list = food['food']
            message = TextTemplate(choice(food_list)).get_message()
            message = add_quick_reply(message, 'One more!', modules.generate_postback('food'))
            message = add_quick_reply(message, 'Show me a quote.', modules.generate_postback('quote'))
            message = add_quick_reply(message, 'Tell me a fact.', modules.generate_postback('fact'))
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output