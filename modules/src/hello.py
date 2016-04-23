import re
import random

def process(input, entities=None):
    greetings = [
        'Welcome home, sir...',
        'All wrapped up here, sir. Will there be anything else?',
        'Sir, I think I need to sleep now...',
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, sir.',
        'You are not authorized to access this area.',
        'Oh hello, sir!',
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.'
    ]
    output = {
        'input': input,
        'output': random.choice(greetings),
        'success': True
    }
    return output
