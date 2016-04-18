import re
import random

def match(input):
    greetings = [
        'hi',
        'hello',
        'jarvis',
        'hi jarvis',
        'hello jarvis',
        'are you there'
    ]
    input = re.sub(r'[^a-zA-Z\d\s]', '', input).lower()
    return input in greetings

def process(input):
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
