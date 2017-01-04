import json
import random
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {
	1: u'\u2680',
	2: u'\u2681',
	3: u'\u2682',
	4: u'\u2683',
	5: u'\u2684',
	6: u'\u2685'
}

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
