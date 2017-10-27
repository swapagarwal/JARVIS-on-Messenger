import random
import os

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

dir = os.getcwd()

# Use gif in images directory
coin_images = {
    'heads':'file:///' + dir + '/images/front.gif',
    'tails':'file:///' + dir + '/images/back.gif'
}


def process(input, entities=None):
    message = AttachmentTemplate(coin_images[random.choice(['heads', 'tails'])], type='image').get_message()
    message = add_quick_reply(message, 'Flip again!', modules.generate_postback('coin'))
    message = add_quick_reply(message, 'Roll a die.', modules.generate_postback('dice'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
