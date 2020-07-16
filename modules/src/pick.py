import random

import modules
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply


def process(input, entities):
    greetings = ["have fun!", "enjoy!", "good luck!"]
    values_string = entities['pick'][0]['value']
    if "," in values_string:
        words = values_string.split(',')
    else:
        words = values_string.split()
    answer = random.choice(words).strip()+', '+random.choice(greetings)
    message = TextTemplate(answer).get_message()
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
