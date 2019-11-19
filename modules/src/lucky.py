import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    output = {}
    try:
        with open(config.LUCKY_SOURCE_FILE) as lucky_file:
            lucky = json.load(lucky_file)
            lucky_list = lucky['lucky']
            message = TextTemplate(choice(lucky_list)).get_message()
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output
