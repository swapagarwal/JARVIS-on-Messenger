import random
import os
import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

dir = os.getcwd()

dice_sides = {
        1: 'file:///' + dir + '/images/num_1.gif',
        2: 'file:///' + dir + '/images/num_2.gif',
        3: 'file:///' + dir + '/images/num_3.gif',
        4: 'file:///' + dir + '/images/num_4.gif',
        5: 'file:///' + dir + '/images/num_5.gif',
        6: 'file:///' + dir + '/images/num_6.gif'
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
