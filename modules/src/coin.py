import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

# Images by US Mint; published on wikimedia under public domain rights
coin_images = {
    'heads': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/2006_Quarter_Proof.png/244px-2006_Quarter_Proof.png',
    'tails': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Oregon_quarter%2C_reverse_side%2C_2005.jpg/236px-Oregon_quarter%2C_reverse_side%2C_2005.jpg'
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
