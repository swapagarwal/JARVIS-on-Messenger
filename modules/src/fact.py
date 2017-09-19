import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        with open(config.FACTS_SOURCE_FILE) as facts_file:
            facts = json.load(facts_file)
            facts_list = facts['facts']
            message = TextTemplate(choice(facts_list)).get_message()
            message = add_quick_reply(message, 'Another fact!', modules.generate_postback('fact'))
            message = add_quick_reply(message, 'Tell me a joke.', modules.generate_postback('joke'))
            message = add_quick_reply(message, 'Show me a quote.', modules.generate_postback('quote'))
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
