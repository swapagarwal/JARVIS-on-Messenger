"""
Love Module

If given input has a me/you love/like intent, then returns
a loving response about JARVIS's affectionate feelings towards
the user.

Currently returns a random loving quote from the JSON file.
"""
import json
from random import choice

import config
import modules
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        # Open the local json file containing the love responses
        with open(config.LOVE_RESPONSES_SOURCE_FILE) as love_responses_file:
            love_json = json.load(love_responses_file)

            # Check if return love or defining love
            love_quotes_list = love_json['love_responses']
            if 'what' in input.lower():
                love_quotes_list = love_json['love_definitions']

            # Set output to a random quote from the list
            output['input'] = input
            output['output'] = TextTemplate(choice(love_quotes_list)).get_message()
            output['success'] = True
    except:
        error_message = 'I couldn\'t understand what you were trying to convey.\n'
        error_message += 'Please ask again!'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output