import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply


def process(input, entities=None):
    message = AttachmentTemplate('https://i.kym-cdn.com/entries/icons/original/000/006/306/FlipTable.jpg', type='image').get_message()
    message = add_quick_reply(message, 'Again!', modules.generate_postback('table'))
    message = add_quick_reply(message, 'Roll a die.', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Flip a coin instead.', modules.generate_postback('coin'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
