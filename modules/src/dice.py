import json
import random
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

def process(input, entities=None):
    roll = TextTemplate(str(random.randint(1, 6))).get_message()
    postback = {
        'intent': 'dice',
        'entities': None
    }
    message = add_quick_reply(roll, 'Roll again!', json.dumps(postback))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
