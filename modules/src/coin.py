import json
import random
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

def process(input, entities=None):
    toss = TextTemplate(random.choice(['heads', 'tails'])).get_message()
    postback = {
        'intent': 'coin',
        'entities': None
    }
    message = add_quick_reply(toss, 'Flip again!', json.dumps(postback))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
