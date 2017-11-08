import random
from jarvis import app

from templates.text import TextTemplate


def process(input, entities=None):
    app.logger.info('Accessing Thanks module')
    messages = [
        u"\u2764",  # Red Heart Emoji
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(messages)).get_message(),
        'success': True
    }
    return output
