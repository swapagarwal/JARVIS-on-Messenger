import random

from templates.text import TextTemplate


def process(input, entities=None):
    messages = [
        u"\u2764",  # Red Heart Emoji
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(messages)).get_message(),
        'success': True
    }
    return output
