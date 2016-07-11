import random
from templates.text import TextTemplate

def process(input, entities=None):
    greetings = [
        'Have a good day, sir.',
        'Wonderful, I think it\'s time for my evening nap...',
        'Bye to you as well, good sir.',
        'It was my pleasure talking to you.',
        'Oh, please do not go!',
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
