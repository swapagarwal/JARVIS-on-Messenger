import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {
    1: 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png',
    2: 'https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png',
    3: 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png',
    4: 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png',
    5: 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_5.png',
    6: 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_6.png'
}


def process(input, entities=None):
    message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
    message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
