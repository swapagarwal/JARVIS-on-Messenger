import random
from templates.text import TextTemplate

def process(input, entities=None):
    greetings = [
        'Welcome home, sir...',
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
