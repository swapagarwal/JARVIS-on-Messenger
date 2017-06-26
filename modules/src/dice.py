import json
import random
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {1: 'https://upload.wikimedia.org/wikipedia/commons/6/62/Kismet-Ace.png',
              2: 'https://upload.wikimedia.org/wikipedia/commons/6/6d/Kismet-Deuce.png',
              3: 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Kismet-Trey.png',
              4: 'https://upload.wikimedia.org/wikipedia/commons/1/11/Kismet-Four.png',
              5: 'https://upload.wikimedia.org/wikipedia/commons/8/8e/Kismet-Five.png',
              6: 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Kismet-Six.png'}

def process(input, entities=None):
    roll = TextTemplate(dice_sides[random.randint(1, 6)]).get_message()
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
