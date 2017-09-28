import json
from random import choice

import config
import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


# List of all emoticons
__all__ = [
    '\U0001f604',
    '\U0001f600',
    '\U0001f601',
    '\U0001f602',
    '\U0001f603',
    '\U0001f606',
    '\U0001f609',
    '\U0001f60a',
    '\U0002f61a',
    '\U0001f610',
    '\U0002f639',
    '\U0001f610',
    '\U0001f611',
    '\U0001f644',
    '\U0001f60f',
    '\U0001f623',
    '\U0001f62e',
    '\U0001f62a',
    '\U0001f62b',
    '\U0001f620',
    '\U0001f615',
    '\U0001f631',
    '\U0001f62c',
    '\U0001f628',
    '\U0001f62d',
    '\U0001f61f',
    '\U0001f61e',
    '\U0001f641',
    '\U0001f60b',
    '\U0001f60e',
]




def process(input):
    output = {}
    try:
        with open(config.EMOTICONS_SOURCE_FILE) as emoticons_file:
            emoticons = json.load(emoticons_file)

            emoticons_list = emoticons[input]

            print emoticons_list
            message = TextTemplate(choice(emoticons_list)).get_message()
            output['input'] = input
            output['output'] = message
            output['success'] = True
    except:
        output['success'] = False
    return output




